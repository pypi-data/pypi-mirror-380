"""
Circle Detection SDK

基于改进的Hough变换和YOLO目标检测的圆形检测SDK

主要功能:
- 多算法融合的圆形检测
- YOLO目标检测集成
- 动态参数调整
- 高精度圆形定位
- 可视化结果展示

作者: Circle Detection Team
版本: 1.0.0
"""

# 从同目录下的main.py导入ImprovedCircleDetector类
from .main import ImprovedCircleDetector

__version__ = "1.0.0"
__author__ = "Circle Detection Team"
__email__ = "support@circledetection.com"

__all__ = ["ImprovedCircleDetector"]