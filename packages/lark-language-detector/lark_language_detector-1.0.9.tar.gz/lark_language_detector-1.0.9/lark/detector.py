#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lark Language Detector
"""

import json
import torch
import logging
import os
import requests
from typing import Dict, List
from pathlib import Path

# 导入模型和分词器
from .model import LarkModel
from .tokenizer import batch_tokenize

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LarkDetector:
    """Lark 语言检测器"""
    
    def __init__(self, model_path: str = None, 
                 labels_path: str = None,
                 precision: str = "float16"):
        """
        初始化语言检测器
        
        Args:
            model_path: 模型权重文件路径，如果为None则自动下载
            labels_path: 标签文件路径，如果为None则自动下载
            precision: 推理精度，支持 "float32", "float16", "bfloat16"
        """
        self.precision = precision
        # 检查CUDA可用性
        if torch.cuda.is_available():
            self.device = torch.device("cuda")
            logger.info("检测到CUDA，将使用GPU进行推理")
        else:
            self.device = torch.device("cpu")
            logger.info("未检测到CUDA，将使用CPU进行推理")
        self.model = None
        self.labels = []
        self.label2id = {}
        self.id2label = {}
        
        # 设置默认路径或下载模型
        if model_path is None:
            model_path = self._download_model()
        if labels_path is None:
            labels_path = self._download_labels()
            
        self.model_path = model_path
        self.labels_path = labels_path
        
        self._load_labels()
        self._load_model()
    
    def _download_model(self) -> str:
        """获取模型文件路径，优先使用包内文件"""
        # 首先尝试包内文件
        package_model_path = Path(__file__).parent / "farshore" / "save_lark" / "lark_epoch1.pth"
        if package_model_path.exists():
            logger.info(f"使用包内模型文件: {package_model_path}")
            return str(package_model_path)
        
        # 如果包内没有，尝试用户目录
        # 优先使用环境变量 HF_ENDPOINT
        hf_endpoint = os.environ.get("HF_ENDPOINT", "https://huggingface.co")
        model_url = f"{hf_endpoint}/jiangchengchengNLP/Lark/resolve/main/lark_epoch1.pth"
        mirror_url = "https://hf-mirror.com/jiangchengchengNLP/Lark/resolve/main/lark_epoch1.pth"
        model_dir = Path.home() / ".lark" / "models"
        model_path = model_dir / "lark_epoch1.pth"
        
        # 如果模型文件已存在，直接返回路径
        if model_path.exists():
            logger.info(f"模型文件已存在: {model_path}")
            return str(model_path)
        
        # 创建目录
        model_dir.mkdir(parents=True, exist_ok=True)
        
        logger.info(f"正在下载模型文件到: {model_path}")
        
        try:
            # 使用wget下载
            logger.info(f"使用wget从镜像下载: {mirror_url}")
            import subprocess
            result = subprocess.run(
                ["wget", "-O", str(model_path), mirror_url],
                capture_output=True, text=True, timeout=300
            )
            if result.returncode == 0:
                logger.info("模型文件使用wget下载完成")
                return str(model_path)
            else:
                raise Exception(f"wget下载失败: {result.stderr}")
                
        except Exception as e:
            logger.error(f"wget下载失败: {e}")
            raise Exception(f"模型文件下载失败: {e}")
    
    def _download_labels(self) -> str:
        """获取标签文件路径，优先使用包内文件"""
        # 首先尝试包内文件
        package_labels_path = Path(__file__).parent / "farshore" / "all_dataset_labels.json"
        if package_labels_path.exists():
            logger.info(f"使用包内标签文件: {package_labels_path}")
            return str(package_labels_path)
        
        # 如果包内没有，尝试用户目录
        # 优先使用环境变量 HF_ENDPOINT
        hf_endpoint = os.environ.get("HF_ENDPOINT", "https://huggingface.co")
        labels_url = f"{hf_endpoint}/jiangchengchengNLP/Lark/resolve/main/all_dataset_labels.json"
        mirror_url = "https://hf-mirror.com/jiangchengchengNLP/Lark/resolve/main/all_dataset_labels.json"
        model_dir = Path.home() / ".lark" / "models"
        labels_path = model_dir / "all_dataset_labels.json"
        
        # 如果标签文件已存在，直接返回路径
        if labels_path.exists():
            logger.info(f"标签文件已存在: {labels_path}")
            return str(labels_path)
        
        # 创建目录
        model_dir.mkdir(parents=True, exist_ok=True)
        
        logger.info(f"正在下载标签文件到: {labels_path}")
        
        try:
            # 使用wget下载
            logger.info(f"使用wget从镜像下载: {mirror_url}")
            import subprocess
            result = subprocess.run(
                ["wget", "-O", str(labels_path), mirror_url],
                capture_output=True, text=True, timeout=300
            )
            if result.returncode == 0:
                logger.info("标签文件使用wget下载完成")
                return str(labels_path)
            else:
                raise Exception(f"wget下载失败: {result.stderr}")
                
        except Exception as e:
            logger.error(f"wget下载失败: {e}")
            raise Exception(f"标签文件下载失败: {e}")
        
    def _load_labels(self):
        """加载语言标签"""
        try:
            with open(self.labels_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.labels = data.get("all_labels", [])
                self.label2id = {lang: i for i, lang in enumerate(self.labels)}
                self.id2label = {i: lang for i, lang in enumerate(self.labels)}
            logger.info(f"加载了 {len(self.labels)} 种语言标签")
        except Exception as e:
            logger.error(f"加载标签文件失败: {e}")
            raise
    
    def _load_model(self):
        """加载模型并设置精度"""
        try:
            # 确定数据类型
            if self.precision == "float16":
                dtype = torch.float16
            elif self.precision == "bfloat16":
                dtype = torch.bfloat16
            else:
                dtype = torch.float32
            
            logger.info(f"使用精度: {self.precision} ({dtype})")
            
            # 创建模型实例
            self.model = LarkModel(
                d_model=256, 
                n_layers=4, 
                n_heads=8, 
                ff=512,
                label_size=len(self.labels), 
                max_len=1024,
                dtype=dtype,
                dropout=0.1
            )
            
            # 加载权重 - 直接使用weights_only=False，因为模型文件需要
            logger.info("使用weights_only=False加载模型，请确保模型文件来源可信")
            state_dict = torch.load(self.model_path, map_location="cpu", weights_only=False)
            
            self.model.load_state_dict(state_dict)
            
            # 移动到设备并设置评估模式
            self.model.to(self.device)
            self.model.eval()
            
            logger.info(f"模型加载成功，设备: {self.device}")
            
        except Exception as e:
            logger.error(f"模型加载失败: {e}")
            raise
    
    def _is_traditional_chinese(self, text: str) -> bool:
        """
        判断文本是否为繁体中文
        
        Args:
            text: 要判断的文本
            
        Returns:
            是否为繁体中文
        """
        try:
            import zhconv
            
            # 转换为简体
            simplified = zhconv.convert(text, 'zh-hans')
            
            # 如果转换后文本有变化，说明是繁体
            if simplified != text:
                # 进一步验证：检测转换后的置信度是否更高
                token_ids, pad_mask = batch_tokenize([text], max_len=1024)
                token_ids = token_ids.to(self.device)
                pad_mask = pad_mask.to(self.device)
                
                with torch.no_grad():
                    if self.precision in ["float16", "bfloat16"]:
                        with torch.autocast(device_type=str(self.device), dtype=torch.float16 if self.precision == "float16" else torch.bfloat16):
                            logits = self.model(token_ids, pad_mask, training=False)
                    else:
                        logits = self.model(token_ids, pad_mask, training=False)
                
                probabilities = torch.softmax(logits, dim=-1)
                zh_index = self.label2id.get("zh")
                original_zh_prob = probabilities[0][zh_index].item() if zh_index is not None else 0
                
                # 检测转换后的文本
                token_ids_simp, pad_mask_simp = batch_tokenize([simplified], max_len=1024)
                token_ids_simp = token_ids_simp.to(self.device)
                pad_mask_simp = pad_mask_simp.to(self.device)
                
                with torch.no_grad():
                    if self.precision in ["float16", "bfloat16"]:
                        with torch.autocast(device_type=str(self.device), dtype=torch.float16 if self.precision == "float16" else torch.bfloat16):
                            logits_simp = self.model(token_ids_simp, pad_mask_simp, training=False)
                    else:
                        logits_simp = self.model(token_ids_simp, pad_mask_simp, training=False)
                
                probabilities_simp = torch.softmax(logits_simp, dim=-1)
                simplified_zh_prob = probabilities_simp[0][zh_index].item() if zh_index is not None else 0
                
                # 如果转换为简体后置信度明显上升，则认为是繁体中文
                if simplified_zh_prob > original_zh_prob + 0.01:
                    return True
                else:
                    return False
            else:
                return False
                
        except ImportError:
            # 如果zhconv不可用，使用字符统计方法
            logger.warning("zhconv不可用，使用字符统计方法判断简繁体")
            
            # 繁体中文特有字符
            traditional_chars = {
                '麼', '為', '們', '個', '會', '體', '國', '灣', '華', '語',
                '學', '習', '經', '濟', '發', '展', '歷', '史', '文', '化',
                '電', '腦', '網', '絡', '資', '訊', '時', '間', '空', '間',
                '愛', '情', '友', '誼', '家', '庭', '社', '會', '政', '治',
                '法', '律', '宗', '教', '藝', '術', '音', '樂', '電', '影',
                '視', '聽', '新', '聞', '報', '導', '廣', '播', '電', '台',
                '電', '視', '台', '網', '站', '論', '壇', '社', '群', '網',
                '絡', '遊', '戲', '娛', '樂', '休', '閒', '運', '動', '健',
                '康', '醫', '療', '保', '健', '食', '品', '飲', '料', '衣',
                '服', '住', '宅', '交', '通', '工', '具', '旅', '遊', '觀',
                '光', '商', '業', '工', '業', '農', '業', '服', '務', '金',
                '融', '保', '險', '證', '券', '投', '資', '房', '地', '產',
                '建', '築', '工', '程', '設', '計', '製', '造', '生', '產',
                '銷', '售', '市', '場', '價', '格', '質', '量', '品', '牌',
                '客', '戶', '服', '務', '技', '術', '研', '發', '創', '新',
                '管', '理', '組', '織', '人', '力', '資', '源', '財', '務',
                '會', '計', '審', '計', '稅', '務', '法', '律', '合', '規',
                '風', '險', '控', '制', '戰', '略', '規', '劃', '目', '標',
                '績', '效', '評', '估', '改', '進', '優', '化', '變', '革',
                '發', '展', '成', '長', '競', '爭', '合', '作', '共', '贏',
                '價', '值', '理', '念', '文', '化', '使', '命', '願', '景'
            }
            
            # 简体中文特有字符
            simplified_chars = {
                '么', '为', '们', '个', '会', '体', '国', '湾', '华', '语',
                '学', '习', '经', '济', '发', '展', '历', '史', '文', '化',
                '电', '脑', '网', '络', '资', '讯', 'time', '间', '空', '间',
                '爱', '情', '友', '谊', '家', '庭', '社', '会', '政', '治',
                '法', '律', '宗', '教', '艺', '术', '音', '乐', '电', '影',
                '视', '听', '新', '闻', '报', '导', '广', '播', '电', '台',
                '电', '视', '台', '网', '站', '论', '坛', '社', '群', '网',
                '络', '游', '戏', '娱', '乐', '休', '闲', '运', '动', '健',
                '康', '医', '疗', '保', '健', '食', '品', '饮', '料', '衣',
                '服', '住', '宅', '交', '通', '工', '具', '旅', '游', '观',
                '光', '商', '业', '工', '业', '农', '业', '服', '务', '金',
                '融', '保', '险', '证', '券', '投', '资', '房', '地', '产',
                '建', '筑', '工', '程', '设', '计', '制', '造', '生', '产',
                '销', '售', '市', '场', '价', '格', '质', '量', '品', '牌',
                '客', '户', '服', '务', '技', '术', '研', '发', '创', '新',
                '管', '理', '组', '织', '人', '力', '资', '源', '财', '务',
                '会', '计', '审', '计', '税', '务', '法', '律', '合', '规',
                '风', '险', '控', '制', '战', '略', '规', '划', '目', '标',
                '绩', '效', '评', '估', '改', '进', '优', '化', '变', '革',
                '发', '展', '成', '长', '竞', '争', '合', '作', '共', '赢',
                '价', '值', '理', '念', '文', '化', '使', '命', '愿', '景'
            }
            
            # 统计繁体字符和简体字符数量
            trad_count = sum(1 for char in text if char in traditional_chars)
            simp_count = sum(1 for char in text if char in simplified_chars)
            
            # 如果繁体字符明显多于简体字符，则认为是繁体中文
            if trad_count > simp_count and trad_count >= 1:
                return True
            return False
    
    def detect(self, text: str) -> Dict:
        """
        检测单文本语言
        
        Args:
            text: 要检测的文本
            
        Returns:
            检测结果，包含语言和置信度
        """
        try:
            # 分词
            token_ids, pad_mask = batch_tokenize([text], max_len=1024)
            token_ids = token_ids.to(self.device)
            pad_mask = pad_mask.to(self.device)
            
            # 推理 - 使用inference_mode减少内存占用
            if self.device.type == "cuda":
                with torch.inference_mode():
                    if self.precision in ["float16", "bfloat16"]:
                        with torch.autocast(device_type=str(self.device), dtype=torch.float16 if self.precision == "float16" else torch.bfloat16):
                            logits = self.model(token_ids, pad_mask, training=False)
                    else:
                        logits = self.model(token_ids, pad_mask, training=False)
            else:
                with torch.no_grad():
                    if self.precision in ["float16", "bfloat16"]:
                        with torch.autocast(device_type=str(self.device), dtype=torch.float16 if self.precision == "float16" else torch.bfloat16):
                            logits = self.model(token_ids, pad_mask, training=False)
                    else:
                        logits = self.model(token_ids, pad_mask, training=False)
            
            # 计算概率
            probabilities = torch.softmax(logits, dim=-1)
            top_probs, top_indices = torch.topk(probabilities, k=5, dim=-1)
            
            # 获取最高概率的语言
            detected_lang_id = top_indices[0][0].item()
            confidence = top_probs[0][0].item()
            detected_language = self.id2label[detected_lang_id]
            
            # 后处理：如果检测到中文，进一步判断是否为繁体中文
            if detected_language == "zh" and self._is_traditional_chinese(text):
                detected_language = "zh-TW"
            
            return {
                "detected_language": detected_language,
                "confidence": round(confidence, 4)
            }
            
        except Exception as e:
            logger.error(f"检测失败: {e}")
            return {
                "detected_language": "en",  # 默认英语
                "confidence": 0.0,
                "top_languages": []
            }
    
    def detect_new(self, text: str, language_code: str) -> Dict:
        """
        检测文本语言并判断是否需要LLM
        
        Args:
            text: 要检测的文本
            language_code: 期望的语言代码
            
        Returns:
            检测结果，包含是否需要LLM的判断
        """
        result = self.detect(text)
        detected_lang = result["detected_language"]
        
        # 判断是否需要 LLM
        is_need_llm = detected_lang != language_code

        return {
            "detected_language": detected_lang,
            "confidence": result["confidence"],
            "is_need_llm": is_need_llm
        }
    
    def get_info(self) -> Dict:
        """获取模型信息"""
        return {
            "model_name": "Lark Language Detector",
            "precision": self.precision,
            "device": str(self.device),
            "supported_languages": self.labels,
            "total_languages": len(self.labels)
        }
