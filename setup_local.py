from setuptools import setup
from extension_helpers import get_extensions

def get_custom_extensions():
    extensions = get_extensions()
    return [ext for ext in extensions if '_np_utils' not in ext.name]

setup(ext_modules=get_custom_extensions())
