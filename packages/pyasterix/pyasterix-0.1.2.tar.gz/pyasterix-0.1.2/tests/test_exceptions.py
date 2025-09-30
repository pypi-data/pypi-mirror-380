"""
Comprehensive tests for the AsterixDB exception handling system.

This test suite validates:
- PEP 249 compliance
- Exception hierarchy correctness
- Error mapping functionality
- Context preservation
- Backward compatibility
"""

import json
import time
import pytest
from unittest.mock import Mock, patch, MagicMock
from typing import Dict, Any

from src.pyasterix.exceptions import (
    # Base exceptions
    AsterixError, Warning, Error,
    
    # PEP 249 standard exceptions
    InterfaceError, DatabaseError, DataError, OperationalError,
    IntegrityError, InternalError, ProgrammingError, NotSupportedError,
    
    # AsterixDB-specific exceptions
    TypeMismatchError, ResultProcessingError, NetworkError, HTTPError,
    TimeoutError, AuthenticationError, ResourceError, PoolExhaustedError,
    ConnectionValidationError, SyntaxError, IdentifierError, QueryBuildError,
    AsyncQueryError, AsyncTimeoutError, HandleError, PoolError, PoolShutdownError,
    DataFrameError,
    
    # Error mapping utilities
    ErrorMapper, AsyncErrorMapper,
    
    # Legacy aliases
    ConnectionError, QueryError, ValidationError, TypeMappingError
)


class TestExceptionHierarchy:
    """Test the exception hierarchy and PEP 249 compliance."""
    
    def test_base_exception_hierarchy(self):
        """Test that all exceptions inherit correctly from base classes."""
        # All exceptions should inherit from AsterixError
        assert issubclass(Warning, AsterixError)
        assert issubclass(Error, AsterixError)
        
        # PEP 249 hierarchy
        assert issubclass(InterfaceError, Error)
        assert issubclass(DatabaseError, Error)
        assert issubclass(DataError, DatabaseError)
        assert issubclass(OperationalError, DatabaseError)
        assert issubclass(IntegrityError, DatabaseError)
        assert issubclass(InternalError, DatabaseError)
        assert issubclass(ProgrammingError, DatabaseError)
        assert issubclass(NotSupportedError, DatabaseError)
    
    def test_asterix_specific_hierarchy(self):
        """Test AsterixDB-specific exception hierarchy."""
        # Data errors
        assert issubclass(TypeMismatchError, DataError)
        assert issubclass(ResultProcessingError, DataError)
        
        # Operational errors
        assert issubclass(NetworkError, OperationalError)
        assert issubclass(HTTPError, OperationalError)
        assert issubclass(TimeoutError, OperationalError)
        assert issubclass(AuthenticationError, OperationalError)
        assert issubclass(ResourceError, OperationalError)
        assert issubclass(PoolExhaustedError, OperationalError)
        assert issubclass(ConnectionValidationError, OperationalError)
        
        # Programming errors
        assert issubclass(SyntaxError, ProgrammingError)
        assert issubclass(IdentifierError, ProgrammingError)
        assert issubclass(QueryBuildError, ProgrammingError)
        
        # Async and pool errors
        assert issubclass(AsyncQueryError, DatabaseError)
        assert issubclass(AsyncTimeoutError, TimeoutError)
        assert issubclass(HandleError, DatabaseError)
        assert issubclass(PoolError, DatabaseError)
        assert issubclass(PoolShutdownError, InterfaceError)
        assert issubclass(DataFrameError, DatabaseError)
    
    def test_legacy_aliases(self):
        """Test that legacy aliases point to correct new exceptions."""
        assert ConnectionError is NetworkError
        assert QueryError is AsyncQueryError
        assert ValidationError is DataError
        assert TypeMappingError is TypeMismatchError


