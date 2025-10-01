'''
Use of this source code is governed by a MIT-style license that can be found in the LICENSE file.
Created on Jan 27, 2017
@author: Niels Lubbes

sage -python setup.py pytest
sage -python setup.py sdist
twine upload --skip-existing dist/* --verbose

https://python-packaging.readthedocs.io/en/latest/minimal.html
https://pypi.python.org/pypi?%3Aaction=list_classifiers
'''

from setuptools import setup

setup( 
    name='moebius_aut',
    version='2',
    description='Computing Moebius automorphisms of surfaces',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Mathematics',
        ],
    keywords='surfaces automorphisms circles',
    url='http://github.com/niels-lubbes/moebius_aut',
    author='Niels Lubbes',
    license='MIT',
    package_dir={'moebius_aut': 'src/moebius_aut'},
    packages=['moebius_aut'],
    package_data={'moebius_aut': ['ma_tools.sobj']},
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['run-moebius_aut=moebius_aut.__main__:main'],
    },
    zip_safe=False
    )

