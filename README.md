# EEA-datasets-handler
Library which handles the air pollution datasets provided by EEA.

There are three groups of functions.
1. Functions to get the EEA supported values.
2. Functions to filter only the EEA supported values.
3. Functions to download and handle the EEA datasets.
    
This library is part of my bachelor thesis, do check it out the other works.
- [ILMETEO-datasets-handler](https://github.com/EnricoPittini/ILMETEO-datasets-handler) 
- [model-selection](https://github.com/EnricoPittini/model-selection) 
- [timeSeries-processing](https://github.com/EnricoPittini/timeSeries-processing) 

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install EEA-datasets-handler.

```bash
pip install EEA-datasets-handler
```

## Main usage

```python
import EEA_datasets_handler as eea 

# Download datasets
dest_path = "C:\\Datasets"
countries_cities_dict = {"IT":["Milano","Venezia"], 
                         "CY":"all", 
                         "AT":["Lienz","Wien"], 
                         "GB":["London"]}
pollutants = ["PM10", "PM15"]
years = [2015, 2020]
eea.download_datasets(dest_path, countries_cities_dict, pollutants, years)

# Load datasets in a raw pandas DataFrame
source_path = "C:\\Datasets\\EEA"
countries_cities_dict = {"IT":["Milano"]}
pollutants = ["PM10"]
years = [2020] 
df = eea.load_datasets(source_path, countries_cities_dict, pollutants, years)

# Preprocess the DataFrame to time series DataFrames
df_mean, df_min, df_max = eea.preprocessing(df, fill=True)
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
