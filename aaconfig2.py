#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser
import os
import sys
import io

configuration = ConfigParser.RawConfigParser()
__init = """
[user]
nickname =
email =

[server]
url =
"""

def init_config():
    configuration.readfp(io.BytesIO(__init))
    #configuration.read({'user': {'nickname': '', 'email': ''}, 'server': {'url': ''}})
    __save()

def __save():
    with open(__get_config_file(), "wb") as f:
        configuration.write(f)

def __get_config_file():
    return os.getenv('HOME')+'/.aaconfig'

def config(params):
    configuration.read(__get_config_file())
    if not configuration.has_section('user'):
        init_config()
    if len(params) == 2:
        attribute, value = params
        if attribute.count('.') == 1:
            section, attribute = attribute.split('.')
            if not configuration.has_section(section):
                configuration.add_section(section)
            configuration.set(section, attribute, value)
        else:
            configuration.set('user', attribute, value)
        __save()

if __name__ == "__main__":
    init_config()

