"""
cvHough SDK - YOLO物体检测与霍夫圆检测集成工具包

这个SDK封装了基于YOLO的物体检测和霍夫圆检测算法，
专门用于在检测到的物体区域内进行精确的圆形检测。

主要功能:
- YOLO物体检测
- 区域内霍夫圆检测
- 多种二值化方法支持
- 结果可视化

作者: cvHough Team
版本: 1.0.0
"""

import cv2
import numpy as np
from ultralytics import YOLO
import matplotlib.pyplot as plt
import os
import time
from pathlib import Path

# 解决OpenMP库冲突问题
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

# 配置matplotlib中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

class YOLOCircleDetector:
    def __init__(self, yolo_model_path=None, conf_threshold=0.2, binary_method='manual'):
        """
        初始化YOLO圆形检测器
        
        参数:
        yolo_model_path: YOLO模型文件路径，如果为None则使用内置模型
        conf_threshold: YOLO置信度阈值 (默认=0.2，与main函数保持一致)
        binary_method: 二值化方法 (默认='manual'，与main函数保持一致)
        """
        self.yolo_model = None
        
        # 保存默认配置参数（来自main函数）
        self.conf_threshold = conf_threshold
        self.binary_method = binary_method
        self.save_binary_images = False  # 默认不保存二值化图像
        
        # 霍夫圆检测默认参数（来自main函数）
        self.hough_params = {
            'dp': 1,
            'min_dist': 15,
            'param1': 15,
            'param2': 8,
            'min_radius': 3
        }
        
        # 如果没有指定模型路径，使用内置模型
        if yolo_model_path is None:
            # 获取当前文件所在目录
            current_dir = Path(__file__).parent
            yolo_model_path = current_dir / "models" / "best1.pt"
        
        # 加载YOLO模型
        if Path(yolo_model_path).exists():
            print(f"正在加载YOLO模型: {yolo_model_path}")
            try:
                self.yolo_model = YOLO(yolo_model_path)
                print("YOLO模型加载成功")
            except Exception as e:
                print(f"YOLO模型加载失败: {e}")
                self.yolo_model = None
        else:
            print(f"YOLO模型文件不存在: {yolo_model_path}")
    
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
            print("YOLO模型未加载，跳过物体检测")
            return []
        
        print(f"\n=== YOLO物体检测 ===")
        print(f"输入图像尺寸: {image.shape}")
        print(f"置信度阈值: {conf_threshold}")
        
        try:
            # 进行推理
            yolo_start = time.time()
            results = self.yolo_model(image, conf=conf_threshold, verbose=False)
            inference_time = time.time() - yolo_start
            print(f"  YOLO推理耗时: {inference_time:.3f}秒")
            
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
            
            print(f"检测完成，用时: {inference_time:.3f}秒")
            print(f"检测到 {len(detections)} 个物体")
            
            # 显示检测结果详情
            for i, (x1, y1, x2, y2, conf, class_id) in enumerate(detections):
                w, h = x2 - x1, y2 - y1
                print(f"  物体 {i+1}: 位置({x1}, {y1}, {x2}, {y2}), 尺寸({w}x{h}), 置信度: {conf:.3f}, 类别: {class_id}")
            
            return detections
            
        except Exception as e:
            print(f"YOLO检测过程中出现错误: {e}")
            return []
    
    def detect_circles_in_region(self, image, x1, y1, x2, y2, 
                                dp=1, min_dist=15, param1=15, param2=8, 
                                min_radius=3, max_radius=50, save_binary=False, 
                                binary_method='adaptive'):
        """
        在指定区域内使用霍夫圆检测圆形（针对二值化图像优化）
        
        参数:
        image: 输入图像
        x1, y1, x2, y2: 检测区域边界框
        dp: 累加器分辨率与图像分辨率的反比 (默认=1)
        min_dist: 检测到的圆心之间的最小距离 (默认=15，适合小圆检测)
        param1: Canny边缘检测的高阈值 (默认=15，二值化图像边缘清晰，降低以提高敏感度)
        param2: 圆心检测阈值 (默认=8，大幅降低以检测更多圆形)
        min_radius: 最小圆半径 (默认=3，检测更小的圆)
        max_radius: 最大圆半径 (默认=50，适合中等大小圆形)
        save_binary: 是否保存二值化图像用于调试
        binary_method: 二值化方法 ('adaptive', 'otsu', 'manual')
        
        处理流程:
        1. 提取ROI区域
        2. 转换为灰度图像
        3. 高斯模糊降噪
        4. 二值化处理（生成黑白图像）
        5. 形态学操作优化
        6. 霍夫圆检测（针对白色圆形区域优化）
        
        返回:
        circles: 检测到的圆形列表，每个元素包含 (center_x, center_y, radius)
        """
        print(f"\n--- 在区域 ({x1}, {y1}, {x2}, {y2}) 内检测圆形 ---")
        
        # 确保边界框在图像范围内
        h, w = image.shape[:2]
        x1 = max(0, x1)
        y1 = max(0, y1)
        x2 = min(w, x2)
        y2 = min(h, y2)
        
        # 提取感兴趣区域
        roi = image[y1:y2, x1:x2]
        
        if roi.size == 0:
            print("区域为空，跳过圆形检测")
            return []
        
        print(f"ROI尺寸: {roi.shape}")
        
        # 转换为灰度图像
        if len(roi.shape) == 3:
            gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        else:
            gray_roi = roi.copy()
        
        # 应用高斯模糊减少噪声（针对二值化优化，减少模糊程度）
        blurred = cv2.GaussianBlur(gray_roi, (5, 5), 1)
        
        # 二值化处理
        binary = self.apply_binarization(blurred, method=binary_method)
        
        # 可选：保存二值化图像用于调试
        if save_binary:
            timestamp = int(time.time() * 1000)  # 毫秒级时间戳
            binary_filename = f"binary_region_{timestamp}_{x1}_{y1}_{x2}_{y2}.jpg"
            cv2.imwrite(binary_filename, binary)
            print(f"二值化图像已保存到: {binary_filename}")
        
        # 使用霍夫圆检测（在二值化图像上进行）
        circles = cv2.HoughCircles(
            binary,
            cv2.HOUGH_GRADIENT,
            dp=dp,
            minDist=min_dist,
            param1=param1,
            param2=param2,
            minRadius=min_radius,
            maxRadius=max_radius
        )
        
        detected_circles = []
        
        if circles is not None:
            circles = np.round(circles[0, :]).astype("int")
            
            for (cx, cy, r) in circles:
                # 将相对坐标转换为绝对坐标
                abs_cx = cx + x1
                abs_cy = cy + y1
                detected_circles.append((abs_cx, abs_cy, r))
            
            print(f"检测到 {len(detected_circles)} 个圆形")
            for i, (cx, cy, r) in enumerate(detected_circles):
                print(f"  圆形 {i+1}: 中心({cx}, {cy}), 半径: {r}")
        else:
            print("未检测到圆形")
        
        return detected_circles
    
    def apply_binarization(self, gray_image, method='adaptive'):
        """
        对灰度图像应用不同的二值化方法
        
        参数:
        gray_image: 输入的灰度图像
        method: 二值化方法 ('adaptive', 'otsu', 'manual')
        
        返回:
        binary: 二值化后的图像
        """
        if method == 'adaptive':
            # 自适应阈值二值化
            binary = cv2.adaptiveThreshold(
                gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                cv2.THRESH_BINARY, 11, 2
            )
            print("使用自适应阈值二值化")
        elif method == 'otsu':
            # OTSU自动阈值二值化
            _, binary = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            print("使用OTSU阈值二值化")
        elif method == 'manual':
            # 手动阈值二值化
            _, binary = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)
            print("使用手动阈值二值化 (阈值=200)")
        else:
            # 默认使用自适应阈值
            binary = cv2.adaptiveThreshold(
                gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                cv2.THRESH_BINARY, 11, 2
            )
            print("使用默认自适应阈值二值化")
        
        # 形态学操作优化
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
        binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
        
        return binary
    
    def visualize_results(self, image, yolo_detections, circle_results, save_path=None):
        """
        可视化YOLO检测和圆形检测结果
        
        参数:
        image: 原始图像
        yolo_detections: YOLO检测结果
        circle_results: 圆形检测结果，格式为 [(region_info, circles), ...]
        save_path: 保存路径
        
        返回:
        result_image: 标注后的图像
        """
        result_image = image.copy()
        
        # 绘制YOLO检测框
        for i, (x1, y1, x2, y2, conf, class_id) in enumerate(yolo_detections):
            # 绘制边界框
            cv2.rectangle(result_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            # 添加标签
            label = f"Object {i+1}: {conf:.2f}"
            label_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)[0]
            cv2.rectangle(result_image, (x1, y1 - label_size[1] - 10), 
                         (x1 + label_size[0], y1), (0, 255, 0), -1)
            cv2.putText(result_image, label, (x1, y1 - 5), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
        
        # 绘制检测到的圆形
        circle_count = 0
        for region_info, circles in circle_results:
            x1, y1, x2, y2 = region_info[:4]
            
            for cx, cy, r in circles:
                circle_count += 1
                # 绘制圆形
                cv2.circle(result_image, (cx, cy), r, (0, 0, 255), 2)
                # 绘制圆心
                cv2.circle(result_image, (cx, cy), 3, (255, 0, 0), -1)
                
                # 添加圆形标签和坐标
                circle_label = f"Circle {circle_count}"
                coord_label = f"({cx}, {cy})"
                
                # 绘制圆形编号（在圆的上方）
                cv2.putText(result_image, circle_label, (cx - 30, cy - r - 25), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                
                # 绘制坐标（在圆的上方，圆形编号下面）
                cv2.putText(result_image, coord_label, (cx - 35, cy - r - 10), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 255), 2)
        
        # 保存结果图像
        if save_path:
            cv2.imwrite(save_path, result_image)
            print(f"结果图像已保存到: {save_path}")
        
        return result_image
    
    def process_image(self, image_path, conf_threshold=None, save_result=True, 
                     binary_method=None, save_binary_images=None):
        """
        处理单张图像：YOLO检测 + 二值化 + 圆形检测
        
        参数:
        image_path: 图像路径
        conf_threshold: YOLO置信度阈值，如果为None则使用初始化时的默认值
        save_result: 是否保存结果
        binary_method: 二值化方法，如果为None则使用初始化时的默认值
        save_binary_images: 是否保存二值化图像，如果为None则使用初始化时的默认值
        
        返回:
        result_image: 处理后的图像
        yolo_detections: YOLO检测结果
        circle_results: 圆形检测结果
        """
        # 使用默认参数（如果没有指定的话）
        if conf_threshold is None:
            conf_threshold = self.conf_threshold
        if binary_method is None:
            binary_method = self.binary_method
        if save_binary_images is None:
            save_binary_images = self.save_binary_images
        print(f"\n{'='*80}")
        print(f"处理图像: {image_path}")
        print(f"{'='*80}")
        
        # 读取图像
        image = cv2.imread(image_path)
        if image is None:
            print(f"无法读取图像: {image_path}")
            return None, [], []
        
        print(f"图像尺寸: {image.shape}")
        
        # 步骤1: YOLO物体检测
        yolo_detections = self.detect_objects_with_yolo(image, conf_threshold)
        
        # 步骤2: 在每个检测区域内进行圆形检测
        circle_results = []
        
        if len(yolo_detections) > 0:
            print(f"\n{'='*50}")
            print("步骤2: 在检测区域内进行圆形检测")
            print(f"{'='*50}")
            
            hough_start = time.time()
            for i, (x1, y1, x2, y2, conf, class_id) in enumerate(yolo_detections):
                print(f"\n处理物体 {i+1}/{len(yolo_detections)}")
                
                # 在当前区域检测圆形（使用默认的霍夫圆参数）
                circles = self.detect_circles_in_region(
                    image, x1, y1, x2, y2,
                    dp=self.hough_params['dp'], 
                    min_dist=self.hough_params['min_dist'], 
                    param1=self.hough_params['param1'], 
                    param2=self.hough_params['param2'],
                    min_radius=self.hough_params['min_radius'], 
                    max_radius=min(x2-x1, y2-y1)//2,
                    save_binary=save_binary_images,
                    binary_method=binary_method
                )
                
                circle_results.append(((x1, y1, x2, y2, conf, class_id), circles))
            hough_time = time.time() - hough_start
            print(f"  霍夫圆检测总耗时: {hough_time:.3f}秒")
        else:
            print("\n未检测到物体，跳过圆形检测")
        
        # 步骤3: 可视化结果
        print(f"\n{'='*50}")
        print("步骤3: 生成可视化结果")
        print(f"{'='*50}")
        
        save_path = None
        if save_result:
            base_name = Path(image_path).stem
            save_path = f"{base_name}_detection_result.jpg"
        
        result_image = self.visualize_results(image, yolo_detections, circle_results, save_path)
        
        # 统计结果
        total_circles = sum(len(circles) for _, circles in circle_results)
        print(f"\n检测结果统计:")
        print(f"- YOLO检测物体数量: {len(yolo_detections)}")
        print(f"- 检测到的圆形总数: {total_circles}")
        
        return result_image, yolo_detections, circle_results
    
    def detect_image(self, image_path):
        """
        简化的接口函数：只需要输入图片路径即可进行检测
        使用所有默认参数，相当于原来的main函数功能
        
        参数:
        image_path: 图像路径
        
        返回:
        result_image: 处理后的图像
        yolo_detections: YOLO检测结果
        circle_results: 圆形检测结果
        """
        return self.process_image(image_path, save_result=True)

def display_binary_images():
    """
    显示所有保存的二值化图像
    """
    import glob
    
    # 查找所有二值化图像文件
    binary_files = glob.glob('binary_region_*.jpg')
    
    if not binary_files:
        print("未找到二值化图像文件")
        return
    
    print(f"\n找到 {len(binary_files)} 个二值化图像文件")
    
    # 计算显示布局
    n_images = len(binary_files)
    cols = min(4, n_images)  # 最多4列
    rows = (n_images + cols - 1) // cols  # 计算需要的行数
    
    plt.figure(figsize=(4*cols, 3*rows))
    
    for i, binary_file in enumerate(sorted(binary_files)):
        # 读取二值化图像
        binary_img = cv2.imread(binary_file, cv2.IMREAD_GRAYSCALE)
        
        if binary_img is not None:
            plt.subplot(rows, cols, i+1)
            plt.imshow(binary_img, cmap='gray')
            
            # 从文件名提取区域信息
            filename = os.path.basename(binary_file)
            region_info = filename.replace('binary_region_', '').replace('.jpg', '')
            coords = region_info.split('_')
            # 新格式: timestamp_x1_y1_x2_y2，旧格式: x1_y1_x2_y2
            if len(coords) == 5:  # 带时间戳的新格式
                timestamp, x1, y1, x2, y2 = coords
                plt.title(f'区域 ({x1},{y1})-({x2},{y2})', fontsize=10)
            elif len(coords) == 4:  # 旧格式
                x1, y1, x2, y2 = coords
                plt.title(f'区域 ({x1},{y1})-({x2},{y2})', fontsize=10)
            else:
                plt.title(f'区域 {i+1}', fontsize=10)
            
            plt.axis('off')
    
    plt.suptitle(f'二值化处理结果 (共{n_images}个区域)', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.show()

# 导出主要类和函数
__all__ = ['YOLOCircleDetector', 'display_binary_images']
__version__ = '1.0.0'