# well-analysis

A high-level Python wrapper for **well performance & nodal analysis** built on top of Schlumberger **PIPESIM PTK**.  
It automates model setup, black-oil characterization, IPR/VLP matching, PT profiling, gas-lift design, and sensitivity studies. It is intended for those who are new to Pipesim and Python. 

> **Requires**: PIPESIM Python Toolkit installed. Run your scripts with the same interpreter that ships with PIPESIM (or ensure PTK site-packages are importable).

## Features
- Model setup: Well, Tubing, Casing, Packer, Perforation
- Black-oil fluid definition
- IPR Generation (PI or FBHP-based)
- IPR–VLP Matching
- Pressure–Temperature Profiling
- Nodal Analysis
- Gas-Lift Analysis
- Sensitivity Analysis (Tubing Head Pressure, Tubing Size, Gas-Lift Rate, Water Cut, Gas Oil Ratio, Reservoir Pressure)
- Exports: Excel reports & PNG plots

## Documentation

The core module (core.py) serves as the main abstraction layer and includes:

- Full parameter descriptions and expected units
- Input validation logic
- Return object structure (DataFrames, plots, reports)
- Notes on PIPESIM model generation
- Real-world usage examples

## Installation
```bash
pip install well-analysis
```

## Example Usage
```python
import pandas as pd
from well_analysis import WELL_ANALYSIS

# Step 1: Initialize the well model
well1 = WELL_ANALYSIS(
    well_name="well1",
    tubing_dia=2.99,
    perforation_depth=2800,
    well_trajectory=pd.DataFrame({
        "MeasuredDepth": [0, 1100, 2200, 3200],
        "TrueVerticalDepth": [0, 1000, 2000, 2800]
    })
)

# Step 2: (Optional) Add gas lift configuration
well1.add_gas_lift(gl_depth=500, gl_rate=5000)

# Step 3: Add black-oil fluid properties
well1.add_black_oil(q_gas=90000, q_oil=5, q_water=5, api=30, gg=0.7, gas_well=True)

# Step 4: Create IPR curve
well1.create_ipr(reservoir_temperature=130, reservoir_pressure=95, liquid_pi=0.5)

# Step 5: Perform IPR–VLP matching
well1.ipr_vlp_matching(thp=30, fbhp=52)

# Step 6: Conduct PT analysis (generates Excel report)
well1.perform_pt_analysis(study_name="Study 1", thp=30)

# Step 7: Plot operating point (saves PNG plot)
well1.plot_operating_point()

# Step 8: Install new gas-lift valve
well1.install_new_glv(gas_injection_pressure=50, thp=30)

# Step 9: Perform multi-variable sensitivity study
well1.perform_sensitivity(
    study_name="Study 1",
    thp_sensitivity=[1, 10],
    tubing_sensitivity=[2.44, 3.49],
    lift_gas_sensitivity=[0, 10000],
    watercut_sensitivity=[0, 50],
    GOR_sensitivity=[100, 1000],
    reservoir_pressure_sensitivity=[100, 80]
)