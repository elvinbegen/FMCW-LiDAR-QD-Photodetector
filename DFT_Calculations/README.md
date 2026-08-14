# Density Functional Theory (DFT) Calculations

This directory contains the computational materials science workflow for modeling Ag2Te. The calculations are executed using VASP to evaluate the structural, electronic, and optical characteristics of the material. The workflow is structured into four sequential stages: initial structural relaxation, state density evaluation, band structure extraction, and optical property calculation. A data alignment process is applied to the optical outputs, with a pending scissor operator correction planned to adjust the fundamental bandgap before utilizing the parameters in device-level simulations.

## Workflow Directories

### 1. `01_Geometry_Optimization`
Contains the input configurations for the structural relaxation of the material. The objective is to determine the geometric ground state of the cell parameters and ionic positions.

### 2. `02_Density_of_States`
Contains the setup for static calculations. The objective is to evaluate the distribution of electronic states across the energy spectrum.

### 3. `03_Band_Structure`
Contains the input files for non-self-consistent calculations. The k-point mesh is configured in line-mode to extract the electronic band structure along designated high-symmetry paths.

### 4. `04_Optical_Properties`
Contains the parameters for calculating frequency-dependent dielectric matrices (`LOPTICS = .TRUE.`). 
*   **Data Processing:** Includes custom Python scripts utilized for resolving dimensional mismatches in the raw optical data arrays and plotting the dielectric functions.
*   **Pending Operation:** The application of a scissor operator is scheduled for the subsequent phase to correct the standard DFT bandgap underestimation present in the current raw optical spectra.
