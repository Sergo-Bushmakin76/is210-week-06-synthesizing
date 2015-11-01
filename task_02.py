#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Prepare data as if sending automated emails."""


def prepare_email(appointments):
    """Runs a for loop to send out email responses.

    Args:
        appointments(mixed): name and date.

    Returns:
        mixed: auto response email with info filled out properly.

    Examples:
        
    """
    
    email = ('Dear {},\nI look forward to meeting with you on {}.\nBest, \nMe')
    appointments = []
    for items in appointments:
        appointments.append(email.format(items[0], items[1]))
    return email

