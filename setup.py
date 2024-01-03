from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in restaurantexperts/__init__.py
from restaurantexperts import __version__ as version

setup(
	name="restaurantexperts",
	version=version,
	description="Restaurants tools to help managment team",
	author="Hasan Al-Muhaimed",
	author_email="h-m-m@outlook.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
