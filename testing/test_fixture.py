#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


def test_case1(login):
    print("用例1")
    print(login)


def test_case2():
    print("用例2")


def test_case3(conn_db):
    print("用例3")
