import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))

setup(
  name = 'word2number-i18n',
  include_package_data=True,
  packages = ['word2numberi18n','word2numberi18n/data'],  # this must be the same as the name above
  package_data={
    'word2numberi18n/data': ["*.txt"],
  },
  version = '0.1',
  license=open('LICENSE.txt').read(),
  description = 'Convert i18n number words eg. three hundred and forty two to numbers (342).',
  author = 'Sebastian Ritter',
  python_requires='>=3',
  author_email = 'nospam@example.com',
  url = 'https://github.com/bastie/w2ni18n',  # use the URL to the github repo
  project_urls={
      'Source': 'https://github.com/bastie/w2ni18n',
  },
  keywords = ['numbers', 'convert', 'words', 'i18n'],  # arbitrary keywords
  classifiers = [
      'Intended Audience :: Developers',
      'Programming Language :: Python',
      'Development Status :: 5 - Production/Stable',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3',
      'Topic :: Software Development :: Internationalization'
  ],
  long_description=open_file('README.rst').read()
)