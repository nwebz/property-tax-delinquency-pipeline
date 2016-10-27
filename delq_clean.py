#!/usr/bin/env python

from __future__ import print_function
import petl
import phila_delinquents
import sys

import logging


# Import dataset
table = petl.fromcsv(delimiter='|')


# Verify sure that the header is as we expect
header = tuple(name.strip() for name in table.header())
if header != phila_delinquents.ORIGINAL_HEADER:
    logging.error('Unexpected table header: {}'.format(header))
    sys.exit(1)


# Apply the transformations:
# 1) replace the header.
# 2) replace occurrences of "NULL" with None.
# 3) apply hyphenate to select cols.

def hyphenate(dtstr):
    '''format a string with hyphens'''
    if dtstr and len(dtstr) > 6:
        assert 1 <= int(dtstr[4:6]) <= 12
        return '{}-{}-{}'.format(dtstr[0:4], dtstr[4:6], dtstr[6:])
    else:
        return dtstr

def NULL_to_None(val):
    '''Convert "NULL" values to None.'''
    return None if val == 'NULL' else val

clean = table.setheader(phila_delinquents.CLEAN_HEADER)\
             .convert(phila_delinquents.CLEAN_HEADER, 'strip')\
             .convert(phila_delinquents.CLEAN_HEADER, NULL_to_None)\
             .convert(("most_recent_year_owed",
                       "oldest_year_owed",
                       "most_recent_payment_date",
                       "collection_agency_most_recent",
                       "collection_agency_oldest_year",
                       "bankruptcy_max",
                       "bankruptcy_min"), hyphenate)



# Export transormation to csv
clean.progress().tocsv()
