from distutils.core import setup
import py2exe

setup(
  options={
    'py2exe': {
      'bundle_files': 1,
      'optimize': 2,
      'compressed': True
    }
  },
  console=['aiobfd/__main__.py'],
  zipfile=None,
)