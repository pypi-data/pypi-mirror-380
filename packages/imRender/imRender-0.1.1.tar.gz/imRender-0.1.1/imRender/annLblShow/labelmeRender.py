#!/usr/bin/env python3
# encoding: utf-8
# @author: firstelfin
# @time: 2025/09/27 10:14:47

import os
import json
import warnings
import cv2 as cv
import numpy as np
from tqdm import tqdm
from pathlib import Path
from loguru import logger
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, List, Any, Tuple
from PIL import Image, ImageDraw, ImageFont

warnings.filterwarnings('ignore')


class LabelmeChineseRenderer:

    def __init__(
            self,
            font_path=Path.home() / ".config/elfin/fonts/Arial.Unicode.ttf",
            verbose: bool = False,
            flags_key_map: Dict[str, str] = {},
        ):
        self.verbose = verbose
        # 定义汇报级别对应的颜色 (BGR格式)
        self.report_level_colors = {
            "critical": (0, 0, 255),      # 红色 - 关键/严重问题
            "high": (0, 165, 255),        # 橙色 - 高优先级
            "medium": (0, 255, 255),      # 黄色 - 中等优先级
            "low": (0, 255, 0),           # 绿色 - 低优先级
            "info": (255, 255, 255),      # 白色 - 信息类
            "default": (128, 128, 128)    # 灰色 - 默认
        }
        self.flags_key_map = flags_key_map
        self.thickness_map = {"critical": 3, "high": 3, "medium": 3, "low": 2, "info": 2, "default": 2}
        # 加载字体
        assert font_path.exists(), f"The font file '{self.font_path}' does not exist."
        self.font = ImageFont.truetype(font_path, 20)
        self.text_color = (0, 0, 0)  # 黑色
        self.font_path = font_path
        self.ascent, self.descent = self.font.getmetrics()
        self.image_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff'}
    
    def load_labelme_annotation(self, json_path: str | Path) -> Dict[str, Any]:
        """Load labelme annotation file."""
        with open(json_path, 'r', encoding='utf-8') as f:
            annotation = json.load(f)
        return annotation
    
    def get_bounding_box_from_shape(self, shape: Dict[str, Any]) -> Tuple[int, int, int, int]:
        """Extract bounding boxes from the points data of labelme instances."""
        points = np.array(shape['points'])
        x_min = int(points[:, 0].min())
        y_min = int(points[:, 1].min())
        x_max = int(points[:, 0].max())
        y_max = int(points[:, 1].max())
        return x_min, y_min, x_max, y_max
    
    def get_report_level(self, flags: Dict[str, bool]) -> Tuple[str, Tuple[int, int, int]]:
        """Get the level of rendering required for the current instance.

        :param Dict[str, bool] flags: labelme flags
        :return Tuple[str, Tuple[int, int, int]]: report level
        """

        new_flags = {self.flags_key_map.get(flag_key, flag_key): flag_value for flag_key, flag_value in flags.items()}
        for key, value in self.report_level_colors.items():
            if new_flags.get(key, False):
                return key, value

        return "default", self.report_level_colors["default"]
    
    def get_confidence(self, shape: Dict[str, Any]) -> float:
        """Obtain confidence level from labelme instance."""
        score = 1.0
        if 'score' in shape:
            score = shape['score']
        elif 'confidence' in shape:
            score = shape['confidence']
        return score
    
    def put_chinese_text(self, image: np.ndarray, text: str, position: Tuple[int, int], 
                        color: Tuple[int, int, int] = (255, 255, 255)) -> np.ndarray:
        """Draw Chinese text on the image."""
        
        img_pil = Image.fromarray(cv.cvtColor(image, cv.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(img_pil)
        draw.text(position, text, font=self.font, fill=color)
        
        # 转换回OpenCV格式
        return cv.cvtColor(np.array(img_pil), cv.COLOR_RGB2BGR)
    
    @staticmethod
    def bbox_valid(bbox: Tuple[int, int, int, int], image_shape: Tuple[int, int]) -> Tuple:
        """Calibrate the border of the annotation instance."""
        x_min, y_min, x_max, y_max = bbox
        x_min = max(0, x_min)
        y_min = max(0, y_min)
        x_max = min(image_shape[1], x_max)
        y_max = min(image_shape[0], y_max)
        if x_min >= x_max or y_min >= y_max:
            return ()
        return x_min, y_min, x_max, y_max

    def draw_bounding_box(self, image: np.ndarray, bbox: Tuple[int, int, int, int], 
                         class_name: str, confidence: float, report: Tuple) -> np.ndarray:
        """Draw bbox and label information on the image.

        :param image: _description_
        :type image: np.ndarray
        :param bbox: _description_
        :type bbox: Tuple[int, int, int, int]
        :param class_name: _description_
        :type class_name: str
        :param confidence: _description_
        :type confidence: float
        :param report_level: _description_
        :type report_level: str
        :return: _description_
        :rtype: np.ndarray
        """
        valid_bbox = self.bbox_valid(bbox, image.shape[:2])
        if not valid_bbox:
            return image
        x_min, y_min, x_max, y_max = valid_bbox
        
        # 获取对应汇报级别的颜色
        report_level, report_color = report
        
        # 绘制边界框 - 根据汇报级别调整线条粗细
        thickness = self.thickness_map.get(report_level, 2)
        
        cv.rectangle(image, (x_min, y_min), (x_max, y_max), report_color, thickness)
        
        # 准备显示文本
        label_text = f"{class_name}: {confidence:.2f}" if confidence >= 0 else class_name
        
        # 计算文本背景大小
        label_box = self.font.getbbox(label_text)
        text_width, text_height = int(label_box[2] - label_box[0]), int(label_box[3] - label_box[1])
        
        # 绘制文本背景
        text_bg_cy = max(0, y_min - text_height - thickness)
        cv.rectangle(image, 
                     (x_min, text_bg_cy - text_height-1), 
                     (x_min + text_width, text_bg_cy + text_height + 1), 
                     report_color, -1)
        
        # 绘制文本 - 使用中文支持
        image = self.put_chinese_text(
            image, label_text, 
            (x_min, text_bg_cy - (text_height + 2) // 2 - self.descent // 2), 
            color=self.text_color
        )
        
        return image

    def render_image(
            self,
            image_path: str,
            json_path: str,
            output_path: str,
            just_flags: bool = True,
            show_score: bool = True,
            ind: int = 0
        ) -> np.ndarray:
        """Render a single image for display and save to a specified address."""

        chech_info = f" Please check the file[index={ind}]."
        # 加载图像
        image = cv.imread(image_path)
        if image is None: raise ValueError(f"Unable to load image: {image_path}." + chech_info)
        
        # 检查标注文件是否存在
        if not Path(json_path).exists(): raise ValueError(f"The annotation file {json_path} does not exist." + chech_info)
        
        annotation = self.load_labelme_annotation(json_path)
        
        # 渲染每个检测目标
        shapes: List[Dict[str, Any]] = annotation.get('shapes', [])
        for shape in shapes:
            flags: dict[str, bool] = shape.get("flags", {})
            if just_flags and True not in flags.values():
                continue
            bbox = self.get_bounding_box_from_shape(shape)  # 获取边界框
            class_name = shape.get('label', 'Unknown')
            confidence = self.get_confidence(shape)
            report = self.get_report_level(flags=shape.get("flags", {}))
            image = self.draw_bounding_box(image, bbox, class_name, confidence if show_score else -1, report)
        
        # 确保输出目录存在
        Path(output_path).parent.mkdir(exist_ok=True, parents=True)
        
        # 保存图像到指定地址
        success = cv.imwrite(output_path, image)
        if not success: raise ValueError(f"Unable to save image to: {output_path}." + chech_info)

        if self.verbose: logger.info(f"The image has been rendered and saved to: the {output_path}" + chech_info)
        
        return image
    
    def load_img_lbls(self, img_dir: Path, lbl_dir: Path | None = None):
        """Match images and labels."""
        img_files = [f for f in img_dir.rglob("*") if f.suffix.lower() in self.image_extensions]
        if lbl_dir is None:
            lbl_files = [img_file.with_suffix(".json") for img_file in img_files]
        else:
            lbl_files = [list(lbl_dir.rglob(f"{f.stem}.json")) for f in img_files]
            lbl_files = [f[0] if f and f[0].exists() else None for f in lbl_files]
        return img_files, lbl_files

    def render_batch(
            self, 
            images_dir: Path, 
            labels_dir: Path | None, 
            output_dir: Path, 
            just_flags: bool = True, 
            show_score: bool = True
        ):
        """Batch processing of image rendering.

        :param Path images_dir: images directory
        :param Path | None labels_dir: labels directory
        :param Path output_dir: output directory
        :param bool, optional just_flags: only show labeled objects in flags, defaults to True
        :param bool, optional show_score: show confidence score, defaults to True
        """

        images_dir = Path(images_dir)
        ann_dir = Path(labels_dir) if labels_dir is not None else None
        output_dir = Path(output_dir)
        output_dir.mkdir(exist_ok=True, parents=True)
        
        # 查找所有图像文件
        img_files, lbl_files = self.load_img_lbls(images_dir, ann_dir)
        out_files = [output_dir / img_file.name for img_file in img_files]
        
        # 批量渲染图像
        workers = os.cpu_count()
        workers = max(4, workers // 2) if workers is not None else 4
        res = []
        with ThreadPoolExecutor(max_workers=workers) as executor:
            ind = 0
            for img_file, lbl_file, out_file in zip(img_files, lbl_files, out_files):
                res.append(
                    executor.submit(
                        self.render_image, str(img_file), str(lbl_file), str(out_file),
                        just_flags=just_flags, show_score=show_score, ind=ind,
                    )
                )
                ind += 1
            
            # 生成执行进度条
            exec_bar = tqdm(as_completed(res), total=len(res), desc="RenderingImages", colour="#CD8500")
            for ft in exec_bar:
                ft.result()
