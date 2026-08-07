import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dft = pd.read_csv("MOSFET_ID_VGS.csv") 

target_vds = sorted(dft['V_DS (V)'].unique())[0]
g = dft[dft['V_DS (V)'] == target_vds].sort_values('V_GS (V)')

vgs = g['V_GS (V)'].values
i_d = g['I_D (mA)'].values

gm = np.gradient(i_d, vgs)
peak_idx = np.argmax(gm)

window = 3
lo = max(0, peak_idx - window)
hi = min(len(vgs), peak_idx + window + 1)

slope, intercept = np.polyfit(vgs[lo:hi], i_d[lo:hi], 1)
VT = -intercept / slope

print(f"VDS used for extraction: {target_vds} V")
print(f"Slope = {slope:.4f} mA/V, Intercept = {intercept:.4f} mA")
print(f"Extracted V_T = {VT:.4f} V")

plt.figure(figsize=(8, 6))
plt.plot(vgs, i_d, 'o', label='$I_D$ data')
fit_line = slope * vgs + intercept
plt.plot(vgs, fit_line, '--', label='Linear extrapolation')
plt.axvline(VT, color='r', linestyle=':', label=f'$V_T$ = {VT:.3f} V')
plt.xlabel('$V_{GS}$ (V)')
plt.ylabel('$I_D$ (mA)')
plt.title('Threshold Voltage Extraction (Linear Extrapolation)', fontweight='bold')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('vt_extraction.png', dpi=300)
plt.show()