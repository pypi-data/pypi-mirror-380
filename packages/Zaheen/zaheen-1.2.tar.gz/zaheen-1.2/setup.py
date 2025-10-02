from setuptools import setup, find_packages

setup(
    name = "Zaheen",
    version = "1.2",
    author = "Zaheen Iqbal",
    author_email = "zaheen6iqbal@gmail.com",
    description = "This is just a test package",
    packages = find_packages(),
    python_requires = ">=3.6",
    entry_point = {
        "console_script" : [
            "zaheen6iqbal@gmail.com"
            ],
        },
    )