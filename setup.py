import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))

setup(
  name = 'word2number_es',
  packages = ['word2number_es'],  # this must be the same as the name above
  version = '1.0',
  license=open('LICENSE.txt').read(),
  description = 'Convert number words (eg. twenty one) to numeric digits (spanish)',
  author = 'Neuri',
  author_email = 'support@neuri.ai',
  url = 'https://github.com/Neuri-ai/w2n_es',  # use the URL to the github repo
  keywords = ['numbers', 'convert', 'words', 'spanish'],  # arbitrary keywords
  classifiers = [
      'Intended Audience :: Developers',
      'Programming Language :: Python'
  ],
  long_description=open_file('README.rst').read()
)