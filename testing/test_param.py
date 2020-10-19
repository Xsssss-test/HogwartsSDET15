#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.mark.parametrize('b', [4, 5, 6])
@pytest.mark.parametrize('a', [1, 2, 3])
def test_parm(a, b):
    print(a, b)
