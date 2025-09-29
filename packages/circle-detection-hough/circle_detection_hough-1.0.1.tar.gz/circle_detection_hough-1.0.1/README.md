# Circle Detection SDK

基于改进的Hough变换和YOLO目标检测的圆形检测SDK，提供高精度的圆形检测功能。

## 功能特性

- **多算法融合**: 结合YOLO目标检测、改进的Hough变换、随机Hough变换和最小二乘拟合
- **动态参数调整**: 自动调整检测参数以获得最佳检测效果
- **颜色验证**: 支持基于颜色信息的圆形验证
- **可视化功能**: 提供丰富的检测结果可视化选项
- **高性能**: 优化的算法实现，支持实时检测
- **一键检测**: 提供简单易用的一键检测接口

## 安装

### 从PyPI安装（推荐）

```bash
pip install circle-detection-sdk
```

### 从源码安装

```bash
git clone https://github.com/yourusername/circle-detection-sdk.git
cd circle-detection-sdk
pip install -e .
```

### 依赖要求

- Python >= 3.7
- OpenCV >= 4.5.0
- NumPy >= 1.19.0
- PyTorch >= 1.9.0
- Ultralytics >= 8.0.0

## 快速开始

### 一键检测（推荐）

```python
from circle_detection_sdk import ImprovedCircleDetector
import cv2

# 初始化检测器
detector = ImprovedCircleDetector()

# 加载图像
image = cv2.imread('your_image.jpg')

# 一键检测所有圆形（自动使用YOLO+圆形检测）
circles = detector.detect_all_circles(
    image, 
    save_result=True,  # 自动保存可视化结果
    output_path="detection_result.jpg"
)

print(f"检测到 {len(circles)} 个圆形")
for i, (x, y, radius, confidence) in enumerate(circles, 1):
    print(f"圆形 {i}: 圆心({x:.1f}, {y:.1f}), 半径={radius:.1f}, 置信度={confidence:.3f}")
```

### 基本使用

```python
from circle_detection_sdk import ImprovedCircleDetector
import cv2

# 初始化检测器
detector = ImprovedCircleDetector()

# 加载图像
image = cv2.imread('your_image.jpg')

# 检测圆形
circles = detector.detect_circles(image)

# 可视化结果
result_image = detector.visualize_combined_results(image, circles)

# 保存结果
cv2.imwrite('result.jpg', result_image)
```

### 高级使用

