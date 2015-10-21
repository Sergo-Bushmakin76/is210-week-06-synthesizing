#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Returns headcount and number of tables needed."""


def get_party_stats(families, table_size=6):
    """
    """
    number_of_guests = 0
    number_of_tables = 0
    for guests in families:
        number_of_guests += len(guests)
        number_of_tables += -(-len(guests) // table_size)
    return (number_of_guests, number_of_tables)
