import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("MOSFET_ID_VDS.csv") 

plt.figure(1, figsize=(10, 6))

for v_gs, group in df.groupby('V_GS (V)'):
    group = group.sort_values('V_DS (V)')
    plt.plot(
        group['V_DS (V)'],
        group['I_D (mA)'],
        marker='o',
        linewidth=2,
        label=f'$V_{{GS}}$ = {v_gs} V'
    )

plt.title('MOSFET Output Characteristics ($I_D$ vs $V_{DS}$)',
          fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Drain-to-Source Voltage, $V_{DS}$ (V)', fontsize=12, labelpad=10)
plt.ylabel('Drain Current, $I_D$ (mA)', fontsize=12, labelpad=10)
plt.legend(title='Gate-Source Voltage', title_fontsize='11',
           loc='upper left', fontsize='10')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('id_vds.png', dpi=300)  