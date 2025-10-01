from setuptools import setup, find_packages

setup(
    name ="binance_Alan",
    version="0.0.2",
    author="Alan",
    author_email="zienzeng0510@gmail.com",
    description="获取bitcoin,eth等一天内分钟级别的价格在binance.us",
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/AlanZeng-Coder/binance-Alan",
    packages=find_packages(),
    install_requires=["pandas","python-binance"],
    classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)