"""
Lark Language Detection Package
A lightweight language detection library similar to fasttext and Google's implementation.
"""

from .detector import LarkDetector

__version__ = "1.0.0"
__author__ = "Farshore Team"
__all__ = ["LarkDetector"]

# 创建全局实例
detector = LarkDetector()

# 提供便捷函数
def detect(text: str):
    """检测文本语言"""
    return detector.detect(text)

def detect_new(text: str, language_code: str):
    """检测文本语言并判断是否需要LLM"""
    return detector.detect_new(text, language_code)

def get_info():
    """获取模型信息"""
    return detector.get_info()
