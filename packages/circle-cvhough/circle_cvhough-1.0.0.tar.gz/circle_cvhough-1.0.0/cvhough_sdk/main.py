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
    def __init__(self, yolo_model_path):
        """
        初始化YOLO圆形检测器
        
        参数:
        yolo_model_path: YOLO模型文件路径
        """
        self.yolo_model = None
        
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
        # 确保边界框在图像范围内
        h, w = image.shape[:2]
        x1 = max(0, x1)
        y1 = max(0, y1)
        x2 = min(w, x2)
        y2 = min(h, y2)
        
        # 提取感兴趣区域
        roi = image[y1:y2, x1:x2]
        
        if roi.size == 0:
            return []
        
        # 转换为灰度图像
        if len(roi.shape) == 3:
            gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        else:
            gray_roi = roi.copy()
        
        # 应用高斯模糊减少噪声（针对二值化优化，减少模糊程度）
        blurred = cv2.GaussianBlur(gray_roi, (5, 5), 1)
        
        # 二值化处理
        binary = self.apply_binarization(blurred, method=binary_method)
        
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
    
    def process_image(self, image_path, conf_threshold=0.5, save_result=True, 
                     binary_method='adaptive', save_binary_images=True):
        """
        处理单张图像：YOLO检测 + 二值化 + 圆形检测
        
        参数:
        image_path: 图像路径
        conf_threshold: YOLO置信度阈值
        save_result: 是否保存结果
        binary_method: 二值化方法 ('adaptive', 'otsu', 'manual')
        save_binary_images: 是否保存二值化图像用于调试
        
        返回:
        result_image: 处理后的图像
        yolo_detections: YOLO检测结果
        circle_results: 圆形检测结果
        """
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
            hough_start = time.time()
            for i, (x1, y1, x2, y2, conf, class_id) in enumerate(yolo_detections):
                # 在当前区域检测圆形（使用针对二值化图像优化的参数）
                circles = self.detect_circles_in_region(
                    image, x1, y1, x2, y2,
                    dp=1, min_dist=15, param1=15, param2=8,
                    min_radius=3, max_radius=min(x2-x1, y2-y1)//2,
                    save_binary=save_binary_images,
                    binary_method=binary_method
                )
                
                circle_results.append(((x1, y1, x2, y2, conf, class_id), circles))
            hough_time = time.time() - hough_start
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
        
        # 输出每个物体的圆心和半径信息
        if circle_results:
            print(f"\n每个物体的圆形检测详情:")
            for i, ((x1, y1, x2, y2, conf, class_id), circles) in enumerate(circle_results):
                print(f"物体 {i+1}: 区域({x1}, {y1}, {x2}, {y2})")
                if circles:
                    for j, (cx, cy, r) in enumerate(circles):
                        print(f"  圆形 {j+1}: 中心({cx}, {cy}), 半径: {r}")
                else:
                    print(f"  未检测到圆形")
        
        return result_image, yolo_detections, circle_results

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

def main():
    """
    主函数
    """
    # 记录开始时间
    start_time = time.time()
    
    # 配置参数
    yolo_model_path = 'cvhough_sdk/models/best1.pt'  # YOLO模型路径（使用SDK内置模型）
    image_path = '922/2.png'          # 输入图像路径（相对于cvhough_sdk目录）
    conf_threshold = 0.2                 # YOLO置信度阈值
    
    # 二值化和调试选项
    binary_method = 'manual'           # 二值化方法: 'adaptive', 'otsu', 'manual'
    save_binary_images = False         # 不保存二值化图像
    
    print(f"使用二值化方法: {binary_method}")
    
    # 创建检测器
    print("正在初始化YOLO模型...")
    init_start = time.time()
    detector = YOLOCircleDetector(yolo_model_path)
    init_time = time.time() - init_start
    print(f"模型初始化完成，耗时: {init_time:.2f}秒")
    
    # 检查图像文件是否存在
    if not Path(image_path).exists():
        print(f"图像文件不存在: {image_path}")
        return
    
    # 处理图像
    print("开始处理图像...")
    process_start = time.time()
    result_image, yolo_detections, circle_results = detector.process_image(
        image_path, conf_threshold, save_result=True,
        binary_method=binary_method, save_binary_images=save_binary_images
    )
    process_time = time.time() - process_start
    print(f"图像处理完成，耗时: {process_time:.2f}秒")
    
    # 计算总时间
    total_time = time.time() - start_time
    
    if result_image is not None:
        # 显示结果
        print(f"\n{'='*50}")
        print("显示检测结果")
        print(f"{'='*50}")
        
        plt.figure(figsize=(15, 10))
        plt.imshow(cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB))
        
        total_circles = sum(len(circles) for _, circles in circle_results)
        plt.title(f'YOLO物体检测 + 霍夫圆检测结果\n'
                 f'检测到 {len(yolo_detections)} 个物体，{total_circles} 个圆形', 
                 fontsize=16, fontweight='bold')
        plt.axis('off')
        plt.tight_layout()
        plt.show()
        
        print("\n检测完成！")
        
        print(f"\n=== 时间统计 ===")
        print(f"模型初始化时间: {init_time:.2f}秒")
        print(f"图像处理时间: {process_time:.2f}秒")
        print(f"总耗时: {total_time:.2f}秒")
    else:
        print("\n检测失败！")
        print(f"总耗时: {total_time:.2f}秒")

if __name__ == "__main__":
    main()