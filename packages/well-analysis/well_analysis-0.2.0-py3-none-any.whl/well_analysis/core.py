"""
Core abstraction module for the Well Analysis system.

This module provides a high-level interface for performing
nodal analysis, pressure–temperature (PT) profiling, IPR/VLP
matching, gas lift optimization, and fluid characterization.

All heavy computation and PIPESIM interaction are handled by
the compiled backend located under `_impl`. This abstraction
layer exists for:
    - Documentation and API clarity
    - Public exposure on PyPI
    - Consistency and validation
    - Hidden implementation safety

IMPORTANT: You need to have Pipesim's Python toolkit installed in your system and you the same python interpreter to run the following code.

Guide:
Initially make the object of WELL_ANALYSIS class. Then follow the following instructions:
- add the black oil fluid details (required for further analysis)
- add the IPR
- add gas lift valves (optional)
- match IPR-VLP (IPR is required for this)
- perform PT analysis (get report in form of excel)
- find deepest point of injection
- perform nodal analysis (get plot in form of png)
- perform sensitivity analysis, including gas lift sensitivity (get report in form of excel)
- Bonus: Pipesim models will also be automatically generated corresponding to above settings.

Example
-------
>>>    import pandas as pd

>>>    well1= WELL_ANALYSIS("well1", tubing_dia=2.99, perforation_depth=2800, well_trajectory= pd.DataFrame({"MeasuredDepth":[0, 1100, 2200, 3200], "TrueVerticalDepth":[0, 1000, 2000, 2800]}))

>>>    well1.add_gas_lift(gl_depth=500, gl_rate=5000)

>>>    well1.add_black_oil(q_gas=90000, q_oil=5, q_water=5, api=30, gg=0.7, gas_well=True)

>>>    well1.create_ipr(reservoir_temperature=130, reservoir_pressure=95, liquid_pi=0.5)

>>>    well1.ipr_vlp_matching(thp=30, fbhp=52)

>>>    well1.perform_pt_analysis(study_name="Study 1", thp=30)

>>>    well1.perform_pt_analysis(study_name="Study 2", thp=35)

>>>    well1.perform_pt_analysis(study_name="Study 3", thp=25)

>>>    well1.plot_operating_point()

>>>    well1.install_new_glv(gas_injection_pressure=50, thp=30)

>>>    well1.perform_sensitivity(study_name="Study 1", thp_sensitivity=[1, 10], tubing_sensitivity=[2.44, 3.49], lift_gas_sensitivity=[0, 10000], watercut_sensitivity=[0, 50], GOR_sensitivity=[100, 1000], reservoir_pressure_sensitivity=[100, 80])

>>>    well1.perform_sensitivity(study_name="Study 2", thp_sensitivity=[2, 10], tubing_sensitivity=[2.44, 3.49], lift_gas_sensitivity=[0, 10000], watercut_sensitivity=[0, 50], GOR_sensitivity=[100, 1000], reservoir_pressure_sensitivity=[100, 80])

>>>    well1.perform_sensitivity(study_name="Study 3", thp_sensitivity=[5, 10], tubing_sensitivity=[2.44, 3.49], lift_gas_sensitivity=[0, 10000], watercut_sensitivity=[0, 50], GOR_sensitivity=[100, 1000], reservoir_pressure_sensitivity=[100, 80])
"""

from well_analysis._impl import well_analysis

