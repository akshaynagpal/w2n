import setuptools
import os

def read_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setuptools.setup(
    name = "word2number-i18n",
    version = "0.1.3",
    description = "Convert i18n number words eg. three hundred and forty two to numbers (342).",
    long_description=read_file("README.md"),
    long_description_content_type='text/markdown',
    author = 'Sebastian Ritter',
    python_requires='>=3',
    author_email = 'nospam@example.com',
    url = 'https://github.com/bastie/w2ni18n',  # use the URL to the github repo
    project_urls={
        'Source': 'https://github.com/bastie/w2ni18n',
    },
    keywords = ['numbers', 'convert', 'words', 'i18n'],  # arbitrary keywords
    include_package_data=True,
    packages = ['word2numberi18n','word2numberi18n/data'], 
    package_data={
        'word2numberi18n/data': ["*.txt"],
    },
    classifiers = [
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Internationalization'
    ]
)

