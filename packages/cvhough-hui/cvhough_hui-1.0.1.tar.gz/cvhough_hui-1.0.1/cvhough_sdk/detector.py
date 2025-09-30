"""
CVHough SDK - 简化接口

提供最简单的接口，只需要提供图片路径，所有参数都使用main.py中的默认值。
"""

import os
from . import CVHoughDetector


def detect_gray_circles(image_path):
    """
    检测图像中的灰色圆形 - 简化接口
    
    参数:
        image_path (str): 图像文件路径
        
    返回:
        dict: 检测结果 {object_id: [(center_x, center_y, radius, circularity, gray_percentage), ...]}
        
    示例:
        >>> from cvhough_sdk import detect_gray_circles
        >>> results = detect_gray_circles("image.jpg")
        >>> print(f"检测到 {len(results)} 个物体")
    """
    # 获取SDK内置模型路径
    current_dir = os.path.dirname(__file__)
    model_path = os.path.join(current_dir, "models", "best.pt")
    
    # 创建检测器实例
    detector = CVHoughDetector(model_path=model_path)
    
    # 使用main.py中的默认参数调用检测函数
    return detector.detect_circles_in_object_boxes(image_path)


__all__ = ['detect_gray_circles']