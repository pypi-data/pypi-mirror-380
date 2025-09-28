import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="file-of-test-of-wangziming",
    version="0.0.6",
    author="王梓明",
    author_email="1272660211@qq.com",
    description="这是一个测试项目，测试成功。",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    #packages=setuptools.find_packages(),
    py_modules=["file_of_test_of_wangziming"],
    #package_data={'': ['*.yaml']} # 包含MANIFEST.in里的文件
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    scripts=["file_of_test_of_wangziming.py"],
)