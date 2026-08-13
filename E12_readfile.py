import pandas as pd
import matplotlib.pyplot as plt

def load_ngspice(path):
    df = pd.read_csv(path, sep=r'\s+', header=None,
                      names=['x1', 'v_d', 'x2', 'i_vds', 'x3', 'v_g'])
    df['i_vds'] = -df['i_vds'] * 1e3 
    return df[['v_d', 'i_vds', 'v_g']]

def plot_one(df, title, filename):
    plt.figure(figsize=(8, 6))
    for vgs, group in df.groupby('v_g'):
        plt.plot(group['v_d'], group['i_vds'], linewidth=2,
                  label=f'$V_{{GS}}$ = {vgs:.0f} V')
    plt.title(title, fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Drain-to-Source Voltage, $V_{DS}$ (V)', fontsize=12, labelpad=10)
    plt.ylabel('Drain Current, $I_D$ (mA)', fontsize=12, labelpad=10)
    plt.legend(title='Gate-Source Voltage', title_fontsize='11', fontsize='10')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig(filename, dpi=350, bbox_inches='tight')
    print(f"Saved {filename}")

df1 = load_ngspice('level1_output.csv')
df3 = load_ngspice('level3_output.csv')

plot_one(df1, 'MOSFET $I_D$-$V_{DS}$ (SPICE Level 1)', 'e12a_level1.png')
plot_one(df3, 'MOSFET $I_D$-$V_{DS}$ (SPICE Level 3)', 'e12b_level3.png')

plt.show()