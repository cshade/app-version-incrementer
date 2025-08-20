import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import pytest
from increment_app_version import increment_version

def test_increment_major():
    assert increment_version("1.2.3", "major") == "2.0.0"
    assert increment_version("0.0.9", "major") == "1.0.0"

def test_increment_minor():
    assert increment_version("1.2.3", "minor") == "1.3.0"
    assert increment_version("2.9.9", "minor") == "2.10.0"

def test_increment_patch():
    assert increment_version("1.2.3", "patch") == "1.2.4"
    assert increment_version("0.0.0", "patch") == "0.0.1"

def test_invalid_part():
    with pytest.raises(ValueError):
        increment_version("1.2.3", "invalid")
