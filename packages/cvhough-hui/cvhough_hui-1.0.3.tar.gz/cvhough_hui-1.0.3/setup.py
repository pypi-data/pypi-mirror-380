"""
CVHough SDK 安装配置文件

这个文件定义了CVHough SDK的安装配置，包括依赖项、包信息等。
"""

from setuptools import setup, find_packages
import os

# 读取README文件作为长描述
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "CVHough SDK - 基于YOLO和Hough变换的灰色圆形检测SDK"

setup(
    name="cvhough-hui",
    version="1.0.3",
    author="ruantong",
    author_email="ypwucu@isoftstone.com",
    description="基于YOLO和Hough变换的灰色圆形检测SDK",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/ruantong/cvhough-hui",
    packages=find_packages(),
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
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=[
        "opencv-python>=4.5.0",
        "numpy>=1.19.0",
        "torch>=1.9.0",
        "ultralytics>=8.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
        ],
        "gpu": [
            "torch>=1.9.0",
        ],
    },
    package_data={
        "cvhough_sdk": [
            "models/*.pt",
            "*.py",
        ],
    },
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "cvhough-detect=cvhough_sdk.main:main",
        ],
    },
    keywords=[
        "computer vision",
        "object detection", 
        "circle detection",
        "YOLO",
        "Hough transform",
        "image processing",
        "machine learning",
        "deep learning",
    ],
    project_urls={
        "Bug Reports": "https://github.com/cvhough/cvhough-hui/issues",
        "Source": "https://github.com/cvhough/cvhough-hui",
        "Documentation": "https://cvhough-hui.readthedocs.io/",
    },
)