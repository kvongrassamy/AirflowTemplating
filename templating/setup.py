import setuptools

setuptools.setup(
    name='test_plugins_package',
    packages=setuptools.find_packages(),
    entry_points={
        'airflow.plugins': [
            'job_builder = job_builder.job_builder_plugin:JobBuilderPlugin'

        ]
    },
    license='Apache License 2.0',
    #packages=['sample_provider', 'sample_provider.hooks',
    #          'sample_provider.sensors', 'sample_provider.operators'],
    install_requires=['apache-airflow>=2.0'],
    #setup_requires=['setuptools', 'wheel'],
    #author='Pete DeJoy',
    #author_email='pete@astronomer.io',
    #url='http://astronomer.io/',
    python_requires='~=3.7',
)