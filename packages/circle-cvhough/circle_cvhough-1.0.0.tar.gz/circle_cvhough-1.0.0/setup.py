"""
cvHough SDK 安装配置文件

这个文件定义了cvHough SDK的安装配置，包括依赖项、包信息等。
"""

from setuptools import setup, find_packages
import os

# 读取README文件作为长描述
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "cvHough SDK - YOLO物体检测与霍夫圆检测集成工具包"

setup(
    name="circle-cvhough",
    version="1.0.0",
    author="ruantong",
    author_email="ypwucu@isoftstone.com",
    description="YOLO物体检测与霍夫圆检测集成工具包",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/ruantong/circle-cvhough",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=[
        "opencv-python>=4.5.0",
        "numpy>=1.19.0",
        "ultralytics>=8.0.0",
        "matplotlib>=3.3.0",
        "pathlib2>=2.3.0; python_version<'3.4'",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
        "docs": [
            "sphinx>=3.0",
            "sphinx-rtd-theme>=0.5",
        ],
    },
    package_data={
        "cvhough_sdk": [
            "models/*.pt",
            "models/*.onnx",
            "*.md",
        ],
    },
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "cvhough-detect=cvhough_sdk:main",
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
        "Bug Reports": "https://github.com/ruantong/circle-cvhough/issues",
        "Source": "https://github.com/ruantong/circle-cvhough",
        "Documentation": "https://circle-cvhough.readthedocs.io/",
    },
    zip_safe=False,
)