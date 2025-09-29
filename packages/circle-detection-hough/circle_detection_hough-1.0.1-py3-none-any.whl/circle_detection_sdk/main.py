import cv2
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations
import random
from scipy.optimize import least_squares
import math
import torch
from ultralytics import YOLO
import time
from pathlib import Path
import os

# 解决OpenMP库冲突问题
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

# 配置matplotlib中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

class ImprovedCircleDetector:
    def __init__(self, circle_detection_threshold=0.3, error_range=10, noise_tolerance=2, yolo_model_path=None):
        """
        改进的圆形检测器
        
        参数:
        circle_detection_threshold: 圆形检测阈值，边缘点占总数的比例
        error_range: 误差范围σ
        noise_tolerance: 噪声容忍度δ
        yolo_model_path: YOLO模型路径
        """
        self.circle_detection_threshold = circle_detection_threshold
        self.error_range = error_range
        self.noise_tolerance = noise_tolerance
        
        # 动态参数调整策略配置 - 10个级别的渐进式参数调整
        self.dynamic_params = [
            {'error_range': 10, 'noise_tolerance': 2},   # 级别1: 最保守参数
            {'error_range': 12, 'noise_tolerance': 2},   # 级别2: 微调error_range
            {'error_range': 15, 'noise_tolerance': 3},   # 级别3: 适中参数
            {'error_range': 18, 'noise_tolerance': 3},   # 级别4: 进一步放宽
            {'error_range': 20, 'noise_tolerance': 4},   # 级别5: 宽松参数
            {'error_range': 23, 'noise_tolerance': 4},   # 级别6: 更宽松
            {'error_range': 25, 'noise_tolerance': 5},   # 级别7: 很宽松
            {'error_range': 28, 'noise_tolerance': 5},   # 级别8: 非常宽松
            {'error_range': 30, 'noise_tolerance': 6},   # 级别9: 极宽松
            {'error_range': 35, 'noise_tolerance': 7},   # 级别10: 最宽松参数
        ]
        
        # 初始化YOLO模型
        self.yolo_model = None
        
        # 如果没有指定模型路径，自动查找内置模型
        if yolo_model_path is None:
            # 获取当前文件所在目录
            current_dir = Path(__file__).parent
            # 尝试多个可能的模型路径
            possible_paths = [
                current_dir / "models" / "best1.pt",
                current_dir.parent / "yolo" / "best1.pt",
                current_dir.parent / "circle_detection_sdk" / "models" / "best1.pt",
                Path("circle_detection_sdk/models/best1.pt"),
                Path("yolo/best1.pt"),
                Path("models/best1.pt")
            ]
            
            for path in possible_paths:
                if path.exists():
                    yolo_model_path = str(path)
                    print(f"自动找到YOLO模型: {yolo_model_path}")
                    break
        
        # 加载YOLO模型
        if yolo_model_path and Path(yolo_model_path).exists():
            try:
                self.yolo_model = YOLO(yolo_model_path)
                print(f"YOLO模型加载成功: {yolo_model_path}")
            except Exception as e:
                print(f"YOLO模型加载失败: {e}")
                self.yolo_model = None
        else:
            print("警告: 未找到YOLO模型文件，将使用无YOLO模式")
    
    def detect_objects_with_yolo(self, image, conf_threshold=0.5):
        """
        使用YOLO模型检测图像中的物体
        
        参数:
        image: 输入图像
        conf_threshold: 置信度阈值
        
        返回:
        detections: 检测结果列表，每个元素包含 (x1, y1, x2, y2, conf, class_id)
        """
        if self.yolo_model is None:
            return []
        
        try:
            # 进行推理
            start_time = time.time()
            results = self.yolo_model(image, conf=conf_threshold, verbose=False)
            inference_time = time.time() - start_time
            
            detections = []
            
            # 处理检测结果
            for result in results:
                boxes = result.boxes
                if boxes is not None:
                    for box in boxes:
                        # 获取边界框坐标
                        x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                        conf = box.conf[0].cpu().numpy()
                        class_id = int(box.cls[0].cpu().numpy())
                        
                        detections.append((int(x1), int(y1), int(x2), int(y2), float(conf), class_id))
            
            return detections
            
        except Exception as e:
            print(f"YOLO检测过程中出现错误: {e}")
            return []
    

    
    def visualize_yolo_detections_with_numbers(self, image, detections, save_path="yolo_detection_result.png"):
        """
        可视化YOLO检测结果，重点突出物体编号
        
        参数:
        image: 原始图像
        detections: 检测结果列表
        save_path: 保存路径
        """
        if len(detections) == 0:
            return image.copy()
        
        # 创建结果图像
        result_image = image.copy()
        
        # 统一使用绿色
        color = (0, 255, 0)  # 绿色
        
        for i, (x1, y1, x2, y2, conf, class_id) in enumerate(detections):  # 循环使用颜色
            
            # 绘制边界框（更粗的线条）
            cv2.rectangle(result_image, (x1, y1), (x2, y2), color, 3)
            
            # 添加大号物体编号（在框的左上角）
            number_text = f"#{i+1}"
            number_size = cv2.getTextSize(number_text, cv2.FONT_HERSHEY_SIMPLEX, 1.2, 3)[0]
            
            # 绘制编号背景（圆形）
            center_x = x1 + number_size[0] // 2 + 10
            center_y = y1 - 15
            cv2.circle(result_image, (center_x, center_y), 25, color, -1)
            cv2.circle(result_image, (center_x, center_y), 25, (0, 0, 0), 2)
            
            # 绘制编号文字（白色）
            cv2.putText(result_image, number_text, (x1 + 5, y1 - 5), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 3)
            
            # 添加详细标签（在框的底部）
            label = f"Object_{class_id}: {conf:.2f}"
            label_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)[0]
            
            # 绘制标签背景
            cv2.rectangle(result_image, (x1, y2), 
                         (x1 + label_size[0] + 10, y2 + label_size[1] + 10), color, -1)
            
            # 绘制标签文字
            cv2.putText(result_image, label, (x1 + 5, y2 + label_size[1] + 5), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        # 保存结果
        cv2.imwrite(save_path, result_image)
        
        return result_image
    
    def edge_detection(self, image, show_steps=True):
        """
        步骤1: 使用边缘检测算法获取待检测图像中的边缘点
        """
        # 转换为灰度图
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image.copy()
        
        # 高斯模糊降噪
        blurred = cv2.GaussianBlur(gray, (5, 5), 1.4)
        
        # Canny边缘检测
        edges = cv2.Canny(blurred, 50, 150)
        
        # 边缘增强处理：在白布上用粗黑线条绘制边缘
        # 创建白色背景图像
        white_canvas = np.ones_like(gray) * 255
        
        # 膨胀操作，使边缘线条更粗
        kernel = np.ones((3, 3), np.uint8)  # 3x3膨胀核
        thick_edges = cv2.dilate(edges, kernel, iterations=2)
        
        # 在白色画布上绘制粗黑边缘
        enhanced_canvas = white_canvas.copy()
        enhanced_canvas[thick_edges > 0] = 0  # 边缘位置设为黑色
        
        # 基于增强后的图像重新提取边缘点
        # 对增强图像进行边缘检测
        final_edges = cv2.Canny(enhanced_canvas, 50, 150)
        
        # 获取最终边缘点坐标（优化版本）
        y_coords, x_coords = np.where(final_edges > 0)
        edge_points = np.column_stack((x_coords, y_coords))
        
        # 显示边缘检测的中间步骤
        # if show_steps:
        #     self.show_edge_detection_steps(image, gray, blurred, edges, edge_points, enhanced_canvas, final_edges)
        
        return final_edges, edge_points
    

    
    def calculate_circle_from_three_points(self, p1, p2, p3):
        """
        根据三个不共线的点计算圆心和半径
        """
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        
        # 检查三点是否共线
        det = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
        if abs(det) < 1e-6:
            return None, None
        
        # 计算圆心
        d = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
        if abs(d) < 1e-6:
            return None, None
        
        ux = ((x1**2 + y1**2) * (y2 - y3) + (x2**2 + y2**2) * (y3 - y1) + (x3**2 + y3**2) * (y1 - y2)) / d
        uy = ((x1**2 + y1**2) * (x3 - x2) + (x2**2 + y2**2) * (x1 - x3) + (x3**2 + y3**2) * (x2 - x1)) / d
        
        # 计算半径
        radius = np.sqrt((x1 - ux)**2 + (y1 - uy)**2)
        
        return (ux, uy), radius
    
    def count_points_on_circle(self, edge_points, center, radius, tolerance=2):
        """
        计算在圆上的边缘点个数（向量化优化版本）
        """
        if center is None or radius is None:
            return 0, []
        
        cx, cy = center
        
        # 向量化计算距离
        distances = np.sqrt((edge_points[:, 0] - cx)**2 + (edge_points[:, 1] - cy)**2)
        
        # 向量化筛选
        mask = np.abs(distances - radius) <= tolerance
        points_on_circle = edge_points[mask]
        
        return np.sum(mask), points_on_circle
    
    def calculate_variance(self, edge_points, center, radius):
        """
        计算边缘点到圆心距离与半径的方差（向量化优化版本）
        """
        if center is None or radius is None:
            return float('inf')
        
        if len(edge_points) == 0:
            return float('inf')
        
        cx, cy = center
        
        # 向量化计算所有点到圆心的距离
        distances = np.sqrt((edge_points[:, 0] - cx)**2 + (edge_points[:, 1] - cy)**2)
        
        # 向量化计算方差
        variance = np.mean((distances - radius)**2)
        
        return variance
    
    def random_hough_transform(self, edge_points, num_iterations=5000):
        """
        步骤2: 改进的随机Hough变换检测圆形
        """
        
        if len(edge_points) < 3:
            return None, None, None
        
        best_variance = float('inf')
        best_center = None
        best_radius = None
        candidate_circles = []
        valid_circles_count = 0
        failed_calculations = 0
        invalid_radius_count = 0
        low_support_count = 0
        
        # 预转换为列表以提高随机采样效率
        edge_points_list = edge_points.tolist() if isinstance(edge_points, np.ndarray) else list(edge_points)
        edge_points_array = np.array(edge_points) if not isinstance(edge_points, np.ndarray) else edge_points
        total_points = len(edge_points)
        
        # 步骤一：随机选择三点组合
        for i in range(num_iterations):
            # 随机选择三个不同的点索引（更高效）
            if total_points < 3:
                continue
                
            indices = np.random.choice(total_points, 3, replace=False)
            three_points = edge_points_array[indices]
            center, radius = self.calculate_circle_from_three_points(*three_points)
            
            if center is None or radius is None:
                failed_calculations += 1
                continue
            
            if radius <= 0 or radius > 1000:  # 添加合理的半径范围检查
                invalid_radius_count += 1
                continue
            
            # 计算在圆上的点数
            points_count, points_on_circle = self.count_points_on_circle(
                edge_points_array, center, radius, self.noise_tolerance
            )
            
            # 检查是否满足圆形检测阈值
            ratio = points_count / total_points
            
            # 每1000次迭代输出一些详细信息
            if (i + 1) % 1000 == 0 and i < 10:
                pass
            
            if ratio > self.circle_detection_threshold:
                valid_circles_count += 1
                # 计算方差
                variance = self.calculate_variance(edge_points_array, center, radius)
                candidate_circles.append((center, radius, variance, points_on_circle))
                
                # print(f"  候选圆 {valid_circles_count}: 圆心({center[0]:.2f}, {center[1]:.2f}), 半径{radius:.2f}, 支持点{points_count}个({ratio:.3f}), 方差{variance:.2f}")
                
                # 记录最小方差的圆
                if variance < best_variance:
                    best_variance = variance
                    best_center = center
                    best_radius = radius
                    # print(f"    -> 更新最佳候选圆 (方差: {variance:.2f})")
                    
                    # 早期停止优化：如果找到非常好的候选圆且已有足够样本，可以提前结束
                    if variance < 1.0 and valid_circles_count >= 5 and i > num_iterations // 4:
                        # print(f"  早期停止：找到高质量候选圆 (方差: {variance:.2f})，已完成 {i+1} 次迭代")
                        break
            else:
                low_support_count += 1
            
            # 每500次迭代输出一次进度（减少I/O开销）
            if (i + 1) % 500 == 0:
                pass  # print(f"  已完成 {i + 1}/{num_iterations} 次迭代，找到 {valid_circles_count} 个候选圆")
        
        if best_center is not None:
            pass  # print(f"  最佳候选圆: 圆心({best_center[0]:.2f}, {best_center[1]:.2f}), 半径{best_radius:.2f}, 方差{best_variance:.2f}")
        else:
            # print("  未找到符合条件的候选圆")
            pass
        
        return best_center, best_radius, candidate_circles
    
    def standard_hough_transform(self, edge_points, center_estimate, radius_estimate):
        """
        步骤三：标准Hough变换进一步筛选
        """
        # print("\n=== 步骤3: 标准Hough变换精化 ===")
        
        if center_estimate is None or radius_estimate is None:
            # print("输入的圆心或半径估计值为空，无法进行精化")
            return None, None, []
        
        cx_est, cy_est = center_estimate
        r_est = radius_estimate
        sigma = self.error_range
        
        # print(f"初始估计: 圆心({cx_est:.2f}, {cy_est:.2f}), 半径{r_est:.2f}")
        # print(f"搜索范围σ: {sigma}")
        
        # 定义搜索范围
        a_min, a_max = int(cx_est - sigma), int(cx_est + sigma)
        b_min, b_max = int(cy_est - sigma), int(cy_est + sigma)
        r_min, r_max = int(r_est - sigma), int(r_est + sigma)
        
        # 确保范围有效
        r_min = max(1, r_min)
        
        # print(f"参数空间范围:")
        # print(f"  a (圆心x): [{a_min}, {a_max}]")
        # print(f"  b (圆心y): [{b_min}, {b_max}]")
        # print(f"  r (半径): [{r_min}, {r_max}]")
        
        total_combinations = (a_max - a_min + 1) * (b_max - b_min + 1) * (r_max - r_min + 1)
        # print(f"总参数组合数: {total_combinations}")
        
        # 三维累加器
        accumulator = {}
        max_count = 0
        processed = 0
        
        # print("\n开始参数空间搜索...")
        
        # 转换为numpy数组以提高计算效率
        edge_points_array = np.array(edge_points) if not isinstance(edge_points, np.ndarray) else edge_points
        
        # 遍历参数空间（优化版本）
        for a in range(a_min, a_max + 1):
            for b in range(b_min, b_max + 1):
                for r in range(r_min, r_max + 1):
                    # 向量化计算所有点到圆心的距离
                    distances = np.sqrt((edge_points_array[:, 0] - a)**2 + (edge_points_array[:, 1] - b)**2)
                    # 向量化统计满足条件的点数
                    count = np.sum(np.abs(distances - r) <= self.noise_tolerance)
                    
                    accumulator[(a, b, r)] = count
                    
                    if count > max_count:
                        max_count = count
                        # print(f"  新的最高得分: {count} (圆心({a}, {b}), 半径{r})")
                    
                    processed += 1
                    
                    # 每5000个组合输出一次进度（减少I/O开销）
                    if processed % 5000 == 0:
                        progress = processed / total_combinations * 100
                        # print(f"  搜索进度: {processed}/{total_combinations} ({progress:.1f}%), 当前最高得分: {max_count}")
        
        # 找到最大累加值对应的参数
        if not accumulator:
            # print("累加器为空，搜索失败")
            return None, None, []
        
        best_params = max(accumulator.keys(), key=lambda k: accumulator[k])
        best_center = (best_params[0], best_params[1])
        best_radius = best_params[2]
        best_score = accumulator[best_params]
        
        # print(f"\n标准Hough变换完成:")
        # print(f"  最佳参数: 圆心({best_center[0]}, {best_center[1]}), 半径{best_radius}")
        # print(f"  最高得分: {best_score} (支持点数量)")
        
        # 提取该圆上的边缘点（向量化优化）
        distances = np.sqrt((edge_points_array[:, 0] - best_center[0])**2 + (edge_points_array[:, 1] - best_center[1])**2)
        mask = np.abs(distances - best_radius) <= self.noise_tolerance
        filtered_points = edge_points_array[mask]
        
        return best_center, best_radius, filtered_points
    
    def least_squares_fitting(self, points):
        """
        步骤4：最小二乘法精确定位圆心（亚像素级）
        """
        
        if len(points) < 3:
            return None, None
        
        points = np.array(points)
        
        def circle_residuals(params, points):
            cx, cy, r = params
            distances = np.sqrt((points[:, 0] - cx)**2 + (points[:, 1] - cy)**2)
            return distances - r
        
        # 初始估计（使用点的重心和平均距离）
        center_init = np.mean(points, axis=0)
        distances_init = np.sqrt(np.sum((points - center_init)**2, axis=1))
        radius_init = np.mean(distances_init)
        
        initial_guess = [center_init[0], center_init[1], radius_init]
        
        try:
            # 最小二乘拟合
            result = least_squares(circle_residuals, initial_guess, args=(points,))
            
            if result.success:
                cx, cy, r = result.x
                
                # 计算拟合精度
                final_distances = np.sqrt((points[:, 0] - cx)**2 + (points[:, 1] - cy)**2)
                residuals = final_distances - r
                rms_error = np.sqrt(np.mean(residuals**2))
                max_error = np.max(np.abs(residuals))
                
                # 与初始估计的比较
                center_shift = np.sqrt((cx - center_init[0])**2 + (cy - center_init[1])**2)
                radius_change = abs(r - radius_init)
                
                return (cx, cy), r
            else:
                return None, None
        except Exception as e:
            return None, None
    
    def expand_detection_box(self, x1, y1, x2, y2, image_shape, expand_pixels=50):
        """
        扩展YOLO检测框，向四周扩大指定像素
        
        Args:
            x1, y1, x2, y2: 原始检测框坐标
            image_shape: 图像尺寸 (height, width, channels)
            expand_pixels: 向四周扩展的像素数
            
        Returns:
            tuple: 扩展后的检测框坐标 (new_x1, new_y1, new_x2, new_y2)
        """
        height, width = image_shape[:2]
        
        # 向四周扩展
        new_x1 = max(0, x1 - expand_pixels)
        new_y1 = max(0, y1 - expand_pixels)
        new_x2 = min(width, x2 + expand_pixels)
        new_y2 = min(height, y2 + expand_pixels)
        
        return new_x1, new_y1, new_x2, new_y2
    
    def detect_circles_in_regions(self, image, detections, num_iterations=5000, show_individual_steps=False, expand_pixels=50):
        """
        在YOLO检测的每个区域内进行圆形检测
        
        参数:
        image: 原始图像
        detections: YOLO检测结果列表
        num_iterations: 每个区域的随机Hough迭代次数
        show_individual_steps: 是否显示每个区域的详细步骤
        expand_pixels: 检测框向四周扩展的像素数
        
        返回:
        results: 检测结果列表，每个元素包含 (region_info, center, radius, detection_success)
        """
        if len(detections) == 0:
            print("没有检测到物体区域，执行全图圆形检测")
            center, radius, edges, edge_points = self.detect_circles(image, num_iterations)
            return [(None, center, radius, center is not None)]
        
        results = []
        total_start_time = time.time()
        
        for i, (x1, y1, x2, y2, conf, class_id) in enumerate(detections):
            print(f"\n--- 处理区域 {i+1}/{len(detections)} ---")
            print(f"原始区域位置: ({x1}, {y1}) -> ({x2}, {y2})")
            print(f"原始区域尺寸: {x2-x1} x {y2-y1}")
            
            # 扩展检测框
            exp_x1, exp_y1, exp_x2, exp_y2 = self.expand_detection_box(
                x1, y1, x2, y2, image.shape, expand_pixels
            )
            print(f"扩展后区域位置: ({exp_x1}, {exp_y1}) -> ({exp_x2}, {exp_y2})")
            print(f"扩展后区域尺寸: {exp_x2-exp_x1} x {exp_y2-exp_y1}")
            print(f"置信度: {conf:.3f}, 类别: {class_id}")
            
            region_start_time = time.time()
            
            # 提取扩展后的区域图像
            try:
                # 使用扩展后的坐标提取区域图像
                region_image = image[exp_y1:exp_y2, exp_x1:exp_x2]
                
                if region_image.size == 0:
                    print(f"  区域 {i+1}: 无效区域，跳过")
                    results.append(((x1, y1, x2, y2, conf, class_id), None, None, False))
                    continue
                
                print(f"  提取区域图像尺寸: {region_image.shape}")
                
                # 在区域内进行圆形检测（关闭详细步骤显示以提高速度）
                center, radius, edges, edge_points = self.detect_circles(
                    region_image, num_iterations, show_steps=show_individual_steps
                )
                
                # 将相对坐标转换为绝对坐标（基于扩展后的区域）
                if center is not None:
                    abs_center = (center[0] + exp_x1, center[1] + exp_y1)
                    
                    # 对绝对坐标进行颜色验证
                    print(f"  区域 {i+1}: 检测成功，进行颜色验证...")
                    color_valid = self.validate_circle_color(image, abs_center)
                    
                    final_center = abs_center
                    final_color_valid = color_valid
                    
                    if color_valid:
                        print(f"  区域 {i+1}: 颜色验证通过!")
                    else:
                        print(f"  区域 {i+1}: 颜色验证失败，保留原检测结果")
                    
                    results.append(((x1, y1, x2, y2, conf, class_id), final_center, radius, final_color_valid))
                else:
                    print(f"  区域 {i+1}: 未检测到圆形")
                    results.append(((x1, y1, x2, y2, conf, class_id), None, None, False))
                
                region_time = time.time() - region_start_time
                print(f"  区域 {i+1} 处理用时: {region_time:.3f}秒")
                
            except Exception as e:
                print(f"  区域 {i+1} 处理出错: {e}")
                results.append(((x1, y1, x2, y2, conf, class_id), None, None, False))
        
        total_time = time.time() - total_start_time
        successful_detections = sum(1 for _, _, _, success in results if success)
        
        print(f"\n=== 多区域检测完成 ===")
        print(f"总处理时间: {total_time:.3f}秒")
        print(f"平均每区域: {total_time/len(detections):.3f}秒")
        print(f"成功检测: {successful_detections}/{len(detections)} 个区域")
        print(f"成功率: {successful_detections/len(detections)*100:.1f}%")
        
        return results
    
    def detect_circle_in_single_region(self, image, detection, object_num, num_iterations=5000, expand_pixels=50):
        """
        在单个YOLO检测区域内进行圆形检测
        
        参数:
        image: 输入图像
        detection: 单个YOLO检测结果 (x1, y1, x2, y2, conf, class_id)
        object_num: 物体编号
        num_iterations: 迭代次数
        expand_pixels: 扩展检测区域的像素数
        
        返回:
        result: (region_info, center, radius, success)
        """
        x1, y1, x2, y2, conf, class_id = detection
        
        print(f"  原始区域: ({x1}, {y1}) -> ({x2}, {y2})")
        print(f"  区域尺寸: {x2-x1} x {y2-y1}")
        
        # 扩展检测区域
        expanded_x1, expanded_y1, expanded_x2, expanded_y2 = self.expand_detection_box(
            x1, y1, x2, y2, image.shape, expand_pixels
        )
        
        print(f"  扩展后区域: ({expanded_x1}, {expanded_y1}) -> ({expanded_x2}, {expanded_y2})")
        print(f"  扩展后尺寸: {expanded_x2-expanded_x1} x {expanded_y2-expanded_y1}")
        
        # 提取区域图像
        region_image = image[expanded_y1:expanded_y2, expanded_x1:expanded_x2].copy()
        
        if region_image.size == 0:
            print(f"  区域图像为空，跳过")
            return (detection, None, None, False)
        
        print(f"  提取区域图像尺寸: {region_image.shape}")
        
        try:
            # 在区域内进行圆形检测
            print(f"  开始圆形检测...")
            
            center, radius, edges, edge_points = self.detect_circles(
                region_image, num_iterations, show_steps=False
            )
            
            if center is not None:
                # 将相对坐标转换为绝对坐标
                absolute_center = (center[0] + expanded_x1, center[1] + expanded_y1)
                
                return (detection, absolute_center, radius, True)
            else:
                print(f"  未找到有效圆形")
                return (detection, None, None, False)
                
        except Exception as e:
            print(f"  检测过程中出现错误: {e}")
            return (detection, None, None, False)
    
        return result_image
    
    def detect_circles(self, image, num_iterations=5000, show_steps=True, max_retries=10):
        """
        完整的圆形检测流程，包含动态参数调整和颜色验证
        """
        # 使用动态参数调整策略
        result = self.detect_circles_with_dynamic_params(image, num_iterations, show_steps)
        return result
    
    def detect_circles_with_dynamic_params(self, image, num_iterations=5000, show_steps=True):
        """
        使用动态参数调整策略的圆形检测
        """
        
        # 遍历所有参数级别
        for level, params in enumerate(self.dynamic_params):
            # 临时更新参数
            original_error_range = self.error_range
            original_noise_tolerance = self.noise_tolerance
            
            self.error_range = params['error_range']
            self.noise_tolerance = params['noise_tolerance']
            
            try:
                # 执行单次检测
                result = self.detect_circles_single_attempt(image, num_iterations, show_steps, level + 1)
                
                if result[0] is not None:  # 检测成功
                    center_final, radius_final, edges, final_points = result
                    
                    # 颜色验证
                    if self.validate_circle_color(image, center_final):
                        return center_final, radius_final, edges, final_points
                    
            finally:
                # 恢复原始参数
                self.error_range = original_error_range
                self.noise_tolerance = original_noise_tolerance
        
        return None, None, None, []
    
    def detect_circles_single_attempt(self, image, num_iterations, show_steps, level):
        """
        执行单次圆形检测尝试
        """
        # 步骤1: 边缘检测
        edges, edge_points = self.edge_detection(image, show_steps=False)  # 减少输出
        
        if len(edge_points) < 3:
            print("检测失败: 边缘点数量不足")
            return None, None, edges, []
        
        # 步骤2: 改进的随机Hough变换
        center_est, radius_est, candidates = self.random_hough_transform(
            edge_points, num_iterations
        )
        
        if center_est is None:
            print("检测失败: 未检测到符合条件的圆")
            return None, None, edges, edge_points
        
        # 步骤3: 标准Hough变换精化
        center_refined, radius_refined, filtered_points = self.standard_hough_transform(
            edge_points, center_est, radius_est
        )
        
        if center_refined is None:
            print("警告: Hough变换精化失败，返回初步检测结果")
            center_final = center_est
            radius_final = radius_est
            final_points = edge_points
        else:
            # 步骤4: 最小二乘法亚像素级精确定位
            center_final = center_refined
            radius_final = radius_refined
            final_points = filtered_points
            
            if len(filtered_points) >= 3:
                center_ls, radius_ls = self.least_squares_fitting(filtered_points)
                
                if center_ls is not None:
                    center_final = center_ls
                    radius_final = radius_ls
                    final_points = filtered_points
        
        return center_final, radius_final, edges, final_points
    
    
    def extract_color_info(self, image, center):
        """
        提取圆心位置的HSL和HSB颜色信息
        
        参数:
        image: 原始图像
        center: 圆心坐标 (x, y)
        
        返回:
        hsl_values: HSL值 (H, S, L)
        hsb_values: HSB值 (H, S, B)
        """
        x, y = int(center[0]), int(center[1])
        
        # 确保坐标在图像范围内
        if 0 <= x < image.shape[1] and 0 <= y < image.shape[0]:
            # 获取BGR像素值
            bgr_pixel = image[y, x]
            
            # 转换为RGB
            rgb_pixel = bgr_pixel[::-1]  # BGR to RGB
            
            # 转换为HSV (OpenCV中的HSV实际上是HSB)
            hsv_pixel = cv2.cvtColor(np.uint8([[bgr_pixel]]), cv2.COLOR_BGR2HSV)[0][0]
            
            # 转换为HLS (OpenCV中的HLS)
            hls_pixel = cv2.cvtColor(np.uint8([[bgr_pixel]]), cv2.COLOR_BGR2HLS)[0][0]
            
            # HSB值 (HSV)
            h_hsb, s_hsb, b_hsb = hsv_pixel[0], hsv_pixel[1], hsv_pixel[2]
            
            # HSL值 (HLS)
            h_hsl, l_hsl, s_hsl = hls_pixel[0], hls_pixel[1], hls_pixel[2]
            
            return (h_hsl, s_hsl, l_hsl), (h_hsb, s_hsb, b_hsb)
        else:
            return (0, 0, 0), (0, 0, 0)
    
    def validate_circle_color(self, image, center):
        """
        验证圆心颜色是否满足条件
        条件：HSL第3个通道(L) < 9 且 HSB第3个通道(B) < 10
        
        参数:
        image: 原始图像
        center: 圆心坐标 (x, y)
        
        返回:
        bool: 是否满足颜色条件
        """
        hsl_values, hsb_values = self.extract_color_info(image, center)
        
        # 检查条件：HSL的L通道 < 9 且 HSB的B通道 < 10
        hsl_l = hsl_values[2]  # L通道
        hsb_b = hsb_values[2]  # B通道
        
        is_valid = hsl_l < 9 and hsb_b < 10
        
        return is_valid
    
    
    def visualize_combined_results(self, image, yolo_detections, circle_results, save_path="combined_detection_result.png"):
        """
        综合可视化YOLO检测和圆形检测结果
        
        参数:
        image: 原始图像
        yolo_detections: YOLO检测结果
        circle_results: 圆形检测结果
        save_path: 保存路径
        """
        print(f"\n=== 综合结果可视化 ===")
        
        # 创建结果图像
        result_image = image.copy()
        if len(result_image.shape) == 2:
            result_image = cv2.cvtColor(result_image, cv2.COLOR_GRAY2BGR)
        
        successful_circles = 0
        circle_number = 1  # 圆形编号计数器
        
        # 绘制每个区域的结果
        for i, (region_info, center, radius, success) in enumerate(circle_results):
            if region_info is None:  # 全图检测的情况
                if success and center is not None and radius is not None:
                    # 绘制圆形
                    cv2.circle(result_image, (int(center[0]), int(center[1])), int(radius), (0, 0, 255), 3)
                    cv2.circle(result_image, (int(center[0]), int(center[1])), 5, (0, 0, 255), -1)
                    
                    # 提取颜色信息
                    hsl_values, hsb_values = self.extract_color_info(image, center)
                    
                    # 添加圆形编号
                    cv2.putText(result_image, f"#{circle_number}", (int(center[0] - 15), int(center[1] - 15)), 
                               cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 0), 3)
                    cv2.putText(result_image, f"#{circle_number}", (int(center[0] - 15), int(center[1] - 15)), 
                               cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), 1)
                    
                    # 添加标签和颜色信息
                    label = f"Circle {circle_number}: ({center[0]:.1f}, {center[1]:.1f}), R={radius:.1f}"
                    hsl_label = f"HSL: ({hsl_values[0]}, {hsl_values[1]}, {hsl_values[2]})"
                    hsb_label = f"HSB: ({hsb_values[0]}, {hsb_values[1]}, {hsb_values[2]})"
                    
                    cv2.putText(result_image, label, (int(center[0] - radius), int(center[1] - radius - 40)), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                    cv2.putText(result_image, hsl_label, (int(center[0] - radius), int(center[1] - radius - 20)), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)
                    cv2.putText(result_image, hsb_label, (int(center[0] - radius), int(center[1] - radius - 5)), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0), 1)
                    successful_circles += 1
                    circle_number += 1
                continue
            
            # 解析区域信息
            x1, y1, x2, y2, conf, class_id = region_info
            
            # 绘制YOLO检测框
            if center is not None and radius is not None:
                if success:
                    # 检测到圆形且颜色验证通过 - 绿色框
                    cv2.rectangle(result_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    box_color = (0, 255, 0)
                    status = "✓"
                    successful_circles += 1
                else:
                    # 检测到圆形但颜色验证失败 - 橙色框
                    cv2.rectangle(result_image, (x1, y1), (x2, y2), (0, 165, 255), 2)
                    box_color = (0, 165, 255)
                    status = "⚠"
            else:
                # 未检测到圆形 - 红色框
                cv2.rectangle(result_image, (x1, y1), (x2, y2), (0, 0, 255), 2)
                box_color = (0, 0, 255)
                status = "✗"
            
            # 添加区域标签
            region_label = f"#{i+1} {status} Obj_{class_id}: {conf:.2f}"
            label_size = cv2.getTextSize(region_label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)[0]
            
            # 绘制标签背景
            cv2.rectangle(result_image, (x1, y1 - label_size[1] - 10), 
                         (x1 + label_size[0], y1), box_color, -1)
            
            # 绘制标签文字
            cv2.putText(result_image, region_label, (x1, y1 - 5), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            
            # 如果检测到圆形，绘制圆形（不管颜色验证是否通过）
            if center is not None and radius is not None:
                # 绘制圆形，根据颜色验证结果使用不同颜色
                if success:
                    # 颜色验证通过 - 蓝色圆形
                    circle_color = (255, 0, 0)
                else:
                    # 颜色验证失败 - 紫色圆形
                    circle_color = (255, 0, 255)
                
                cv2.circle(result_image, (int(center[0]), int(center[1])), int(radius), circle_color, 3)
                cv2.circle(result_image, (int(center[0]), int(center[1])), 5, circle_color, -1)
                
                # 提取颜色信息
                hsl_values, hsb_values = self.extract_color_info(image, center)
                
                # 添加圆形编号
                cv2.putText(result_image, f"#{circle_number}", (int(center[0] - 15), int(center[1] - 15)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 0), 3)
                cv2.putText(result_image, f"#{circle_number}", (int(center[0] - 15), int(center[1] - 15)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), 1)
                
                # 添加圆形信息和颜色信息
                color_status = "✓" if success else "✗"
                circle_label = f"Circle {circle_number} {color_status}: ({center[0]:.1f},{center[1]:.1f}) R:{radius:.1f}"
                hsl_label = f"HSL: ({hsl_values[0]}, {hsl_values[1]}, {hsl_values[2]})"
                hsb_label = f"HSB: ({hsb_values[0]}, {hsb_values[1]}, {hsb_values[2]})"
                
                cv2.putText(result_image, circle_label, (int(center[0] - radius), int(center[1] + radius + 20)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0), 2)
                cv2.putText(result_image, hsl_label, (int(center[0] - radius), int(center[1] + radius + 40)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)
                cv2.putText(result_image, hsb_label, (int(center[0] - radius), int(center[1] + radius + 55)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0), 1)
                circle_number += 1
        
        # 添加统计信息
        total_regions = len([r for r in circle_results if r[0] is not None]) or 1
        success_rate = (successful_circles / total_regions) * 100
        
        stats_text = [
            f"YOLO Objects: {len(yolo_detections)}",
            f"Circle Detected: {successful_circles}/{total_regions}",
            f"Success Rate: {success_rate:.1f}%"
        ]
        
        # 在图像上添加统计信息
        y_offset = 30
        for i, text in enumerate(stats_text):
            cv2.putText(result_image, text, (10, y_offset + i * 25), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.putText(result_image, text, (10, y_offset + i * 25), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 1)
        
        # 保存结果
        cv2.imwrite(save_path, result_image)
        print(f"综合检测结果已保存到: {save_path}")
        
        # 显示统计信息
        print(f"检测统计:")
        print(f"  YOLO检测物体数: {len(yolo_detections)}")
        print(f"  圆形检测成功数: {successful_circles}/{total_regions}")
        print(f"  成功率: {success_rate:.1f}%")
        
        return result_image


    def detect_all_circles(self, image, conf_threshold=0.5, num_iterations=1000, save_result=True, output_path="circle_detection_result.jpg"):
        """
        一键检测图片中所有圆形的完整接口 - 逐个输出结果
        
        参数:
        image: 输入图像
        conf_threshold: YOLO置信度阈值
        num_iterations: 圆形检测迭代次数
        save_result: 是否保存检测结果图片
        output_path: 结果图片保存路径
        
        返回:
        circles: 检测到的圆形列表，每个元素为 (x, y, radius, confidence)
        """
        circles = []
        start_time = time.time()
        
        print("=" * 60)
        print("开始圆形检测...")
        print("=" * 60)
        
        try:
            # 步骤1: YOLO目标检测
            print("\n🔍 步骤1: YOLO目标检测")
            yolo_detections = self.detect_objects_with_yolo(image, conf_threshold)
            print(f"   检测到 {len(yolo_detections)} 个潜在目标")
            
            if len(yolo_detections) > 0:
                # 步骤2: 在YOLO检测的区域内检测圆形 - 逐个处理并输出
                print(f"\n🎯 步骤2: 在 {len(yolo_detections)} 个目标区域内检测圆形")
                print("-" * 50)
                
                success_count = 0
                for i, detection in enumerate(yolo_detections, 1):
                    x1, y1, x2, y2, conf, class_id = detection
                    print(f"\n--- 处理区域 {i}/{len(yolo_detections)} ---")
                    print(f"原始区域位置: ({x1}, {y1}) -> ({x2}, {y2})")
                    print(f"原始区域尺寸: {x2-x1} x {y2-y1}")
                    
                    # 扩展检测框
                    exp_x1, exp_y1, exp_x2, exp_y2 = self.expand_detection_box(
                        x1, y1, x2, y2, image.shape, 50
                    )
                    print(f"扩展后区域位置: ({exp_x1}, {exp_y1}) -> ({exp_x2}, {exp_y2})")
                    print(f"扩展后区域尺寸: {exp_x2-exp_x1} x {exp_y2-exp_y1}")
                    print(f"置信度: {conf:.3f}, 类别: {class_id}")
                    
                    region_start_time = time.time()
                    
                    # 提取扩展后的区域图像
                    try:
                        region_image = image[exp_y1:exp_y2, exp_x1:exp_x2]
                        
                        if region_image.size == 0:
                            print(f"  区域 {i}: 无效区域，跳过")
                            print(f"❌ 区域 {i}: 未检测到圆形")
                            continue
                        
                        print(f"  提取区域图像尺寸: {region_image.shape}")
                        
                        # 在单个区域内检测圆形
                        region_result = self.detect_circle_in_single_region(
                            image, detection, i, num_iterations, 50
                        )
                        
                        region_info, center, radius, success = region_result
                        region_end_time = time.time()
                        region_time = region_end_time - region_start_time
                        
                        if success and center is not None:
                            circles.append((center[0], center[1], radius, conf))
                            success_count += 1
                            print(f"  区域 {i} 处理用时: {region_time:.3f}秒")
                            print(f"✅ 圆形 {success_count}: 圆心({center[0]:.1f}, {center[1]:.1f}), 半径={radius:.1f}, 置信度={conf:.3f}")
                        else:
                            print(f"  区域 {i} 处理用时: {region_time:.3f}秒")
                            print(f"❌ 区域 {i}: 未检测到圆形")
                            
                    except Exception as e:
                        print(f"  区域 {i} 处理出错: {e}")
                        print(f"❌ 区域 {i}: 未检测到圆形")
                        
            else:
                # 如果YOLO没检测到目标，进行全图圆形检测
                print("\n🌐 步骤2: 全图圆形检测 (YOLO未检测到目标)")
                print("-" * 50)
                
                full_image_circles = self.detect_circles(image, num_iterations, show_steps=False)
                success_count = 0
                for x, y, r in full_image_circles:
                    circles.append((x, y, r, 0.8))  # 全图检测给予固定置信度
                    success_count += 1
                    print(f"✅ 圆形 {success_count}: 圆心({x:.1f}, {y:.1f}), 半径={r:.1f}, 置信度=0.800")
            
            # 检测总结
            end_time = time.time()
            total_time = end_time - start_time
            
            print("\n" + "=" * 60)
            print("🎉 检测完成 - 结果总结")
            print("=" * 60)
            print(f"📊 总检测时间: {total_time:.2f} 秒")
            print(f"🎯 检测到圆形数量: {len(circles)} 个")
            if len(yolo_detections) > 0:
                print(f"📈 检测成功率: {len(circles)}/{len(yolo_detections)} ({len(circles)/len(yolo_detections)*100:.1f}%)")
            
            # 保存检测结果图片
            if save_result and len(circles) > 0:
                print(f"\n💾 正在保存检测结果到: {output_path}")
                self._save_detection_result(image, yolo_detections, circles, output_path)
                print(f"✅ 检测结果已保存!")
            
            return circles
            
        except Exception as e:
            print(f"❌ 检测过程中出现错误: {e}")
            return []
    
    def _save_detection_result(self, image, yolo_detections, circles, output_path):
        """保存检测结果的可视化图片"""
        result_image = image.copy()
        
        # 绘制YOLO检测框
        for detection in yolo_detections:
            x1, y1, x2, y2 = detection[:4]
            cv2.rectangle(result_image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        
        # 绘制检测到的圆形
        for i, (x, y, radius, confidence) in enumerate(circles, 1):
            # 绘制圆形
            cv2.circle(result_image, (int(x), int(y)), int(radius), (0, 0, 255), 3)
            # 绘制圆心
            cv2.circle(result_image, (int(x), int(y)), 5, (255, 0, 0), -1)
            # 添加标签
            label = f"#{i} r={radius:.1f}"
            cv2.putText(result_image, label, (int(x-radius), int(y-radius-10)), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        
        # 添加统计信息
        info_text = f"Detected: {len(circles)} circles"
        cv2.putText(result_image, info_text, (30, 50), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)
        
        cv2.imwrite(output_path, result_image)


def main():
    """
    主函数：集成YOLO物体检测和圆形检测算法 - 逐个处理每个物体
    """
    print("=" * 80)
    print("集成YOLO物体检测和圆形检测系统 - 逐个处理模式")
    print("=" * 80)
    
    # 配置参数
    yolo_model_path = 'yolo/best1.pt'  # YOLO模型路径
    image_path = '915/1.png'           # 测试图像路径
    conf_threshold = 0.5               # YOLO置信度阈值
    circle_iterations = 1000           # 每个区域的圆形检测迭代次数
    
    # 创建检测器实例
    detector = ImprovedCircleDetector(
        circle_detection_threshold=0.05,  # 圆形检测阈值
        error_range=15,                   # 误差范围σ
        noise_tolerance=2,                # 噪声容忍度δ 
        yolo_model_path=yolo_model_path   # YOLO模型路径
    )
    
    try:
        # 读取测试图像
        print(f"\n正在读取图像: {image_path}")
        image = cv2.imread(image_path)
        
        if image is None:
            print(f"无法读取图像: {image_path}")
            print("创建测试图像...")
            # 创建一个包含多个圆形的测试图像
            test_image = np.zeros((600, 800, 3), dtype=np.uint8)
            test_image.fill(255)  # 白色背景
            
            # 绘制几个圆形
            cv2.circle(test_image, (200, 200), 60, (0, 0, 0), 3)
            cv2.circle(test_image, (500, 300), 80, (0, 0, 0), 3)
            cv2.circle(test_image, (350, 450), 50, (0, 0, 0), 3)
            
            # 添加一些噪声
            noise = np.random.normal(0, 10, test_image.shape).astype(np.uint8)
            test_image = cv2.add(test_image, noise)
            image = test_image
            print("已创建包含多个圆形的测试图像")
        
        print(f"图像尺寸: {image.shape}")
        
        # 步骤1: YOLO物体检测
        print("\n" + "=" * 50)
        print("步骤1: YOLO物体检测")
        print("=" * 50)
        
        yolo_start_time = time.time()
        yolo_detections = detector.detect_objects_with_yolo(image, conf_threshold)
        yolo_time = time.time() - yolo_start_time
        
        # 给每个物体标记数字并可视化YOLO检测结果
        yolo_result_image = detector.visualize_yolo_detections_with_numbers(
            image, yolo_detections, "yolo_detection_boxes.png"
        )
        
        # 显示YOLO检测结果
        print("\n显示YOLO检测结果...")
        plt.figure(figsize=(12, 8))
        plt.imshow(cv2.cvtColor(yolo_result_image, cv2.COLOR_BGR2RGB))
        plt.title(f'YOLO物体检测结果 - 检测到 {len(yolo_detections)} 个物体 (用时: {yolo_time:.3f}秒)', fontsize=14, fontweight='bold')
        plt.axis('off')
        plt.tight_layout()
        plt.show()
        
        print(f"\nYOLO检测完成，用时: {yolo_time:.3f}秒")
        if len(yolo_detections) > 0:
            print("\nYOLO检测详情:")
            for i, (x1, y1, x2, y2, conf, class_id) in enumerate(yolo_detections):
                print(f"  物体 #{i+1}: 位置({x1}, {y1}, {x2}, {y2}), 置信度: {conf:.3f}, 类别: {class_id}")
        
        # 步骤2: 逐个处理每个物体进行圆形检测
        print("\n" + "=" * 50)
        print("步骤2: 逐个物体圆形检测")
        print("=" * 50)
        
        all_results = []
        total_circle_time = 0
        
        if len(yolo_detections) > 0:
            print(f"开始逐个处理 {len(yolo_detections)} 个物体...\n")
            
            for i, detection in enumerate(yolo_detections):
                object_num = i + 1
                x1, y1, x2, y2, conf, class_id = detection
                
                print(f"{'='*30} 处理物体 #{object_num} {'='*30}")
                print(f"物体信息: 位置({x1}, {y1}, {x2}, {y2}), 置信度: {conf:.3f}, 类别: {class_id}")
                
                # 记录开始时间
                object_start_time = time.time()
                
                # 对单个物体进行圆形检测
                result = detector.detect_circle_in_single_region(
                    image, detection, object_num, circle_iterations, expand_pixels=30
                )
                
                # 记录结束时间
                object_end_time = time.time()
                object_processing_time = object_end_time - object_start_time
                total_circle_time += object_processing_time
                
                # 输出单个物体的检测结果
                region_info, center, radius, success = result
                
                print(f"\n物体 #{object_num} 检测结果:")
                print(f"  处理时间: {object_processing_time:.3f}秒")
                
                if success and center is not None:
                    print(f"  ✓ 检测成功")
                    print(f"  圆心坐标: ({center[0]:.2f}, {center[1]:.2f})")
                    print(f"  半径: {radius:.2f}")
                    
                    # 提取颜色信息
                    hsl_values, hsb_values = detector.extract_color_info(image, center)
                else:
                    print(f"  ✗ 检测失败")
                    print(f"  原因: 未能在该区域检测到有效圆形")
                
                all_results.append(result)
                
                print(f"\n物体 #{object_num} 处理完成\n")
                
        else:
            print("未检测到物体，执行全图圆形检测...")
            full_image_start_time = time.time()
            center, radius, edges, edge_points = detector.detect_circles(image, circle_iterations)
            full_image_time = time.time() - full_image_start_time
            total_circle_time = full_image_time
            
            result = (None, center, radius, center is not None)
            all_results = [result]
            
            print(f"\n全图检测结果:")
            print(f"  处理时间: {full_image_time:.3f}秒")
            if center is not None:
                print(f"  ✓ 检测成功")
                print(f"  圆心坐标: ({center[0]:.2f}, {center[1]:.2f})")
                print(f"  半径: {radius:.2f}")
            else:
                print(f"  ✗ 检测失败")
        
        # 步骤3: 综合结果可视化
        print("\n" + "=" * 50)
        print("步骤3: 最终综合结果")
        print("=" * 50)
        
        final_result_image = detector.visualize_combined_results(
            image, yolo_detections, all_results, "final_detection_result.png"
        )
        
        # 显示最终综合检测结果
        print("\n显示最终综合检测结果...")
        total_time = yolo_time + total_circle_time
        plt.figure(figsize=(15, 10))
        plt.imshow(cv2.cvtColor(final_result_image, cv2.COLOR_BGR2RGB))
        plt.title(f'YOLO物体检测 + 圆形检测综合结果\n总用时: {total_time:.3f}秒 (YOLO: {yolo_time:.3f}秒, 圆形检测: {total_circle_time:.3f}秒)', 
                 fontsize=16, fontweight='bold')
        plt.axis('off')
        plt.tight_layout()
        plt.show()
        
        # 显示最终统计
        successful_detections = sum(1 for _, _, _, success in all_results if success)
        total_regions = len(all_results)
        
        print("\n" + "=" * 80)
        print("最终检测结果统计")
        print("=" * 80)
        print(f"YOLO检测物体数量: {len(yolo_detections)}")
        print(f"圆形检测成功数量: {successful_detections}/{total_regions}")
        print(f"整体成功率: {(successful_detections/total_regions)*100:.1f}%")
        print(f"总处理时间: {total_time:.3f}秒")
        print(f"  - YOLO检测时间: {yolo_time:.3f}秒")
        print(f"  - 圆形检测时间: {total_circle_time:.3f}秒")
        if len(yolo_detections) > 0:
            print(f"  - 平均每物体处理时间: {total_circle_time/len(yolo_detections):.3f}秒")
        
        print("\n处理完成！检查以下输出文件:")
        print("  - yolo_detection_boxes.png: YOLO检测结果")
        print("  - final_detection_result.png: 最终综合检测结果")
        
    except Exception as e:
        print(f"处理过程中出现错误: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()