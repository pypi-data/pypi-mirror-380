from __future__ import annotations

from pathlib import Path
import re
from setuptools import find_packages, setup

BASE_DIR = Path(__file__).parent
README_PATH = BASE_DIR / "README.md"

def read_readme() -> str:
    try:
        return README_PATH.read_text(encoding="utf-8")
    except OSError:
        return "jsontable2md: Convert HTML tables embedded in JSON to Markdown extended table syntax."

def read_version() -> str:
    version_file = BASE_DIR / "jsontable2md" / "__init__.py"
    content = version_file.read_text(encoding="utf-8")
    m = re.search(r'__version__\s*=\s*["\']([^"\']+)["\']', content)
    if not m:
        raise RuntimeError("__version__ not found in __init__.py")
    return m.group(1)

package_version = read_version()

setup(
    name="jsontable2md",
    version=package_version,
    author="abachan",
    author_email="aiba1114@cl.cilas.net",
    description="Convert HTML tables embedded in JSON to Markdown extended table syntax",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/abachan/jsontable2md",
    project_urls={
        "Repository": "https://github.com/abachan/jsontable2md",
        "Issues": "https://github.com/abachan/jsontable2md/issues",
    },
    license="MIT",
    packages=find_packages(include=["jsontable2md", "jsontable2md.*"], exclude=["test", "test.*", "scripts", "scripts.*"]),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Text Processing :: Markup :: Markdown",
        "Topic :: Utilities",
    ],
    python_requires=">=3.9",
    install_requires=[
        "beautifulsoup4>=4.9.0",
    ],
    extras_require={
        "dev": [
            "black>=23.0",
            "isort>=5.12",
            "mypy>=1.0",
            "pytest>=7.0",
            "build",
            "twine",
            # 型補完（任意）
            "types-beautifulsoup4; python_version>='3.9'",
        ],
    },
    keywords=["markdown", "html", "table", "conversion", "json"],
    zip_safe=False,
)