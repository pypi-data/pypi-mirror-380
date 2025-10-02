from._logger import logger
from sixgill.definitions import ModelComponents,Parameters,Constants
from sixgill.definitions import Parameters,SystemVariables,ProfileVariables,Constants
import pandas as A,numpy as H
from scipy.interpolate import interp1d
import math
def z_factor(sg_gas,p,t,A=0,B=0):C=sg_gas;I=709.6-58.7*C;D=170.5+307.3*C;E=120*(A**.9-A**1.6)+15*(B**.5-B**4);F=D-E;J=I*(F/(D+B*(1-B)*E));G=p/J;H=(t+460)/F;K=1-3.52*G/10**(.9813*H)+.274*G**2/10**(.8157*H);return K
def gas_annulus_pressure(depth,surface_pressure,sg_gas,t1,t2):
	C=sg_gas;B=depth;D=200;G=H.linspace(0,B,D);A=[surface_pressure]
	for I in G:
		E=((t2-t1)/B*I+2*t1)/2+460
		if len(A)<2:F=A[-1]
		else:F=(A[-1]+A[-2])/2
		J=z_factor(C,F,E);K=.01877*C*B/D/J/E;A.append(A[-1]*math.e**K)
	return A
def install_new_glv(self,gas_injection_pressure,thp=None):
	J='Elevation';H=gas_injection_pressure;G='GLV';C=thp;A=self
	if C is not None:A.thp=C
	if A.thp>=H:logger.info('Injection not possible.')
	else:
		try:
			D=A.perform_pt_analysis(study_name='internal-use',thp=A.thp,q_gas=A.q_gas,q_oil=A.q_oil,q_water=A.q_water,api=A.api,gg=A.gg,gl_depth=A.gl_depth,gl_rate=0);K=D.loc[D['BranchEquipment']=='Tub1','Pressure'].values[0];C=A.thp;E=D[J].min();F=gas_annulus_pressure(E,H,A.gg,50,A.reservoir_temperature);L=(K-C)/E;M=(F[-1]-F[0])/E;N=(F[0]-C)/(L-M);O=D[J].values;I=D['TotalDistance'].values;P=interp1d(O,I,kind='linear',fill_value='extrapolate');B=float(P(N));B=min(A.packer_depth-50,max(I)-B-50);A.gl_depth=B
			try:A.model.set_value(context=G,parameter=Parameters.GasLiftInjection.TOPMEASUREDDEPTH,value=B);A.model.set_value(context=G,parameter=Parameters.GasLiftInjection.GASRATE,value=A.gl_rate)
			except:A.model.add(ModelComponents.GASLIFTINJECTION,G,context='main_well',parameters={Parameters.GasLiftInjection.TOPMEASUREDDEPTH:B,Parameters.GasLiftInjection.GASRATE:A.gl_rate})
			logger.info(f"New GLV has been installed at depth: {B:.2f} m")
		except:logger.info('Gas injection not possible.')