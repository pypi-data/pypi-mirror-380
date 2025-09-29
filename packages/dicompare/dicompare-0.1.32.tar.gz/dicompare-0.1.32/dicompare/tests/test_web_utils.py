"""
Unit tests for dicompare.web_utils module.
"""

import unittest
import pandas as pd
import numpy as np
import json
import asyncio
import pytest
from unittest.mock import patch, Mock, MagicMock

from dicompare.web_utils import (
    prepare_session_for_web, format_compliance_results_for_web,
    create_field_selection_helper, prepare_schema_generation_data,
    format_validation_error_for_web, convert_pyodide_data, create_download_data,
    load_schema_for_web, analyze_dicom_files_for_web,
    # New wrapper functions
    analyze_dicom_files, validate_compliance, generate_validation_template,
    parse_schema, get_field_info, search_fields, get_example_dicom_data,
    get_example_dicom_data_for_ui, get_example_validation_schema, clear_session_cache
)


class TestWebUtils(unittest.TestCase):
    """Test cases for web utility functions."""
    
    def setUp(self):
        """Set up test data."""
        # Create sample session DataFrame
        self.session_df = pd.DataFrame({
            'Acquisition': ['T1_MPRAGE'] * 3 + ['T2_FLAIR'] * 2,
            'DICOM_Path': [f'/path/{i}.dcm' for i in range(5)],
            'RepetitionTime': [2000, 2000, 2000, 9000, 9000],
            'EchoTime': [0.01, 0.01, 0.01, 0.1, 0.1],
            'FlipAngle': [30, 30, 30, 90, 90],
            'InstanceNumber': [1, 2, 3, 1, 2],
            'SliceThickness': [1.0, 1.0, 1.0, 3.0, 3.0],
            'ImageType': ['ORIGINAL'] * 5,
            'SeriesInstanceUID': ['1.2.3'] * 3 + ['1.2.4'] * 2
        })
        
        # Sample compliance results
        self.compliance_results = {
            'schema acquisition': {
                'T1_MPRAGE': {
                    'compliant': True,
                    'compliance_percentage': 95.0,
                    'message': 'Mostly compliant',
                    'detailed_results': [
                        {
                            'field': 'RepetitionTime',
                            'expected': 2000,
                            'actual': 2000,
                            'compliant': True,
                            'message': 'Match',
                            'difference_score': 0
                        },
                        {
                            'field': 'EchoTime',
                            'expected': 0.01,
                            'actual': 0.01,
                            'compliant': True,
                            'message': 'Match',
                            'difference_score': 0
                        }
                    ]
                },
                'T2_FLAIR': {
                    'compliant': False,
                    'compliance_percentage': 60.0,
                    'message': 'Some fields differ',
                    'detailed_results': [
                        {
                            'field': 'RepetitionTime',
                            'expected': 8000,
                            'actual': 9000,
                            'compliant': False,
                            'message': 'Value differs',
                            'difference_score': 5
                        }
                    ]
                }
            }
        }
    
    def test_prepare_session_for_web_basic(self):
        """Test basic functionality of prepare_session_for_web."""
        result = prepare_session_for_web(self.session_df)
        
        # Check structure
        self.assertIn('session_characteristics', result)
        self.assertIn('preview_data', result)
        self.assertIn('acquisition_summaries', result)
        self.assertEqual(result['status'], 'success')
        
        # Check session characteristics
        char = result['session_characteristics']
        self.assertEqual(char['total_files'], 5)
        self.assertEqual(char['total_acquisitions'], 2)
        self.assertIn('T1_MPRAGE', char['acquisition_names'])
        self.assertIn('T2_FLAIR', char['acquisition_names'])
        self.assertTrue(char['has_pixel_data_paths'])
    
    def test_prepare_session_for_web_preview_limit(self):
        """Test preview data limiting."""
        # Test with limit smaller than data
        result = prepare_session_for_web(self.session_df, max_preview_rows=3)
        
        preview = result['preview_data']
        self.assertEqual(preview['total_rows_shown'], 3)
        self.assertTrue(preview['is_truncated'])
        self.assertEqual(len(preview['data']), 3)
        
        # Test with limit larger than data
        result = prepare_session_for_web(self.session_df, max_preview_rows=10)
        preview = result['preview_data']
        self.assertEqual(preview['total_rows_shown'], 5)
        self.assertFalse(preview['is_truncated'])
    
    def test_prepare_session_for_web_acquisition_summaries(self):
        """Test acquisition summary generation with real function."""
        result = prepare_session_for_web(self.session_df)
        
        # Check acquisition summaries in result
        self.assertGreater(len(result['acquisition_summaries']), 0)
        
        # Verify actual summary structure
        summaries = result['acquisition_summaries']
        t1_summary = next((s for s in summaries if s['acquisition'] == 'T1_MPRAGE'), None)
        self.assertIsNotNone(t1_summary)
        self.assertEqual(t1_summary['file_count'], 3)
        self.assertEqual(t1_summary['display_name'], 'T1 Mprage')
    
    @patch('dicompare.web_utils.logger')
    @patch('dicompare.web_utils.create_acquisition_summary')
    def test_prepare_session_for_web_summary_error_handling(self, mock_summary, mock_logger):
        """Test error handling in acquisition summary generation."""
        # Make summary function raise an exception
        mock_summary.side_effect = Exception("Summary failed")
        
        result = prepare_session_for_web(self.session_df)
        
        # Should handle the error gracefully
        self.assertEqual(result['status'], 'success')
        mock_logger.warning.assert_called()
    
    def test_format_compliance_results_for_web_basic(self):
        """Test basic functionality of format_compliance_results_for_web."""
        result = format_compliance_results_for_web(self.compliance_results)
        
        # Check summary
        summary = result['summary']
        self.assertEqual(summary['total_acquisitions'], 2)
        self.assertEqual(summary['compliant_acquisitions'], 1)
        self.assertEqual(summary['compliance_rate'], 50.0)
        self.assertEqual(summary['status'], 'completed')
        
        # Check acquisition details (now a dictionary keyed by acquisition name)
        details = result['acquisition_details']
        self.assertEqual(len(details), 2)
        
        # Check that both acquisitions are present with correct data
        self.assertIn('T1_MPRAGE', details)
        self.assertIn('T2_FLAIR', details)
        self.assertEqual(details['T1_MPRAGE']['acquisition'], 'T1_MPRAGE')
        self.assertEqual(details['T1_MPRAGE']['compliance_percentage'], 95.0)
        self.assertEqual(details['T2_FLAIR']['acquisition'], 'T2_FLAIR')
        self.assertEqual(details['T2_FLAIR']['compliance_percentage'], 60.0)
    
    def test_format_compliance_results_for_web_detailed_results(self):
        """Test detailed results processing."""
        result = format_compliance_results_for_web(self.compliance_results)
        
        details = result['acquisition_details']
        
        # Check T1_MPRAGE details (now accessed by key)
        t1_details = details['T1_MPRAGE']
        self.assertEqual(t1_details['total_fields_checked'], 2)
        self.assertEqual(t1_details['compliant_fields'], 2)
        self.assertTrue(t1_details['compliant'])
        
        # Check detailed results structure
        detailed = t1_details['detailed_results']
        self.assertEqual(len(detailed), 2)
        self.assertEqual(detailed[0]['field'], 'RepetitionTime')
        self.assertTrue(detailed[0]['compliant'])
    
    def test_format_compliance_results_for_web_empty_results(self):
        """Test with empty compliance results."""
        empty_results = {'schema acquisition': {}}
        result = format_compliance_results_for_web(empty_results)
        
        summary = result['summary']
        self.assertEqual(summary['total_acquisitions'], 0)
        self.assertEqual(summary['compliant_acquisitions'], 0)
        self.assertEqual(summary['compliance_rate'], 0)
        
        self.assertEqual(len(result['acquisition_details']), 0)
    
    def test_create_field_selection_helper_basic(self):
        """Test basic functionality of create_field_selection_helper."""
        result = create_field_selection_helper(self.session_df, 'T1_MPRAGE')
        
        self.assertEqual(result['status'], 'success')
        self.assertEqual(result['acquisition'], 'T1_MPRAGE')
        self.assertEqual(result['total_files'], 3)
        
        # Check recommendations structure
        recommended = result['recommended']
        self.assertIn('constant_fields', recommended)
        self.assertIn('series_grouping_fields', recommended)
        self.assertIn('priority_constant', recommended)
        self.assertIn('priority_variable', recommended)
        
        # RepetitionTime should be constant for T1_MPRAGE
        self.assertIn('RepetitionTime', recommended['priority_constant'])
        
        # InstanceNumber should be variable 
        self.assertIn('InstanceNumber', recommended['series_grouping_fields'])
    
    def test_create_field_selection_helper_priority_fields(self):
        """Test priority field handling with custom priority list."""
        priority_fields = ['RepetitionTime', 'EchoTime', 'FlipAngle', 'InstanceNumber']
        result = create_field_selection_helper(
            self.session_df, 'T1_MPRAGE', priority_fields
        )
        
        recommended = result['recommended']
        
        # RepetitionTime should be in priority_constant (it's constant in our test data)
        self.assertIn('RepetitionTime', recommended['priority_constant'])
        
        # InstanceNumber should be in priority_variable (it varies in our test data)
        self.assertIn('InstanceNumber', recommended['priority_variable'])
    
    def test_create_field_selection_helper_error_handling(self):
        """Test error handling in field selection helper."""
        result = create_field_selection_helper(self.session_df, 'NONEXISTENT')
        
        self.assertEqual(result['status'], 'failed')
        self.assertIn('error', result)
        self.assertIn('No data found for acquisition', result['error'])
    
    def test_prepare_schema_generation_data_basic(self):
        """Test basic functionality of prepare_schema_generation_data."""
        result = prepare_schema_generation_data(self.session_df)
        
        self.assertEqual(result['status'], 'ready')
        self.assertEqual(result['acquisition_count'], 2)
        self.assertEqual(result['total_files'], 5)
        self.assertIn('T1_MPRAGE', result['acquisitions'])
        self.assertIn('T2_FLAIR', result['acquisitions'])
        
        # Should have acquisition analysis
        self.assertIn('acquisition_analysis', result)
        self.assertEqual(len(result['acquisition_analysis']), 2)
        
        # Should have suggested fields (commonly constant across acquisitions)
        self.assertIn('suggested_fields', result)
        suggested = result['suggested_fields']
        # RepetitionTime is constant within each acquisition (though different values)
        # ImageType and SeriesInstanceUID are constant within each acquisition
        self.assertGreater(len(suggested), 0)
    
    def test_format_validation_error_for_web(self):
        """Test formatting of validation errors."""
        error = ValueError("Field 'EchoTime' not found in data")
        result = format_validation_error_for_web(error)
        
        self.assertEqual(result['error_type'], 'ValueError')
        self.assertIn("Field 'EchoTime' not found", result['error_message'])
        self.assertEqual(result['status'], 'error')
        self.assertIn('user_message', result)
        self.assertIn('suggestions', result)
        self.assertIsInstance(result['suggestions'], list)
    
    def test_convert_pyodide_data_basic(self):
        """Test basic Pyodide data conversion."""
        # Test with regular Python objects
        regular_data = {'a': 1, 'b': [2, 3], 'c': {'d': 4}}
        result = convert_pyodide_data(regular_data)
        self.assertEqual(result, regular_data)
        
        # Test with mock JSProxy object
        class MockJSProxy:
            def to_py(self):
                return {'converted': True}
        
        js_data = MockJSProxy()
        result = convert_pyodide_data(js_data)
        self.assertEqual(result, {'converted': True})
    
    def test_convert_pyodide_data_nested(self):
        """Test nested Pyodide data conversion."""
        class MockJSProxy:
            def __init__(self, data):
                self.data = data
            def to_py(self):
                return self.data
        
        # Nested structure with JSProxy objects
        nested_data = {
            'normal': 'value',
            'js_object': MockJSProxy({'inner': 'converted'}),
            'list_with_js': [1, MockJSProxy('converted_item'), 3]
        }
        
        result = convert_pyodide_data(nested_data)
        
        expected = {
            'normal': 'value',
            'js_object': {'inner': 'converted'},
            'list_with_js': [1, 'converted_item', 3]
        }
        self.assertEqual(result, expected)
    
    def test_create_download_data_json(self):
        """Test JSON download data creation."""
        data = {'schema': {'acquisitions': {'T1': {'fields': []}}}}
        result = create_download_data(data, 'my_schema', 'json')
        
        self.assertEqual(result['filename'], 'my_schema.json')
        self.assertEqual(result['mime_type'], 'application/json')
        self.assertEqual(result['status'], 'ready')
        
        # Content should be valid JSON
        content = result['content']
        loaded = json.loads(content)
        self.assertEqual(loaded, data)
        
        # Should have size information
        self.assertIn('size_bytes', result)
        self.assertGreater(result['size_bytes'], 0)
    
    def test_create_download_data_csv(self):
        """Test CSV download data creation."""
        # Tabular data
        data = [
            {'field': 'RepetitionTime', 'value': 2000},
            {'field': 'EchoTime', 'value': 0.01}
        ]
        result = create_download_data(data, 'results', 'csv')
        
        self.assertEqual(result['filename'], 'results.csv')
        self.assertEqual(result['mime_type'], 'text/csv')
        
        # Content should be CSV format
        content = result['content']
        self.assertIn('field,value', content)
        self.assertIn('RepetitionTime,2000', content)
    
    def test_create_download_data_csv_non_tabular(self):
        """Test CSV creation with non-tabular data."""
        data = {'not': 'tabular'}
        result = create_download_data(data, 'test', 'csv')
        
        self.assertEqual(result['content'], 'No tabular data available')
    
    def test_create_download_data_default_format(self):
        """Test default format handling."""
        data = {'test': 'data'}
        result = create_download_data(data, 'test', 'unknown_format')
        
        # Should default to JSON
        self.assertEqual(result['filename'], 'test.json')
        self.assertEqual(result['mime_type'], 'application/json')
        
        # Content should be valid JSON
        loaded = json.loads(result['content'])
        self.assertEqual(loaded, data)
    
    def test_create_download_data_with_numpy_data(self):
        """Test download data creation with numpy arrays."""
        data = {
            'array': np.array([1, 2, 3]),
            'scalar': np.int64(42),
            'nested': {'inner_array': np.array([[1, 2], [3, 4]])}
        }
        
        result = create_download_data(data, 'numpy_test')
        
        # Should handle numpy serialization
        content = result['content']
        loaded = json.loads(content)
        
        self.assertEqual(loaded['array'], [1, 2, 3])
        self.assertEqual(loaded['scalar'], 42)
        self.assertEqual(loaded['nested']['inner_array'], [[1, 2], [3, 4]])
    
    def test_prepare_schema_generation_data_error_handling(self):
        """Test error handling in schema generation data preparation."""
        # Create DataFrame with an acquisition that will cause issues
        problematic_df = pd.DataFrame({
            'Acquisition': ['VALID', 'PROBLEMATIC'],
            'RepetitionTime': [2000, 'invalid_value'],  # Invalid data type
        })
        
        # Function should handle errors gracefully
        result = prepare_schema_generation_data(problematic_df)
        
        # Should complete successfully despite potential issues
        self.assertEqual(result['status'], 'ready')
        self.assertEqual(result['acquisition_count'], 2)
        
        # May have partial analysis depending on which acquisitions succeed
        self.assertIn('acquisition_analysis', result)
    
    def test_edge_cases_empty_dataframe(self):
        """Test edge cases with empty DataFrame."""
        empty_df = pd.DataFrame()
        
        # prepare_session_for_web should handle empty data
        result = prepare_session_for_web(empty_df)
        char = result['session_characteristics']
        self.assertEqual(char['total_files'], 0)
        self.assertEqual(char['total_acquisitions'], 0)
    
    def test_json_serialization_integration(self):
        """Test that all web utils properly handle JSON serialization."""
        # Test data with various numpy/pandas types
        complex_df = self.session_df.copy()
        complex_df['numpy_field'] = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
        complex_df['nan_field'] = [1, np.nan, 3, np.nan, 5]
        
        result = prepare_session_for_web(complex_df)
        
        # Should be JSON serializable
        json_str = json.dumps(result)
        loaded = json.loads(json_str)
        
        # Basic structure should be preserved
        self.assertIn('session_characteristics', loaded)
        self.assertIn('preview_data', loaded)
    
    @pytest.mark.asyncio
    async def test_analyze_dicom_files_for_web_basic(self):
        """Test analyze_dicom_files_for_web with mock DICOM data."""
        from ..web_utils import analyze_dicom_files_for_web
        
        # Create mock DICOM files (minimal byte data)
        mock_files = {
            'file1.dcm': b'mock_dicom_data_1',
            'file2.dcm': b'mock_dicom_data_2'
        }
        
        # Mock reference fields
        reference_fields = ['SeriesDescription', 'RepetitionTime', 'EchoTime']
        
        # This will likely fail because we don't have real DICOM data,
        # but should return an error response gracefully
        result = await analyze_dicom_files_for_web(mock_files, reference_fields)
        
        # Should return a dict with expected structure
        self.assertIsInstance(result, dict)
        self.assertIn('status', result)
        self.assertIn('total_files', result)
        self.assertIn('acquisitions', result)
        self.assertIn('field_summary', result)
        self.assertIn('message', result)
        
        # With mock data, expect error status but proper structure
        self.assertEqual(result['total_files'], 2)
        self.assertIsInstance(result['acquisitions'], dict)
    
    @pytest.mark.asyncio
    async def test_analyze_dicom_files_for_web_empty_files(self):
        """Test analyze_dicom_files_for_web with empty file dict."""
        from ..web_utils import analyze_dicom_files_for_web
        
        result = await analyze_dicom_files_for_web({})
        
        # Should handle empty input gracefully
        self.assertEqual(result['total_files'], 0)
        self.assertEqual(result['status'], 'error')
        self.assertIn('acquisitions', result)
        self.assertIn('field_summary', result)
    
    @pytest.mark.asyncio
    async def test_analyze_dicom_files_for_web_default_fields(self):
        """Test analyze_dicom_files_for_web uses default fields when none provided."""
        from ..web_utils import analyze_dicom_files_for_web
        
        mock_files = {'test.dcm': b'mock_data'}
        
        result = await analyze_dicom_files_for_web(mock_files)  # No reference_fields provided
        
        # Should use DEFAULT_DICOM_FIELDS and return proper structure
        self.assertIsInstance(result, dict)
        self.assertIn('status', result)
        self.assertEqual(result['total_files'], 1)




