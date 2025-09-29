from setuptools import setup, find_packages

setup(
    name="SoullessAi-Dem",
    version="1.0.9.2",
    author="ceylon1cy",
    author_email="ceylon1cy@gmail.com",
    description="Библиотека для создания демотиваторов",
    long_description="Библиотека для создания демотиваторов. Совместима с aiogram, telebot и другими библиотеками для Telegram ботов, а также с библиотеками для ВКонтакте.",
    long_description_content_type="text/markdown",
    packages=find_packages(include=['soulless_ai_dem', 'soulless_ai_dem.*']),
    include_package_data=True,
    package_data={
        'soulless_ai_dem': [
            '*.py',
            'fonts/*.ttf',
            'templates/*.png',
            'templates/*.jpg'
        ]
    },
    install_requires=[
        "Pillow>=8.0.0",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.6",
)