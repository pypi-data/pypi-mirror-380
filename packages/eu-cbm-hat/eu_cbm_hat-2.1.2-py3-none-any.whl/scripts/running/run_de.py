#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Written by Lucas Sinclair and Paul Rougieux.

JRC Biomass Project.
Unit D1 Bioeconomy.

A script to run Luxembourg.

Typically you would run this file from a command line like this:

     ipython3 -i -- ~/eu_cbm/eu_cbm_hat/scripts/running/run_de.py

"""

from eu_cbm_hat.core.continent import continent
runner = continent.combos['reference'].runners['DE'][-1]
runner.num_timesteps = 2070 - runner.country.inventory_start_year
output = runner.run(keep_in_ram=True, verbose=True, interrupt_on_error=True)



