import pathlib
from pip.req import parse_requirements
from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

reqs = [str(ir.req) for ir in parse_requirements(here / 'requirements.txt')]

setup(
    name='craimodels',
    version='0.0.1',
    description='Models trained with CRAI (https://github.com/FREVA-CLINT/climatereconstructionAI).',
    long_description=long_description,
    url='https://github.com/climateintelligence/craimodels',
    author='Climate Informatics and Technology group at DKRZ (Deutsches Klimarechenzentrum)',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Atmospheric Science',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Programming Language :: Python :: 3.10",
        'Programming Language :: Python :: 3 :: Only',
    ],

    keywords='climate, artificial intelligence, infilling, missing values, partial convolution, NetCDF',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.9, <4',
    include_package_data=True,
    install_requires=reqs,
)
