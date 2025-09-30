#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2020-2025 Félix Chénier

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Format the console output of dictionaries and classes with attributes.

This module formats the console output of dicts in IPython, so that
instead of just using repr(), it displays a nicer list of keys with
abbreviated values if required, so that there is a maximum of one key
per line. This is very useful for nested dicts, as their repr()
representation is recursive and becomes unmanageable when the dict
becomes larger.

It also provides helper functions to nicely format the repr() of data
classes.

"""
__author__ = "Félix Chénier"
__copyright__ = "Copyright (C) 2020-2025 Félix Chénier"
__email__ = "chenier.felix@uqam.ca"
__license__ = "Apache 2.0"


import numpy as np
from typing import Any


def _format_dict_entries(
    the_dict: Any, quotes: bool = True, overrides={}, hide_private=False
) -> str:
    """
    Format a dict nicely on screen.

    This function makes every element of a dict appear on a separate line,
    with each key right-aligned:
        {
           'key1': value1
           'key2': value2
        'longkey': value3
        }

    Parameters
    ----------
    the_dict:
        The input dictionary
    quotes:
        False to remove quotes from keys when they are strings. Default is
        True.
    overrides:
        Optional. Dictionary of entry names to override. For example, if a
        class has private attributes that should be accessed using properties,
        e.g.: {"_data": "data", "_time": "time"}.
    hide_private:
        Optional. True to hide any attribute that begins with '_'. This is
        checked after applying overrides.

    Returns
    -------
    A string that should be shown by the __repr__ method.

    """
    max_width = 79  # How many characters should we print
    out = ""

    widest = 0
    # Find the widest key name
    for key in the_dict:
        key_label = repr(overrides.get(key, key))
        if quotes is False and isinstance(key_label, str):
            key_label = key_label[1:-1]
        widest = max(widest, len(key_label))

    # Print each key value
    for key in the_dict:
        if hide_private and overrides.get(key, key).startswith("_"):
            continue
        key_label = repr(overrides.get(key, key))
        if quotes is False and isinstance(key_label, str):
            key_label = key_label[1:-1]
        key_label = " " * (widest - len(key_label)) + key_label

        value = the_dict[key]

        # Print the value
        if widest + len(repr(value)) <= max_width:
            value_label = repr(value)
        else:
            if isinstance(value, dict):
                value_label = "<dict with " + str(len(value)) + " entries>"
            elif isinstance(value, list):
                value_label = "<list of " + str(len(value)) + " items>"
            elif isinstance(value, np.ndarray):
                value_label = "<array of shape " + str(np.shape(value)) + ">"
            else:
                value_label = repr(value)

        # Remove line breaks and multiple-spaces
        value_label = " ".join(value_label.split())

        # Printout
        to_print = f"    {key_label}: {value_label}"

        if len(to_print) > max_width:
            to_print = to_print[0 : max_width - 3] + "..."

        out += to_print
        out += "\n"

    return out


def _format_class_attributes(obj, overrides, hide_private=False) -> str:
    """
    Format a class that has attributes nicely on screen.

    This function lists every attribute of a class on a separate line, using the
    _format_dict_entries function:

        ClassName with attributes:
           'attribute1': value1
           'attribute2': value2
        'longattribute': value3

    Parameters
    ----------
    obj: Any
        The class instance.
    overrides:
        Optional. Dictionary of entry names to override. For example, if a
        class has private attributes that should be accessed using properties,
        e.g.: {"_data": "data", "_time": "time"}.

    Returns
    -------
    A string that should be shown by the __repr__ method.

    """
    # Return the type of class (header)
    class_name = type(obj).__name__
    out = class_name + " with attributes:\n"

    # Return the list of attributes
    out += _format_dict_entries(
        obj.__dict__,
        quotes=False,
        overrides=overrides,
        hide_private=hide_private,
    )
    return out


def _ktk_format_dict(value, p, cycle):
    """Format a dict nicely on screen in IPython."""
    try:
        get_ipython()

        if cycle:
            p.pretty("...")
        else:
            p.text("{\n")
            p.text(_format_dict_entries(value))
            p.text("}")

    except:
        p.text(repr(value))
