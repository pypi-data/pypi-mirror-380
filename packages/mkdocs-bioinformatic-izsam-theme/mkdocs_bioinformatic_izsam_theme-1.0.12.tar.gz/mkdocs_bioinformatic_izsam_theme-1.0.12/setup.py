from setuptools import setup, find_packages
from mkdocs.commands.setup import babel_cmdclass

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

VERSION = '1.0.12'

setup(
    name='mkdocs-bioinformatic-izsam-theme',
    version=VERSION,
    url='',
    description="MkDocs theme designed for Bioinformatic Unit of the Istituto Zooprofilattico dell' Abruzzo e del Molise G. Caporale",
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    keywords=['MkDocs', 'Theme', 'Software documentation'],
    license='MIT',
    author='Alessandro De Luca',
    author_email='al.deluca@izs.it',
    install_requires=[
        'mkdocs>=1.0.4'
    ],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'bioinformatic-izsam-theme = bioinformatic_izsam_theme'
        ]
    },
    zip_safe=False,
    cmdclass=babel_cmdclass
)