import matplotlib.pyplot as plt
import numpy as np

# 1. Import data
real_data = np.loadtxt('REAL.in', comments='#')
imag_data = np.loadtxt('IMAG.in', comments='#')
ref_data = np.loadtxt('REFRACTIVE.dat', comments='#')
ext_data = np.loadtxt('EXTINCTION.dat', comments='#')

# 2. Top subplot data (Truncated to first 3000 rows to isolate the primary block)
energy_diel = real_data[:3000, 0]
eps1 = real_data[:3000, 1]
eps2 = imag_data[:3000, 1]

# 3. Bottom subplot data (Standard 3000 rows)
energy_ref = ref_data[:, 0]
n = ref_data[:, 1]
k = ext_data[:, 1]

# 4. Create the plots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# --- TOP SUBPLOT: Dielectric Constant ---
ax1.plot(energy_diel, eps1, label='Real Part (ε1)', color='blue', linewidth=2)
ax1.plot(energy_diel, eps2, label='Imaginary Part (ε2)', color='red', linewidth=2)
ax1.set_ylabel('Dielectric Constant', fontsize=12)
ax1.set_title('β-Ag2Te Pure Bulk Optical Properties (PBE)', fontsize=14)
ax1.set_xlim(0, 5)
ax1.legend()
ax1.grid(True, linestyle='--', alpha=0.7)

# --- BOTTOM SUBPLOT: Refractive Index ---
ax2.plot(energy_ref, n, label='Refractive Index (n)', color='green', linewidth=2)
ax2.plot(energy_ref, k, label='Extinction Coefficient (k)', color='purple', linewidth=2)
ax2.set_xlabel('Energy (eV)', fontsize=12)
ax2.set_ylabel('Index / Coefficient', fontsize=12)
ax2.set_xlim(0, 5)
ax2.legend()
ax2.grid(True, linestyle='--', alpha=0.7)

# 5. Save and Show
plt.tight_layout()
plt.savefig('optical_properties_final.png', dpi=300)
plt.show()