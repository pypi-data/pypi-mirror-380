import matplotlib.pyplot as plt
from .llm import get_plot_code_from_prompt, render_code_safely

def prompt_plot(prompt: str, df, model="llama3.2", host="http://localhost:11434"):
    code = get_plot_code_from_prompt(prompt, model=model, host=host)
    print("Generated code:\n", code)
    env = {"df": df, "vai": __import__("visualizerai"), "plt": plt}
    render_code_safely(code, env)
    plt.show()
    return env
