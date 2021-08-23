# EEA-datasets-handler
Library which handles the air pollution datasets provided by [EEA](https://www.eea.europa.eu/data-and-maps/data/aqereporting-8).

There are three groups of functions.
1. Functions to get the EEA supported values.
2. Functions to filter only the EEA supported values.
3. Functions to download and handle the EEA datasets.

This library is part of my bachelor thesis, check out the other works.
- [ILMETEO-datasets-handler](https://github.com/EnricoPittini/ILMETEO-datasets-handler)
- [model-selection](https://github.com/EnricoPittini/model-selection)
- [timeSeries-processing](https://github.com/EnricoPittini/timeSeries-processing)
- [Air-quality-prediction](https://github.com/EnricoPittini/Air-quality-prediction)

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install EEA-datasets-handler.

```bash
pip install EEA-datasets-handler
```

## Main usage

```python
import EEA_datasets_handler as eea

# Download the datasets
dest_path = "C:\\Datasets"
countries_cities_dict = {"IT":["Milano","Venezia"],
                         "CY":"all",
                         "AT":["Lienz","Wien"],
                         "GB":["London"]}
pollutants = ["PM10", "PM15"]
years = [2015, 2020]
eea.download_datasets(dest_path, countries_cities_dict, pollutants, years)

# Load the datasets into a raw pandas DataFrame
source_path = "C:\\Datasets\\EEA"
countries_cities_dict = {"IT":["Milano"]}
pollutants = ["PM10"]
years = [2020]
df = eea.load_datasets(source_path, countries_cities_dict, pollutants, years)

# Preprocess the DataFrame into time series DataFrames
df_mean, df_min, df_max = eea.preprocessing(df, fill=True)
```

# References
- [EEA](https://www.eea.europa.eu/). The European Environment Agency (EEA) is an agency of the European Union, whose task is to provide sound, independent information on the environment.
- [pandas](https://pandas.pydata.org/) is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
built on top of the Python programming language.
- [requests](https://docs.python-requests.org/en/master/) is an elegant and simple HTTP library for Python, built for human beings.

## License
[MIT](https://choosealicense.com/licenses/mit/)
