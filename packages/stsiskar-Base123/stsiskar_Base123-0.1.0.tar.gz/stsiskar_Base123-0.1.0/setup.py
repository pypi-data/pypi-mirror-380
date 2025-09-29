from setuptools import setup, find_packages

setup(
    name="stsiskar_Base123",             # პაკეტის სახელი (უნიკალური უნდა იყოს PyPI-ზე)
    version="0.1.0",              # ვერსია
    description="A simple Base class example",
    author="Shota Tsiskaridze",
    author_email="shota.tsiskaridze@iliauni.edu.ge",
    packages=find_packages(),     # ავტომატურად იპოვის პაკეტებს
    python_requires=">=3.6",      # მინიმალური Python ვერსია
)