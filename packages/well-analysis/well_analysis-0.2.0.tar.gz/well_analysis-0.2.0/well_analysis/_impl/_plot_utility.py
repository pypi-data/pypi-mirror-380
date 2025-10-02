L=False
H=True
F=sorted
B=zip
import pandas as C,matplotlib.pyplot as A,os
os.makedirs('./pipesim-results',exist_ok=H)
def NA_plot(inflowP,inflowQL,outflowP,outflowQL,NA_Point_pressure,NA_Point_LiquidRate,Operating_envelope,gas_well=L,well_name=None):
	Y='tight';X='Pressure at nodal point (ksc)';W='Nodal analysis plot';V='Operation Point';U='Outflow';T='Inflow';R=NA_Point_LiquidRate;Q=NA_Point_pressure;P=outflowQL;O=outflowP;N=inflowQL;M=inflowP;G='r';C=well_name;S=A.figure(1,figsize=(12,8))
	if gas_well==L:D,I=B(*F(B(N,M)));E,J=B(*F(B(P,O)));A.plot(D,I,'b',label=T);A.plot(E,J,G,label=U);A.scatter(R,Q,s=200,c=G,label=V);A.legend(loc=1);S.suptitle(W,fontsize=18);A.xlabel('Stock-tank liquid rate at nodal point (m3/d)',fontsize=14);A.ylabel(X,fontsize=14);A.grid(H,linestyle='--',alpha=.6);A.xlim(left=0);A.ylim(bottom=0);C=C;K=f"./pipesim-plots/{C}-nodal-analysis.png";A.savefig(K,dpi=300,bbox_inches=Y)
	else:D,I=B(*F(B(N,M)));E,J=B(*F(B(P,O)));D=[A*1000000 for A in D];E=[A*1000000 for A in E];A.plot(D,I,'b',label=T);A.plot(E,J,G,label=U);A.scatter(R*1000000,Q,s=200,c=G,label=V);A.legend(loc=1);S.suptitle(W,fontsize=18);A.xlabel('Stock-tank gas rate at nodal point (SCMD)',fontsize=14);A.ylabel(X,fontsize=14);A.grid(H,linestyle='--',alpha=.6);A.xlim(left=0);A.ylim(bottom=0);C=C;K=f"./pipesim-results/{C}-nodal-analysis.png";A.savefig(K,dpi=300,bbox_inches=Y)