# encoding: utf-8

##################################################
# This script shows uses the pandas and matplotlib libraries to produce different kind of plots
# It also combines data from two sources and create multiple plots
# Find extra documentation about data frame here:
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.scatter.html
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

# We need to import pandas library as well as the plot library matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# We read the file for population data and gross domestic product
amb_mplts = pd.read_csv('../data/catalunya/AMB_municipalities_min.csv')
lu_mplts = pd.read_csv('../data/luxembourg/population.csv', skiprows=[2,3])

# First, we filter data for a single country, mind the way to select only columns having numeric data
pop_cat = amb_mplts['population']
area_cat = amb_mplts['area']

pop_lu = lu_mplts[['Year', '2020']]
pop_lu.columns = ['canton', 'population']

pop_lu_1821 = lu_mplts[['Year', '1821']]
pop_lu_1821.columns = ['canton', 'population']

# Plots allow basic configuration of visual features. Here some of the most common
colors = np.random.rand(len(pop_cat))
plt.scatter(x=pop_cat, y=area_cat, c=colors)
plt.show()


# Charts can also use lines to represent patterns from different subsets
for value in lu_mplts['Year']:
    a_pop = lu_mplts[lu_mplts['Year'] == value]
    a_pop = a_pop.iloc[0, 1:15]
    plt.plot(a_pop)
plt.show()

# try to customise axis
#plt.xticks(np.arange(0, 2020, 100))
plt.yticks(np.arange(0,175000, 50000))


# There are different ways to represent data density,
# this 2d histogram shows population and area distribution
plt.hist2d(pop_cat, area_cat)
plt.show()


# We can create the arrangement for multiple plots and compare the differences in patterns
fig, axs = plt.subplots(2, 2, sharex=False, sharey=False)
axs[0, 0].scatter(x=pop_cat, y=area_cat, c=colors)
axs[1, 0].hist2d(pop_cat, area_cat, bins=20)
axs[0, 1].scatter(x=pop_lu['population'], y=pop_lu_1821['population'])
axs[1, 1].hist2d(x=pop_lu['population'], y=pop_lu_1821['population'], bins=20)
plt.show()

# We can create the arrangement for multiple plots and compare the differences in patterns
fig, axs = plt.subplots(1, 2, sharex=True, sharey=True)
axs[0].scatter(x=pop_lu['population'], y=pop_lu_1821['population'])
axs[1].hist2d(x=pop_lu['population'], y=pop_lu_1821['population'], bins=20)
plt.show()

