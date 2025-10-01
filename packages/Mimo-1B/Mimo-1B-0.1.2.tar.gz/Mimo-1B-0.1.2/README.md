# Mimo LLM Project - Fine-tuning and GGUF Export

This project provides the necessary scripts and instructions to fine-tune the `deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B` model using QLoRA on a macOS system with limited RAM (~8GB), convert it to the GGUF format, and make it ready for use with Ollama and LM Studio.

## Objective

*   **Base Model**: `deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B` from Hugging Face.
*   **Fine-tuning Method**: QLoRA for efficient adaptation on low-resource hardware.
*   **Dataset**: `yahma/alpaca-cleaned` (public text dataset).
*   **RAM Optimization**: Tuned for ~8GB RAM.
*   **Output Format**: GGUF (quantized 4-bit or 8-bit).
*   **Final Model Name**: Mimo
*   **Attribution**: "Créé par ABDESSEMED Mohamed Redha"
*   **Compatibility**: Ollama and LM Studio.

## Setup Instructions

1.  **Create a Python virtual environment (recommended)**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    *Note: Ensure you have the correct PyTorch version installed for your macOS system (CPU or Metal/MPS for Apple Silicon). Refer to the official PyTorch website for installation instructions.*
    Or ```pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```
For Apple Silicon (MPS) : ```pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```


## Fine-tuning (QLoRA)

The `train_qlora.py` script handles the fine-tuning process. It loads the base model, applies 4-bit quantization and QLoRA, and trains on the specified dataset.

*   **To start training**:
    ```bash
    python train_qlora.py
    ```
*   **Output**: The fine-tuned model adapters will be saved in the `outputs/mimo-qlora` directory.
*   **RAM Optimization**: The script is configured with `per_device_train_batch_size=1` and `gradient_accumulation_steps=8` to manage memory usage. `max_steps` is set to 100 for a quick example; adjust as needed for longer training. `gradient_checkpointing=True` is also enabled for further memory savings.

## Conversion to GGUF

The `export_to_gguf.py` script first merges the QLoRA adapters into the base model and saves it in Hugging Face format. It then provides instructions on how to convert this merged model into the GGUF format using the `llama.cpp` conversion tools.

1.  **Run the export script**:
    ```bash
    python export_to_gguf.py
    ```
    This will save the merged Hugging Face model in `gguf_model/merged_hf_model/` and print instructions for the GGUF conversion.

2.  **Convert to GGUF using `llama.cpp`**:
    Follow these steps after running `export_to_gguf.py`:
    *   Ensure you have `llama-cpp-python` installed:
        ```bash
        pip install llama-cpp-python
        ```
    *   Navigate to your `llama.cpp` directory (you might need to clone it from GitHub if you don't have it).
    *   Run the `convert.py` script from `llama.cpp`, pointing it to your saved Hugging Face model directory and specifying the desired quantization type.

    **Example command**:
    ```bash
    # Assuming you are in the llama.cpp directory and your merged model is at /Users/mohamed/Downloads/mac_ai_project/gguf_model/merged_hf_model
    # And you want to quantize to 4-bit (q4_0)
    python convert.py /Users/mohamed/Downloads/mac_ai_project/gguf_model/merged_hf_model --outfile /Users/mohamed/Downloads/mac_ai_project/gguf_model/Mimo.gguf --outtype q4_0
    ```
    *   You can choose different quantization types like `q8_0` for 8-bit, `f16` for float16, etc. `q4_0` is a good balance for 4-bit.

*   **Output**: The final GGUF model will be saved as `gguf_model/Mimo.gguf`.

## Usage

### Ollama

1.  **Create a `Modelfile`**:
    Create a file named `Modelfile` (no extension) in the same directory as your `Mimo.gguf` file with the following content:

    ```
    FROM ./Mimo.gguf

    TEMPLATE """{{ .System }}
    {{- if .Prompt }}
    USER: {{ .Prompt }}
    ASSISTANT: {{ .Response }}
    {{- end }}"""

    PARAMETER stop "USER:"
    PARAMETER stop "ASSISTANT:"
    PARAMETER temperature 0.7
    PARAMETER top_k 40
    PARAMETER top_p 0.9
    PARAMETER num_ctx 2048
    PARAMETER repeat_penalty 1.1
    ```
    *Adjust `num_ctx` and other parameters as needed.*

2.  **Import into Ollama**:
    Navigate to the directory containing `Mimo.gguf` and your `Modelfile` in your terminal, then run:
    ```bash
    ollama create mimo -f ./Modelfile
    ```
    You can then interact with the model using `ollama run mimo`.

### LM Studio

1.  Open LM Studio.
2.  Go to the "Local Server" tab or the "AI Models" tab.
3.  Click the folder icon to browse for models.
4.  Navigate to the `gguf_model/` directory and select `Mimo.gguf`.
5.  The model should load, and you can start chatting.

## Attribution

This model, **Mimo**, was created by ABDESSEMED Mohamed Redha.

---
*Modèle Mimo — Créé par ABDESSEMED Mohamed Redha*
