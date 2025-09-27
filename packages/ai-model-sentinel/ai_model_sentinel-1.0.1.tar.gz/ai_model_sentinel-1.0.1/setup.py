from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="ai-model-sentinel",
    version="1.0.1",
    author="Saleh Asaad Abughabraa",
    author_email="saleh87alally@gmail.com",
    description="Military Grade Security Scanner for AI Models and Python Files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SalehAsaadAbughabraa/ai-model-sentinel",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Security",
        "Topic :: Software Development :: Quality Assurance",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "ai-sentinel=military_scanner:main",
        ],
    },
    keywords="security, ai, ml, scanner, cybersecurity, python",
    project_urls={
        "Bug Reports": "https://github.com/SalehAsaadAbughabraa/ai-model-sentinel/issues",
        "Source": "https://github.com/SalehAsaadAbughabraa/ai-model-sentinel",
    },
    license="MIT", 
)