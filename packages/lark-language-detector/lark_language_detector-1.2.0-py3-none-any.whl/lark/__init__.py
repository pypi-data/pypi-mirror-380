"""
Lark Language Detection Package
A lightweight language detection library similar to fasttext and Google's implementation with ONNX support.
"""

from .onnx_detector import LarkONNXDetector

__version__ = "1.2.0"
__author__ = "Farshore Team"
__all__ = ["LarkONNXDetector"]

# 创建全局实例
detector = LarkONNXDetector()

# 提供便捷函数
def detect(text: str):
    """检测文本语言"""
    return detector.detect(text)

def detect_batch(texts: list):
    """批量检测文本语言"""
    return detector.detect_batch(texts)

def get_supported_languages():
    """获取支持的语言列表"""
    return detector.get_supported_languages()

def get_info():
    """获取模型信息"""
    return detector.get_info()
