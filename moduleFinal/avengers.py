import numpy as np
import pandas as pd
from pysentimiento import create_analyzer
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path
import matplotlib.animation as animation

# See https://matplotlib.org/stable/gallery/animation/animated_histogram.html#sphx-glr-gallery-animation-animated-histogram-py

data = pd.read_csv('tweets.csv', sep=",", encoding='cp1252')
all_texts = [x for x in data.text]
analyzer = create_analyzer(task="sentiment", lang="en")
freqs = {"POS" : 0., "NEU" : 0., "NEG" : 0.}

# Fixing bin edges
HIST_BINS = np.linspace(0, 4, 3)

# histogram our data with numpy
n, _ = np.histogram(list(freqs.values()), HIST_BINS)
def prepare_animation(bar_container, freqs, texts):

    def animate(frame_number):
        
        t = next(texts)
        out = analyzer.predict(t)

        freqs[out.output] += 1

        # simulate new freqs.values() coming in
        n, _ = np.histogram(list(freqs.values()), HIST_BINS)
        for count, rect in zip(n, bar_container.patches):
            rect.set_height(count)
        return bar_container.patches
    return animate

fig, ax = plt.subplots()
_, _, bar_container = ax.hist(list(freqs.values()), HIST_BINS, lw=1,
                              ec="yellow", fc="green", alpha=0.5)
ax.set_ylim(top=10000)  # set safe limit to ensure that all data is visible.

ani = animation.FuncAnimation(
    fig, prepare_animation(
        bar_container, freqs, iter(all_texts)
        ), 1000, repeat=False, blit=True)

plt.show()