class WELL_ANALYSIS:
    """
    A high-level abstraction class for Well Performance and Nodal Analysis.

    This class provides an easy-to-use interface for setting up and running
    well models using Schlumberger PIPESIM.

    Parameters
    ----------
    well_name : str, required
        Unique name for the well (e.g., "Well-1").
    tubing_dia : float, required
        Internal tubing diameter in inches.
    perforation_depth : float, required
        Depth (m) where perforations exist.
    packer_depth : float, optional
        Depth (m) of packer installation.
        Defaults to `perforation_depth - 100m` if not provided.
    well_trajectory : str, optional
        Provide the well deviation in form of pandas dataframe (See example above), use the same column names.
        If well trajectory is not provided then well will be assumed as a vertical well.
    tubing_shoe_depth : float, optional
        Tubing shoe depth (m). Defaults to `perforation_depth - 5m`.
    casing_dia : float, default=6.18
        Casing inner diameter (inches).
    casing_shoe_depth : float, optional
        Casing shoe depth (m). Defaults to `perforation_depth + 5m`.

    Notes
    -----
    - Units are assumed **consistent** (all metric).
    - Model is created in **metric** internally.
    - The generated file `<well_name>.pips` is saved in the working directory.

    """

    def __init__(
        self,
        well_name: str,
        tubing_dia: float,
        perforation_depth: float,
        packer_depth: float = None,
        well_trajectory: str = None,
        tubing_shoe_depth: float = None,
        casing_dia: float = 6.18,
        casing_shoe_depth: float = None,
    ):
        """Initialize the well model."""
        self._impl = well_analysis.WELL_ANALYSIS(
            well_name=well_name,
            tubing_dia=tubing_dia,
            perforation_depth=perforation_depth,
            packer_depth=packer_depth,
            well_trajectory=well_trajectory,
            tubing_shoe_depth=tubing_shoe_depth,
            casing_dia=casing_dia,
            casing_shoe_depth=casing_shoe_depth,
        )

    # -------------------------------------------------------------------------
    # Black-Oil Model
    # -------------------------------------------------------------------------
    def add_black_oil(self, q_gas, q_oil, q_water, api, gg, gas_well=False):
        """
        Add a black-oil fluid model to the well. This is necessary method for further analysis.

        Parameters
        ----------
        q_gas : float, required
            Gas production rate (SCMD).
        q_oil : float, required
            Oil production rate (sm3/d).
        q_water : float, required
            Water rate (sm3/d).
        api : float, required
            Oil API gravity.
        gg : float, required
            Gas gravity (relative to air = 1).
        gas_well : bool, default=False
            Indicates if the well is gas-dominated. This is a reservoir characterstic. 

        Returns
        -------
        None
        """
        return self._impl.add_black_oil(q_gas, q_oil, q_water, api, gg, gas_well)

    # -------------------------------------------------------------------------
    # Gas Lift Design
    # -------------------------------------------------------------------------
    def add_gas_lift(self, gl_depth, gl_rate):
        """
        Add a gas lift configuration. This is optional method.

        Parameters
        ----------
        gl_depth : float, required
            Depth (m) at which gas is injected.
        gl_rate : float, required
            Injection gas rate (SCMD).

        Returns
        -------
        None
        """
        return self._impl.add_gas_lift(gl_depth, gl_rate)

    # -------------------------------------------------------------------------
    # IPR Curve
    # -------------------------------------------------------------------------
    def create_ipr(self, reservoir_temperature, reservoir_pressure, liquid_pi, fbhp=None):
        """
        Generate the Inflow Performance Relationship (IPR) curve.

        Parameters
        ----------
        reservoir_temperature : float, required
            Reservoir temperature (°C).
        reservoir_pressure : float, required
            Reservoir pressure (ksc).
        liquid_pi : float, optional
            Productivity index (sm3/d/ksc).
        fbhp : float, optional, optional
            Flowing bottomhole pressure (ksc). Default: None.

        Note: Either provide liquid_pi or fbhp to generate the IPR curve.

        Returns
        -------
        None
        """
        return self._impl.create_ipr(reservoir_temperature, reservoir_pressure, liquid_pi, fbhp)

    # -------------------------------------------------------------------------
    # IPR-VLP Matching
    # -------------------------------------------------------------------------
    def ipr_vlp_matching(self, thp, fbhp):
        """
        Perform IPR–VLP matching to determine stable operating point.

        Parameters
        ----------
        thp : float, required
            Tubing head pressure (ksc).
        fbhp : float, required
            Flowing bottomhole pressure (ksc).

        Returns
        -------
        None
        """
        return self._impl.ipr_vlp_matching(thp, fbhp)

    # -------------------------------------------------------------------------
    # Pressure-Temperature Analysis
    # -------------------------------------------------------------------------
    def perform_pt_analysis(
        self,
        study_name=None,
        thp=None,
        q_gas=None,
        q_oil=None,
        q_water=None,
        api=None,
        gg=None,
        gl_depth=None,
        gl_rate=None,
    ):
        """
        Run a full Pressure–Temperature (PT) analysis for given well conditions.

        Parameters
        ----------
        study_name : str, optional
            Identifier for the study (used as Excel sheet name).
        thp : float, optional
            Tubing head pressure (ksc).
        q_gas : float, optional
            Gas rate (SCMD).
        q_oil : float, optional
            Oil rate (sm3/d).
        q_water : float, optional
            Water rate (sm3/d).
        api : float, optional
            API gravity of oil.
        gg : float, optional
            Gas gravity.
        gl_depth : float, optional
            Depth of gas lift injection (m).
        gl_rate : float, optional
            Gas lift injection rate (SCMD).

        Returns
        -------
        pd.DataFrame
            Dataframe with depth-wise PT profile.

        Also the results will be saved and published in form of excel sheet for furture reference in a dedicated folder
        in same working directory.
        """
        return self._impl.perform_pt_analysis(
            study_name, thp, q_gas, q_oil, q_water, api, gg, gl_depth, gl_rate
        )

    # -------------------------------------------------------------------------
    # Plotting
    # -------------------------------------------------------------------------
    def plot_operating_point(self, thp=None):
        """
        Plot the operating point on the VLP curve.

        Parameters
        ----------
        thp : float, optional
            Tubing head pressure (ksc).

        Returns
        -------
        matplotlib.figure.Figure
            VLP curve with annotated operating point.

        Also the plot will be saved in an dedicated folder inside the working directory in form of PNG file.
        """
        return self._impl.plot_operating_point(thp)

    # -------------------------------------------------------------------------
    # Gas Lift Valve Installation
    # -------------------------------------------------------------------------
    def install_new_glv(self, gas_injection_pressure, thp=None):
        """
        Install a new gas-lift valve at the deepest possible injection point.

        Parameters
        ----------
        gas_injection_pressure : float, required
            Injection gas surface pressure (ksc).
        thp : float, optional, required
            Tubing head pressure (ksc).

        Returns
        -------
        str
            Confirmation message upon successful valve installation along with the installation depth in MD (m).
        """
        return self._impl.install_new_glv(gas_injection_pressure, thp)

    # -------------------------------------------------------------------------
    # Sensitivity Analysis
    # -------------------------------------------------------------------------
    def perform_sensitivity(
        self,
        study_name=None,
        thp_sensitivity=None,
        tubing_sensitivity=None,
        lift_gas_sensitivity=None,
        watercut_sensitivity=None,
        GOR_sensitivity=None,
        reservoir_pressure_sensitivity=None,
    ):
        """
        Perform multi-variable sensitivity analysis.

        Parameters
        ----------
        study_name : str, optional
            Study identifier for output storage.
        thp_sensitivity : list of float, optional (ksc)
            Range of tubing head pressures to evaluate.
        tubing_sensitivity : list of float, optional
            Tubing diameters (in inches).
        lift_gas_sensitivity : list of float, optional
            Gas lift injection rates (SCMD). 
        watercut_sensitivity : list of float, optional
            Watercut percentages (0–100).
        GOR_sensitivity : list of float, optional
            Gas–oil ratios to test (m3/m3).
        reservoir_pressure_sensitivity : list of float, optional
            Reservoir pressures to test (ksc).

        Returns
        -------
        Report of sensitivity analysis will be saved in a excel sheet for future reference in a dedicated folder
        in same workign directory.
        """
        return self._impl.perform_sensitivity(
            study_name,
            thp_sensitivity,
            tubing_sensitivity,
            lift_gas_sensitivity,
            watercut_sensitivity,
            GOR_sensitivity,
            reservoir_pressure_sensitivity,
        )


