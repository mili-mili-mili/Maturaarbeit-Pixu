import numpy as np
import matplotlib.pyplot as plt

pink = "#C40062"
pink_hell = "#E36A9D"
pink_sehr_hell = "#F3B8D0"

x = np.linspace(-2, 10, 600)
y = 2 + 0.35 * x + 0.7 * np.sin(0.6 * x)

a = 2
b = 8

y_a = 2 + 0.35 * a + 0.7 * np.sin(0.6 * a)
y_b = 2 + 0.35 * b + 0.7 * np.sin(0.6 * b)

fig, ax = plt.subplots(figsize=(9, 6))

ax.plot(
    x,
    y,
    color=pink,
    linewidth=2.5
)

bereich = (x >= a) & (x <= b)

ax.fill_between(
    x[bereich],
    0,
    y[bereich],
    color=pink_sehr_hell,
    alpha=1
)

ax.annotate(
    "",
    xy=(10.25, 0),
    xytext=(-2.2, 0),
    arrowprops=dict(
        arrowstyle="->",
        color="black",
        linewidth=1.2
    )
)

ax.annotate(
    "",
    xy=(0, 6.05),
    xytext=(0, -0.55),
    arrowprops=dict(
        arrowstyle="->",
        color="black",
        linewidth=1.2
    )
)

ax.vlines(
    a,
    0,
    y_a,
    color=pink_hell,
    linestyle="--",
    linewidth=1.5
)

ax.vlines(
    b,
    0,
    y_b,
    color=pink_hell,
    linestyle="--",
    linewidth=1.5
)

ax.text(
    a,
    -0.18,
    "a",
    ha="center",
    va="top",
    fontsize=17,
    color=pink
)

ax.text(
    b,
    -0.18,
    "b",
    ha="center",
    va="top",
    fontsize=17,
    color=pink
)

ax.text(
    (a + b) / 2,
    1.25,
    "A",
    ha="center",
    va="center",
    fontsize=22,
    color=pink
)

ax.text(
    8.9,
    5.2,
    "f(x)",
    fontsize=18,
    color=pink
)

ax.text(
    10.15,
    -0.25,
    "x",
    fontsize=16,
    ha="right",
    va="top"
)

ax.text(
    -0.18,
    5.95,
    "y",
    fontsize=16,
    ha="right",
    va="top"
)

ax.set_xticks([])
ax.set_yticks([])

for spine in ax.spines.values():
    spine.set_visible(False)

ax.set_xlim(-2.25, 10.3)
ax.set_ylim(-0.55, 6.1)

plt.savefig(
    "../integral_1.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()