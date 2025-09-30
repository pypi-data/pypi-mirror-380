from setuptools import setup, find_packages


setup(
    name="Figure_square",
    version="0.0.2",  
    author="zteewt",
    author_email="dzynyok@mail.ru",
    description="Решение задачи №2 в вакансии.",
    url="https://github.com/zteewt/MindBox/",
    packages=find_packages(),  
    py_modules=["Figure_square"],  
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9", 
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)