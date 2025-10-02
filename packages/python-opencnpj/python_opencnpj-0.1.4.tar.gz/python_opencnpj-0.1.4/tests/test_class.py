import pytest
from opencnpj import OpenCnpj
from opencnpj.exceptions import InvalidCNPJError, CNPJNotFoundError, OpenCNPJError

cnpj = OpenCnpj()

def test_format_cnpj():
    result = cnpj.format_cnpj("12345678910111")
    assert result == "12.345.678/9101-11"

def test_format_invalid_cnpj():
    with pytest.raises(InvalidCNPJError):
        cnpj.format_cnpj("123")

def test_format_not_string_cnpj():
    with pytest.raises(OpenCNPJError):
        cnpj.get(12345678912345)
        cnpj.get['2', 2, 1]
    
def test_get_not_string_cnpj():
    with pytest.raises(OpenCNPJError):
        cnpj.get(12345678912345)
        cnpj.get['2', 2, 1]

def test_get_not_found_cnpj():
    with pytest.raises(CNPJNotFoundError):
        cnpj.get("12345678912345")

def test_get_invalid_cnpj():
    with pytest.raises(InvalidCNPJError):
        cnpj.get("123")