from setuptools import setup

version = '1.0'

setup(
    name='cbagent',
    version=version,
    author='Couchbase',
    license='Apache Software License',
    packages=[
        'cbagent',
        'cbagent.cli_wrappers',
        'cbagent.collectors',
        'cbagent.collectors.libstats'
    ],
    entry_points={
        'console_scripts': [
            'ns_collector = cbagent.cli_wrappers.ns_collector:main',
            'atop_collector = cbagent.cli_wrappers.atop_collector:main',
            'at_collector = cbagent.cli_wrappers.at_collector:main',
        ]
    },
    include_package_data=True,
    install_requires=[
        'argparse==1.2.1',
        'eventlet==0.12.1',
        'fabric==1.6.0',
        'logger',
        'requests==1.2.0',
        'seriesly',
    ],
)
