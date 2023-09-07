#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="James Michael DuPont",
    author_email='jmikedupont2@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Creating an Autopoietic Narrative Ecosystem: A Python-based Cookiecutter Template",
    entry_points={
        'console_scripts': [
            'metameme=metameme.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='metameme',
    name='metameme',
    packages=find_packages(include=['metameme', 'metameme.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/jmikedupont2/metameme',
    version='0.1.0',
    zip_safe=False,
)
