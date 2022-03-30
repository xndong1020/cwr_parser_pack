from setuptools import setup
import setuptools

setup(
    name="cwr_parser_pack",
    version="0.1",
    description="CWR file parser",
    url="git@github.com:xndong1020/cwr_parser_pack.git",
    author="JGU",
    author_email="jgu@apra.com.au",
    license="MIT",
    packages=setuptools.find_namespace_packages(include=["cwr_parser_pack.*"]),
    namespace_packages=["cwr_parser_pack"],
    # zip_safe=False
)
