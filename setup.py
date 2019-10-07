from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='core_logic',
    # author='some author',
    # author_email='',
    # Needed to actually package something
    packages=['core_logic'],
    # install_requires=['numpy'], # Not required here
    version='0.1',
    license='MIT',
    description='An example of a python package from pre-existing code',
)

