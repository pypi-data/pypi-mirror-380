"""
CVHough SDK - 基于YOLO和Hough变换的灰色圆形检测SDK

这个SDK提供了一个完整的解决方案，用于在图像中检测灰色圆形物体。
它首先使用YOLO模型识别物体，然后在每个物体框内使用多种方法检测灰色圆形。

主要功能:
- YOLO物体检测
- Hough圆检测
- 轮廓检测
- Otsu阈值分割
- 灰色像素百分比分析
- 自适应显示和可视化

作者: CVHough Team
版本: 1.0.0
"""

import cv2
import numpy as np
import torch
from ultralytics import YOLO
import time
import os
import json

__version__ = "1.0.0"
__author__ = "CVHough Team"

# 全局性能优化
try:
    cv2.setUseOptimized(True)
    cv2.setNumThreads(0)
except Exception:
    pass

try:
    torch.set_grad_enabled(False)
    torch.set_num_threads(max(1, torch.get_num_threads()))
    torch.set_num_interop_threads(max(1, torch.get_num_interop_threads()))
except Exception:
    pass


class CVHoughDetector:
    """
    CVHough检测器类
    
    这个类封装了所有的检测功能，包括YOLO物体检测和灰色圆形检测。
    """
    
    def __init__(self, model_path=None):
        """
        初始化检测器
        
        参数:
            model_path (str, optional): YOLO模型文件路径。如果为None，将使用默认路径
        """
        if model_path is None:
            # 使用SDK包内的默认模型
            current_dir = os.path.dirname(__file__)
            model_path = os.path.join(current_dir, "models", "best.pt")
        
        self.model_path = model_path
        self.model = None
        self._load_model()
    
    def _load_model(self):
        """加载YOLO模型"""
        try:
            self.model = YOLO(self.model_path)
            print(f"成功加载YOLO模型: {self.model_path}")
        except Exception as e:
            print(f"加载YOLO模型失败: {e}")
            self.model = None
    
    def get_adaptive_font_scale(self, image_width, image_height, base_width=800, base_height=600):
        """
        根据图像尺寸自适应计算字体大小
        
        参数:
            image_width, image_height: 图像的实际宽度和高度
            base_width, base_height: 基准显示尺寸
        
        返回:
            float: 自适应字体大小比例
        """
        width_ratio = image_width / base_width
        height_ratio = image_height / base_height
        scale_ratio = min(width_ratio, height_ratio)
        font_scale = max(0.3, min(3.0, scale_ratio))
        return font_scale

    def get_adaptive_thickness(self, image_width, image_height, base_width=800, base_height=600):
        """
        根据图像尺寸自适应计算线条粗细
        
        参数:
            image_width, image_height: 图像的实际宽度和高度
            base_width, base_height: 基准显示尺寸
        
        返回:
            int: 自适应线条粗细
        """
        width_ratio = image_width / base_width
        height_ratio = image_height / base_height
        scale_ratio = min(width_ratio, height_ratio)
        base_thickness = 2
        thickness = max(1, int(base_thickness * scale_ratio))
        return thickness

    def resize_for_display(self, image, max_width=1000, max_height=800):
        """
        将图像按比例缩小以适配显示窗口，避免过大导致无法观看。
        不放大，只缩小。
        """
        if image is None:
            return image
        height, width = image.shape[:2]
        if width == 0 or height == 0:
            return image
        scale = min(max_width / float(width), max_height / float(height), 1.0)
        if scale < 1.0:
            new_size = (int(width * scale), int(height * scale))
            return cv2.resize(image, new_size, interpolation=cv2.INTER_AREA)
        return image

    def detect_gray_color_percentage(self, image, center_x, center_y, radius, gray_threshold=0.5):
        """
        检测圆形内部灰色像素的百分比（向量化实现以提升性能，逻辑与原方法一致）。
        返回 (is_gray_dominant, gray_percentage, total_pixels, gray_pixels)
        """
        h_img, w_img = image.shape[:2]
        if radius <= 0 or center_x < 0 or center_y < 0 or center_x >= w_img or center_y >= h_img:
            return False, 0.0, 0, 0

        # 仅在圆的最小外接矩形内构造掩码，减少计算量
        left = max(0, center_x - radius)
        top = max(0, center_y - radius)
        right = min(w_img, center_x + radius + 1)
        bottom = min(h_img, center_y + radius + 1)

        roi = image[top:bottom, left:right]
        mask = np.zeros(roi.shape[:2], dtype=np.uint8)
        cv2.circle(mask, (center_x - left, center_y - top), radius, 255, -1)

        # 颜色空间与通道
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        s = hsv[:, :, 1]
        v = hsv[:, :, 2]
        b, g, r = cv2.split(roi)
        max_rgb = np.maximum.reduce([r, g, b]).astype(np.float32)
        min_rgb = np.minimum.reduce([r, g, b]).astype(np.float32)
        rgb_ratio = np.divide(min_rgb, max_rgb + 1e-6)

        # 三种判定条件（与原逻辑一致）
        gray_low_sat = (s < 50)
        rgb_close = (rgb_ratio > 0.7)
        silver_like = (s < 30) & (v > 150)

        gray_binary = (gray_low_sat | rgb_close | silver_like)
        gray_binary = gray_binary & (mask.astype(bool))

        gray_pixels = int(np.count_nonzero(gray_binary))
        total_pixels = int(np.count_nonzero(mask))

        if total_pixels == 0:
            return False, 0.0, 0, 0

        gray_percentage = gray_pixels / float(total_pixels)
        is_gray_dominant = gray_percentage >= gray_threshold

        return is_gray_dominant, gray_percentage, total_pixels, gray_pixels

    def find_inner_gray_circle(self, image, center_x, center_y, outer_radius, retain_threshold=0.8):
        """
        在给定的大圆内部查找一个更小的灰色圆形（灰色比例≥retain_threshold）。
        返回 (inner_x, inner_y, inner_radius, circularity, gray_percentage) 或 None。
        """
        height, width = image.shape[:2]
        left = max(0, center_x - outer_radius)
        top = max(0, center_y - outer_radius)
        right = min(width - 1, center_x + outer_radius)
        bottom = min(height - 1, center_y + outer_radius)
        roi = image[top:bottom + 1, left:right + 1]
        if roi.size == 0:
            return None

        # 在ROI上构建外圆掩码
        mask = np.zeros(roi.shape[:2], dtype=np.uint8)
        cv2.circle(mask, (center_x - left, center_y - top), outer_radius, 255, -1)

        # 灰色二值掩码（低饱和、RGB接近、银色）
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        s = hsv[:, :, 1]
        v = hsv[:, :, 2]
        gray_low_sat = (s < 50)
        b, g, r = cv2.split(roi)
        max_rgb = np.maximum.reduce([r, g, b]).astype(np.float32)
        min_rgb = np.minimum.reduce([r, g, b]).astype(np.float32)
        ratio = np.divide(min_rgb, max_rgb + 1e-6)
        rgb_close = (ratio > 0.7)
        silver_like = (s < 30) & (v > 150)
        gray_binary = (gray_low_sat | rgb_close | silver_like).astype(np.uint8) * 255
        gray_binary = cv2.bitwise_and(gray_binary, gray_binary, mask=mask)

        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
        gray_binary = cv2.morphologyEx(gray_binary, cv2.MORPH_CLOSE, kernel)
        gray_binary = cv2.morphologyEx(gray_binary, cv2.MORPH_OPEN, kernel)

        contours, _ = cv2.findContours(gray_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        best = None
        for contour in contours:
            area = cv2.contourArea(contour)
            if area < 500:
                continue
            perimeter = cv2.arcLength(contour, True)
            if perimeter == 0:
                continue
            circularity = 4 * np.pi * area / (perimeter * perimeter)
            if circularity < 0.6:
                continue
            (cx, cy), radius = cv2.minEnclosingCircle(contour)
            radius = int(radius)
            if radius < 10 or radius >= outer_radius:
                continue
            inner_x = int(left + cx)
            inner_y = int(top + cy)
            # 计算内圆灰度比例
            _, inner_gray_pct, _, _ = self.detect_gray_color_percentage(image, inner_x, inner_y, radius, retain_threshold)
            if inner_gray_pct >= retain_threshold:
                score = (inner_gray_pct, area)
                if best is None or score > best[0]:
                    best = (score, inner_x, inner_y, radius, circularity, inner_gray_pct)

        if best is None:
            return None
        _, inner_x, inner_y, radius, circularity, inner_gray_pct = best
        return (inner_x, inner_y, radius, circularity, inner_gray_pct)

    def is_duplicate_circle(self, detected_circles, center_x, center_y, distance_threshold=150):
        """
        判断与已保存的圆是否重复（基于圆心距离）。
        """
        for existing_circle in detected_circles:
            existing_x, existing_y = existing_circle[0], existing_circle[1]
            distance = np.sqrt((center_x - existing_x)**2 + (center_y - existing_y)**2)
            if distance < distance_threshold:
                return True
        return False

    def add_circle_per_rule(self, img, detected_circles, center_x, center_y, radius, circularity,
                            retain_threshold=0.8, lower_threshold=0.5, context_prefix=""):
        """
        按三段阈值规则处理候选圆：
        - 灰度≥retain_threshold: 保留外圆
        - lower_threshold≤灰度<retain_threshold: 在外圆内搜索灰色小圆，若找到且≥retain_threshold则保留内圆
        - 灰度<lower_threshold: 舍弃
        会更新 detected_circles 并打印说明。
        """
        _, gray_pct, _, _ = self.detect_gray_color_percentage(img, center_x, center_y, radius, lower_threshold)

        if gray_pct >= retain_threshold:
            if not self.is_duplicate_circle(detected_circles, center_x, center_y):
                detected_circles.append((center_x, center_y, radius, circularity, gray_pct))
            return

        if gray_pct >= lower_threshold:
            inner = self.find_inner_gray_circle(img, center_x, center_y, radius, retain_threshold)
            if inner is not None:
                ix, iy, ir, icirc, igray = inner
                if not self.is_duplicate_circle(detected_circles, ix, iy):
                    detected_circles.append((ix, iy, ir, icirc, igray))
            return

    def detect_objects_with_yolo(self, image):
        """
        使用YOLO模型检测图像中的物体
        
        参数:
            image: 输入图像
            
        返回:
            list: 检测到的物体框 [(x1, y1, x2, y2, confidence, class_id), ...]
        """
        if self.model is None:
            print("模型未加载，无法进行物体检测")
            return []
        
        try:
            # 使用YOLO模型进行检测
            results = self.model(image)
            
            detected_objects = []
            for result in results:
                boxes = result.boxes
                if boxes is not None:
                    for box in boxes:
                        # 获取边界框坐标
                        x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                        
                        # 获取置信度和类别
                        confidence = float(box.conf[0])
                        class_id = int(box.cls[0])
                        
                        detected_objects.append((x1, y1, x2, y2, confidence, class_id))
            
            return detected_objects
        
        except Exception as e:
            print(f"YOLO检测失败: {e}")
            return []

    def detect_circles_in_object_boxes(self, image_path):
        """
        先用YOLO模型识别物体，然后在每个物体框内检测灰色圆
        
        参数:
            image_path: 图像文件路径
            
        返回:
            dict: 每个物体框内检测到的圆形 {object_id: [(center_x, center_y, radius, circularity, gray_percentage), ...]}
        """
        # 使用与main.py完全相同的默认参数
        visualize = False  # 改为不显示，直接保存
        gray_threshold = 0.5
        total_start_time = time.time()
        
        # 读取图像
        img = cv2.imread(image_path)
        if img is None:
            print(f"无法读取图像: {image_path}")
            return {}
        
        # 复制原图用于绘制结果
        result = img.copy()
        
        # 获取图像尺寸
        height, width = img.shape[:2]
        print(f"图像尺寸: {width}x{height}")
        
        # 使用YOLO检测物体
        print("正在使用YOLO模型检测物体...")
        detected_objects = self.detect_objects_with_yolo(img)
        
        if not detected_objects:
            print("未检测到任何物体，将检测整个图像")
            detected_objects = [(0, 0, width, height, 1.0, -1)]  # 使用整个图像作为检测区域
        
        # 存储每个物体框内检测到的圆形
        object_circles = {}

        # 在每个物体框内检测圆形
        for obj_id, (x1, y1, x2, y2, confidence, class_id) in enumerate(detected_objects):
            # 步骤1：提取物体区域(ROI)
            object_roi = img[y1:y2, x1:x2]
            if object_roi.size == 0:
                continue
            
            # 存储当前物体框内检测到的圆形
            object_circles[obj_id] = []
            
            # 步骤2：转灰度
            gray_roi = cv2.cvtColor(object_roi, cv2.COLOR_BGR2GRAY)
            
            # 步骤3：对比度增强（复用CLAHE实例，减少频繁创建开销）
            if 'GLOBAL_CLAHE' not in globals():
                globals()['GLOBAL_CLAHE'] = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
            enhanced_roi = globals()['GLOBAL_CLAHE'].apply(gray_roi)
            
            # 使用增强后的图像进行后续处理
            gray_roi = enhanced_roi
            
            # 方法1：使用Hough圆检测
            # 步骤4a：Hough算法特定预处理 - 高斯模糊
            blurred = cv2.GaussianBlur(gray_roi, (9, 9), 2)
            
            # Hough圆检测参数 - 针对不同大小的圆形
            circles = cv2.HoughCircles(
                blurred,
                cv2.HOUGH_GRADIENT,
                dp=1,
                minDist=50,     # 减小最小距离，适应物体框内的圆形
                param1=50,
                param2=25,      # 降低阈值，更容易检测到圆形
                minRadius=20,   # 减小最小半径
                maxRadius=100   # 减小最大半径
            )
            
            if circles is not None:
                circles = np.round(circles[0, :]).astype("int")
                for (cx, cy, r) in circles:
                    # 转换回原图坐标
                    center_x = x1 + cx
                    center_y = y1 + cy
                    
                    # 检查圆形是否在物体框内
                    if (x1 <= center_x <= x2 and y1 <= center_y <= y2):
                        # 按三段规则处理
                        self.add_circle_per_rule(
                            img,
                            object_circles[obj_id],
                            center_x,
                            center_y,
                            r,
                            1.0,
                            retain_threshold=0.8,
                            lower_threshold=0.5,
                            context_prefix=f"物体框 {obj_id+1} Hough: "
                        )
            
            # 方法2：轮廓检测
            # 步骤4b：轮廓算法特定预处理 - 自适应阈值分割
            binary = cv2.adaptiveThreshold(gray_roi, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                          cv2.THRESH_BINARY_INV, 11, 2)
            
            # 形态学操作清理噪声
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
            binary_closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
            binary = cv2.morphologyEx(binary_closed, cv2.MORPH_OPEN, kernel)
            
            # 查找轮廓
            contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            # 筛选圆形轮廓
            for contour in contours:
                area = cv2.contourArea(contour)
                # 调整面积范围，适应物体框内的圆形
                min_area = 1000   # 约π * 18²
                max_area = 30000  # 约π * 98²
                if area < min_area or area > max_area:
                    continue
                    
                perimeter = cv2.arcLength(contour, True)
                if perimeter == 0:
                    continue
                    
                # 计算圆度
                circularity = 4 * np.pi * area / (perimeter * perimeter)
                
                # 计算最小外接圆
                (cx, cy), radius = cv2.minEnclosingCircle(contour)
                center_x = int(x1 + cx)  # 转换回原图坐标
                center_y = int(y1 + cy)
                radius = int(radius)
                
                # 检查圆形是否在物体框内
                if (x1 <= center_x <= x2 and y1 <= center_y <= y2):
                    if circularity > 0.6 and 15 <= radius <= 100:  # 调整半径范围
                        # 检查是否与已检测的圆形重叠
                        is_duplicate = False
                        for existing_circle in object_circles[obj_id]:
                            existing_x, existing_y = existing_circle[0], existing_circle[1]
                            distance = np.sqrt((center_x - existing_x)**2 + (center_y - existing_y)**2)
                            if distance < 50:  # 减小距离阈值
                                is_duplicate = True
                                break
                        
                        if not is_duplicate:
                            # 按三段规则处理
                            self.add_circle_per_rule(
                                img,
                                object_circles[obj_id],
                                center_x,
                                center_y,
                                radius,
                                circularity,
                                retain_threshold=0.8,
                                lower_threshold=0.5,
                                context_prefix=f"物体框 {obj_id+1} 轮廓: "
                            )
            
            # 方法3：Otsu阈值分割
            if len(object_circles[obj_id]) < 3:
                # 步骤4c：Otsu算法特定预处理 - Otsu阈值分割
                _, otsu_binary = cv2.threshold(gray_roi, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
                
                # 形态学操作
                kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
                otsu_closed = cv2.morphologyEx(otsu_binary, cv2.MORPH_CLOSE, kernel)
                binary = cv2.morphologyEx(otsu_closed, cv2.MORPH_OPEN, kernel)
                
                contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                
                for contour in contours:
                    area = cv2.contourArea(contour)
                    min_area = 1000
                    max_area = 30000
                    if area < min_area or area > max_area:
                        continue
                        
                    perimeter = cv2.arcLength(contour, True)
                    if perimeter == 0:
                        continue
                        
                    circularity = 4 * np.pi * area / (perimeter * perimeter)
                    (cx, cy), radius = cv2.minEnclosingCircle(contour)
                    center_x = int(x1 + cx)
                    center_y = int(y1 + cy)
                    radius = int(radius)
                    
                    if (x1 <= center_x <= x2 and y1 <= center_y <= y2):
                        if circularity > 0.5 and 15 <= radius <= 100:
                            # 检查是否与已检测的圆形重叠
                            is_duplicate = False
                            for existing_circle in object_circles[obj_id]:
                                existing_x, existing_y = existing_circle[0], existing_circle[1]
                                distance = np.sqrt((center_x - existing_x)**2 + (center_y - existing_y)**2)
                                if distance < 50:
                                    is_duplicate = True
                                    break
                            
                            if not is_duplicate:
                                # 按三段规则处理
                                self.add_circle_per_rule(
                                    img,
                                    object_circles[obj_id],
                                    center_x,
                                    center_y,
                                    radius,
                                    circularity,
                                    retain_threshold=0.8,
                                    lower_threshold=0.5,
                                    context_prefix=f"物体框 {obj_id+1} Otsu: "
                                )
        
        # 获取图像尺寸用于自适应字体和线条
        img_height, img_width = result.shape[:2]
        font_scale = self.get_adaptive_font_scale(img_width, img_height)
        line_thickness = self.get_adaptive_thickness(img_width, img_height)
        
        # 绘制物体框和检测到的圆形
        if visualize:
            # 只保留：采用灰色比例保留的灰色圆的图
            retained_gray_circles_image = img.copy()
            for obj_id, (x1, y1, x2, y2, confidence, class_id) in enumerate(detected_objects):
                # 只绘制满足灰色比例阈值的圆形，不显示YOLO方框
                if obj_id in object_circles:
                    for i, (center_x, center_y, radius, circularity, gray_percentage) in enumerate(object_circles[obj_id]):
                        # 只保留灰色比例 >= 80% 的圆形
                        if gray_percentage >= 0.8:
                            # 满足阈值的圆形用绿色绘制
                            circle_color = (0, 255, 0)  # 绿色
                            cv2.circle(retained_gray_circles_image, (center_x, center_y), radius, circle_color, line_thickness)
                            
                            # 绘制圆心（蓝色）
                            center_radius = max(3, int(8 * font_scale))
                            cv2.circle(retained_gray_circles_image, (center_x, center_y), center_radius, (255, 0, 0), -1)
                            
                            # 添加编号标签
                            label = f"{obj_id+1}-{i+1}"
                            cv2.putText(retained_gray_circles_image, label, (center_x + 5, center_y - 5),
                                        cv2.FONT_HERSHEY_SIMPLEX, font_scale * 0.8, (255, 255, 255), line_thickness, cv2.LINE_AA)
                            
                            # 在圆形下方添加坐标信息
                            coord_text = f"({center_x},{center_y})"
                            cv2.putText(retained_gray_circles_image, coord_text, (center_x - 20, center_y + radius + 15),
                                        cv2.FONT_HERSHEY_SIMPLEX, font_scale * 0.6, (255, 255, 0), line_thickness, cv2.LINE_AA)
                            
                            # 添加半径信息
                            radius_text = f"r={radius}"
                            cv2.putText(retained_gray_circles_image, radius_text, (center_x - 15, center_y + radius + 30),
                                        cv2.FONT_HERSHEY_SIMPLEX, font_scale * 0.6, (0, 255, 255), line_thickness, cv2.LINE_AA)
                            
                            # 添加灰色百分比信息
                            gray_text = f"Gray:{gray_percentage:.1%}"
                            cv2.putText(retained_gray_circles_image, gray_text, (center_x - 20, center_y + radius + 45),
                                        cv2.FONT_HERSHEY_SIMPLEX, font_scale * 0.6, (128, 128, 128), line_thickness, cv2.LINE_AA)
            
            # 保存检测结果图像而不是显示
            output_path = os.path.splitext(image_path)[0] + "_detected_circles.jpg"
            display_img = self.resize_for_display(retained_gray_circles_image, max_width=800, max_height=600)
            cv2.imwrite(output_path, display_img)
            print(f"检测结果已保存到: {output_path}")
        
        return object_circles


# 导出主要类和函数
from .detector import detect_gray_circles

__all__ = ['CVHoughDetector', 'detect_gray_circles', '__version__', '__author__']