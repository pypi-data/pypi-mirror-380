# Python OpenCNPJ Library

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Python library to fetch Brazilian CNPJ company data via [OpenCNPJ](https://opencnpj.org/).

---

## 🚀 Features

- Query company information by CNPJ
- Check if a CNPJ exists
- Utility function: Format CNPJ

---

## 📦 Installation

```bash
pip install python-opencnpj  
```

## 🔧 Use cases

### Fetch company informations

```python
from opencnpj import OpenCnpj

# Initialize client
client = OpenCnpj()

data = client.get("12345678000195")

print(data["razao_social"])

```

### Check if CNPJ exists

```python
from opencnpj import OpenCnpj

# Initialize client
client = OpenCnpj()

exists = client.exists("12.345.678/0001-95")

if exists:
    print('Exists!')
else:
    print('Does not exists!')
```

### Format to readable CNPJ

```python
from opencnpj import OpenCnpj

# Initialize client
client = OpenCnpj()

read_cnpj = client.format_cnpj("123456780001-95")

print(read_cnpj)

#### OUTPUT ####
# - 12.345.678/0001-95
```

## Working under a proxy server

```python
from opencnpj import OpenCnpj

proxies = {
    "http": "http://your_proxy_ip:port",
    "https": "http://your_proxy_ip:port",
}

# Initialize client
client = OpenCnpj(proxies=proxies)

data = client.get("123456780001-95")