class TestWebInterfaceFunctions(unittest.TestCase):
    """Test cases for web interface functions."""
    
    def test_load_schema_for_web_dict_input(self):
        """Test load_schema_for_web with dictionary input."""
        schema_dict = {
            'acquisitions': {
                'T1_MPRAGE': {
                    'fields': [
                        {'field': 'RepetitionTime', 'value': 2000},
                        {'field': 'EchoTime', 'value': 0.01}
                    ],
                    'series': []
                }
            }
        }
        
        result = load_schema_for_web(schema_dict, 'test_schema')
        
        # Check structure
        self.assertEqual(result['schema_id'], 'test_schema')
        self.assertEqual(result['schema_type'], 'json')
        self.assertEqual(result['validation_status'], 'valid')
        self.assertEqual(len(result['errors']), 0)
        
        # Check acquisitions
        self.assertIn('T1_MPRAGE', result['acquisitions'])
        acq = result['acquisitions']['T1_MPRAGE']
        self.assertEqual(acq['name'], 'T1_MPRAGE')
        self.assertEqual(len(acq['fields']), 2)
        self.assertEqual(acq['metadata']['field_count'], 2)
        
        # Check metadata
        metadata = result['metadata']
        self.assertEqual(metadata['total_acquisitions'], 1)
        self.assertIn('T1_MPRAGE', metadata['acquisition_names'])
    
    def test_load_schema_for_web_invalid_schema(self):
        """Test load_schema_for_web with invalid schema."""
        invalid_schema = {
            'name': 'invalid'  # Missing 'acquisitions' key
        }
        
        result = load_schema_for_web(invalid_schema, 'invalid_test')
        
        # Should mark as invalid
        self.assertEqual(result['validation_status'], 'invalid')
        self.assertGreater(len(result['errors']), 0)
        self.assertIn('acquisitions', result['errors'][0])
    
    def test_load_schema_for_web_acquisition_filter(self):
        """Test load_schema_for_web with acquisition filter."""
        schema_dict = {
            'acquisitions': {
                'T1_MPRAGE': {'fields': [], 'series': []},
                'T2_FLAIR': {'fields': [], 'series': []},
                'DWI': {'fields': [], 'series': []}
            }
        }
        
        result = load_schema_for_web(schema_dict, 'filtered_test', acquisition_filter='T1_MPRAGE')
        
        # Should only include filtered acquisition
        self.assertEqual(len(result['acquisitions']), 1)
        self.assertIn('T1_MPRAGE', result['acquisitions'])
        self.assertNotIn('T2_FLAIR', result['acquisitions'])
        self.assertEqual(result['metadata']['total_acquisitions'], 1)
    
    def test_load_schema_for_web_missing_acquisition_filter(self):
        """Test load_schema_for_web with non-existent acquisition filter."""
        schema_dict = {
            'acquisitions': {
                'T1_MPRAGE': {'fields': [], 'series': []}
            }
        }
        
        result = load_schema_for_web(schema_dict, 'test', acquisition_filter='NONEXISTENT')
        
        # Should have error and empty acquisitions
        self.assertGreater(len(result['errors']), 0)
        self.assertIn('NONEXISTENT', result['errors'][0])
        self.assertEqual(len(result['acquisitions']), 0)
    


