# -*- coding: utf-8 -*-

from tools.vals import wchar_vals as vals
from tools.factories import generator_comb_factory

test_sets = [
    ('wide char tests', b'C', vals),
]

cases_generator = generator_comb_factory(test_sets)
