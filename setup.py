from setuptools import setup, find_packages

setup(
    name='selflab',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'click',
        'matplotlib',
	'webpy'
    ],
    entry_points='''
        [console_scripts]
        selflabweb=selflab.webserver:run
    ''',
)
