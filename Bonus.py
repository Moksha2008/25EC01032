
import numpy as np
import matplotlib.pyplot as plt

IS = 1e-12
Vt = 0.02585
n_values = [1.0, 1.5, 2.0]

v_d = np.arange(0, 0.8 + 0.01, 0.01)

i_d = {}
for n in n_values:
    i_d[n] = IS * (np.exp(v_d / (n * Vt)) - 1)

plt.figure(1, figsize=(8, 5))
for n in n_values:
    plt.plot(v_d, i_d[n], linewidth=2, label=f'$n$ = {n}')
plt.title('Diode $I_D$-$V_D$ Characteristics (Linear Scale)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Diode Voltage, $V_D$ (V)', fontsize=12, labelpad=10)
plt.ylabel('Diode Current, $I_D$ (A)', fontsize=12, labelpad=10)
plt.legend(title='Ideality Factor', loc='upper left', fontsize='10')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('diode_iv_linear.png', dpi=300)

plt.figure(2, figsize=(8, 5))
for n in n_values:
    plt.semilogy(v_d, i_d[n], linewidth=2, label=f'$n$ = {n}')
plt.title('Diode $I_D$-$V_D$ Characteristics (Log Scale)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Diode Voltage, $V_D$ (V)', fontsize=12, labelpad=10)
plt.ylabel('Diode Current, $I_D$ (A)', fontsize=12, labelpad=10)
plt.legend(title='Ideality Factor', loc='upper left', fontsize='10')
plt.grid(True, which='both', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('diode_iv_log.png', dpi=300)

plt.figure(3, figsize=(8, 5))
for n in n_values:
    g_d = np.gradient(i_d[n], v_d)
    plt.semilogy(v_d, g_d, linewidth=2, label=f'$n$ = {n}')
plt.title('Small-Signal Diode Conductance ($g_d = dI_D/dV_D$)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Diode Voltage, $V_D$ (V)', fontsize=12, labelpad=10)
plt.ylabel('Conductance, $g_d$ (S)', fontsize=12, labelpad=10)
plt.legend(title='Ideality Factor', loc='upper left', fontsize='10')
plt.grid(True, which='both', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('diode_gd.png', dpi=300)

plt.show()
