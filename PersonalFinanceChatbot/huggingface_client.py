from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Directly set your Hugging Face token here (embedded in the code)
hf_token = "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"  # 🔐 Token embedded directly

model_name = "ibm-granite/granite-3.1-2b-instruct"

# Load tokenizer and model with authentication
tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=hf_token)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    use_auth_token=hf_token,
    device_map="auto",
    torch_dtype="auto"
)
model.eval()

# Inference function
def ask_hf(prompt: str) -> str:
    messages = [{"role": "user", "content": prompt}]

    # Apply chat template and move to correct device
    input_tokens = tokenizer.apply_chat_template(
        messages,
        return_tensors="pt",
        add_generation_prompt=True
    ).to(model.device)

    # Generate response
    outputs = model.generate(
        input_ids=input_tokens,
        max_new_tokens=200,
        do_sample=True,
        top_p=0.9
    )

    decoded = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    return decoded[0]

