from setuptools import setup, find_packages

setup(
    name="baseline-checker",
    version="0.1.0",
    packages=find_packages(),  # automatically finds baseline_checker folder
    install_requires=[
        "rich",
        "tqdm",
        "pandas",
        "python-docx",
        "reportlab",
        "fpdf",
        # etc...
    ],
    package_data={
        "baseline_checker": ["config/baseline_data.json"]
    },
    entry_points={
        "console_scripts": [
            "baseline-checker = baseline_checker.core:run",  # point CLI to main function
        ],
    },
)
