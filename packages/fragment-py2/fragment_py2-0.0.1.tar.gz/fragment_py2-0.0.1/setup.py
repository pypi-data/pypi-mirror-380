from setuptools import setup, find_packages

# Read the contents of README file if it exists
try:
    # Try different encodings to handle BOM and encoding issues
    for encoding in ['utf-8-sig', 'utf-8', 'cp1251', 'latin-1']:
        try:
            with open("README.md", "r", encoding=encoding) as fh:
                long_description = fh.read()
                break
        except UnicodeDecodeError:
            continue
    else:
        # If all encodings fail, use default description
        long_description = "Fragment Python Library - A Python library for interacting with Fragment platform (Telegram usernames, stars, premium, TON wallets)"
except FileNotFoundError:
    long_description = "Fragment Python Library - A Python library for interacting with Fragment platform (Telegram usernames, stars, premium, TON wallets)"

setup(
    name="fragment-py2",
    version="0.0.1",
    author="kompromizzdev",
    author_email="your.email@example.com",
    description="A Python library for interacting with Fragment platform (Telegram usernames, stars, premium, TON wallets)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/illussioon/fragment-py",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Communications :: Chat",
    ],
    license="MIT",
    python_requires=">=3.7",
    install_requires=[
        "requests",
        "beautifulsoup4",
        "TonTools",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0.0",
            "flake8>=3.8.0",
            "mypy>=0.800",
        ],
    },
    keywords="fragment telegram ton blockchain stars premium usernames",
    project_urls={
        "Bug Tracker": "https://github.com/illussioon/fragment-py/issues",
        "Documentation": "https://github.com/illussioon/fragment-py#readme",
        "Source Code": "https://github.com/illussioon/fragment-py",
    },
    include_package_data=True,
    zip_safe=False,
) 