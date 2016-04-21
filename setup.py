from setuptools import setup, find_packages

setup(
    name = 'the_count',
    version = '0.1.0',
    description = 'Handy class for counting things',
    author = 'Brian Lauber',
    author_email = 'constructible.truth@gmail.com',
    packages = find_packages(exclude = ["tests"]),
    install_requires = [],
    test_suite = 'tests',
    tests_require = ["mock>=1.0.0"]
)
