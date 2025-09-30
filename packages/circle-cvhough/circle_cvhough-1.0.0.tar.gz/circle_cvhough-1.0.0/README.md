# cvHough SDK

**YOLO物体检测与霍夫圆检测集成工具包**

cvHough SDK 是一个专业的计算机视觉工具包，集成了YOLO物体检测和霍夫圆检测算法，专门用于在检测到的物体区域内进行精确的圆形检测。

## 🚀 主要功能

- **YOLO物体检测**: 使用预训练的YOLO模型快速检测图像中的物体
- **区域内圆形检测**: 在YOLO检测到的区域内使用霍夫变换检测圆形
- **多种二值化方法**: 支持自适应阈值、OTSU和手动阈值三种二值化方法
- **结果可视化**: 自动生成带有检测结果标注的图像
- **调试支持**: 可选保存二值化图像用于算法调试

## 📦 安装

### 使用pip安装（推荐）

```bash
pip install circle-cvhough
```

### 从源码安装

```bash
git clone https://github.com/ruantong/circle-cvhough.git
cd circle-cvhough
pip install -e .
```

## 🛠️ 依赖项

- Python >= 3.8
- OpenCV >= 4.5.0
- NumPy >= 1.19.0
- Ultralytics >= 8.0.0
- Matplotlib >= 3.3.0

## 📖 快速开始

### 最简使用（推荐）

```python
from cvhough_sdk import YOLOCircleDetector

# 初始化检测器
detector = YOLOCircleDetector()

# 检测图像 - 只需要一行代码！
result_image, yolo_detections, circle_results = detector.detect_image('your_image.jpg')

print(f"检测到 {len(yolo_detections)} 个物体")
total_circles = sum(len(circles) for _, circles in circle_results)
print(f"检测到 {total_circles} 个圆形")
```

### 自定义参数使用

```python
from cvhough_sdk import YOLOCircleDetector

# 初始化检测器（自定义参数）
detector = YOLOCircleDetector(
    conf_threshold=0.3,        # YOLO置信度阈值
    binary_method='adaptive'   # 二值化方法
)

# 检测图像
result_image, yolo_detections, circle_results = detector.detect_image('your_image.jpg')
```

### 详细参数控制

```python
from cvhough_sdk import YOLOCircleDetector

# 初始化检测器（使用内置模型）
detector = YOLOCircleDetector()

# 或者使用自定义模型
# detector = YOLOCircleDetector('path/to/your/model.pt')

# 处理图像（详细参数控制）
result_image, yolo_detections, circle_results = detector.process_image(
    image_path='your_image.jpg',
    conf_threshold=0.5,
    save_result=True,
    binary_method='adaptive',
    save_binary_images=False
)

print(f"检测到 {len(yolo_detections)} 个物体")
total_circles = sum(len(circles) for _, circles in circle_results)
print(f"检测到 {total_circles} 个圆形")
```

### 高级使用

```python
from cvhough_sdk import YOLOCircleDetector
import cv2

# 初始化检测器
detector = YOLOCircleDetector()

# 读取图像
image = cv2.imread('your_image.jpg')

# 步骤1: YOLO物体检测
yolo_detections = detector.detect_objects_with_yolo(image, conf_threshold=0.3)

# 步骤2: 在特定区域检测圆形
for x1, y1, x2, y2, conf, class_id in yolo_detections:
    circles = detector.detect_circles_in_region(
        image, x1, y1, x2, y2,
        dp=1,                    # 累加器分辨率
        min_dist=15,            # 圆心最小距离
        param1=15,              # Canny高阈值
        param2=8,               # 圆心检测阈值
        min_radius=3,           # 最小半径
        max_radius=50,          # 最大半径
        save_binary=True,       # 保存二值化图像
        binary_method='manual'  # 二值化方法
    )
    
    print(f"在区域 ({x1}, {y1}, {x2}, {y2}) 检测到 {len(circles)} 个圆形")

# 步骤3: 可视化结果
circle_results = [((x1, y1, x2, y2, conf, class_id), circles) 
                  for (x1, y1, x2, y2, conf, class_id), circles in zip(yolo_detections, [circles])]

result_image = detector.visualize_results(
    image, yolo_detections, circle_results, 
    save_path='result.jpg'
)
```

## 🔧 参数说明

### YOLOCircleDetector 初始化参数

- `yolo_model_path` (str, optional): YOLO模型文件路径，默认使用内置模型
- `conf_threshold` (float, optional): YOLO置信度阈值，默认0.2
- `binary_method` (str, optional): 二值化方法，可选 'adaptive', 'otsu', 'manual'，默认'manual'

### detect_image 方法参数（推荐使用）

- `image_path` (str): 输入图像路径

**说明**: `detect_image` 是简化接口，使用所有默认参数，相当于原来的main函数功能。

