# setup.py
from setuptools import setup, Extension
from Cython.Build import cythonize
import os, glob

# --- Step 1: Collect all implementation .py files ---
impl_files = glob.glob(os.path.join("well_analysis", "_impl", "*.py"))
impl_files = [f for f in impl_files if not f.endswith("__init__.py")]

# --- Step 2: Convert file paths to valid module names ---
# e.g. well_analysis/_impl/_add_black_oil.py → well_analysis._impl._add_black_oil
extensions = [
    Extension(
        os.path.splitext(f)[0].replace(os.path.sep, "."),
        [f]
    )
    for f in impl_files
]

# --- Step 3: Run Cython build ---
setup(
    name="well-analysis",
    ext_modules=cythonize(
        extensions,
        compiler_directives={"language_level": "3"}
    ),
)

# --- Step 4: Clean up intermediate files (optional but recommended) ---
# Delete generated .c and original .py files (keep only __init__.py and .pyd binaries)
for pattern in ["well_analysis/_impl/*.c", "well_analysis/_impl/*.py"]:
    for file in glob.glob(pattern):
        if not file.endswith("__init__.py"):
            try:
                os.remove(file)
            except Exception as e:
                print(f"⚠️ Warning: Could not remove {file}: {e}")
