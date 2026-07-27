import requests

# 🔪 Split long text into chunks
def split_text(text, size=800):
    return [text[i:i+size] for i in range(0, len(text), size)]

# 🧠 Summarize each chunk
def summarize_chunk(chunk):
    prompt = f"""
Summarize the following text into meaningful structured bullet points.

Rules:
- Combine similar ideas
- Avoid repetition
- Do NOT split sentence-by-sentence
- Extract only important information
- Keep it concise and clear
- Each bullet should represent a key idea
- Only bullet points (no extra sentences)
- Do NOT write any introduction

Text:
{chunk}

Bullet Points:
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()["response"]

    # 🔥 Ensure clean bullet formatting
    result = result.replace("•", "\n•")

    return result.strip()

# 🚀 Combine all summaries
def summarize_text(text):
    chunks = split_text(text)
    final_summary = ""

    for chunk in chunks:
        summary = summarize_chunk(chunk)
        final_summary += summary + "\n"

    return final_summary.strip()