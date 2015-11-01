#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Returns headcount and number of tables needed."""


def get_party_stats(families, table_size=6):
    """Runs for loop to determine headcount and tables needed.

    Args:
    families(list): list of families.
    table_size(int): the max number of seats at each table.  Default is six.'

    Returns:
    (int): number of guests.
    (int): number of families.

    Examples:
    >>> get_party_stats([['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis']])
    (6, 3)

    >>> get_party_stats([['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis']], 2)
    (6, 4)
    """
    
    number_of_guests = 0
    number_of_tables = 0
    for guests in families:
        number_of_guests += len(guests)
        number_of_tables += -(-len(guests) // table_size)
    return (number_of_guests, number_of_tables)
