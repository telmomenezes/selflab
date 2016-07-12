from setuptools import setup, find_packages

setup(
    name='selflab',
    version='0.1',
    packages=['selflab'],
    install_requires=[
        'numpy',
        'scipy',
        'click',
        'matplotlib',
        'bottle'
    ],
    entry_points='''
        [console_scripts]
        selflab=selflab.selflab:cli
    ''',
)
