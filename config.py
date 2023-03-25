"""config.py

Provides wrapper for gathering config parameters from several sources

Sources include:
    - .env file created in project's root (Recommended for development machines)
    - System environments (Recommended for production environments)
    - Fall back hard-codded strings (Not recommended)

===

Version 1.0
Initial release

===

This script requires that `python-dotenv==0.13.0` be installed within the Python environment you are running this script

This file can be imported as a module and contains the following class(es):

    * Config - Provides access to required configuration variables
"""

import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    """
    Configuration parameters for the application

    Attributes
    ----------
    GEOCODE_ENDPOINT : str
        Location of Geocode endpoint
    """
    GEOCODE_ENDPOINT = os.environ.get('GEOCODE_ENDPOINT') or 'http://geocode:80'
