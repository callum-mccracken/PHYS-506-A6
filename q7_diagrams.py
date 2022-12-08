"""
Make diagrams for q7
"""
import matplotlib.pyplot as plt
from feynman import Diagram

ew_boson_kwargs = {'style': 'wiggly', 'nwiggles': 5, 'amplitude': 0.02}
higgs_kwargs = {'style': 'dashed', 'arrow': False}

# for some reason the gluons are still wacky
gluon_kwargs = {'style': 'loopy', 'nloops': 2, 'arrow': False, 'amplitude': 0.005}
fermion_kwargs = {'arrow': True}


# initialize figure
fig = plt.figure(figsize=(10.,6.))
ax = fig.add_axes([0,0,1,1], frameon=False)

# initialize diagram
diagram = Diagram(ax)

# set endpoints (same for all diagrams)
u1_top = diagram.vertex(xy=(.1,.90), marker='')
u2_top = diagram.vertex(xy=(.1,.85), marker='')
d1_top = diagram.vertex(xy=(.1,.80), marker='')

u1_btm = diagram.vertex(xy=(.1,.20), marker='')
u2_btm = diagram.vertex(xy=(.1,.15), marker='')
d1_btm = diagram.vertex(xy=(.1,.10), marker='')

u1_mid = diagram.vertex(xy=(.5,.90), marker='.')
u1_mid = diagram.vertex(xy=(.5,.90), marker='.')


# draw incoming fermion lines
q1 = diagram.line(in_top, inter_top, **fermion_kwargs)
q2 = diagram.line(in_bottom, inter_bottom, **fermion_kwargs)

# middle fermion
mid_bos = diagram.line(inter_top, inter_bottom, **ew_boson_kwargs)

upper_photon = diagram.line(inter_top, out_top, **fermion_kwargs)
lower_photon = diagram.line(inter_bottom, out_bottom, **fermion_kwargs)

# set labels
in_top.text(r'$e^-$', fontsize=30)
out_top.text(r'$e^-$', fontsize=30, x=0.05)
in_bottom.text(r'$\mu^-$', fontsize=30)
out_bottom.text(r'$\mu^-$', fontsize=30, x=0.05)


mid_bos.text(r"$\gamma$", fontsize=30, t=0.5)

# plot lines on axis
diagram.plot()

# save figure
fig_title = "q6_channel.png"
plt.savefig(fig_title, dpi=300, transparent=True)
plt.cla(); plt.clf()
plt.close()
