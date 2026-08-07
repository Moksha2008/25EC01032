import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Diode_IV_Temperature.csv")
print(df.columns)

plt.figure(figsize=(10, 6))

for temp, group in df.groupby('T (C)'):
    group = group.sort_values('V (V)')
    plt.plot(
        group['V (V)'],
        group['I (mA)'],
        marker='o',
        markersize=4,
        linewidth=2,
        label=f'T = {temp} $^\\circ$C'
    )

plt.title('Diode I-V Characteristics at Different Temperatures',
          fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Voltage, $V$ (V)', fontsize=12, labelpad=10)
plt.ylabel('Current, $I$ (mA)', fontsize=12, labelpad=10)
plt.yscale('log') 
plt.legend(title='Ambient Temperature', title_fontsize='11',
           loc='upper left', fontsize='10')
plt.grid(True, which='both', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('diode_iv.png', dpi=350, bbox_inches='tight')  
plt.show()