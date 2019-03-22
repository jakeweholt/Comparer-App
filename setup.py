from setuptools import setup

setup(
    name='comparer_app',
    packages=['model'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)