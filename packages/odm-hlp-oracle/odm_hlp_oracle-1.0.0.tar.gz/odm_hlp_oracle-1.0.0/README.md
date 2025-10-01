# ODM Oracle Helper

Oracle database utilities for ETL operations with decorators.

## Installation

```bash
pip install odm-hlp-oracle
```

## Usage

```python
from odm_hlp_oracle import get_engine, load, call_procedure

# Get Oracle engine
engine = get_engine('dev', 'stg')

# Load data to table
load(engine, dataframe, 'table_name', dtype_dict)

# Call stored procedure
result = call_procedure(engine, 'procedure_name', [param1, param2])
```

## Requirements

- Python 3.8+
- oracledb
- sqlalchemy  
- odm-hlp-decorations

## Configuration

Create a `.env` file with Oracle connection parameters:
```
dev_odm_tns=localhost:1521/XEPDB1
odm_usr_stg=username
odm_pass_stg=password
logs_path=./logs/
```

## License

MIT