from setuptools import setup

setup(
    name="django-markdown-renderer",
    version="0.1.0",
    author="xoxxel",
    author_email="xoxxel.com@gmail.com",
    description="A Django app for rendering Markdown with real-time preview",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/xoxxel/django-markdown-renderer",
    packages=["markdown_renderer"],
    package_dir={"": "src"},
    package_data={"markdown_renderer": ["templates/markdown_renderer/*.html"]},
    include_package_data=True,
    license="MIT",
    install_requires=["Django>=3.2", "markdown2>=2.4.0", "bleach>=4.1.0"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
    ],
    python_requires=">=3.8",
)