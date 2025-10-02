D=None
from._logger import logger
from sixgill.definitions import ModelComponents,Parameters,Constants
def create_ipr(self,reservoir_temperature,reservoir_pressure,liquid_pi,fbhp=D):
	E=liquid_pi;C=1.;B=fbhp;A=self
	try:
		A.reservoir_pressure=reservoir_pressure*.980665+1.01325;A.reservoir_temperature=reservoir_temperature
		if B is not D and E is D:B=B*.980665+1.01325;E=(A.q_oil+A.q_water)/(A.reservoir_pressure-B)
		A.model.add(ModelComponents.COMPLETION,'VertComp1',context='main_well',parameters={Parameters.Completion.TOPMEASUREDDEPTH:A.perforation_depth,Parameters.Completion.FLUIDENTRYTYPE:Constants.CompletionFluidEntry.SINGLEPOINT,Parameters.Completion.GEOMETRYPROFILETYPE:Constants.Orientation.VERTICAL,Parameters.Completion.IPRMODEL:Constants.IPRModels.IPRPIMODEL,Parameters.Completion.RESERVOIRPRESSURE:A.reservoir_pressure,Parameters.IPRPIModel.LIQUIDPI:E,Parameters.IPRPIModel.USEVOGELBELOWBUBBLEPOINT:False,Parameters.Completion.RESERVOIRTEMPERATURE:A.reservoir_temperature,Parameters.Well.ASSOCIATEDBLACKOILFLUID:'wellfluid'})
		if A.gas_well==True:A.model.sim_settings.global_flow_correlation({Parameters.FlowCorrelation.Multiphase.Vertical.CORRELATION:Constants.MultiphaseFlowCorrelation.BakerJardine.GRAY_MODIFIED,Parameters.FlowCorrelation.Multiphase.Vertical.FRICTIONFACTOR:C,Parameters.FlowCorrelation.Multiphase.Vertical.HOLDUPFACTOR:C})
		else:A.model.sim_settings.global_flow_correlation({Parameters.FlowCorrelation.Multiphase.Vertical.CORRELATION:Constants.MultiphaseFlowCorrelation.BakerJardine.DUNSROS,Parameters.FlowCorrelation.Multiphase.Vertical.FRICTIONFACTOR:C,Parameters.FlowCorrelation.Multiphase.Vertical.HOLDUPFACTOR:C})
		logger.info('IPR created with reservoir conditions and fluid properties.')
	except:logger.error('Unable to creater the desired IPR.')