from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="event-journal",
    version="1.1.0",
    author="Amol Saini",
    author_email="amol.saini567@gmail.com",
    description="A simple Python library for logging events to PostgreSQL database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amolsr/event_journal",
    project_urls={
        "Bug Reports": "https://github.com/amolsr/event_journal/issues",
        "Source": "https://github.com/amolsr/event_journal",
        "Documentation": "https://github.com/amolsr/event_journal#readme",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Logging",
        "Topic :: Database",
    ],
    python_requires=">=3.8",
    install_requires=[
        "psycopg2-binary>=2.8.6",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=22.0",
            "flake8>=4.0",
            "twine>=4.0",
            "build>=0.10",
        ],
    },
    entry_points={
        "console_scripts": [
            "event-journal-test=event_journal.standalone:test_connection",
        ],
    },
    keywords="python, logging, events, postgresql, supabase, database, audit",
    include_package_data=True,
    zip_safe=False,
)
