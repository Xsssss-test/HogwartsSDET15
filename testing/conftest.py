#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def login():
    # setup 操作
    print("登录操作")
    # yield 相当于return操作
    yield ['tom', '111']
    # teardown 操作
    print("登出操作")


@pytest.fixture(scope='session')
def conn_db():
    print("连接数据库")
