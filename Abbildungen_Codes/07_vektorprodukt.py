import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Arc

pink = "#C40062"
mittelrosa = "#E36A9D"
hellrosa = "#F3B8D0"
sehrhellrosa = "#FCE1EC"

a = np.array([5.0, 0.0])
b = np.array([1.7, 2.6])

O = np.array([0.0, 0.0])
A = a
B = b
C = a + b
H = np.array([b[0], 0.0])

phi = np.degrees(np.arctan2(b[1], b[0]))

fig, ax = plt.subplots(figsize=(9, 5.5))

ax.fill(
    [O[0], A[0], B[0]],
    [O[1], A[1], B[1]],
    color=hellrosa,
    alpha=0.65,
    zorder=1
)

ax.fill(
    [A[0], B[0], C[0]],
    [A[1], B[1], C[1]],
    color=sehrhellrosa,
    alpha=0.8,
    zorder=1
)

punkte = np.array([O, A, C, B, O])

ax.plot(
    punkte[:, 0],
    punkte[:, 1],
    color="black",
    linewidth=1.6,
    zorder=2
)

ax.plot(
    [A[0], B[0]],
    [A[1], B[1]],
    color=mittelrosa,
    linestyle="--",
    linewidth=1.8,
    zorder=3
)

pfeil_a = FancyArrowPatch(
    O, A,
    arrowstyle="-|>",
    mutation_scale=18,
    linewidth=2.5,
    color=pink,
    zorder=5
)

ax.add_patch(pfeil_a)

pfeil_b = FancyArrowPatch(
    O, B,
    arrowstyle="-|>",
    mutation_scale=18,
    linewidth=2.5,
    color=pink,
    zorder=5
)

ax.add_patch(pfeil_b)

ax.plot(
    [B[0], H[0]],
    [B[1], H[1]],
    color="black",
    linestyle="--",
    linewidth=1.4,
    zorder=4
)

r = 0.28

rechter_winkel = Arc(
    H,
    width=2*r,
    height=2*r,
    angle=0,
    theta1=0,
    theta2=90,
    color="black",
    linewidth=1.4,
    zorder=6
)

ax.add_patch(rechter_winkel)

ax.plot(
    H[0] + 0.12,
    H[1] + 0.12,
    marker=".",
    color="black",
    markersize=7,
    zorder=7
)

winkelbogen = Arc(
    O,
    width=1.5,
    height=1.5,
    angle=0,
    theta1=0,
    theta2=phi,
    color="black",
    linewidth=1.4
)

ax.add_patch(winkelbogen)

ax.text(
    2.5, -0.32,
    r"$\vec{a}$",
    fontsize=17,
    ha="center"
)

ax.text(
    0.48, 1.55,
    r"$\vec{b}$",
    fontsize=17,
    ha="center"
)

ax.text(
    H[0] + 0.15, 1.35,
    r"$h$",
    fontsize=16
)

ax.text(
    0.87, 0.32,
    r"$\varphi$",
    fontsize=16
)

ax.set_aspect("equal")
ax.set_xlim(-0.6, 7.4)
ax.set_ylim(-0.65, 3.25)

ax.axis("off")

plt.tight_layout()

plt.savefig(
    "Vektorprodukt_Parallelogramm.png",
    dpi=300,
    bbox_inches="tight",
    facecolor="white"
)

plt.show()