class TestNewWrapperFunctions(unittest.TestCase):
    """Test cases for new API wrapper functions."""
    
    def setUp(self):
        """Set up test data."""
        # Clear any cached session data
        clear_session_cache()
    
    def test_parse_schema_valid_json(self):
        """Test parse_schema with valid JSON."""
        schema_content = '{"acquisitions": {"T1": {"fields": []}}}'
        result = parse_schema(schema_content, "json")
        
        self.assertIn("parsed_schema", result)
        self.assertEqual(result["parsed_schema"]["acquisitions"]["T1"]["fields"], [])
    
    def test_parse_schema_invalid_json(self):
        """Test parse_schema with invalid JSON."""
        schema_content = '{"invalid json'
        result = parse_schema(schema_content, "json")
        
        self.assertIn("error", result)
        self.assertEqual(result["error_type"], "SchemaParseError")
    
    def test_parse_schema_missing_acquisitions(self):
        """Test parse_schema with missing acquisitions key."""
        schema_content = '{"name": "test"}'
        result = parse_schema(schema_content, "json")
        
        self.assertIn("error", result)
        self.assertIn("acquisitions", result["error"])
    
    def test_parse_schema_unsupported_format(self):
        """Test parse_schema with unsupported format."""
        result = parse_schema("{}", "unsupported")
        
        self.assertIn("error", result)
        self.assertIn("Unsupported schema format", result["error"])
    
    def test_get_example_dicom_data(self):
        """Test get_example_dicom_data returns valid structure."""
        result = get_example_dicom_data()
        
        self.assertIn("acquisitions", result)
        self.assertIn("summary", result)
        self.assertIsInstance(result["acquisitions"], list)
        self.assertGreater(len(result["acquisitions"]), 0)
        
        # Check first acquisition structure
        acq = result["acquisitions"][0]
        self.assertIn("id", acq)
        self.assertIn("acquisition_fields", acq)
        self.assertIn("series_fields", acq)
        self.assertIn("series", acq)
        self.assertIn("metadata", acq)
    
    def test_get_example_dicom_data_for_ui(self):
        """Test get_example_dicom_data_for_ui returns acquisition list."""
        result = get_example_dicom_data_for_ui()
        
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        
        # Should be same as acquisitions from get_example_dicom_data
        full_data = get_example_dicom_data()
        self.assertEqual(result, full_data["acquisitions"])
    
    def test_get_example_validation_schema(self):
        """Test get_example_validation_schema returns valid schema."""
        result = get_example_validation_schema()
        
        self.assertIn("acquisitions", result)
        self.assertIn("version", result)
        self.assertIn("name", result)
        self.assertIsInstance(result["acquisitions"], dict)
        
        # Check schema structure
        for acq_name, acq_data in result["acquisitions"].items():
            self.assertIn("fields", acq_data)
            self.assertIsInstance(acq_data["fields"], list)
            
            # Check field structure
            for field in acq_data["fields"]:
                self.assertIn("field", field)
                self.assertIn("expected", field)
                self.assertIn("validation", field)
    
    @patch('pydicom.datadict.dictionary_VR', {0x00080060: 'CS'})
    @patch('pydicom.datadict.keyword_dict', {'Modality': 0x00080060})
    @patch('pydicom.datadict.dictionary_description', {0x00080060: 'Modality'})
    def test_get_field_info_valid_tag(self):
        """Test get_field_info with valid DICOM tag."""
        result = get_field_info("0008,0060")
        
        self.assertNotIn("error", result)
        self.assertEqual(result["tag"], "0008,0060")
        self.assertEqual(result["keyword"], "Modality")
        self.assertEqual(result["vr"], "CS")
        self.assertEqual(result["suggested_data_type"], "string")
    
    def test_get_field_info_invalid_tag_format(self):
        """Test get_field_info with invalid tag format."""
        result = get_field_info("invalid")
        
        self.assertIn("error", result)
        self.assertEqual(result["error_type"], "TagNotFoundError")
    
    @patch('pydicom.datadict.keyword_dict', {
        'Modality': 0x00080060,
        'RepetitionTime': 0x00180080,
        'EchoTime': 0x00180081
    })
    @patch('pydicom.datadict.dictionary_description', {
        0x00080060: 'Modality',
        0x00180080: 'Repetition Time',
        0x00180081: 'Echo Time'
    })
    @patch('pydicom.datadict.dictionary_VR', {
        0x00080060: 'CS',
        0x00180080: 'DS',
        0x00180081: 'DS'
    })
    def test_search_fields_basic(self):
        """Test search_fields with basic query."""
        with patch('dicompare.web_utils.get_field_info') as mock_get_field:
            mock_get_field.return_value = {
                "tag": "0008,0060",
                "keyword": "Modality",
                "vr": "CS"
            }
            
            result = search_fields("modality", limit=5)
            
            self.assertIsInstance(result, list)
            self.assertLessEqual(len(result), 5)
    
    def test_validate_compliance_no_session(self):
        """Test validate_compliance with no cached session."""
        clear_session_cache()
        
        result = validate_compliance(schema_content='{"acquisitions": {}}')
        
        self.assertIn("error", result)
        self.assertEqual(result["error_type"], "ValidationError")
        self.assertIn("No DICOM data available", result["error"])
    
    def test_generate_validation_template_no_session(self):
        """Test generate_validation_template with no cached session."""
        clear_session_cache()
        
        result = generate_validation_template([], {})
        
        self.assertIn("error", result)
        self.assertEqual(result["error_type"], "ValidationError")
        self.assertIn("No session data available", result["error"])
    
    def test_analyze_dicom_files_invalid_format(self):
        """Test analyze_dicom_files with invalid file format."""
        invalid_files = ["not_a_dict"]
        
        result = analyze_dicom_files(invalid_files)
        
        self.assertIn("error", result)
        self.assertEqual(result["error_type"], "DicomError")
        self.assertIn("Invalid file format", result["error"])
    
    def test_analyze_dicom_files_valid_format(self):
        """Test analyze_dicom_files with valid file format but mock data."""
        mock_files = [
            {"name": "file1.dcm", "content": b"mock_dicom_data"}
        ]
        
        # This will likely fail due to invalid DICOM data, but should handle gracefully
        result = analyze_dicom_files(mock_files)
        
        # Should return a structured response even on error
        self.assertIn("error", result)  # Expected due to mock data
        self.assertEqual(result["error_type"], "DicomError")


