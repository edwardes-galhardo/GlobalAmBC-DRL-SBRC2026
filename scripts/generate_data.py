import numpy as np
import pandas as pd

np.random.seed(42)

time = np.arange(0, 100)

# Sem controle → caótico
no_control = 0.55 + 0.15 * np.sin(0.2 * time) + 0.15 * np.random.randn(len(time))
no_control = np.clip(no_control, 0.25, 0.85)

# DRL → mais estável
drl = 0.75 + 0.05 * np.sin(0.1 * time) + 0.03 * np.random.randn(len(time))
drl = np.clip(drl, 0.65, 0.90)

df = pd.DataFrame({
    "time": time,
    "success_no_control": no_control,
    "success_drl": drl
})

df.to_csv("../data/figure3_data.csv", index=False)

print("Dados gerados com sucesso!")