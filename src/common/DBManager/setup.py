from distutils.core import setup

setup(
    name='DBManager',
    version='0.1dev',
    packages=['db_manager',],
    install_requires=['../FootyAuth'],
    license='',
    long_description=open('README').read()
)
