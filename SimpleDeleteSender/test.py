#!/usr/bin/python
# -*- coding:utf-8 -*-

from fabric.api import *
from fabric.contrib import *


with settings(
    host_string = '1.255.85.210',
    user = 'root',
    password = 'dev123#$%'
):
    contrib.files.exists('/home/lim/test.py')