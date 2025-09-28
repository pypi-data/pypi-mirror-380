from setuptools import setup, find_packages

setup(
    name="baseline_checker",
    version="0.1.3",
    packages=find_packages(),  # automatically finds baseline_checker + subpackages
    python_requires=">=3.6",
    install_requires=[
        "rich",
        "tqdm",
        "pandas",
        "python-docx",
        "reportlab",
        "colorama",
        "fpdf"
    ],
    entry_points={
        "console_scripts": [
            "baseline-checker=baseline_checker.baseline_checker:main",
        ],
    },
)