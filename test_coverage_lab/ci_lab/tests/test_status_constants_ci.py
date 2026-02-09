"""
CI Lab - Student Authored Test
Validates HTTP status code constants.
"""
from src.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_404_NOT_FOUND,
    HTTP_405_METHOD_NOT_ALLOWED,
    HTTP_409_CONFLICT,
)

def test_http_status_constants_values():
    """HTTP status constants should match standard numeric codes."""
    assert HTTP_200_OK == 200
    assert HTTP_201_CREATED == 201
    assert HTTP_204_NO_CONTENT == 204
    assert HTTP_404_NOT_FOUND == 404
    assert HTTP_405_METHOD_NOT_ALLOWED == 405
    assert HTTP_409_CONFLICT == 409
