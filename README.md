# FMCW-LiDAR-QD-Photodetector
# Theoretical Development of Ag2Te Quantum Dot Photodetector for FMCW LiDAR in Autonomous Vehicles

## Project Overview
This repository contains the ongoing research and development of an Ag2Te Quantum Dot (QD) photodetector specifically tailored for Frequency-Modulated Continuous-Wave (FMCW) LiDAR systems. The current phase of the project heavily focuses on theoretical materials modeling, optical component design, and foundational experimental validation. 

System-level Python simulations and signal processing algorithms are outlined in the repository structure and are planned for the next development phase.

## Current Progress & Methodologies

### 1. Computational Materials Science (DFT)
- **Material:** Ag2Te Quantum Dots
- **Framework:** Electronic minimization and optical property calculations are performed using VASP on the TRUBA computing cluster. 
- **Status:** Dielectric constants and basic optical responses have been extracted and visualized (using custom Python scripts and VESTA).

### 2. Optical Simulations (FDTD)
- **Framework:** Lumerical FDTD
- **Objective:** Simulating the optical behavior and absorption characteristics of the modeled QD active layer.
- **Status:** Parameter configuration across Lumerical modules is currently in progress to bridge the gap between DFT outputs and component-level performance.

### 3. Experimental Setup (Michelson Interferometer)
- **Objective:** Building a physical proof-of-concept for FMCW LiDAR principles.
- **Hardware:** Visible-light setup utilizing a 650 nm laser diode, a beam splitter, and a silicon photodiode.
- **Status:** Exact component distance metrics and optical hardware alignment are established to observe interference patterns and validate beat frequency concepts.

## Repository Structure & Roadmap
The repository is structured to eventually house a full system simulation. Directories currently acting as placeholders for future work are marked below.

- `DFT_Calculations/Ag2Te/`: Contains calculation parameters and extracted optical properties.
- `Lumerical_Simulations/QD_PD/`: FDTD simulation files and scripts.
- `Optical_Experiment/Michelson/`: Schematics, alignment metrics, and physical setup documentation.
- `System_Simulation/FMCW/` *(In Progress)*: Python architecture for chirp generation, range estimation, and system noise modeling.
- `Signal_Processing/` *(Planned)*: Advanced signal extraction techniques.

## Future Work
- Integration of the Lumerical detector model into the FMCW simulation environment.
- Completion of the `System_Simulation` scripts to evaluate target detection capabilities mathematically.

