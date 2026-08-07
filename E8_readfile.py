import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("MOSFET_ID_VDS.csv") 

plt.figure(2, figsize=(10, 6))

gd_data = {}

for v_gs, group in df.groupby('V_GS (V)'):
    group = group.sort_values('V_DS (V)')
    v_ds = group['V_DS (V)']
    i_d = group['I_D (mA)']

    gd = np.gradient(i_d, v_ds)
    gd_data[v_gs] = (v_ds.values, gd)

    plt.plot(v_ds, gd, marker='s', linestyle='--', linewidth=2,
              label=f'$V_{{GS}}$ = {v_gs} V')

plt.title('Differential Output Conductance $g_d = dI_D/dV_{DS}$',
          fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Drain-to-Source Voltage, $V_{DS}$ (V)', fontsize=12, labelpad=10)
plt.ylabel('Conductance, $g_d$ (mS)', fontsize=12, labelpad=10)
plt.legend(title='Gate-Source Voltage', loc='upper right', fontsize='10')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('gd_vds.png', dpi=300)
plt.show()

highest_vgs = max(gd_data.keys())
v_ds_h, gd_h = gd_data[highest_vgs]
gd_sat_mS = gd_h[-1]
gd_sat_S = gd_sat_mS * 1e-3
ro_ohm = 1 / gd_sat_S
ro_kohm = ro_ohm / 1e3

print(f"At VGS = {highest_vgs} V, gd (saturation) = {gd_sat_mS:.4f} mS")
print(f"ro = 1/gd = {ro_kohm:.3f} kOhm")