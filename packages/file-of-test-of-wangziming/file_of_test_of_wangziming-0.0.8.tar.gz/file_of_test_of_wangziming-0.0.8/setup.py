import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="file_of_test_of_wangziming",
    version="0.0.8",
    author="王梓明",
    author_email="1272660211@qq.com",
    description="这是一个测试项目，测试成功。",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    package_data={'file_of_test_of_wangziming': ['data/*']},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    #python_requires='>=3.13',
    install_requires=[],
    entry_points={
        'console_scripts': [
            'file_of_test_of_wangziming=file_of_test_of_wangziming.file_of_test:main',
        ]
    },
)