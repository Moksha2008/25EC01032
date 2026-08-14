import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("Diode_IV_Temperature.csv")
df.columns = df.columns.str.strip()     
print(df.columns)
print(df.shape)

plt.figure(figsize=(8, 6))

temperatures = sorted(df["T (C)"].unique())

for T in temperatures:
    subset = df[df["T (C)"] == T].sort_values("V (V)")
    plt.plot(subset["V (V)"], subset["I (mA)"], marker='o', markersize=3,
             label=f"T = {T}°C")

plt.xlabel("Voltage, V (V)")
plt.ylabel("Current, I (mA)")
plt.title("Diode I–V Characteristics at Different Temperatures")
plt.legend(title="Temperature")
plt.grid(True)
plt.tight_layout()
plt.savefig("diode_IV_temperature.png", dpi=350)
plt.show()