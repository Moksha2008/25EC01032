import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dft = pd.read_csv("MOSFET_ID_VGS.csv") 

fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))

peak_gm = -np.inf
peak_vgs = None

for v_ds, g in dft.groupby('V_DS (V)'):
    g = g.sort_values('V_GS (V)')
    gm = np.gradient(g['I_D (mA)'], g['V_GS (V)'])

    ax[0].plot(g['V_GS (V)'], g['I_D (mA)'], linewidth=2,
               label=f'$V_{{DS}}$ = {v_ds} V')
    ax[1].plot(g['V_GS (V)'], gm, linewidth=2,
               label=f'$V_{{DS}}$ = {v_ds} V')

    if gm.max() > peak_gm:
        peak_gm = gm.max()
        peak_vgs = g['V_GS (V)'].values[np.argmax(gm)]

ax[1].plot(peak_vgs, peak_gm, 'r*', markersize=15,
           label=f'Peak gm @ VGS={peak_vgs:.2f} V')

ax[0].set_title('Transfer characteristics', fontweight='bold')
ax[0].set_xlabel('$V_{GS}$ (V)'); ax[0].set_ylabel('$I_D$ (mA)')
ax[1].set_title('Transconductance $g_m = dI_D/dV_{GS}$', fontweight='bold')
ax[1].set_xlabel('$V_{GS}$ (V)'); ax[1].set_ylabel('$g_m$ (mS)')

for a in ax:
    a.grid(True, linestyle='--', alpha=0.6)
    a.legend(fontsize=9)

plt.tight_layout()
plt.savefig('gm_transfer.png', dpi=300)
plt.show()

print(f"Peak gm = {peak_gm:.4f} mS at VGS = {peak_vgs:.3f} V")