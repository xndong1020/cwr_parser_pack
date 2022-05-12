from setuptools import setup
import setuptools

setup(
    name="cwr_parser_pack",
    version="0.11",
    description="CWR file parser",
    url="https@github.com:xndong1020/cwr_parser_pack.git",
    author="JGU",
    author_email="jgu@apra.com.au",
    license="MIT",
    packages=setuptools.find_namespace_packages(include=["cwr_parser.*"]),
    namespace_packages=["cwr_parser"],
    # zip_safe=False
)
