import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))

setup(
  name = 'word2number-i18n',
  packages = ['word2numberi18n'],  # this must be the same as the name above
  version = '0.1',
  license=open('LICENSE.txt').read(),
  description = 'Convert i18n number words eg. three hundred and forty two to numbers (342).',
  author = 'Sebastian Ritter',
  author_email = 'nospam@example.com',
  url = 'https://github.com/bastie/w2ni18n',  # use the URL to the github repo
  download_url = 'https://github.com/akshaynagpal/w2n/tarball/1.1', 
  keywords = ['numbers', 'convert', 'words', 'i18n'],  # arbitrary keywords
  classifiers = [
      'Intended Audience :: Developers',
      'Programming Language :: Python'
  ],
  long_description=open_file('README.rst').read()
)