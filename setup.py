import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))

setup(
  name = 'word2number',
  packages = ['word2number'],  # this must be the same as the name above
  version = '1.1',
  license=open('LICENSE.txt').read(),
  description = 'Convert number words eg. three hundred and forty two to numbers (342).',
  author = 'Akshay Nagpal',
  author_email = 'akshay2626@gmail.com',
  url = 'https://github.com/akshaynagpal/w2n',  # use the URL to the github repo
  download_url = 'https://github.com/akshaynagpal/w2n/tarball/1.1', 
  keywords = ['numbers', 'convert', 'words'],  # arbitrary keywords
  classifiers = [
      'Intended Audience :: Developers',
      'Programming Language :: Python'
  ],
  long_description=open_file('README.rst').read()
)