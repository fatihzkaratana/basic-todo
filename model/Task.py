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

@package model
@date 26/11/13
@author fatih
@version 1.0.0
"""

__author__ = 'fatih'
__date__ = '26/11/13'
__version__ = ''

import uuid


class Task(dict):
    """
    Task object inherited from Python builtin dictionary object to store data inside

    Actually I wish to use SQLAlchemy but forgave because of package dependency.
    It can be moderated by SQLAlchemy entity easier than this way.
    """
    __id = None
    due_date = None
    assignee = None
    value = None
    status = None

    def __init__(self):
        """
        Super constructor for Task object
        """
        super(Task, self).__init__()
        self.set_id()

    def get_id(self):
        """
        Getter method to gather due_date variable

        @return due date of task
        """
        return self["__id"]

    def set_id(self):
        """
        Create a random id for unique task
        """

        self["__id"] = str(uuid.uuid4())

    def get_due_date(self):
        """
        Getter method to gather due_date variable

        @return due date of task
        """
        return self["due_date"]

    def set_due_date(self, due_date):
        """
        Due date setter for Task object
        @param due_date
        """
        self["due_date"] = due_date

    def get_assignee(self):
        """
        Getter method to gather assignee of task variable

        @return assignee of task
        """
        return self["assignee"]

    def set_assignee(self, assignee):
        """
        Assignee setter for Task object
        @param assignee of the task
        """
        self["assignee"] = assignee

    def get_value(self):
        """
        Getter method to gather value variable

        @return value of value
        """
        return self["value"]

    def set_value(self, value):
        """
        Value setter for Task object
        @param value
        """
        self.assignee = value

    def get_status(self):
        """
        Getter method to gather value variable

        @return value of value
        """
        return self["status"]

    def set_status(self, status):
        """
        Value setter for Task object
        @param value
        """
        self["status"] = status