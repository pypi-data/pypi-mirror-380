#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Written by Lucas Sinclair and Paul Rougieux.

JRC Biomass Project.
Unit D1 Bioeconomy.

This script loads the harvest that originates from the economic model
called "GFTMX". This economic model is not run dymamically, instead it
was run once in the past and the outputs recorded in the `eu_cbm_data`
repository.

The wood product harvest used in the `eu_cbm_hat` simulations is seen as the
production from the perspective of the economic model.

Usage:

    >>> from eu_cbm_hat.info.harvest import gftm_outputs
    >>> from eu_cbm_hat.info.harvest import combined

Related issues:

* https://gitlab.com/bioeconomy/eu_cbm/eu_cbm_hat/-/issues/8

This script provides a dictionary `gftm_outputs` that looks like this:

    'reference':   {'irw': <OutputGFTM object>,
                    'fw':  <OutputGFTM object>},
    'market_drop': {'irw': <OutputGFTM object>,
                    'fw':  <OutputGFTM object>}, ...}

It also provides a `combined` dictionary.
"""

# Built-in modules #

# Third party modules #
import pandas

# First party modules #
from plumbing.cache import property_cached

# Internal modules #
from eu_cbm_hat.constants import eu_cbm_data_dir
from eu_cbm_hat.core.country import all_country_codes

# Constant directory for all the data #
harvest_dir = eu_cbm_data_dir + 'domestic_harvest/'

# Constant file names for every scenario #
roundwood = "irw_harvest.csv"
fuelwood  = "fw_harvest.csv"

# A mapping between country names and codes #
country_to_iso2 = all_country_codes[['country', 'iso2_code']]

""
def wide_to_long(df):
    """Convert a harvest dataset to the long format."""
    # List columns for pivot #
    cols = ['faostat_name', 'element', 'unit', 'country']
    # Convert #
    df = pandas.wide_to_long(df,
                             stubnames = 'value',
                             i         = cols,
                             j         = 'year',
                             sep       = '_')
    # Reset index #
    df = df.reset_index()
    # Return #
    return df

""
class OutputGFTM:
    """
    Access to the raw harvest coming from the GFTM model, for a particular
    scenario and a particular wood type. We also provide a filtered and
    transformed version of the data.
    """

    def __init__(self, scenario, csv_name):
        self.scenario = scenario
        self.csv_name = csv_name

    @property_cached
    def csv_path(self):
        return harvest_dir + self.scenario + '/' + self.csv_name

    @property
    def raw(self):
        return pandas.read_csv(self.csv_path)

    @property_cached
    def df(self):
        # Load #
        df = self.raw
        # Wide to long transform #
        df = wide_to_long(df)
        # Add country codes (and remove all unknown countries) #
        df = df.merge(country_to_iso2, on='country')
        # Remove other columns that give no information #
        df = df[['iso2_code', 'year', 'value']]
        # Return #
        return df

""
class Demand:
    """
    Access the specific harvest values for the current simulation run.
    For both industrial roundwood and fuelwood.
    """

    def __init__(self, parent):
        # Default attributes #
        self.parent = parent
        self.runner = parent
        # Shortcuts #
        self.combo = self.runner.combo
        self.code  = self.runner.country.iso2_code
        # Choices made for harvest in the current combo #
        self.choices = self.combo.config['harvest']

    def make_df(self, wood_type):
        # Case number 1: there is only a single scenario specified #
        if isinstance(self.choices, str):
            df = gftm_outputs[self.choices][wood_type].df
        # Case number 2: the scenarios picked vary according to the year #
        else:
            df = self.choices.merge(combined[wood_type],
                                    how = 'left',
                                    on = ['year', 'scenario'])
        # Filter for current country #
        df = df.query("iso2_code == '%s'" % self.code)
        # Check there is data left #
        assert not df.empty
        # Return #
        return df

    #----------------------------- Properties --------------------------------#
    @property_cached
    def irw(self): return self.make_df('irw')
    @property_cached
    def fw(self):  return self.make_df('fw')

###############################################################################
# Figure out all possible harvest scenarios that we have #
scenarios = [d.name for d in harvest_dir.flat_directories if d]

# Load all the GFTM outputs for every scenario and every wood type #
gftm_outputs = {scen: {'irw': OutputGFTM(scen, roundwood),
                       'fw':  OutputGFTM(scen, fuelwood)}
                for scen in scenarios}

# A function to combine all scenarios together for a given wood type #
def make_combined(wood_type):
    df = [out[wood_type].df for out in gftm_outputs.values()]
    df = pandas.concat(df, keys=scenarios, names=['scenario'])
    df = df.reset_index(level='scenario').reset_index(drop=True)
    return df

# Provide two dataframes that contain all scenarios combined #
combined = {'irw': make_combined('irw'),
            'fw':  make_combined('fw')}
