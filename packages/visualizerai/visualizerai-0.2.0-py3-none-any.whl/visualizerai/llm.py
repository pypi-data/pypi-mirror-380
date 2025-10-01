import json, requests
class OllamaClient:
    def __init__(self, host="http://localhost:11434"):
        self.host = host.rstrip('/')
    def generate(self, prompt, model="llama3.2"):
        payload = {"model": model, "prompt": prompt, "stream": False}
        resp = requests.post(f"{self.host}/api/generate", data=json.dumps(payload))
        resp.raise_for_status()
        data = resp.json()
        if "response" in data: return data["response"]
        if "message" in data and isinstance(data["message"], dict):
            return data["message"].get("content", "")
        return str(data)
def get_plot_code_from_prompt(prompt, model="llama3.2", host="http://localhost:11434"):
    system = (
        "Write runnable Python plotting code.\n"
        "- Only output code.\n"
        "- Use matplotlib or visualizerai.plot_time_series.\n"
        "- Assume DataFrame `df` is available.\n"
    )
    client = OllamaClient(host)
    return client.generate(system + prompt, model=model)
def render_code_safely(code, local_env=None):
    if local_env is None:
        local_env = {}

    # --- Strip Markdown fences completely ---
    if code.strip().startswith("```"):
        lines = code.strip().splitlines()
        # Drop first line (``` or ```python) and last line if it's ```
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        code = "\n".join(lines).strip()

    safe_globals = {"__builtins__": __builtins__}
    exec(code, safe_globals, local_env)
    return local_env


