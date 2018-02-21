# Script to call other scripts whilst dev

# Magic needed for reloading in changes to imports automatically
# after changing .py files
from IPython import get_ipython
ipython = get_ipython()
ipython.magic("load_ext autoreload") #
ipython.magic("autoreload 2") # %autoreload 2

#import dep
import numpy as np
import pandas as pd


from EDdata import EDdata

pmED = EDdata('pmth')

pmED.loadCLEAN()

pmED.status()

pmED.checks()


set(pmED._dataCLEANpat.columns)