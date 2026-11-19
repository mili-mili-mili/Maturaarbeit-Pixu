import numpy as np
import matplotlib.pyplot as plt

pink = "#C40062"
mittelrosa = "#E36A9D"
hellrosa = "#F3B8D0"

def f(x):
    return 3.4 - 0.45*x - 0.18*x**2

x0 = 0.8
x1 = 2.4

y0 = f(x0)
y1 = f(x1)

x = np.linspace(0.2, 3.1, 400)
y = f(x)

x_sehne = np.array([x0, x1])
y_sehne = np.array([y0, y1])

fig, ax = plt.subplots(figsize=(8, 5.5))

ax.fill(
    [x0, x0, x1, x1],
    [0, y0, y1, 0],
    color=hellrosa,
    alpha=0.65,
    zorder=1
)

ax.plot(
    x,
    y,
    color="black",
    linewidth=2,
    label=r"$y=f(x)$",
    zorder=3
)

ax.plot(
    x_sehne,
    y_sehne,
    color=pink,
    linewidth=2.5,
    zorder=4
)

ax.vlines(
    [x0, x1],
    0,
    [y0, y1],
    color=mittelrosa,
    linewidth=2,
    zorder=2
)

ax.scatter(
    [x0, x1],
    [y0, y1],
    color=pink,
    s=45,
    zorder=5
)

ax.text(
    x0 - 0.18,
    y0 + 0.18,
    r"$P_0$",
    fontsize=13
)

ax.text(
    x1 + 0.06,
    y1 + 0.12,
    r"$P_1$",
    fontsize=13
)

ax.text(
    x0 - 0.12,
    y0 / 2,
    r"$y_0$",
    fontsize=12,
    horizontalalignment="right"
)

ax.text(
    x1 + 0.10,
    y1 / 2,
    r"$y_1$",
    fontsize=12
)

ax.text(
    x0,
    -0.18,
    r"$x_0$",
    fontsize=12,
    horizontalalignment="center"
)

ax.text(
    x1,
    -0.18,
    r"$x_1$",
    fontsize=12,
    horizontalalignment="center"
)

ax.annotate(
    "",
    xy=(x1, -0.48),
    xytext=(x0, -0.48),
    arrowprops=dict(
        arrowstyle="<->",
        color="black",
        linewidth=1.3
    )
)

ax.text(
    (x0 + x1) / 2,
    -0.68,
    r"$h$",
    fontsize=13,
    horizontalalignment="center"
)

mitte_x = (x0 + x1) / 2
mitte_y = (y0 + y1) / 2

ax.annotate(
    "Sehne",
    xy=(mitte_x, mitte_y),
    xytext=(1.75, 3.15),
    fontsize=12,
    color=pink,
    arrowprops=dict(
        arrowstyle="->",
        color=pink,
        linewidth=1.2
    )
)

ax.text(
    2.65,
    f(2.65) + 0.13,
    r"$y=f(x)$",
    fontsize=12
)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_visible(False)

ax.set_xticks([])
ax.set_yticks([])

ax.annotate(
    "",
    xy=(3.25, 0),
    xytext=(0, 0),
    arrowprops=dict(
        arrowstyle="->",
        color="black",
        linewidth=1.3
    )
)

ax.annotate(
    "",
    xy=(0, 3.8),
    xytext=(0, 0),
    arrowprops=dict(
        arrowstyle="->",
        color="black",
        linewidth=1.3
    )
)

ax.text(3.28, -0.08, r"$x$", fontsize=13)
ax.text(-0.10, 3.82, r"$y$", fontsize=13)

ax.set_xlim(-0.15, 3.45)
ax.set_ylim(-0.85, 4.0)

plt.tight_layout()

plt.savefig(
    "../Trapezformel_einzelnes_Trapez.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()