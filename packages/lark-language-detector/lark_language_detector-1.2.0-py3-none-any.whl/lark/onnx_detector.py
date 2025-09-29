#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ONNX版本的Lark语言检测器 - 集成到主包
"""

import os
import json
import numpy as np
import onnxruntime as ort
from typing import Dict, List, Optional, Union
import logging

# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LarkONNXDetector:
    """ONNX版本的Lark语言检测器"""
    
    def __init__(self, model_path: Optional[str] = None, labels_path: Optional[str] = None, device: str = "auto"):
        """
        初始化ONNX检测器
        
        Args:
            model_path: ONNX模型文件路径，如果为None则自动下载
            labels_path: 标签文件路径，如果为None则自动下载
            device: 设备类型，可选 'auto', 'cpu', 'cuda'
        """
        self.device = device
        
        # 设置默认路径或下载模型
        if model_path is None:
            model_path = self._download_onnx_model()
        if labels_path is None:
            labels_path = self._download_labels()
            
        self.model_path = model_path
        self.labels_path = labels_path
        
        # 检查模型文件是否存在
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"ONNX模型文件不存在: {model_path}")
        
        # 加载标签
        self._load_labels()
        
        # 确定执行提供者
        providers = self._get_providers()
        
        # 初始化ONNX Runtime会话
        logger.info(f"加载ONNX模型: {model_path}")
        logger.info(f"使用设备: {providers}")
        self.session = ort.InferenceSession(model_path, providers=providers)
        
        # 获取输入输出名称
        self.input_names = [input.name for input in self.session.get_inputs()]
        self.output_names = [output.name for output in self.session.get_outputs()]
        
        logger.info(f"输入名称: {self.input_names}")
        logger.info(f"输出名称: {self.output_names}")
        logger.info(f"支持的语言数量: {len(self.id2label)}")
    
    def _download_onnx_model(self) -> str:
        """获取ONNX模型文件路径"""
        # 首先尝试包内文件
        package_model_path = os.path.join(os.path.dirname(__file__), "..", "lark_model.onnx")
        if os.path.exists(package_model_path):
            logger.info(f"使用包内ONNX模型文件: {package_model_path}")
            return package_model_path
        
        # 如果包内没有，尝试用户目录
        hf_endpoint = os.environ.get("HF_ENDPOINT", "https://huggingface.co")
        model_url = f"{hf_endpoint}/jiangchengchengNLP/Lark/resolve/main/lark_model.onnx"
        mirror_url = "https://hf-mirror.com/jiangchengchengNLP/Lark/resolve/main/lark_model.onnx"
        model_dir = os.path.join(os.path.expanduser("~"), ".lark", "models")
        model_path = os.path.join(model_dir, "lark_model.onnx")
        
        # 如果模型文件已存在，直接返回路径
        if os.path.exists(model_path):
            logger.info(f"ONNX模型文件已存在: {model_path}")
            return model_path
        
        # 创建目录
        os.makedirs(model_dir, exist_ok=True)
        
        logger.info(f"正在下载ONNX模型文件到: {model_path}")
        
        try:
            # 使用wget下载
            logger.info(f"使用wget从镜像下载: {mirror_url}")
            import subprocess
            result = subprocess.run(
                ["wget", "-O", model_path, mirror_url],
                capture_output=True, text=True, timeout=300
            )
            if result.returncode == 0:
                logger.info("ONNX模型文件使用wget下载完成")
                return model_path
            else:
                raise Exception(f"wget下载失败: {result.stderr}")
                
        except Exception as e:
            logger.error(f"wget下载失败: {e}")
            raise Exception(f"ONNX模型文件下载失败: {e}")
    
    def _download_labels(self) -> str:
        """获取标签文件路径"""
        # 首先尝试包内文件
        package_labels_path = os.path.join(os.path.dirname(__file__), "..", "farshore", "all_dataset_labels.json")
        if os.path.exists(package_labels_path):
            logger.info(f"使用包内标签文件: {package_labels_path}")
            return package_labels_path
        
        # 如果包内没有，尝试用户目录
        hf_endpoint = os.environ.get("HF_ENDPOINT", "https://huggingface.co")
        labels_url = f"{hf_endpoint}/jiangchengchengNLP/Lark/resolve/main/all_dataset_labels.json"
        mirror_url = "https://hf-mirror.com/jiangchengchengNLP/Lark/resolve/main/all_dataset_labels.json"
        model_dir = os.path.join(os.path.expanduser("~"), ".lark", "models")
        labels_path = os.path.join(model_dir, "all_dataset_labels.json")
        
        # 如果标签文件已存在，直接返回路径
        if os.path.exists(labels_path):
            logger.info(f"标签文件已存在: {labels_path}")
            return labels_path
        
        # 创建目录
        os.makedirs(model_dir, exist_ok=True)
        
        logger.info(f"正在下载标签文件到: {labels_path}")
        
        try:
            # 使用wget下载
            logger.info(f"使用wget从镜像下载: {mirror_url}")
            import subprocess
            result = subprocess.run(
                ["wget", "-O", labels_path, mirror_url],
                capture_output=True, text=True, timeout=300
            )
            if result.returncode == 0:
                logger.info("标签文件使用wget下载完成")
                return labels_path
            else:
                raise Exception(f"wget下载失败: {result.stderr}")
                
        except Exception as e:
            logger.error(f"wget下载失败: {e}")
            raise Exception(f"标签文件下载失败: {e}")
    
    def _get_providers(self):
        """
        根据设备参数获取ONNX Runtime执行提供者
        
        Returns:
            执行提供者列表
        """
        available_providers = ort.get_available_providers()
        logger.info(f"可用的执行提供者: {available_providers}")
        
        if self.device == "cuda":
            if "CUDAExecutionProvider" in available_providers:
                return ['CUDAExecutionProvider', 'CPUExecutionProvider']
            else:
                logger.warning("CUDA不可用，将使用CPU")
                return ['CPUExecutionProvider']
        elif self.device == "cpu":
            return ['CPUExecutionProvider']
        else:  # auto
            # 自动选择：优先CUDA，其次CPU
            if "CUDAExecutionProvider" in available_providers:
                logger.info("自动选择CUDA执行提供者")
                return ['CUDAExecutionProvider', 'CPUExecutionProvider']
            else:
                logger.info("自动选择CPU执行提供者")
                return ['CPUExecutionProvider']
    
    def _load_labels(self):
        """加载语言标签"""
        try:
            with open(self.labels_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                labels_list = data.get("all_labels", [])
                self.id2label = {i: label for i, label in enumerate(labels_list)}
                self.label2id = {label: i for i, label in enumerate(labels_list)}
            logger.info(f"加载了 {len(self.id2label)} 种语言标签")
        except Exception as e:
            logger.error(f"加载标签文件失败: {e}")
            raise
    
    def _tokenize(self, text: str, max_len: int = 1024) -> tuple:
        """
        分词函数 - 与原始模型保持一致
        
        Args:
            text: 输入文本
            max_len: 最大长度
            
        Returns:
            token_ids: 分词ID
            pad_mask: 填充掩码
        """
        # 特殊字节标记
        START_BYTE = 256
        END_BYTE = 257
        PAD_BYTE = 258
        
        # 编码文本
        if text == "":
            # 特殊情况
            byte_seq = [START_BYTE]
            max_len = 1
        else:
            # 添加开始和结束标记
            text_bytes = list(text.encode("utf-8"))
            byte_seq = [START_BYTE] + text_bytes + [END_BYTE]
        
        # 截断或填充
        if len(byte_seq) >= max_len:
            token_ids = byte_seq[:max_len]
            pad_mask = [1.0] * max_len  # 1=有效
        else:
            pad_len = max_len - len(byte_seq)
            token_ids = byte_seq + [PAD_BYTE] * pad_len
            pad_mask = [1.0] * len(byte_seq) + [0.0] * pad_len  # 1=有效, 0=padding
        
        # 转换为正确的数据类型
        token_ids = np.array(token_ids, dtype=np.int64).reshape(1, -1)
        pad_mask = np.array(pad_mask, dtype=np.float32).reshape(1, -1)
        
        return token_ids, pad_mask
    
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
                token_ids, pad_mask = self._tokenize(text)
                outputs = self.session.run(
                    self.output_names,
                    {
                        self.input_names[0]: token_ids,
                        self.input_names[1]: pad_mask
                    }
                )
                logits = outputs[0]
                exp_logits = np.exp(logits - np.max(logits, axis=-1, keepdims=True))
                probabilities = exp_logits / np.sum(exp_logits, axis=-1, keepdims=True)
                zh_index = self.label2id.get("zh")
                original_zh_prob = probabilities[0, zh_index] if zh_index is not None else 0
                
                # 检测转换后的文本
                token_ids_simp, pad_mask_simp = self._tokenize(simplified)
                outputs_simp = self.session.run(
                    self.output_names,
                    {
                        self.input_names[0]: token_ids_simp,
                        self.input_names[1]: pad_mask_simp
                    }
                )
                logits_simp = outputs_simp[0]
                exp_logits_simp = np.exp(logits_simp - np.max(logits_simp, axis=-1, keepdims=True))
                probabilities_simp = exp_logits_simp / np.sum(exp_logits_simp, axis=-1, keepdims=True)
                simplified_zh_prob = probabilities_simp[0, zh_index] if zh_index is not None else 0
                
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
    
    def detect(self, text: str) -> Dict[str, Union[str, float]]:
        """
        检测文本语言
        
        Args:
            text: 输入文本
            
        Returns:
            包含检测结果和置信度的字典
        """
        if not text or not text.strip():
            return {"detected_language": "unknown", "confidence": 0.0}
        
        try:
            # 分词
            token_ids, pad_mask = self._tokenize(text)
            
            # ONNX推理
            outputs = self.session.run(
                self.output_names,
                {
                    self.input_names[0]: token_ids,
                    self.input_names[1]: pad_mask
                }
            )
            
            logits = outputs[0]  # [batch_size, num_classes]
            
            # 计算softmax概率
            exp_logits = np.exp(logits - np.max(logits, axis=-1, keepdims=True))
            probabilities = exp_logits / np.sum(exp_logits, axis=-1, keepdims=True)
            
            # 获取最高概率的语言
            top_idx = np.argmax(probabilities, axis=-1)[0]
            confidence = probabilities[0, top_idx]
            
            detected_language = self.id2label.get(top_idx, "unknown")
            
            # 后处理：如果检测到中文，进一步判断是否为繁体中文
            if detected_language == "zh" and self._is_traditional_chinese(text):
                detected_language = "zh-TW"
            
            return {
                "detected_language": detected_language,
                "confidence": float(confidence)
            }
            
        except Exception as e:
            logger.error(f"语言检测失败: {e}")
            return {"detected_language": "unknown", "confidence": 0.0}
    
    def detect_batch(self, texts: List[str]) -> List[Dict[str, Union[str, float]]]:
        """
        批量检测文本语言
        
        Args:
            texts: 输入文本列表
            
        Returns:
            检测结果列表
        """
        results = []
        for text in texts:
            results.append(self.detect(text))
        return results
    
    def get_supported_languages(self) -> List[str]:
        """获取支持的语言列表"""
        return list(self.label2id.keys())
    
    def get_info(self) -> Dict:
        """获取模型信息"""
        return {
            "model_name": "Lark ONNX Language Detector",
            "device": self.device,
            "supported_languages": self.get_supported_languages(),
            "total_languages": len(self.id2label),
            "model_path": self.model_path
        }
