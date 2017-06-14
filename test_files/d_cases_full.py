# -*- coding: utf-8 -*-

from tools.vals import pos_num_vals, neg_num_vals
from tools.factories import generator_comb_factory

test_sets = [
    ('d tests', b'd', pos_num_vals + neg_num_vals),
]

cases_generator = generator_comb_factory(test_sets)
