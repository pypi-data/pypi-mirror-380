import importlib.util
import os
import sys
import warnings

# List of modules you want to load dynamically
modules_to_load = [
    "_add_black_oil",
    "_add_gas_lift",
    "_create_ipr",
    "_install_new_glv",
    "_ipr_vlp_matching",
    "_logger",
    "_perform_pt_analysis",
    "_perform_sensitivity",
    "_plot_operating_point",
    "_plot_utility",
    "_pt_analysis_for_vlp",
    "well_analysis"
]

_pkg_dir = os.path.dirname(__file__)

for mod_name in modules_to_load:
    # Match any platform-specific .pyd file
    for file in os.listdir(_pkg_dir):
        if file.startswith(mod_name) and file.endswith(".pyd"):
            full_path = os.path.join(_pkg_dir, file)
            try:
                spec = importlib.util.spec_from_file_location(f"well_analysis._impl.{mod_name}", full_path)
                module = importlib.util.module_from_spec(spec)
                sys.modules[f"well_analysis._impl.{mod_name}"] = module
                spec.loader.exec_module(module)
                globals()[mod_name] = module
            except Exception as e:
                warnings.warn(f"⚠️ Failed to import {mod_name}: {e}")
            break
