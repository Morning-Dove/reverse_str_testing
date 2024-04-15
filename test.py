import pytest
import main

def test_reverse_string():
    r = main.reverse("string")
    assert r == "gnirts"

    
