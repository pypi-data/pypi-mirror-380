R=range
from._logger import logger
from sixgill.definitions import ModelComponents,Parameters,Constants
from scipy.optimize import minimize
class EarlyStopException(Exception):0
def ipr_vlp_matching(self,thp,fbhp):
	U='VertComp1';T='Elevation';Q='params';L=fbhp;K='diff';J=True;B=1.;A=self
	try:
		A.thp=thp*.980665+1.01325;A.fbhp=L*.980665+1.01325;E={}
		if A.gas_well==J:
			C={0:{Parameters.FlowCorrelation.Multiphase.Vertical.CORRELATION:Constants.MultiphaseFlowCorrelation.BakerJardine.GRAY_MODIFIED,Parameters.FlowCorrelation.Multiphase.Vertical.FRICTIONFACTOR:B,Parameters.FlowCorrelation.Multiphase.Vertical.HOLDUPFACTOR:B},1:{Parameters.FlowCorrelation.Multiphase.Vertical.CORRELATION:Constants.MultiphaseFlowCorrelation.BakerJardine.GRAY_ORIGINAL,Parameters.FlowCorrelation.Multiphase.Vertical.FRICTIONFACTOR:B,Parameters.FlowCorrelation.Multiphase.Vertical.HOLDUPFACTOR:B}}
			for G in C.keys():A.model.sim_settings.global_flow_correlation(C[G]);E[G],S=A._pt_analysis_for_vlp()
			D=[]
			for M in R(len(E)):D.append((E[M]-L)**2)
			F=C[D.index(min(D))];A.model.sim_settings.global_flow_correlation(F)
		else:
			C={0:{Parameters.FlowCorrelation.Multiphase.Vertical.CORRELATION:Constants.MultiphaseFlowCorrelation.BakerJardine.DUNSROS,Parameters.FlowCorrelation.Multiphase.Vertical.FRICTIONFACTOR:B,Parameters.FlowCorrelation.Multiphase.Vertical.HOLDUPFACTOR:B},1:{Parameters.FlowCorrelation.Multiphase.Vertical.CORRELATION:Constants.MultiphaseFlowCorrelation.BakerJardine.HAGEDORNBROWN,Parameters.FlowCorrelation.Multiphase.Vertical.FRICTIONFACTOR:B,Parameters.FlowCorrelation.Multiphase.Vertical.HOLDUPFACTOR:B}}
			for G in C.keys():A.model.sim_settings.global_flow_correlation(C[G]);E[G],S=A._pt_analysis_for_vlp()
			D=[]
			for M in R(len(E)):D.append((E[M]-L)**2)
			F=C[D.index(min(D))];A.model.sim_settings.global_flow_correlation(F)
		A.model.sim_settings.global_flow_correlation(F);S,N=A._pt_analysis_for_vlp();A.model.save();V=N[N['BranchEquipment']=='Tub1'].index[0];I=N.loc[V:].copy().reset_index(drop=J);I=I.sort_values(by=T,ascending=J).reset_index(drop=J);I['dZ']=I[T].diff().fillna(0).abs();H={K:float('inf'),Q:None}
		def W(factors):
			C,D=factors;E={Parameters.FlowCorrelation.Multiphase.Vertical.CORRELATION:F[Parameters.FlowCorrelation.Multiphase.Vertical.CORRELATION],Parameters.FlowCorrelation.Multiphase.Vertical.FRICTIONFACTOR:D,Parameters.FlowCorrelation.Multiphase.Vertical.HOLDUPFACTOR:C};A.model.sim_settings.global_flow_correlation(E);G,I=A._pt_analysis_for_vlp();B=abs(G-A.fbhp)
			if B<H[K]:H[K]=B;H[Q]=C,D
			if B<=.005*A.fbhp:raise EarlyStopException
			return B
		X=[(.1,1.9),(.8,1.2)];Y=[B,B]
		try:Z=minimize(W,Y,bounds=X,method='L-BFGS-B');O,P=Z.x
		except EarlyStopException:O,P=H[Q];logger.info('Optimization stopped early (tolerance met).')
		a={Parameters.FlowCorrelation.Multiphase.Vertical.CORRELATION:F[Parameters.FlowCorrelation.Multiphase.Vertical.CORRELATION],Parameters.FlowCorrelation.Multiphase.Vertical.FRICTIONFACTOR:P,Parameters.FlowCorrelation.Multiphase.Vertical.HOLDUPFACTOR:O};A.model.sim_settings.global_flow_correlation(a);logger.info(f"Optimized Elevation Factor: {O:.4f}");logger.info(f"Optimized Friction Factor:  {P:.4f}");logger.info(f"Achieved Error: {H[K]:.4f} (Target: {A.fbhp:.2f})");A.model.save();logger.info('IPR VLP matching completed and model saved.');b=(A.q_water+A.q_oil)/(1-.2*A.fbhp/A.reservoir_pressure-.8*(A.fbhp/A.reservoir_pressure)**2);A.model.set_value(context=U,parameter=Parameters.Completion.IPRMODEL,value=Constants.IPRModels.IPRVOGEL);A.model.set_value(context=U,parameter=Parameters.IPRVogel.ABSOLUTEOPENFLOWPOTENTIAL,value=b);logger.info("Updated model's PI as per the FBHP and flow rates.");A.model.save()
	except:logger.error('IPR-VLP matching failed!')