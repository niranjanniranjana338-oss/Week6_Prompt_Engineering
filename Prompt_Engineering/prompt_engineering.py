import csv
import os


def generate_response(prompt, generator=None):
    """
    Generate a response using the prompt.
    Uses a simple fallback if no model is available.
    """
    if generator is not None:
        try:
            result = generator(
                prompt,
                max_new_tokens=100,
                do_sample=True,
                temperature=0.7,
                truncation=True
            )
            return result[0]["generated_text"]
        except Exception as error:
            return f"Generation error: {error}"

    return (
        "Sample response: This prompt asks the model to "
        "provide a clear and relevant answer. "
        f"Original prompt: {prompt}"
    )


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_path = os.path.join(base_dir, "dataset", "prompts.csv")
    output_path = os.path.join(
        base_dir, "dataset", "generated_responses.csv"
    )

    prompts = []

    if os.path.exists(dataset_path):
        with open(dataset_path, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            prompts = list(reader)
    else:
        print("Dataset file not found:", dataset_path)
        return

    generator = None

    try:
        from transformers import pipeline

        print("Loading the text generation model...")
        generator = pipeline(
            "text-generation",
            model="distilgpt2"
        )
        print("Model loaded successfully.")

    except Exception as error:
        print("Could not load the model:", error)
        print("Using sample responses instead.")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        writer.writerow([
            "prompt_type",
            "task",
            "prompt",
            "generated_response"
        ])

        for row in prompts:
            print("Generating:", row.get("prompt_type", "Unknown"))

            prompt = row.get("prompt", "")
            response = generate_response(prompt, generator)

            writer.writerow([
                row.get("prompt_type", ""),
                row.get("task", ""),
                prompt,
                response
            ])

            print(
                "\n",
                row.get("prompt_type", "Unknown"),
                "=>",
                response,
                "\n"
            )

    print("Saved responses to", output_path)
    print(
        "Evaluate outputs manually in evaluation_results.csv. "
        "Model outputs can be inaccurate."
    )


if __name__ == "__main__":
    main()