"""Draws the title-slide network art and the energy-curve diagram into img/. Run from presentation/."""
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
MAROON="#500000"; ROSE="#E3C4C4"; SLATE="#64748B"; NAVY="#1E293B"; GOLD="#C9A227"; PANEL="#F5F1F1"

# 1) Title art: a faint 3D-ish atomic network (right side of the title slide)
rng=np.random.default_rng(3)
pts=[]
for i in range(-4,6):
    for j in range(-3,5):
        for k in range(0,2):
            p=np.array([i+0.5*(j%2), j*0.87, k*0.8])+rng.normal(0,0.09,3)
            pts.append(p)
pts=np.array(pts)
th=np.radians(28); R=np.array([[np.cos(th),-np.sin(th),0],[np.sin(th),np.cos(th),0],[0,0,1]])
P=pts@R.T; x=P[:,0]+0.35*P[:,2]; y=P[:,1]+0.6*P[:,2]; depth=P[:,2]
fig=plt.figure(figsize=(8,7.5),dpi=200); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(-3,5); ax.set_ylim(-3.2,4.3); ax.axis("off")
order=np.argsort(depth)
for a in range(len(P)):
    for b in range(a+1,len(P)):
        d=np.linalg.norm(pts[a]-pts[b])
        if d<1.05:
            ax.plot([x[a],x[b]],[y[a],y[b]],color="#C8CED8",lw=1.2,alpha=0.55,zorder=1)
for a in order:
    big = rng.random()<0.3
    c = ROSE if big else "#D5DCE5"
    s = (260 if big else 150)*(0.7+0.3*depth[a]/1.6)
    ax.scatter(x[a],y[a],s=s,color=c,edgecolor="white",lw=1.5,zorder=2+depth[a],alpha=0.95)
# highlight one atom with its cutoff sphere and a force arrow
cx,cy=1.25,0.55
ax.add_patch(plt.Circle((cx,cy),1.35,fill=False,ls=(0,(4,3)),color=MAROON,lw=1.6,alpha=0.55,zorder=9))
ax.scatter(cx,cy,s=520,color=MAROON,edgecolor="white",lw=2,zorder=10)
ax.add_patch(FancyArrowPatch((cx,cy),(cx+0.95,cy+0.55),arrowstyle="-|>",mutation_scale=22,lw=3,color=GOLD,zorder=11))
fig.savefig("img/title_network.png",transparent=True); plt.close(fig)

# 2) PES diagram: energy vs. bond length with force arrows
r=np.linspace(0.75,2.6,400); De,a,re=4.6,2.2,0.97
E=De*(1-np.exp(-a*(r-re)))**2-De
fig,ax=plt.subplots(figsize=(6.4,4.6),dpi=200)
ax.plot(r,E,color=MAROON,lw=3.2)
ax.set_xlim(0.72,2.6); ax.set_ylim(-5.0,0.4)
for s in ("top","right"): ax.spines[s].set_visible(False)
for s in ("left","bottom"): ax.spines[s].set_color("#94A3B8")
ax.set_xticks([]); ax.set_yticks([])
ax.set_xlabel("atom position  r",color=SLATE,fontsize=15); ax.set_ylabel("energy  E",color=SLATE,fontsize=15)
def Ef(rr): return De*(1-np.exp(-a*(rr-re)))**2-De
def dE(rr): return 2*De*a*np.exp(-a*(rr-re))*(1-np.exp(-a*(rr-re)))
for r0,lab in [(1.5,"stretched"),(0.82,"compressed")]:
    e0=Ef(r0); ax.scatter(r0,e0,s=340,color=NAVY,zorder=5,edgecolor="white",lw=2)
    sl=dE(r0); dx=-np.sign(sl)*0.32
    ax.add_patch(FancyArrowPatch((r0,e0+0.55),(r0+dx,e0+0.55),arrowstyle="-|>",mutation_scale=22,lw=3,color=GOLD))
    ax.text(r0+dx/2,e0+0.85,"F",color=GOLD,fontsize=17,weight="bold",ha="center",style="italic")
    tx=np.linspace(r0-0.22,r0+0.22,2); ax.plot(tx,e0+sl*(tx-r0),color="#94A3B8",lw=1.6,ls="--")
ax.scatter(re,-De,s=340,color=MAROON,zorder=5,edgecolor="white",lw=2)
ax.text(re+0.06,-De-0.05,"  equilibrium: F = 0",color=MAROON,fontsize=13,va="center",weight="bold")
fig.tight_layout(); fig.savefig("img/pes.png",transparent=True); plt.close(fig)
print("ok")
