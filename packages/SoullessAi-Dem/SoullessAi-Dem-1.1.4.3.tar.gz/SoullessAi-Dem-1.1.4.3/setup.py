from setuptools import setup, find_packages
import os

setup(
    name="SoullessAi-Dem",
    version="1.1.4.3",
    author="ceylon1cy",
    author_email="ceylon1cy@gmail.com",
    description="Библиотека для создания демотиваторов",
    long_description="Библиотека для создания демотиваторов. Совместима с aiogram, telebot и другими библиотеками для Telegram, также совместима с ВКонтакте.",
    long_description_content_type="text/markdown",
    packages=find_packages(),
    package_data={
        'soulless_ai_dem': ['templates/*.jpg'],
    },
    include_package_data=True,
    install_requires=[
        "Pillow>=8.0.0",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.7",
    keywords="demotivator, image processing, meme",
)
