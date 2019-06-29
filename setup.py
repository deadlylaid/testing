from setuptools import setup

install_requires = [
    'django>=2.0',
    'pytest',
    'pytest-django',
]

setup(
    name='testing',
    install_requires = install_requires
)
