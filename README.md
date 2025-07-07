**First, install Anaconda, miniconda, or some other way of accessing conda environments:
**https://www.anaconda.com/docs/getting-started/miniconda/install
_(If on a machine with ArcGIS Pro, you already have a conda command line- search "Python Command Prompt" in Windows search)_

**Open Anaconda/Miniconda/Python Command Prompt**

**Type in the following command:**

``conda create --name h3 h3-py geopandas shapely pandas -y``

_(installs a conda environment named h3 with packages: h3-py, geopandas, shapely, pandas, and installs them directly)_


Once the environment is created, type the following command:
``conda activate h3``

Then, run the following command:

``python h3conversion.py /path/to/h3.csv --h3_column [COLUMN with H3 ID] --output /path/to/desired/output.geojson`` (or .shp)

Sample Dataset Command Run:
(from within your h3toSHP directory)

``python h3conversion.py sample_data.csv --h3_column h3 --output sample_data.shp``
