from setuptools import setup

setup(
  name="EEA-datasets-handler",
  version="0.0.3",
  py_modules =["EEA_datasets_handler"],
  description="Library which handles the air pollution datasets provided by EEA",
  url="https://github.com/EnricoPittini/EEA-datasets-handler",
  author="Enrico Pittini",
  author_email="pittinienrico@hotmail.it",
  license="MIT",
  install_requires=['requests',
                    'pandas'],
)