#Example Usage:

if __name__=="__main__":

    import pandas as pd

    well1= WELL_ANALYSIS("well1", tubing_dia=2.99, perforation_depth=2800, well_trajectory= pd.DataFrame({"MeasuredDepth":[0, 1100, 2200, 3200], "TrueVerticalDepth":[0, 1000, 2000, 2800]}))

    well1.add_gas_lift(gl_depth=500, gl_rate=5000)

    well1.add_black_oil(q_gas=90000, q_oil=5, q_water=5, api=30, gg=0.7, gas_well=True)

    well1.create_ipr(reservoir_temperature=130, reservoir_pressure=95, liquid_pi=0.5)

    well1.ipr_vlp_matching(thp=30, fbhp=52)

    well1.perform_pt_analysis(study_name="Study 1", thp=30)

    well1.perform_pt_analysis(study_name="Study 2", thp=35)

    well1.perform_pt_analysis(study_name="Study 3", thp=25)

    well1.plot_operating_point()

    well1.install_new_glv(gas_injection_pressure=50, thp=30)

    well1.perform_sensitivity(study_name="Study 1", thp_sensitivity=[1, 10], tubing_sensitivity=[2.44, 3.49], lift_gas_sensitivity=[0, 10000], watercut_sensitivity=[0, 50], GOR_sensitivity=[100, 1000], reservoir_pressure_sensitivity=[100, 80])

    well1.perform_sensitivity(study_name="Study 2", thp_sensitivity=[2, 10], tubing_sensitivity=[2.44, 3.49], lift_gas_sensitivity=[0, 10000], watercut_sensitivity=[0, 50], GOR_sensitivity=[100, 1000], reservoir_pressure_sensitivity=[100, 80])

    well1.perform_sensitivity(study_name="Study 3", thp_sensitivity=[5, 10], tubing_sensitivity=[2.44, 3.49], lift_gas_sensitivity=[0, 10000], watercut_sensitivity=[0, 50], GOR_sensitivity=[100, 1000], reservoir_pressure_sensitivity=[100, 80])
