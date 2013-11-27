# coding: utf-8
"""
The MIT License (MIT)

Copyright (c) 2013 Fatih Karatana

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

@package helper
@date 26/11/13
@author fatih
@version 1.0.0
"""
import os
import sys
from helper.Utilities import Utilities

__author__ = 'fatih'
__date__ = '26/11/13'
__version__ = ''

PARENT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, '%s' % PARENT_DIR)
utilities = None

# Check utilities object if it is an Utilities instance or not
if not isinstance(utilities, Utilities):
    # Create an Utilities instance
    utilities = Utilities()


class Resources(object):
    """
    Resources file is used as an interface to reach global files
    """

    def __init__(self):
        """
        Constructor for Resources
        """
        super(Resources, self).__init__()


    # Global application setting
    APP = {"host": utilities.config_get("system", "host"),
           "port": int(utilities.config_get("system", "port")),
           "debug": int(utilities.config_get("system", "debug")),
           "title": utilities.config_get("system", "title")}

    # Parameters for logical RDMS or NoSQL databases
    DATABASE = {"host": "", "username": "", "password": "", "database": ""}

    FILE_DB = {"tasks": PARENT_DIR + "/basic-todo/" + utilities.config_get("file", "tasks"),
               "users": PARENT_DIR + "/basic-todo/" + utilities.config_get("file", "users")}