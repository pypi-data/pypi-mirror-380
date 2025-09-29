from setuptools import setup, find_packages
import os

# 读取README文件
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "Circle Detection SDK - 基于改进的Hough变换和YOLO目标检测的圆形检测SDK"

setup(
    name="circle-detection-hough",
    version="1.0.1",
    author="ruantong",
    author_email="ypwucu@isoftstone.com",
    description="基于改进的Hough变换和YOLO目标检测的圆形检测SDK",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/ruantong/circle-detection-hough",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
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
        "matplotlib>=3.3.0",
        "scipy>=1.6.0",
        "torch>=1.9.0",
        "ultralytics>=8.0.0",
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
            "sphinx>=4.0",
            "sphinx-rtd-theme>=0.5",
        ],
    },
    package_data={
        "circle_detection_sdk": [
            "models/*.pt",
            "models/*.yaml",
            "*.md",
        ],
    },
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "circle-detect=circle_detection_sdk.cli:main",
        ],
    },
    keywords=[
        "computer vision",
        "circle detection",
        "hough transform",
        "yolo",
        "object detection",
        "image processing",
        "machine learning",
        "deep learning",
    ],
    project_urls={
        "Bug Reports": "https://github.com/ruantong/circle-detection-hough/issues",
        "Source": "https://github.com/ruantong/circle-detection-hough",
        "Documentation": "https://circle-detection-hough.readthedocs.io/",
    },
)