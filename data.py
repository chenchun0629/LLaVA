# from llava.model.language_model.qwen.tokenization_qwen import QWenTokenizer


# tokenizer = QWenTokenizer.from_pretrained("/data/jupyter/user/cc/llm_models/Qwen-7B-Chat")
# tokenizer.pad_token_id = tokenizer.eod_id
# tokenizer.bos_token_id = tokenizer.eod_id
# tokenizer.eos_token_id = tokenizer.eod_id

# print(tokenizer)

from pathlib import Path

input_file = Path('/data/jupyter/user/cc/llm_datasets/LLaVA-Visual-Instruction-Tuning/llava_v1_5_mix665k.json')
output_file = Path('/data/jupyter/user/cc/llm_datasets/LLaVA-Visual-Instruction-Tuning/llava_v1_5_mix665k.coco.json')
image_dir = Path('/data/jupyter/user/cc/llm_datasets/LLaVA-Visual-Instruction-Tuning/')

"""
item:
{
    "id": "000000033471",
    "image": "coco/train2017/000000033471.jpg",
    ...
"""

import json

with open(input_file, 'r') as f:
    data = json.load(f)

print(len(data))

path_set = set()

output = []
for item in data:
    image = item.get('image', None)
    if not image:
        output.append(item)
        continue

    image_path = image_dir / image
    if image_path.exists():
        path_set.add(image_path.parent.as_posix())
        output.append(item)
        
print(len(output), "===2")
print(len(path_set), "===3")
print(path_set, "===3")

with open(output_file, 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=4)
    