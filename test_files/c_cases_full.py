# -*- coding: utf-8 -*-

from tools.vals import char_vals as vals
from tools.factories import generator_comb_factory

test_sets = [
    ('char tests', b'c', vals),
]

cases_generator = generator_comb_factory(test_sets)