class TestAsterixErrorBase:
    """Test the base AsterixError functionality."""
    
    def test_basic_initialization(self):
        """Test basic exception initialization."""
        error = AsterixError("Test message")
        assert str(error) == "Test message"
        assert error.message == "Test message"
        assert error.error_code is None
        assert error.context == {}
        assert isinstance(error.timestamp, float)
        assert error.errno is None
        assert error.sqlstate is None
    
    def test_full_initialization(self):
        """Test exception initialization with all parameters."""
        context = {"key": "value"}
        error = AsterixError(
            "Test message",
            error_code="ASX1001",
            context=context,
            errno=1001,
            sqlstate="42000"
        )
        
        assert error.message == "Test message"
        assert error.error_code == "ASX1001"
        assert error.context == context
        assert error.errno == 1001
        assert error.sqlstate == "42000"
    
    def test_string_representation(self):
        """Test string representation with error codes."""
        error1 = AsterixError("Simple message")
        assert str(error1) == "Simple message"
        
        error2 = AsterixError("Message with code", error_code="ASX1001")
        assert str(error2) == "[ASX1001] Message with code"
    
    def test_repr_representation(self):
        """Test detailed representation."""
        error = AsterixError("Test", error_code="ASX1001", context={"k": "v"})
        repr_str = repr(error)
        assert "AsterixError" in repr_str
        assert "Test" in repr_str
        assert "ASX1001" in repr_str
        assert "{'k': 'v'}" in repr_str
    
    def test_to_dict_serialization(self):
        """Test exception serialization to dictionary."""
        error = AsterixError(
            "Test message",
            error_code="ASX1001",
            context={"key": "value"},
            errno=1001,
            sqlstate="42000"
        )
        
        error_dict = error.to_dict()
        expected_keys = {
            'type', 'message', 'error_code', 'context', 
            'timestamp', 'errno', 'sqlstate'
        }
        assert set(error_dict.keys()) == expected_keys
        assert error_dict['type'] == 'AsterixError'
        assert error_dict['message'] == 'Test message'
        assert error_dict['error_code'] == 'ASX1001'
        assert error_dict['context'] == {'key': 'value'}
        assert error_dict['errno'] == 1001
        assert error_dict['sqlstate'] == '42000'


class TestSpecializedExceptions:
    """Test specialized exception classes with custom attributes."""
    
    def test_http_error(self):
        """Test HTTPError with status code and response."""
        error = HTTPError(
            "HTTP error occurred",
            status_code=500,
            response_text="Internal Server Error"
        )
        
        assert error.status_code == 500
        assert error.response_text == "Internal Server Error"
        assert error.context['http_status_code'] == 500
        assert error.context['http_response'] == "Internal Server Error"
    
    def test_timeout_error(self):
        """Test TimeoutError with duration and operation type."""
        error = TimeoutError(
            "Operation timed out",
            timeout_duration=30.0,
            operation_type="query_execution"
        )
        
        assert error.timeout_duration == 30.0
        assert error.operation_type == "query_execution"
        assert error.context['timeout_duration'] == 30.0
        assert error.context['operation_type'] == "query_execution"
    
    def test_resource_error(self):
        """Test ResourceError with resource details."""
        error = ResourceError(
            "Resource exhausted",
            resource_type="memory",
            resource_limit="1GB"
        )
        
        assert error.resource_type == "memory"
        assert error.resource_limit == "1GB"
        assert error.context['resource_type'] == "memory"
        assert error.context['resource_limit'] == "1GB"
    
    def test_pool_exhausted_error(self):
        """Test PoolExhaustedError with pool details."""
        error = PoolExhaustedError(
            "Pool exhausted",
            pool_size=10,
            active_connections=10
        )
        
        assert error.pool_size == 10
        assert error.active_connections == 10
        assert error.context['pool_size'] == 10
        assert error.context['active_connections'] == 10
    
    def test_syntax_error(self):
        """Test SyntaxError with query details."""
        query = "SELECT * FROM invalid_syntax WHERE"
        error = SyntaxError(
            "Syntax error in query",
            line_number=1,
            column_number=35,
            query=query
        )
        
        assert error.line_number == 1
        assert error.column_number == 35
        assert error.query == query
        assert error.context['line_number'] == 1
        assert error.context['column_number'] == 35
        assert error.context['query'] == query
    
    def test_async_query_error(self):
        """Test AsyncQueryError with handle and status."""
        error = AsyncQueryError(
            "Async query failed",
            handle="query-handle-123",
            query_status="failed"
        )
        
        assert error.handle == "query-handle-123"
        assert error.query_status == "failed"
        assert error.context['async_handle'] == "query-handle-123"
        assert error.context['query_status'] == "failed"


