from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="pyghost",
    version="1.0.3",
    author="PyGhost Contributors",
    author_email="pyghost@example.com",
    description="A modern, comprehensive Python wrapper for Ghost Admin API with full CRUD support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adamfils/pyghost",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
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
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Content Management System",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary",
        "Topic :: Communications :: Email :: Mailing List Servers",
        "Topic :: Text Processing :: Markup :: HTML",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    keywords="ghost, cms, api, blog, publishing, content-management, webhooks, themes, members, newsletters",
    project_urls={
        "Bug Reports": "https://github.com/adamfils/pyghost/issues",
        "Source": "https://github.com/adamfils/pyghost",
        "Documentation": "https://github.com/adamfils/pyghost#readme",
        "Changelog": "https://github.com/adamfils/pyghost/releases",
    },
    include_package_data=True,
    zip_safe=False,
)
