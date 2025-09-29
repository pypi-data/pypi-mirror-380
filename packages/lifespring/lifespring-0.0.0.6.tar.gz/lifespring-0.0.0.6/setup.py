from setuptools import setup
from setuptools import find_packages


setup(
    name = "lifespring",
    version = "0.0.0.6",
    packages = find_packages(),
    description = "A personal account keeper.",
    author = "parkcai",
    author_email = "sun_retailer@163.com",
    url = "https://github.com/parkcai/lifespring",
    include_package_data = True,
    package_data = {
        "lifespring": ["locales/**/LC_MESSAGES/*.mo"],
    },
    python_requires = ">=3.8",
    install_requires = [
        "numpy>=1.21.0",
        "pywheels>=0.7.5.4",
    ],
)