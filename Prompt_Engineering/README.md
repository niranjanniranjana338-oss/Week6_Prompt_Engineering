# Week 6 – Prompt Engineering

## Aim
Explore zero-shot, one-shot, few-shot, role prompting and a structured reasoning/debugging prompt. Generate and compare responses from a pretrained Hugging Face language model.

## Run
1. Open a terminal in this folder.
2. Install dependencies: `python -m pip install -r requirements.txt`
3. Run: `python prompt_engineering.py`
4. The first run downloads `distilgpt2`, so an internet connection is required and model download may take time.
5. Review `dataset/generated_responses.csv` and fill in the comparison/evaluation CSV files.
6. Open `notebook/Week6_Prompt_Engineering.ipynb` in VS Code or Jupyter.

## Prompt types
- Zero-shot: task instructions without examples.
- One-shot: one example is included.
- Few-shot: several examples are included.
- Role prompting: tells the model which role or perspective to use.
- Structured reasoning prompt: asks for a brief explanation and result. Do not treat the model's explanation as guaranteed to be correct.

## Evaluation
Score relevance, clarity and correctness from 1 (low) to 5 (high). Compare two prompt styles on the same task and record which one gave the more useful answer. Try education, customer support, finance, healthcare information or programming tasks. Do not use generated answers as professional medical or financial advice.

## Limitations
`distilgpt2` is a small demonstration model and may produce irrelevant or inaccurate content. The CSV starter rows are templates; run the script and complete the evaluation with your own observations.
