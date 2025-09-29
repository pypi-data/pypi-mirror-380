
import pytest
from pathlib import Path
import binscheme_parser
from binscheme_parser import data_structures as ds

@pytest.fixture
def complex_scheme_path():
    return Path(__file__).parent / "fixtures" / "complex.binscheme"

@pytest.fixture
def complex_schema_collection(complex_scheme_path):
    return binscheme_parser.load(complex_scheme_path)

def test_load_complex_scheme(complex_schema_collection):
    assert complex_schema_collection is not None
    assert len(complex_schema_collection.schemes) == 2
    assert len(complex_schema_collection.instances) == 2

def test_simple_instance(complex_schema_collection):
    instance1 = complex_schema_collection.instances["instance1"]
    assert instance1.name == "instance1"
    assert instance1.scheme_name == "Simple"
    assert instance1.values["a"] == 10
    assert instance1.values["b"] == 20

def test_complex_instance(complex_schema_collection):
    complex_instance = complex_schema_collection.instances["complex_instance"]
    assert complex_instance.name == "complex_instance"
    assert complex_instance.scheme_name == "Complex"
    assert complex_instance.values["count"] == 2
    simples = complex_instance.values["simples"]
    assert isinstance(simples, list)
    assert len(simples) == 2
    assert simples[0] == {"a": 1, "b": 2}
    assert simples[1] == {"a": 3, "b": 4}

