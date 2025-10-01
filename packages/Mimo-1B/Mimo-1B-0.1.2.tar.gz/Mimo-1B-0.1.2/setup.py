from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    
    long_description = fh.read()

setup(
name="Mimo-1B",
version="0.1.2",
author="ABDESSEMED Mohamed Redha",
author_email="mohamed.abdessemed@eurocybersecurite.fr",
description=(
"Fine-tuning toolkit for the `deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B` "
"model using QLoRA on macOS systems with limited RAM (~8GB). "
"Includes conversion to GGUF format for usage with Ollama and LM Studio."
),
long_description=long_description,
long_description_content_type="text/markdown",
url="https://github.com/eurocybersecurite/Mimo-1B",
project_urls={
"Documentation": "https://github.com/eurocybersecurite/Mimo-1B#readme",
"Source": "https://github.com/eurocybersecurite/Mimo-1B",
"Bug Tracker": "https://github.com/eurocybersecurite/Mimo-1B/issues",
},
license="MIT",
packages=find_packages(where="."),
include_package_data=True,
install_requires=[
"torch==2.8.0",
"transformers==4.56.2",
"datasets==4.1.1",
"accelerate==1.10.1",
"peft==0.17.1",
"sentencepiece==0.2.1",
"llama-cpp-python",
"huggingface_hub==0.35.1",
"pandas==2.3.2",
"regex>=2025.9.18",
"pyarrow==21.0.0",
"psutil==7.1.0",
"dill==0.4.0",
"xxhash",
"safetensors==0.6.2",
"tokenizers==0.22.1",
],
classifiers=[
"Development Status :: 3 - Alpha",
"Intended Audience :: Science/Research",
"Intended Audience :: Developers",
"Topic :: Scientific/Engineering :: Artificial Intelligence",
"Programming Language :: Python :: 3",
"Programming Language :: Python :: 3.8",
"Programming Language :: Python :: 3.9",
"Programming Language :: Python :: 3.10",
"Programming Language :: Python :: 3.11",
"License :: OSI Approved :: MIT License",
"Operating System :: MacOS :: MacOS X",
"Operating System :: POSIX :: Linux",
],
python_requires=">=3.8",
keywords=[
"LLM",
"QLoRA",
"DeepSeek",
"fine-tuning",
"GGUF",
"Ollama",
"LM Studio",
"macOS",
],
)


entry_points={
    "console_scripts": [
        "mimo=mimo.cli:main",
    ],
}
