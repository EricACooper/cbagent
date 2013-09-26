from setuptools import setup

version = '1.5.9'

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
            'latency_collector = cbagent.cli_wrappers.latency_collector:main',
            'xdcr_lag_collector = cbagent.cli_wrappers.xdcr_lag_collector:main',
        ]
    },
    include_package_data=True,
    install_requires=[
        'argparse',
        'couchbase==1.0.0',
        'eventlet==0.12.1',
        'fabric==1.8.0',
        'logger',
        'requests==1.2.0',
        'seriesly',
        'spring'
    ],
)
