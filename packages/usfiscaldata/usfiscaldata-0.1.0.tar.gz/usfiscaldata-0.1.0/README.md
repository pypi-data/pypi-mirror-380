# Treaury Fiscal Data API Client for Python

Python client for accessing the [U.S. Treasury Fiscal Data API](https://fiscaldata.treasury.gov/api-documentation/).

## Installation

```bash
python -m pip install usfiscaldata
```

## Usage

### Example

```python
from usfiscaldata import FiscalData, Filter

client = FiscalData()
endpoint = client.v1.accounting.od.auctions_query
filter_ = Filter()
filter_["record_date"] <= "1984-01-01"
response = endpoint.all(filter=filter_)
df = response.df
print(df.shape)
print(df.head())
```

### Endpoints

The client implements a generic dot-accessor interface for the endpoints, so you need to know the full endpoint path.
The endpoint can also be specified as a string.

```python
from usfiscaldata import FiscalData

client = FiscalData()
endpoint = client.v2.debt.tror.data_act_compliance
endpoint = client("v2/debt/tror/data_act_compliance")
```

### Filters

Filters are specified using a dictionary-like `Filter` object.

```pythonpython
from fiscaldata import Filter
filter_ = Filter()
filter_["record_date"] <= "2000-01-01"
filter_["amount"] > 1000
filter_["fiscal_year"].isin([1999, 2000, 2001])
```

### Response Pagination

The response object contains a `meta` attribute with pagination information, and a `next_page` method to retrieve the next page of results.
When there are no more pages, `next_page` returns `None`.
You can also just call `.all()` as in above example.