```python
from circle_detection_sdk import ImprovedCircleDetector
import cv2

# 使用自定义参数初始化检测器
detector = ImprovedCircleDetector(
    yolo_model_path='path/to/your/model.pt',
    confidence_threshold=0.5,
    iou_threshold=0.4
)

# 加载图像
image = cv2.imread('your_image.jpg')

# 使用YOLO检测目标区域
yolo_results = detector.detect_objects_with_yolo(image)

# 在检测区域内进行圆形检测
circles = detector.detect_circles_in_regions(image, yolo_results)

# 提取颜色信息
color_info = detector.extract_color_info(image, circles)

# 可视化结果
result_image = detector.visualize_combined_results(
    image, 
    circles, 
    yolo_results=yolo_results,
    show_yolo=True,
    show_circles=True
)

# 显示结果
cv2.imshow('Detection Results', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

## API 参考

### ImprovedCircleDetector

主要的圆形检测类，提供完整的检测功能。

#### 初始化参数

- `yolo_model_path` (str, optional): YOLO模型文件路径，默认使用内置模型
- `confidence_threshold` (float): YOLO检测置信度阈值，默认0.25
- `iou_threshold` (float): YOLO非极大值抑制IoU阈值，默认0.45

#### 主要方法

##### `detect_circles(image, **kwargs)`

检测图像中的圆形。

**参数:**
- `image`: 输入图像 (numpy.ndarray)
- `**kwargs`: 其他检测参数

**返回:**
- `list`: 检测到的圆形列表，每个圆形包含 (x, y, radius) 信息

##### `detect_objects_with_yolo(image)`

使用YOLO检测图像中的目标。

**参数:**
- `image`: 输入图像 (numpy.ndarray)

**返回:**
- `list`: YOLO检测结果列表

##### `visualize_combined_results(image, circles, **kwargs)`

可视化检测结果。

**参数:**
- `image`: 原始图像
- `circles`: 检测到的圆形列表
- `yolo_results`: YOLO检测结果 (可选)
- `show_yolo`: 是否显示YOLO检测框 (bool)
- `show_circles`: 是否显示圆形检测结果 (bool)

**返回:**
- `numpy.ndarray`: 可视化结果图像

##### `extract_color_info(image, circles)`

提取圆形区域的颜色信息。

**参数:**
- `image`: 输入图像
- `circles`: 圆形列表

**返回:**
- `list`: 每个圆形的颜色信息

## 检测算法

### 1. YOLO目标检测
- 使用预训练的YOLO模型识别图像中的目标区域
- 支持自定义模型和参数调整

### 2. 改进的Hough变换
- 基于传统Hough变换的改进算法
- 动态参数调整以适应不同场景

### 3. 随机Hough变换
- 使用随机采样提高检测效率
- 适用于复杂背景下的圆形检测

### 4. 最小二乘拟合
- 对检测到的边缘点进行圆形拟合
- 提供更精确的圆形参数估计

## 配置选项

### 检测参数

```python
# 圆形检测参数
detection_params = {
    'num_iterations': 5000,        # 随机Hough变换迭代次数
    'conf_threshold': 0.5,         # YOLO检测置信度阈值
    'save_result': True,           # 是否保存检测结果
    'output_path': 'result.jpg'    # 结果保存路径
}

# 使用自定义参数进行一键检测
circles = detector.detect_all_circles(image, **detection_params)

# 或者初始化时设置检测器参数
detector = ImprovedCircleDetector(
    circle_detection_threshold=0.3,  # 圆形检测阈值
    error_range=10,                  # 误差范围
    noise_tolerance=2                # 噪声容忍度
)
```

### YOLO参数

```python
# YOLO检测参数
yolo_params = {
    'confidence_threshold': 0.5,  # 置信度阈值
    'iou_threshold': 0.4,        # IoU阈值
    'max_detections': 100        # 最大检测数量
}
```

## 性能优化

### 1. 图像预处理
- 建议输入图像分辨率不超过1920x1080
- 确保图像质量良好，避免过度模糊

### 2. 参数调整
- 根据具体应用场景调整检测参数
- 使用动态参数调整功能获得最佳效果

### 3. 硬件加速
- 支持GPU加速的YOLO推理
- 建议使用CUDA兼容的GPU以获得最佳性能

## 故障排除

### 常见问题

1. **检测精度不高**
   - 调整Hough变换参数
   - 检查图像质量和预处理
   - 尝试不同的检测算法组合

2. **检测速度慢**
   - 降低输入图像分辨率
   - 调整YOLO检测参数
   - 使用GPU加速

3. **模型加载失败**
   - 检查模型文件路径
   - 确认模型文件完整性
   - 验证PyTorch和Ultralytics版本兼容性

## 依赖项

- Python >= 3.7
- OpenCV >= 4.5.0
- NumPy >= 1.19.0
- PyTorch >= 1.9.0
- Ultralytics >= 8.0.0
- Matplotlib >= 3.3.0
- SciPy >= 1.6.0

## 许可证

MIT License

## 贡献

欢迎提交Issue和Pull Request来改进这个项目。

## 更新日志

### v1.0.0
- 初始版本发布
- 支持多算法融合的圆形检测
- 集成YOLO目标检测
- 提供完整的可视化功能

## 联系方式

- 邮箱: support@circledetection.com
- GitHub: https://github.com/your-username/circle-detection-sdk
- 文档: https://circle-detection-sdk.readthedocs.io/