class TestErrorMapper:
    """Test the ErrorMapper utility class."""
    
    def test_http_response_mapping_success(self):
        """Test successful HTTP response mapping."""
        # Mock response with AsterixDB error
        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.text = json.dumps({
            "errors": [{"code": "ASX1001", "msg": "Syntax error in query"}]
        })
        mock_response.url = "http://localhost:19002/query/service"
        
        with patch('json.loads') as mock_json:
            mock_json.return_value = {
                "errors": [{"code": "ASX1001", "msg": "Syntax error in query"}]
            }
            
            error = ErrorMapper.from_http_response(mock_response)
            
            assert isinstance(error, SyntaxError)
            assert error.error_code == "ASX1001"
            assert "Syntax error in query" in str(error)
            assert error.context['http_status_code'] == 400
    
    def test_http_response_mapping_no_asterix_error(self):
        """Test HTTP response mapping without AsterixDB error structure."""
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.text = "Internal Server Error"
        mock_response.url = "http://localhost:19002/query/service"
        
        error = ErrorMapper.from_http_response(mock_response)
        
        assert isinstance(error, InternalError)
        assert error.context['http_status_code'] == 500
        assert "Internal Server Error" in str(error)
    
    def test_http_response_mapping_malformed_json(self):
        """Test HTTP response mapping with malformed JSON."""
        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.text = "Invalid JSON {{"
        mock_response.url = "http://localhost:19002/query/service"
        
        error = ErrorMapper.from_http_response(mock_response)
        
        # Should fall back to HTTP status code mapping
        assert isinstance(error, SyntaxError)  # 400 maps to SyntaxError
        assert error.context['http_status_code'] == 400
    
    def test_asterix_error_response_mapping(self):
        """Test mapping of AsterixDB error response structure."""
        response_data = {
            "errors": [
                {
                    "code": "ASX1073",
                    "msg": "Cannot resolve alias reference for undefined identifier"
                }
            ],
            "status": "failed"
        }
        
        error = ErrorMapper.from_asterix_error_response(response_data, 400)
        
        assert isinstance(error, IdentifierError)
        assert error.error_code == "ASX1073"
        assert "Cannot resolve alias reference" in str(error)
        assert error.context['asterix_error_code'] == "ASX1073"
        assert error.context['http_status_code'] == 400
    
    def test_asterix_error_response_no_code(self):
        """Test mapping of AsterixDB error without explicit code."""
        response_data = {
            "errors": ["ASX0002: Type mismatch in function parameter"],
            "status": "failed"
        }
        
        error = ErrorMapper.from_asterix_error_response(response_data)
        
        assert isinstance(error, TypeMismatchError)
        assert error.error_code == "ASX0002"
        assert "Type mismatch" in str(error)
    
    def test_network_error_mapping(self):
        """Test network error mapping."""
        # Test with mock exception that mimics requests.ConnectionError
        import sys
        
        # Create a mock requests module with exceptions
        mock_requests = Mock()
        mock_requests.exceptions.ConnectionError = type('ConnectionError', (Exception,), {})
        mock_requests.exceptions.Timeout = type('Timeout', (Exception,), {})
        mock_requests.exceptions.HTTPError = type('HTTPError', (Exception,), {})
        
        # Patch the import inside the function
        with patch.dict('sys.modules', {'requests': mock_requests}):
            # Test ConnectionError
            original_error = mock_requests.exceptions.ConnectionError("Connection refused")
            error = ErrorMapper.from_network_error(original_error)
            
            assert isinstance(error, NetworkError)
            assert "Connection failed" in str(error)
            assert error.context['original_error_type'] == 'ConnectionError'
            
            # Test Timeout
            timeout_error = mock_requests.exceptions.Timeout("Request timed out")
            error = ErrorMapper.from_network_error(timeout_error)
            
            assert isinstance(error, TimeoutError)
            assert "Request timed out" in str(error)
            
            # Test generic network error
            generic_error = Exception("Generic network error")
            error = ErrorMapper.from_network_error(generic_error)
            
            assert isinstance(error, NetworkError)
            assert "Network error" in str(error)
    
    def test_json_error_mapping(self):
        """Test JSON parsing error mapping."""
        json_error = json.JSONDecodeError("Expecting value", "invalid json", 0)
        response_text = "Invalid JSON content"
        
        error = ErrorMapper.from_json_error(json_error, response_text)
        
        assert isinstance(error, ResultProcessingError)
        assert "Failed to parse JSON response" in str(error)
        assert error.context['original_error_type'] == 'JSONDecodeError'
        assert error.context['response_text'] == response_text
        assert error.context['response_length'] == len(response_text)
    
    def test_validation_error_mapping(self):
        """Test validation error mapping."""
        error = ErrorMapper.from_validation_error(
            "username", 
            "invalid@username", 
            "invalid_characters"
        )
        
        assert isinstance(error, DataError)
        assert "Validation failed for field 'username'" in str(error)
        assert error.context['field_name'] == 'username'
        assert error.context['field_value'] == 'invalid@username'
        assert error.context['validation_type'] == 'invalid_characters'


