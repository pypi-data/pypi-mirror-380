'''
Use of this source code is governed by a MIT-style license that can be found in the LICENSE file.
Created on Jan 27, 2017
@author: Niels Lubbes


sage -python setup.py pytest                        # make sure everything works
sage -python setup.py sdist                         # create source package
twine upload --skip-existing dist/* --verbose       # upload this package to PyPI 

For more information see:

https://xebia.com/blog/a-practical-guide-to-using-setup-py/
https://python-packaging.readthedocs.io/en/latest/minimal.html
https://pypi.python.org/pypi?%3Aaction=list_classifiers
'''

from setuptools import setup

setup( 
    name='ns_lattice',
    version='6',
    description='Algorithms for computing in Neron-Severi lattice',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Mathematics',
        ],
    keywords='Neron-Severi-lattice',
    url='http://github.com/niels-lubbes/ns_lattice',
    author='Niels Lubbes',
    license='MIT',
    package_dir={'ns_lattice': 'src/ns_lattice', 'tests':'src/tests'},
    packages=['ns_lattice', 'tests'],
    package_data={'ns_lattice': ['ns_tools.sobj', 'reducible_conics.sobj']},
    include_package_data=True,
    install_requires=['linear_series'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['run-lattice=ns_lattice.__main__:main'],
    },
    zip_safe=False
    )
