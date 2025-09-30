# setup.py
from setuptools import setup, find_packages

setup(
    # შეცვალეთ ეს თქვენი უნიკალური სახელით PyPI-ზე!
    name='base-operations-pkg-unique-gabriel-1234', 
    version='0.0.1',
    author='თქვენი სახელი',
    author_email='თქვენი-მეილი@example.com',
    description='მარტივი კლასი ძირითადი მათემატიკური ოპერაციებისთვის.',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)