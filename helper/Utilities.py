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
import json

__author__ = 'fatih'
__date__ = '26/11/13'
__version__ = '1.0.0'

try:
    import os
    import sys
    import logging
    import collections
    from time import strftime
    from datetime import datetime
    from logging.handlers import SysLogHandler
    from ConfigParser import RawConfigParser as config_parser
except ImportError as exception:
    print "Error occurred while importing packages in Utilities file with Exception: ", exception.message

# Create system path and insert into os path to reach files
PARENT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, '%s' % PARENT_DIR)
CONFIG_FILE_PATH = PARENT_DIR + "/basic-todo/conf.d/config.cfg"
utilities = None


class Utilities(object):
    """
    Utilities class help us to convert configuration variables gathered from config file into system wide variables
    in our application.
    """
    config = collections.OrderedDict()
    logging = logging

    def __init__(self):
        """
        Constructor for Utilities class
        """
        # Retrieve Config file from Resources script
        self.config_file = CONFIG_FILE_PATH

        # Initiate Config Parser instance
        self.parser = config_parser()

        # Read config file inside
        self.parser.read(self.config_file)

        # Set Config object by config parser sections
        self.config.update(self.parser._sections)

        # Set logging parameters and initiate logging
        self.logger = self.logging.getLogger()

        # Set global NOW value to be used in any where in application
        self.now = strftime(self.config_get("locale", "datetime_format"))

        # Set log destination
        # Convert Json string into DotDict/OrderedDict object
        log_destination = json.loads(unicode(self.config_get("logging", "destination")))

        # Initiate Syslog handler with log destination regarding to the system architecture
        syslog = SysLogHandler(address=log_destination[sys.platform])

        # Set syslog format
        syslog.setFormatter(
            logging.Formatter(self.config_get("logging", "format"))
        )
        self.logger.addHandler(syslog)

    def config_set(self, section, key, value):
        """
        Set config key with given value

        @param key is the key of config
        @param value value which, will be set to the config key
        @return:
        """
        self.config[section][key] = value

    def config_get(self, section, key):
        """
        Get config value by given key

        @param key is the key of config
        @return key value of config
        """
        return self.config[section][key]

    def log(self, severity=logging.DEBUG, message=None):
        """
        Log utility for system wide logging needs
        @param severity Log severity
        @param message Log message
        @return
        """
        self.logger.setLevel(severity)
        self.logger.log(severity, message) if self.config_get("logging", "enable") else ""



