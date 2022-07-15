from setuptools import setup

setup(
    name='salesforce-scripts',
    version='0.1.0', 
    description='Python scripts by Salesforce architects for Salesforce architects',
    url='https://github.com/quanlinguo/salesforce-scripts',
    author='Charlie Guo',
    author_email='architect.charlie.guo',
    license='MIT',
    packages=['salesforce_scripts'],
    install_requires=[
        'simple-salesforce',
        'python-csv',
        'requests',
        'google-cloud-bigquery',
    ],

    classifiers=[
        'Development Status :: 1 - Prototyping',
        'Intended Audience :: Salesforce Architects & Developers',
        'License :: MIT License',
        'Operating System :: macOS',
        'Programming Language :: Python :: 3.9',
    ],
)
