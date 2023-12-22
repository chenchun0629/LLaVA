# from llava.model.language_model.qwen.tokenization_qwen import QWenTokenizer


# tokenizer = QWenTokenizer.from_pretrained("/data/jupyter/user/cc/llm_models/Qwen-7B-Chat")
# tokenizer.pad_token_id = tokenizer.eod_id
# tokenizer.bos_token_id = tokenizer.eod_id
# tokenizer.eos_token_id = tokenizer.eod_id

# print(tokenizer)

# import transformers


# tokenizer_yi = transformers.AutoTokenizer.from_pretrained("/data/jupyter/user/cc/llm_models/Yi-6B-Chat")
# tokenizer_llama = transformers.AutoTokenizer.from_pretrained("/data/jupyter/user/cc/llm_models/llama-2-7b-chat-hf")

# print(tokenizer_yi)

# from deepspeed.ops.zero.offload_optimizer import DeepSpeedZeroOffloadParamConfig

# x = DeepSpeedZeroOffloadParamConfig()

from transformers import ChineseCLIPModel, ChineseCLIPProcessor, CLIPVisionModel, CLIPImageProcessor, CLIPVisionConfig

m = ChineseCLIPModel.from_pretrained('OFA-Sys/chinese-clip-vit-large-patch14-336px')
p = ChineseCLIPProcessor.from_pretrained('OFA-Sys/chinese-clip-vit-large-patch14-336px')

print(m)
print("------------")
print(p)
print("============")