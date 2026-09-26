import matplotlib.pyplot as plt

# Data from the experiment (R = 0.46 kΩ)
Vz = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11.8, 11.9, 12, 12.2, 12.5, 12.4, 12.5, 12.5, 12.6]
Iz = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.43, 2.17, 4.13, 6.08, 8.26, 10.0, 12.17, 14.0, 16.0]

plt.figure(figsize=(8, 6))
plt.plot(Vz, Iz, marker='o', color='b', linestyle='-', linewidth=1.5, markersize=5)

plt.title('Zener Diode Characteristics (Vz vs Iz)')
plt.xlabel('Vz (Volts)')
plt.ylabel('Iz (mA)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.axvline(x=11.8, color='r', linestyle=':', linewidth=1, label='Breakdown Voltage ≈ 11.8V')
plt.legend()
plt.tight_layout()

plt.savefig('zener_vz_iz_plot.png', dpi=200)
plt.show()