class TestFieldTransformation(unittest.TestCase):
    """Test field transformation functions for series field dictionaries."""
    
    def test_transform_fields_to_dict_with_values(self):
        """Test _transform_fields_to_dict with single values."""
        from dicompare.web_utils import _transform_fields_to_dict
        
        fields = [
            {"tag": "0008,0060", "name": "Modality", "value": "MR"},
            {"tag": "0018,0080", "name": "RepetitionTime", "value": 2300.0},
            {"tag": None, "name": "UnknownField", "value": "test"}  # Should be ignored
        ]
        
        result = _transform_fields_to_dict(fields)
        
        self.assertEqual(len(result), 2)
        self.assertEqual(result["0008,0060"], "MR")
        self.assertEqual(result["0018,0080"], 2300.0)
        self.assertNotIn(None, result)
    
    def test_transform_fields_to_dict_with_multi_values(self):
        """Test _transform_fields_to_dict with multi-valued fields."""
        from dicompare.web_utils import _transform_fields_to_dict
        
        fields = [
            {"tag": "0018,0020", "name": "ScanningSequence", "values": ["SE", "IR"]},
            {"tag": "0028,0030", "name": "PixelSpacing", "values": [0.5, 0.5]}
        ]
        
        result = _transform_fields_to_dict(fields)
        
        self.assertEqual(len(result), 2)
        self.assertEqual(result["0018,0020"], ["SE", "IR"])
        self.assertEqual(result["0028,0030"], [0.5, 0.5])
    
    def test_transform_fields_to_dict_empty_input(self):
        """Test _transform_fields_to_dict with empty input."""
        from dicompare.web_utils import _transform_fields_to_dict
        
        result = _transform_fields_to_dict([])
        
        self.assertEqual(len(result), 0)
        self.assertIsInstance(result, dict)
    
    def test_transform_fields_to_dict_missing_data(self):
        """Test _transform_fields_to_dict with missing tag or value data."""
        from dicompare.web_utils import _transform_fields_to_dict
        
        fields = [
            {"name": "MissingTag", "value": "test"},  # No tag
            {"tag": "0008,0060"},  # No value
            {"tag": "0018,0080", "name": "RepetitionTime", "value": 2300.0}  # Valid
        ]
        
        result = _transform_fields_to_dict(fields)
        
        self.assertEqual(len(result), 1)
        self.assertEqual(result["0018,0080"], 2300.0)


if __name__ == '__main__':
    unittest.main()