### process_image 方法参数（详细控制）

- `image_path` (str): 输入图像路径
- `conf_threshold` (float, optional): YOLO置信度阈值，如果为None则使用初始化时的默认值
- `save_result` (bool): 是否保存结果图像，默认True
- `binary_method` (str, optional): 二值化方法，如果为None则使用初始化时的默认值
- `save_binary_images` (bool, optional): 是否保存二值化图像用于调试，如果为None则使用初始化时的默认值（False）

### detect_circles_in_region 方法参数

- `dp` (int): 累加器分辨率与图像分辨率的反比，默认1
- `min_dist` (int): 检测到的圆心之间的最小距离，默认15
- `param1` (int): Canny边缘检测的高阈值，默认15
- `param2` (int): 圆心检测阈值，默认8
- `min_radius` (int): 最小圆半径，默认3
- `max_radius` (int): 最大圆半径，默认为检测区域最小边长的一半
- `save_binary` (bool): 是否保存二值化图像，默认False
- `binary_method` (str): 二值化方法，默认'adaptive'

## 📊 二值化方法

SDK支持三种二值化方法：

1. **adaptive**: 自适应阈值二值化，适合光照不均匀的图像
2. **otsu**: OTSU自动阈值二值化，适合双峰直方图的图像
3. **manual**: 手动阈值二值化（阈值=200），适合已知阈值的场景

## 🎯 使用场景

- 工业质量检测中的圆形零件检测
- 医学图像中的细胞或病灶检测
- 交通标志中的圆形标志识别
- 科学研究中的粒子或气泡检测

## 💡 最简使用示例

想要快速体验？只需要3行代码：

```python
from cvhough_sdk import YOLOCircleDetector
detector = YOLOCircleDetector()
result_image, yolo_detections, circle_results = detector.detect_image('your_image.jpg')
```

就这么简单！SDK会自动：
- 使用内置的YOLO模型检测物体
- 在每个物体区域内检测圆形
- 保存带有标注的结果图像
- 输出检测统计信息，包括每个物体的圆心和半径

## 📁 项目结构

```
circle-cvhough/
├── cvhough_sdk/
│   ├── __init__.py          # 主要SDK代码
│   ├── main.py             # 原始main函数（已集成到SDK中）
│   └── models/
│       └── best1.pt         # 预训练YOLO模型
├── setup.py                 # 安装配置
├── README.md               # 项目文档
├── example_usage.py        # 详细使用示例
├── simple_example.py       # 最简使用示例
└── 922/                    # 测试图像目录
    ├── 1.png
    ├── 2.png
    └── ...
```

## 🔍 调试功能

SDK提供了丰富的调试功能：

```python
from cvhough_sdk import YOLOCircleDetector

# 初始化检测器，启用调试功能
detector = YOLOCircleDetector(
    conf_threshold=0.2,
    binary_method='manual'
)

# 处理图像并保存二值化结果（用于调试）
result_image, yolo_detections, circle_results = detector.process_image(
    'image.jpg', 
    save_binary_images=True  # 启用二值化图像保存
)

# 注意：新版本默认不显示二值化图像，专注于最终结果
# 如需查看二值化过程，可以查看保存的二值化图像文件
```

## ⚡ 性能优化建议

1. **参数调优**: 根据具体应用场景调整霍夫圆检测参数
2. **图像预处理**: 对于噪声较多的图像，可以增加高斯模糊的核大小
3. **区域筛选**: 使用更高的YOLO置信度阈值减少误检
4. **批量处理**: 对于大量图像，考虑使用多线程处理

## 🤝 贡献

欢迎提交Issue和Pull Request来改进这个项目！

## 📄 许可证

本项目采用MIT许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 📞 联系我们

- 项目主页: https://github.com/cvhough/circle-cvhough
- 问题反馈: https://github.com/cvhough/circle-cvhough/issues
- 邮箱: cvhough@example.com

## 🔄 更新日志

### v1.0.0 (2024-01-XX)
- 初始版本发布
- 集成YOLO物体检测和霍夫圆检测
- 支持多种二值化方法
- 提供完整的可视化功能
- 包含调试工具和示例代码

### v1.1.0 (最新版本)
- **新增简化接口**: 添加 `detect_image()` 方法，只需一行代码即可完成检测
- **参数封装优化**: 将main函数的所有参数封装到SDK类中，支持默认配置
- **输出格式优化**: 
  - 移除冗余的步骤输出信息
  - 在最终统计中显示每个物体的圆心和半径
  - 默认不保存和显示二值化图像，专注于最终结果
- **使用体验提升**: 
  - 提供最简使用示例（3行代码）
  - 支持自定义参数初始化
  - 保持向后兼容性
- **文档完善**: 更新README，添加多种使用方式的示例

---

**感谢使用 cvHough SDK！** 🎉