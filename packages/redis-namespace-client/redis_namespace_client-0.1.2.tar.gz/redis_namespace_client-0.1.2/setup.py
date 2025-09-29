from setuptools import setup, find_packages

setup(
    name="redis-namespace-client",
    version="0.1.2",
    description="Redis client with namespacing and JSON support for middleware apps.",
    author="Onyekelu Chukwuebuka",
    author_email="conyekelu@yahoo.com",
    packages=find_packages(),
    include_package_data=True,
    long_description=open('README.md', encoding="utf-8").read(),
    long_description_content_type='text/markdown',
    url='https://github.com/cloudtechy/redis-namespace-client',
    download_url='https://github.com/cloudtechy/redis-namespace-client/archive/refs/tags/0.1.2.tar.gz',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        "redis>=4.0.0",
        "python-dotenv",
    ],
    python_requires=">=3.7",
)
