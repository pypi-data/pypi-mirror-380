# -*- coding: utf-8 -*-

import pandas as pd
import os

# %%


def data(file='auto'):
    module_dir = os.path.dirname(__file__)
    if file == 'auto':
        df = pd.read_csv(module_dir+'/auto.csv')
    if file == 'motor-performance':
        df = pd.read_csv(module_dir+'/motor-performance.csv')

    return df
