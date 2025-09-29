import os 
import onnxruntime as ort
import numpy as np
from tokenizers import Tokenizer
from tokenizers.models import WordPiece
from tokenizers.pre_tokenizers import Whitespace
from tokenizers.processors import TemplateProcessing

# Load distilbert file directly
module_dir = os.path.dirname(__file__)  # folder containing this Python file
vocab_path = os.path.join(module_dir, "data", "vocab.txt")

tokenizer_base = Tokenizer(WordPiece(vocab=vocab_path, unk_token="[UNK]"))

# Set pre-tokenization (whitespace split)
tokenizer_base.pre_tokenizer = Whitespace()

# Add special token handling ([CLS], [SEP], [PAD])
tokenizer_base.post_processor = TemplateProcessing(
    single="[CLS] $A [SEP]",
    pair="[CLS] $A [SEP] $B:1 [SEP]:1",
    special_tokens=[
        ("[CLS]", tokenizer_base.token_to_id("[CLS]")),
        ("[SEP]", tokenizer_base.token_to_id("[SEP]")),
    ],
)

def tokenizer(text, padding=True, truncation=True, max_length=128):
    encoded = tokenizer_base.encode(text)
    # input IDs
    input_ids = encoded.ids
    # attention mask (1 for tokens, 0 for padding)
    attention_mask = [1] * len(input_ids)

    if padding:
        # pad IDs
        if len(input_ids) < max_length:
            attention_mask += [0] * (max_length - len(input_ids))
            input_ids += [tokenizer_base.token_to_id("[PAD]")] * (max_length - len(input_ids))
        elif len(input_ids) > max_length and truncation:
            input_ids = input_ids[:max_length]
            attention_mask = attention_mask[:max_length]
    
    input_ids_np = np.array(input_ids, dtype=np.int64)
    attention_mask_np = np.array(attention_mask, dtype=np.int64)

    input_ids_np = np.expand_dims(input_ids_np, axis=0)        # shape (1, seq_len)
    attention_mask_np = np.expand_dims(attention_mask_np, axis=0)  # shape (1, seq_len)

    return {"input_ids": input_ids_np, "attention_mask": attention_mask_np}


