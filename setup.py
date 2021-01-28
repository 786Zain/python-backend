import io
from setuptools import find_packages
from setuptools import setup
with io.open("info.txt", "rt", encoding="utf8") as f:
    readme = f.read()
setup(
    name="ZT-Flask",
    version="1.0.0",
    url="",
    license="BSD",
    maintainer="Mohammad Zainulla",
    maintainer_email="786zainulla@gmail.com",
    description="Confidential Data Backup Server",
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False
)
from app.main import *