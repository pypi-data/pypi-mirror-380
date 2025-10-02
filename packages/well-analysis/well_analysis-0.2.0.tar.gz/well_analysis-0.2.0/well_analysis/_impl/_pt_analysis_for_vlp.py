C=None
B=print
from._logger import logger
from sixgill.definitions import SystemVariables,ProfileVariables,Parameters,Constants
import pandas as J
def _pt_analysis_for_vlp(self,parameters=C,profile_variables=C):
	I='main_well';H=profile_variables;G=parameters;A=self
	try:
		A.system_variables=[SystemVariables.PRESSURE,SystemVariables.TEMPERATURE,SystemVariables.VOLUME_FLOWRATE_LIQUID_STOCKTANK,SystemVariables.VOLUME_FLOWRATE_OIL_STOCKTANK,SystemVariables.VOLUME_FLOWRATE_WATER_STOCKTANK,SystemVariables.VOLUME_FLOWRATE_GAS_STOCKTANK,SystemVariables.GOR_STOCKTANK,SystemVariables.WATER_CUT_STOCKTANK,SystemVariables.VOLUME_FLOWRATE_GAS_STOCKTANK,SystemVariables.WATER_CUT_INSITU,SystemVariables.WELLHEAD_VOLUME_FLOWRATE_FLUID_INSITU,SystemVariables.OUTLET_VOLUME_FLOWRATE_GAS_STOCKTANK,SystemVariables.OUTLET_VOLUME_FLOWRATE_OIL_STOCKTANK,SystemVariables.OUTLET_VOLUME_FLOWRATE_WATER_STOCKTANK,SystemVariables.SYSTEM_OUTLET_TEMPERATURE,SystemVariables.BOTTOM_HOLE_PRESSURE,SystemVariables.OUTLET_GLR_STOCKTANK,SystemVariables.OUTLET_WATER_CUT_STOCKTANK]
		if H is C:A.profile_variables=[ProfileVariables.TEMPERATURE,ProfileVariables.PRESSURE,ProfileVariables.ELEVATION,ProfileVariables.TOTAL_DISTANCE]
		else:A.profile_variables=H
		if G is C:A.parameters={Parameters.PTProfileSimulation.OUTLETPRESSURE:A.thp,Parameters.PTProfileSimulation.GASFLOWRATE:A.q_gas/1000000,Parameters.PTProfileSimulation.FLOWRATETYPE:Constants.FlowRateType.GASFLOWRATE,Parameters.PTProfileSimulation.CALCULATEDVARIABLE:Constants.CalculatedVariable.INLETPRESSURE}
		else:A.parameters=G
		K=A.model.tasks.ptprofilesimulation.run(producer=I,parameters=A.parameters,system_variables=A.system_variables,profile_variables=A.profile_variables);L=A.model.tasks.ptprofilesimulation.validate(producer=I);D=1
		for E in L:B('Issue {}'.format(D));B('Path: {}'.format(E.path));B('Message: {}'.format(E.message));B('Property: {}'.format(E.property_name));D=D+1
		for(N,M)in K.profile.items():F=J.DataFrame.from_dict(M)
		return F.loc[F['BranchEquipment']=='Tub1','Pressure'].values[0],F
	except:logger.error('Trying to run PT-analysis at unfeasible parameters.')