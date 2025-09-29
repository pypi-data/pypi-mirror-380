import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="zaishiyishiheji",
    version="0.0.4",
    author="王梓明",
    author_email="1272660211@qq.com",
    description="王梓明写的故事",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://www.sidaxiake.cn/",
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={'zaishiyishiheji': ['data/*']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    #python_requires='>=3.13',
    install_requires=[],
)