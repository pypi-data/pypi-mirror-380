from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="furiek",
    version="2.0.1",
    author="Furieks",
    author_email="furieks@bk.ru",
    description="Современный веб-фреймворк для Python 3.11+ - быстрый, простой и эффективный",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12", 
        "Programming Language :: Python :: 3.13",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.11",
    install_requires=[
        "uvicorn>=0.20.0",
    ],
    keywords="web framework, asgi, http, api",
    project_urls={
        "Homepage": "https://github.com/furieks/furiek",
        "Bug Reports": "https://github.com/furieks/furiek/issues",
        "Source": "https://github.com/furieks/furiek",
    },
)