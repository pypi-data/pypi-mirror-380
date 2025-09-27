"""
Tests for the ChartBeautifierClient.
"""

import pytest
from chart_beautifier import ChartBeautifierClient
from chart_beautifier.exceptions import ValidationError


class TestChartBeautifierClient:
    """Test cases for ChartBeautifierClient."""
    
    def test_init_with_valid_api_key(self):
        """Test client initialization with valid API key."""
        client = ChartBeautifierClient(api_key="test_key")
        assert client.api_key == "test_key"
        assert client.base_url == "https://api.chartbeautifier.com"
    
    def test_init_with_custom_base_url(self):
        """Test client initialization with custom base URL."""
        client = ChartBeautifierClient(
            api_key="test_key", 
            base_url="https://custom.api.com"
        )
        assert client.base_url == "https://custom.api.com"
    
    def test_init_with_empty_api_key_raises_error(self):
        """Test that empty API key raises ValidationError."""
        with pytest.raises(ValidationError):
            ChartBeautifierClient(api_key="")
    
    def test_init_with_none_api_key_raises_error(self):
        """Test that None API key raises ValidationError."""
        with pytest.raises(ValidationError):
            ChartBeautifierClient(api_key=None)
    
    def test_create_chart(self):
        """Test chart creation."""
        client = ChartBeautifierClient(api_key="test_key")
        data = {"labels": ["A", "B", "C"], "datasets": [{"data": [1, 2, 3]}]}
        
        result = client.create_chart(data, chart_type="line")
        
        assert "chart_id" in result
        assert result["chart_type"] == "line"
        assert result["status"] == "created"
    
    def test_get_chart(self):
        """Test chart retrieval."""
        client = ChartBeautifierClient(api_key="test_key")
        
        result = client.get_chart("test_chart_id")
        
        assert result["chart_id"] == "test_chart_id"
        assert result["status"] == "active"
    
    def test_update_chart(self):
        """Test chart update."""
        client = ChartBeautifierClient(api_key="test_key")
        updates = {"title": "Updated Chart"}
        
        result = client.update_chart("test_chart_id", updates)
        
        assert result["chart_id"] == "test_chart_id"
        assert result["status"] == "updated"
    
    def test_delete_chart(self):
        """Test chart deletion."""
        client = ChartBeautifierClient(api_key="test_key")
        
        result = client.delete_chart("test_chart_id")
        
        assert result is True
