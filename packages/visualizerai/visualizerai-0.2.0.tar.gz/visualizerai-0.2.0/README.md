# VisualizerAI

`visualizerai` lets you turn natural language into plots.
It integrates with pandas, matplotlib, and a local Ollama LLM (e.g., LLaMA3.2).

## Quickstart

```python
import pandas as pd
import visualizerai as vai

df = pd.DataFrame({
    "date": pd.date_range("2022-01-01", periods=10),
    "soil_moisture": [0.1,0.15,0.12,0.14,0.13,0.16,0.18,0.20,0.19,0.21],
    "rainfall": [2,3,1,0,5,6,3,2,4,5]
})

# Natural language prompt -> automatic plot
vai.prompt_plot("Show soil_moisture and rainfall on the same graph with labels", df)
```

## License
MIT
