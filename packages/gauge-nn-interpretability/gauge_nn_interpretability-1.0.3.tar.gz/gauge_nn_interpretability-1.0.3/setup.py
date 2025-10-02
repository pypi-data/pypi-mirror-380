"""
Setup script for Gauge Neural Network Interpretability package
"""

from setuptools import setup, find_packages
import os

# Read long description from README
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

# Read requirements - handle both in-place and isolated builds
try:
    with open('requirements.txt', 'r', encoding='utf-8') as f:
        requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]
except FileNotFoundError:
    # Fallback requirements if requirements.txt is not available
    requirements = [
        'torch>=2.0.0',
        'transformers>=4.30.0',
        'numpy>=1.24.0',
        'matplotlib>=3.7.0',
        'seaborn>=0.12.0',
        'scipy>=1.10.0',
        'tqdm>=4.65.0',
    ]

setup(
    name='gauge-nn-interpretability',
    version='1.0.3',
    author='Michael J. Pendleton',
    author_email='michael.pendleton.20@gmail.com',
    description='Computational Gauge Theory for Neural Network Interpretability',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/theaicowboys/gauge-nn-interpretability',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    python_requires='>=3.8',
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'gauge-analyze=gauge_nn_interpretability.cli:main',
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords='neural-networks interpretability gauge-theory transformers machine-learning',
    project_urls={
        'Bug Reports': 'https://github.com/theaicowboys/gauge-nn-interpretability/issues',
        'Source': 'https://github.com/theaicowboys/gauge-nn-interpretability',
        'Documentation': 'https://github.com/theaicowboys/gauge-nn-interpretability/docs',
    },
)
