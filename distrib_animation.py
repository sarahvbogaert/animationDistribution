"""
This script draws an animation with the histograms of 4 distributions (uniform distribution, 2 normal distributions with different standard deviation, gamma distribution) where the size of the sample progressively increases from n = 1 to n = 500.
"""

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np



# function called to draw each frame of the animation
def update(curr):
    if curr == 0:
        curr = n
    for i, x in enumerate(xs):
        ax_ = axs[i]
        ax_.cla()
        ax_.hist(x[:curr], bins=bins[i], color="blue")
        ax_.set_xlim(*xlim[i])
        ax_.set_ylim(*ylim)
        ax_.set_title(titles[i])
    fig.tight_layout()
    plt.subplots_adjust(top=0.85)
    fig.suptitle("n = {}".format(curr), fontsize=16, fontweight="bold")

n = 500
x1 = np.random.random(size=n)
x2 = np.random.randn(n)
x3 = np.random.gamma(2, size=n)
x4 = np.random.normal(scale=2, size=n)
xs = [x1, x2, x3, x4]
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)
axs = [ax1, ax2, ax3, ax4]
bins1 = np.arange(0, 1, 0.05)
bins2 = np.arange(-6, 6, 0.5)
bins3 = np.arange(0, 10, 0.5)
bins4 = np.arange(-6, 6, 0.5)
bins = [bins1, bins2, bins3, bins4]
xlim = [(0,1), (-6,6), (0,10), (-6, 6)]
ylim = [0, 100]
titles = ["Uniform", "Normal ($\sigma = 1$)", "Gamma", "Normal ($\sigma = 2$)"]
a = animation.FuncAnimation(fig, update, interval = 100, frames=n)
writervideo = animation.FFMpegWriter(fps=50)
a.save('distrib_animation.mp4', writer=writervideo)
plt.close()
