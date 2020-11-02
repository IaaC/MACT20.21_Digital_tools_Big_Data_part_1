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
a_df = pd.read_csv('../data/catalunya/AMB_municipalities_min.csv')

# Range is the combination of min-max values
print('####################')
print('This is an example of the range values for population in Catalunya:')
pop = a_df['population']
min_value = pop.min()
max_value = pop.max()
print('Population ranged between %i and %i' % (min_value, max_value))

# There are a set of statistics to descibe central tendency
mean_value = pop.mean()
mode_value = pop.mode()
median_value = pop.median()
print('####################')
print('The three values for the central tendency of population in Catalunya are:')
print('Mean population: %i' % mean_value)
print('Mode population: %s' % str(mode_value))
print('Median population: %i' % median_value)



# There are statistical values for dispersion
variance_value = pop.var()
stdev_value = pop.std()
print('####################')
print('The two values for the central tendency of population in Catalunya are:')
print('Variance: %f' % variance_value)
print('Standard deviation: %f' % stdev_value)


# Work on differences across the years but especially across municipalities
