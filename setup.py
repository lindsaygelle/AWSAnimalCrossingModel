from typing import Any, Dict, List, Optional

import setuptools

author: str = "lindsaygelle"
author_email: Optional[str] = None
classifiers: List[str] = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
]
description: str = "AWSAnimalCrossing"
github_author: str = author
github_repository: str = "AWSAnimalCrossing"
include_package_data = True
install_requires: List[str] = []
keywords: List[str] = [github_repository]
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()
long_description_content_type = "text/markdown"
maintainer: str = author
maintainer_email: Optional[str] = author_email
name: str = "model"
package_dir: Dict[str, str] = {name: name}
packages: List[str] = [name]
project_urls: Dict[str, str] = {
    "Bug Reports": f"https://github.com/{github_author}/{github_repository}/issues",
    "Documentation": f"https://github.com/{github_author}/{github_repository}",
    "Source Code": f"https://github.com/{github_author}/{github_repository}",
}
python_requires: str = ">= 3.8"
url: str = f"https://www.github.com/{author}/{github_repository}"
with open("VERSION", encoding="utf-8") as f:
    version: str = f.read()

setuptools.setup(
    author=author,
    author_email=author_email,
    classifiers=classifiers,
    description=description,
    include_package_data=include_package_data,
    install_requires=install_requires,
    keywords=keywords,
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    maintainer=maintainer,
    maintainer_email=maintainer_email,
    name=name,
    package_dir=package_dir,
    packages=packages,
    project_urls=project_urls,
    python_requires=python_requires,
    url=url,
    version=version,
)
