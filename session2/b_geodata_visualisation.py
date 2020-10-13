# encoding: utf-8

##################################################
# This script summarises text variables by creating wordclouds. It uses a python library that needs to be installed
# in the virtual environment beforehand through anaconda. This exercise aims to show the basic analysis tool
# used for text as well as to test the work environment.
# To install wordcloud see the documentation here https://pypi.org/project/wordcloud/
##################################################
#
##################################################
# Author: Diego Pajarito
# Copyright: Copyright 2019, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Diego Pajarito
# Email: diego.pajarito@iaac.net
# Status: development
##################################################

# Libraries
import geopandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

# read geospatial data
municipalities_geojson = '../data/catalunya/municipalities.geojson'
municipalities = geopandas.read_file(municipalities_geojson)

# Create a view using geospatial data
municipalities.plot(color='None', edgecolor='gray', linewidth=0.8)
