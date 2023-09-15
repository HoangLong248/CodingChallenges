from setuptools import setup

setup(
    name="ccwc",
    version="1.0",
    py_modules=['ccwc'],
    install_requires=[
        "Click",
    ],
    
    entry_points="""
        [console_scripts]
        ccwc=ccwc:ccwc
    """
)