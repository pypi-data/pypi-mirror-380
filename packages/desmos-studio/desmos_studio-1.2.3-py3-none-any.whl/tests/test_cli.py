import pytest
import tempfile
import os
from pathlib import Path
from image2curves.cli import Image2Curves

def test_image2curves_init():
    """Test basic initialization"""
    converter = Image2Curves()
    assert converter.temp_files == []

def test_cleanup():
    """Test cleanup functionality"""
    converter = Image2Curves()
    
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        temp_path = temp.name
        converter.temp_files = [temp_path]
    
    # File should exist
    assert os.path.exists(temp_path)
    
    # Cleanup should remove it
    converter.cleanup()
    assert not os.path.exists(temp_path)
