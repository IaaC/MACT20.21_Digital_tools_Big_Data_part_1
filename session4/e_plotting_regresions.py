# encoding: utf-8

##################################################
# This script shows uses the pandas library to create statistically describe data sets
# It also shows basic plotting features
# Find extra documentation about data frame here:
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
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

# We need to import pandas library as well as the plot libraries matplotlib and seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# We read the file for population data
pop_cat = pd.read_csv('../data/catalunya/AMB_municipalities_min.csv')

# Range is the combination of min-max values
print('####################')
print('This is an example of calculations based on existing data:')
pop_cat['density'] = pop_cat['population'] / pop_cat['area']


# plot correlation
# ====================================
sns.set_style('ticks')

# Area vs. population
# You can also try removing the confidence interval
# sns.regplot(pop_cat['area'], pop_cat['population'], ci=None)
sns.regplot(x=pop_cat['area'], y=pop_cat['population'])
sns.despine()
plt.show()

sns.regplot(x=pop_cat['area'], y=pop_cat['density'])
sns.despine()
plt.show()

sns.regplot(x=pop_cat['population'], y=pop_cat['density'])
sns.despine()
plt.show()

# rate of growth



