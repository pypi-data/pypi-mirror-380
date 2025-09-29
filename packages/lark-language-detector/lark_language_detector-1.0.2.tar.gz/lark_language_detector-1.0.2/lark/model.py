import torch
import torch.nn as nn
import torch.nn.functional as F

class LarkModel(nn.Module):
    """Lark 语言检测模型"""
    
    def __init__(self, d_model=256, n_layers=4, n_heads=8, ff=512, 
                 label_size=102, max_len=1024, dtype=torch.float32, dropout=0.1):
        super().__init__()
        self.d_model = d_model
        self.n_layers = n_layers
        self.n_heads = n_heads
        self.ff = ff
        self.label_size = label_size
        self.max_len = max_len
        self.dtype = dtype
        self.dropout = dropout
        
        # 词嵌入层
        self.token_embedding = nn.Embedding(50257, d_model)
        
        # 位置编码
        self.position_embedding = nn.Embedding(max_len, d_model)
        
        # Transformer编码器层
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model,
            nhead=n_heads,
            dim_feedforward=ff,
            dropout=dropout,
            batch_first=True,
            dtype=dtype
        )
        self.transformer_encoder = nn.TransformerEncoder(encoder_layer, num_layers=n_layers)
        
        # 分类头
        self.classifier = nn.Linear(d_model, label_size, dtype=dtype)
        
        # Dropout
        self.dropout_layer = nn.Dropout(dropout)
        
    def forward(self, input_ids, attention_mask, training=True):
        batch_size, seq_len = input_ids.shape
        
        # 词嵌入
        token_embeddings = self.token_embedding(input_ids)
        
        # 位置编码
        positions = torch.arange(seq_len, device=input_ids.device).unsqueeze(0).expand(batch_size, seq_len)
        position_embeddings = self.position_embedding(positions)
        
        # 合并嵌入
        embeddings = token_embeddings + position_embeddings
        
        # 应用注意力掩码
        src_key_padding_mask = ~attention_mask.bool()
        
        # Transformer编码
        if training:
            encoder_output = self.transformer_encoder(embeddings, src_key_padding_mask=src_key_padding_mask)
        else:
            with torch.no_grad():
                encoder_output = self.transformer_encoder(embeddings, src_key_padding_mask=src_key_padding_mask)
        
        # 池化：取第一个token的输出（CLS token）
        pooled_output = encoder_output[:, 0, :]
        
        # Dropout
        if training:
            pooled_output = self.dropout_layer(pooled_output)
        
        # 分类
        logits = self.classifier(pooled_output)
        
        return logits
