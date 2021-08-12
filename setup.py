from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name="EEA-datasets-handler",
  version="0.0.4",
  py_modules =["EEA_datasets_handler"],
  description="Library which handles the air pollution datasets provided by EEA",
  long_description=long_description,
  long_description_content_type='text/markdown',
  url="https://github.com/EnricoPittini/EEA-datasets-handler",
  author="Enrico Pittini",
  author_email="pittinienrico@hotmail.it",
  license="MIT",
  install_requires=['requests',
                    'pandas'],
  classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
)
