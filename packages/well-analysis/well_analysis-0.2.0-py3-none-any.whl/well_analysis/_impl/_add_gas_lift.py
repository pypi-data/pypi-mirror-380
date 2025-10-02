from._logger import logger
from sixgill.definitions import ModelComponents,Parameters
def add_gas_lift(self,gl_depth,gl_rate):
	A=self
	try:A.gl_depth=gl_depth;A.gl_rate=gl_rate/1000000;A.model.add(ModelComponents.GASLIFTINJECTION,'GLV',context='main_well',parameters={Parameters.GasLiftInjection.TOPMEASUREDDEPTH:A.gl_depth,Parameters.GasLiftInjection.GASRATE:A.gl_rate});A.model.save();logger.info('Gas lift added to the model.')
	except:logger.error('Unable to add gas lift to the model.')