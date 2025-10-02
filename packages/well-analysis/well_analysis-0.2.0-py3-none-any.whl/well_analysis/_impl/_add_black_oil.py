from._logger import logger
from sixgill.definitions import ModelComponents,Parameters
def add_black_oil(self,q_gas,q_oil,q_water,api,gg,gas_well=False):
	E='wellfluid';D=q_water;C=q_gas;B=q_oil;A=self
	try:
		A.q_gas=C;A.q_water=D
		if B==0:F=9.99*10**9/35.4*6.29;B=C/F;A.q_oil=B
		else:A.q_oil=B
		A.gas_well=gas_well;A.api=api;A.gg=gg;A.gor=C/B;A.wc=D/(D+B)*100;A.model.add(ModelComponents.BLACKOILFLUID,E,parameters={Parameters.BlackOilFluid.GOR:A.gor,Parameters.BlackOilFluid.WATERCUT:A.wc,Parameters.BlackOilFluid.API:A.api,Parameters.BlackOilFluid.GASSPECIFICGRAVITY:A.gg});A.model.set_value(Well='main_well',parameter=Parameters.Well.ASSOCIATEDBLACKOILFLUID,value=E);A.model.save();logger.info('Black oil fluid added to the model.')
	except:logger.error('Unable to add the black oil properties.')