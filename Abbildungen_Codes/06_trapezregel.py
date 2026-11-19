import numpy as np
import matplotlib.pyplot as plt

pink = "#C40062"
pink_hell = "#E36A9D"
pink_sehr_hell = "#F3B8D0"

def f(x):
    return 2 + 0.35 * x + 0.7 * np.sin(0.6 * x)

x = np.linspace(0, 10, 800)
y = f(x)

a = 2
b = 8
n = 5

h = (b - a) / n

x_stuetz = np.linspace(a, b, n + 1)
y_stuetz = f(x_stuetz)

fig, ax = plt.subplots(figsize=(10, 6.5))

for i in range(n):
    ax.fill(
        [
            x_stuetz[i],
            x_stuetz[i],
            x_stuetz[i + 1],
            x_stuetz[i + 1]
        ],
        [
            0,
            y_stuetz[i],
            y_stuetz[i + 1],
            0
        ],
        color=pink_sehr_hell,
        alpha=0.75,
        zorder=1
    )

ax.plot(
    x,
    y,
    color="black",
    linewidth=2.2,
    zorder=2
)

ax.vlines(
    x_stuetz,
    0,
    y_stuetz,
    color=pink_hell,
    linewidth=1.2,
    linestyle="--",
    zorder=3
)

for i in range(n):
    ax.plot(
        [x_stuetz[i], x_stuetz[i + 1]],
        [y_stuetz[i], y_stuetz[i + 1]],
        color=pink,
        linewidth=3.0,
        zorder=4
    )

ax.scatter(
    x_stuetz,
    y_stuetz,
    color=pink,
    edgecolor="white",
    linewidth=0.8,
    s=65,
    zorder=5
)

for i in range(n + 1):
    if i == 0:
        beschriftung = r"$x_0=a$"
    elif i == n:
        beschriftung = rf"$x_{i}=b$"
    else:
        beschriftung = rf"$x_{i}$"

    ax.text(
        x_stuetz[i],
        -0.17,
        beschriftung,
        ha="center",
        va="top",
        fontsize=12,
        color="black"
    )

for i in range(n + 1):
    ax.text(
        x_stuetz[i] + 0.08,
        y_stuetz[i] - 0.22,
        rf"$y_{i}$",
        ha="left",
        va="top",
        fontsize=11,
        color=pink
    )

for i in range(n):
    mitte_x = (x_stuetz[i] + x_stuetz[i + 1]) / 2

    ax.text(
        mitte_x,
        0.65,
        rf"$A_{i+1}$",
        ha="center",
        va="center",
        fontsize=15,
        color=pink
    )

for i in range(n):
    ax.annotate(
        "",
        xy=(x_stuetz[i + 1] - 0.04, -0.52),
        xytext=(x_stuetz[i] + 0.04, -0.52),
        arrowprops=dict(
            arrowstyle="<->",
            color="black",
            linewidth=0.9
        )
    )

    ax.text(
        (x_stuetz[i] + x_stuetz[i + 1]) / 2,
        -0.68,
        r"$h$",
        ha="center",
        va="top",
        fontsize=11
    )

ax.text(
    8.85,
    f(8.85) + 0.42,
    r"$f(x)$",
    fontsize=17,
    color="black"
)

ax.axhline(
    0,
    color="black",
    linewidth=1.3,
    zorder=3
)

ax.axvline(
    0,
    color="black",
    linewidth=1.3,
    zorder=3
)

ax.text(
    9.9,
    -0.18,
    "x",
    fontsize=16,
    ha="right",
    va="top"
)

ax.text(
    -0.15,
    5.8,
    "y",
    fontsize=16,
    ha="right",
    va="top"
)

ax.set_xticks([])
ax.set_yticks([])

for spine in ax.spines.values():
    spine.set_visible(False)

ax.set_xlim(-0.3, 10)
ax.set_ylim(-0.95, 6)

plt.tight_layout()

plt.savefig(
    "../trapezformel_5_trapeze.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()