class TestAsyncErrorMapper:
    """Test the AsyncErrorMapper utility class."""
    
    def test_failed_status_mapping(self):
        """Test mapping of failed async query status."""
        status_data = {
            "status": "failed",
            "errors": [{"code": "ASX1001", "msg": "Syntax error"}],
            "handle": "query-123"
        }
        
        error = AsyncErrorMapper.from_async_status(status_data, "query-123")
        
        assert isinstance(error, SyntaxError)  # Should use main error mapper
        assert error.error_code == "ASX1001"
    
    def test_timeout_status_mapping(self):
        """Test mapping of timeout async query status."""
        status_data = {
            "status": "timeout",
            "handle": "query-123"
        }
        
        error = AsyncErrorMapper.from_async_status(status_data, "query-123")
        
        assert isinstance(error, AsyncTimeoutError)
        assert "Async query timed out" in str(error)
        assert error.context['async_handle'] == "query-123"
        assert error.context['query_status'] == "timeout"
    
    def test_unknown_status_mapping(self):
        """Test mapping of unknown async query status."""
        status_data = {
            "status": "weird_status",
            "handle": "query-123"
        }
        
        error = AsyncErrorMapper.from_async_status(status_data, "query-123")
        
        assert isinstance(error, AsyncQueryError)
        assert "Unexpected async query status" in str(error)
        assert error.handle == "query-123"
        assert error.query_status == "weird_status"


class TestBackwardCompatibility:
    """Test backward compatibility with legacy exception names."""
    
    def test_legacy_exception_usage(self):
        """Test that legacy exception names still work."""
        # These should not raise ImportError and should work as expected
        try:
            raise ConnectionError("Legacy connection error")
        except NetworkError as e:
            assert "Legacy connection error" in str(e)
        
        try:
            raise QueryError("Legacy query error")
        except AsyncQueryError as e:
            assert "Legacy query error" in str(e)
        
        try:
            raise ValidationError("Legacy validation error")
        except DataError as e:
            assert "Legacy validation error" in str(e)
        
        try:
            raise TypeMappingError("Legacy type mapping error")
        except TypeMismatchError as e:
            assert "Legacy type mapping error" in str(e)


class TestExceptionIntegration:
    """Test exception integration with driver components."""
    
    def test_exception_context_preservation(self):
        """Test that exception context is preserved through the stack."""
        original_context = {
            "query": "SELECT * FROM test",
            "timeout": 30,
            "operation": "query_execution"
        }
        
        error = NetworkError("Connection failed", context=original_context)
        
        # Context should be preserved
        assert error.context == original_context
        assert error.context['query'] == "SELECT * FROM test"
        assert error.context['timeout'] == 30
        assert error.context['operation'] == "query_execution"
    
    def test_error_serialization_roundtrip(self):
        """Test that errors can be serialized and deserialized."""
        original_error = HTTPError(
            "HTTP 500 error",
            status_code=500,
            response_text="Internal Server Error",
            error_code="HTTP500",
            context={"url": "http://localhost:19002/query/service"}
        )
        
        # Serialize to dict
        error_dict = original_error.to_dict()
        
        # Verify all information is preserved
        assert error_dict['type'] == 'HTTPError'
        assert error_dict['message'] == 'HTTP 500 error'
        assert error_dict['error_code'] == 'HTTP500'
        assert error_dict['context']['url'] == "http://localhost:19002/query/service"
        assert error_dict['context']['http_status_code'] == 500
    
    def test_exception_chaining(self):
        """Test exception chaining and cause preservation."""
        try:
            # Simulate nested exception scenario
            try:
                raise ValueError("Original error")
            except ValueError as e:
                raise NetworkError("Network operation failed") from e
        except NetworkError as network_error:
            assert network_error.__cause__ is not None
            assert isinstance(network_error.__cause__, ValueError)
            assert "Original error" in str(network_error.__cause__)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
