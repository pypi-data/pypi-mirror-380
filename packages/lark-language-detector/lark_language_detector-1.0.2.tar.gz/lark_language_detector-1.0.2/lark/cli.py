#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lark Language Detection CLI Tool
"""

import argparse
import sys
from . import detect, detect_new, get_info

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="Lark Language Detection CLI")
    subparsers = parser.add_subparsers(dest="command", help="命令")
    
    # detect 命令
    detect_parser = subparsers.add_parser("detect", help="检测文本语言")
    detect_parser.add_argument("text", help="要检测的文本")
    
    # detect-new 命令
    detect_new_parser = subparsers.add_parser("detect-new", help="检测文本语言并判断是否需要LLM")
    detect_new_parser.add_argument("text", help="要检测的文本")
    detect_new_parser.add_argument("language_code", help="期望的语言代码")
    
    # info 命令
    subparsers.add_parser("info", help="显示模型信息")
    
    args = parser.parse_args()
    
    if args.command == "detect":
        result = detect(args.text)
        print(f"检测语言: {result['detected_language']}")
        print(f"置信度: {result['confidence']:.4f}")
        print("Top 5 语言:")
        for lang in result['top_languages']:
            print(f"  {lang['language']}: {lang['confidence']:.4f}")
            
    elif args.command == "detect-new":
        result = detect_new(args.text, args.language_code)
        print(f"检测语言: {result['detected_language']}")
        print(f"期望语言: {args.language_code}")
        print(f"置信度: {result['confidence']:.4f}")
        print(f"是否需要LLM: {result['is_need_llm']}")
        
    elif args.command == "info":
        info = get_info()
        print(f"模型名称: {info['model_name']}")
        print(f"精度: {info['precision']}")
        print(f"设备: {info['device']}")
        print(f"支持语言数量: {info['total_languages']}")
        print(f"前10种语言: {info['supported_languages'][:10]}")
        
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
