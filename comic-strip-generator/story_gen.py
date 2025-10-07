# Very simple prompt engineering: split idea into 4 panels
def make_panels(idea: str, tone: str = "funny"):
    # naive split: try to break idea into 4 parts
    sentences = idea.strip().split(".")
    panels = []
    for i in range(4):
        text = sentences[i].strip() if i < len(sentences) else f"Panel {i+1}: {tone} continuation."
        prompt = f"A {tone} comic panel: {text}"
        panels.append({"text": text or f"Panel {i+1}", "image_prompt": prompt})
    return panels
