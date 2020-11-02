# encoding: utf-8

##################################################
# This script shows uses the pandas library to create statistically describe datasets
# It also shows basic plotting features
# Find extra documentation about data frame here:
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
##################################################
#
##################################################
# Author: Diego Pajarito
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Diego Pajarito
# Email: diego.pajarito@iaac.net
# Status: development
##################################################

# We need to import pandas library
import pandas as pd

# We read the data file for population data
a_df = pd.read_csv('../alvarocerezo/dataexport_20201102T170744.csv')

# Range is the combination of min-max values
print('####################')
print('This is an example of the range values for temperature in Luxembourg:')
lux = a_df['Luxembourg_Temperature']
min_value = lux.min()
max_value = lux.max()
print('Temperature ranged between %i and %i' % (min_value, max_value))

# There are a set of statistics to descibe central tendency
mean_value = lux.mean()
mode_value = lux.mode()
median_value = lux.median()
print('####################')
print('The three values for the central tendency of temperature in Luxembourg are:')
print('Mean temperature: %i' % mean_value)
print('Mode temperature: %s' % str(mode_value))
print('Median temperature: %i' % median_value)



# There are statistical values for dispersion
variance_value = lux.var()
stdev_value = lux.std()
print('####################')
print('The two values for the central tendency of temperature in Luxembourg are:')
print('Variance: %f' % variance_value)
print('Standard deviation: %f' % stdev_value)


# Work on differences across the years but especially across municipalities
