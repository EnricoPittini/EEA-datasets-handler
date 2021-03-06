# EEA-datasets-handler
Library for handling the air pollution datasets provided by [EEA](https://www.eea.europa.eu/data-and-maps/data/aqereporting-8).

This library is part of my bachelor thesis, check out the other works.
- [ILMETEO-datasets-handler](https://github.com/EnricoPittini/ILMETEO-datasets-handler)
- [model-selection](https://github.com/EnricoPittini/model-selection)
- [timeSeries-processing](https://github.com/EnricoPittini/timeSeries-processing)
- [Air-quality-prediction](https://github.com/EnricoPittini/Air-quality-prediction)

## Description
The two main purposes of this library are the following.
The first is to allow the user to download the EEA datasets, in an intuitive and easy way.
The second is to allow the user to process the downloaded datasets into a properly cleaned and prepared pandas DataFrame.

### Guiding principles
The functionalities of this library are built in order to have an interface similar to the one of the [EEA download service](https://discomap.eea.europa.eu/map/fme/AirQualityExport.htm).
The aim of that is to have a set of functionalities which interact with the EEA services from python using the same interface exposed by the EEA itself.
For example, in the EEA interface a user can specify a pollutant using either the numeric notation or the textual one: this feature is kept in the library.

Actually, that interface is even improved. It is made richier and more flexible, in order to facilitate and reduce the user work.
The aim of that is to automate the interaction with the EEA services.
For example, if a user wants to download all the datasets about PM10 in Italy, he doesn’t have to download the dataset of each Italian city one at a time. The user can simply specify that he is interested in all the Italian cities.

Finally, this library is built in order to appropriately warn the user. The user is informed each time he specifies an inappropriate value. In addition, he is also warned each time the action requested is not performed correctly or completely.

### Functionalities
There are three groups of functionalities.

The first group allows the user to know the EEA supported values, by getting them.
The supported values are the values used by the EEA interface. So, in other words, these are the values that the user is allowed to use in order to specify which air pollution datasets are of interest.
There are three kinds of values.
- Years.
- Pollutants.
- Countries and cities. For each country there is an associated list of cities. Actually, there are also countries with no associated cities.

The second group of functionalities allows the user to filter only the EEA supported values. Given a collection of values, only the supported values are kept.

Finally, the third group of functionalities is the most important. It allows the user to actually download the air pollution datasets in his local storage.
Each downloaded dataset is a csv file. Its name has the following structure:
NationCode_CityName_PollutantId_Year_StationId.csv
where the station is the physical place where the air pollution measurements have been made.
This quadruple is an unique identifier of the dataset.
In addition, an appropriate and straightforward structure of directories is built, in order to keep the datasets well organized. If this structure already exists in the local storage, that structure is used ( i.e. a new structure is not created) and the datasets with the same quadruple are overwritten.

Inside the third group there are other important  functionalities.
These allow the user to retrieve and delete the downloaded datasets.
In addition, they allow the user to load the downloaded datasets into a single pandas DataFrame. This is a raw DataFrame, since it simply contains the air pollution measurements (i.e. the measurements are not grouped by day).
Finally, these functionalities allow the user to process the loaded pandas DataFrame into a properly cleaned and prepared new DataFrame. This returned DataFrame is a time series DataFrame, since the measurements are grouped by day.

It is important to notice that, while the raw DataFrame contains several useless features (i.e. features which are simply EEA codes and indicators), the time series DataFrame contains only the air pollution concentrations. In other words, the returned DataFrame is ready to be used.

### Implementation details
In this section, the most significant implementation details are described.

First of all, it is described how the EEA supported values are mainly represented.
It is important to underline that only the python built-in data structures are used.
- The supported years are represented as a list of integers.
- The supported pollutants are mainly represented as a list of integers, which are the pollutants numeric notations.
In addition, the supported pollutants are also represented as a dictionary, which maps the pollutants numeric notations into the pollutants textual notations (i.e. it is a map from strings to strings).
- The supported countries and the associated lists of cities are represented as a dictionary, which maps the countries code notations into the lists of cities (i.e.it is a map from strings to lists of strings).
In addition, the supported countries are also represented as a dictionary, which maps the countries code notations into the countries extended notations (i.e. it is a map from strings to strings).
Other additional data structures are available, such as the list of supported countries and the list of all the supported cities.

Secondly, the main functionality of the library, i.e. the one which is responsible for downloading the datasets, is built on top of the EEA download service.
This means that, under the hood, the same service used by the EEA users is utilized.

The retrieving of the downloaded datasets is performed in a recursive manner. Given the structure of directories where the datasets have been downloaded, the research is firstly carried out on the parent directory and then it is propagated on each sub-folder.

Finally, the cleaning of the data is mainly performed according to the EEA indications. In fact, the EEA feature “Validity” indicates the reliability of the measurements: a positive value means that the measurement is valid.
In addition, other cleaning operations are performed, in order to guarantee the consistency of the data.

### Sources
The supported pollutants have been taken from the official [EEA dataset](http://dd.eionet.europa.eu/vocabulary/aq/pollutant/view?page=7#vocabularyConceptResults), which contains all the pollutants and the related information.
This dataset has been properly processed, in order to keep only the relevant information and in order to build the data structures mentioned above.

Instead, the supported years have been simply taken from the Web page of the EEA downloading service.

Also the supported countries and the associated lists of supported cities have been simply taken from that page.
Actually, this information is taken from the HTML document and from the associated JavaScript file.
From this information, the data structures mentioned above are built.


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

## References
- [EEA](https://www.eea.europa.eu/). The European Environment Agency (EEA) is an agency of the European Union, whose task is to provide sound, independent information on the environment.
- [pandas](https://pandas.pydata.org/) is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
built on top of the Python programming language.
- [requests](https://docs.python-requests.org/en/master/) is an elegant and simple HTTP library for Python, built for human beings.

## License
[MIT](https://choosealicense.com/licenses/mit/)
