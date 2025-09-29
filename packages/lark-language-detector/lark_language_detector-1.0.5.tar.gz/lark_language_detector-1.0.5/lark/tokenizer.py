import torch
import tiktoken

def batch_tokenize(texts, max_len=1024):
    """
    批量分词函数
    
    Args:
        texts: 文本列表
        max_len: 最大序列长度
        
    Returns:
        input_ids: 分词后的ID张量
        attention_mask: 注意力掩码
    """
    # 使用GPT-2的分词器
    enc = tiktoken.get_encoding("gpt2")
    
    # 分词
    input_ids = []
    for text in texts:
        tokens = enc.encode(text)
        # 截断到最大长度
        if len(tokens) > max_len:
            tokens = tokens[:max_len]
        input_ids.append(tokens)
    
    # 填充到相同长度
    max_seq_len = max(len(ids) for ids in input_ids)
    padded_ids = []
    attention_mask = []
    
    for ids in input_ids:
        # 填充
        padding_length = max_seq_len - len(ids)
        padded = ids + [enc.eot_token] * padding_length  # 使用EOT token作为填充
        padded_ids.append(padded)
        
        # 创建注意力掩码（1表示真实token，0表示填充）
        mask = [1] * len(ids) + [0] * padding_length
        attention_mask.append(mask)
    
    # 转换为张量
    input_ids_tensor = torch.tensor(padded_ids, dtype=torch.long)
    attention_mask_tensor = torch.tensor(attention_mask, dtype=torch.long)
    
    return input_ids_tensor, attention_mask_tensor
