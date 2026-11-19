import numpy as np
import matplotlib.pyplot as plt

pink = "#C40062"
mittelrosa = "#E36A9D"
hellrosa = "#F3B8D0"

A = np.array([0, 5])
B = np.array([-1, 1])
C = np.array([2, 0])
D = np.array([5, 2])

polygon = np.array([A, B, C, D, A])

fig, ax = plt.subplots(figsize=(8, 6))

ax.fill(
    [A[0], B[0], C[0]],
    [A[1], B[1], C[1]],
    color=hellrosa,
    alpha=0.65
)

ax.fill(
    [A[0], C[0], D[0]],
    [A[1], C[1], D[1]],
    color=mittelrosa,
    alpha=0.45
)

ax.plot(
    polygon[:, 0],
    polygon[:, 1],
    color=pink,
    linewidth=2.5
)

ax.plot(
    [A[0], C[0]],
    [A[1], C[1]],
    color=pink,
    linestyle="--",
    linewidth=2
)

punkte = np.array([A, B, C, D])

ax.scatter(
    punkte[:, 0],
    punkte[:, 1],
    color=pink,
    s=45,
    zorder=4
)

ax.text(0.15, 5.25, "A (0, 5)", fontsize=12)
ax.text(-1.85, 1.1, "B (-1, 1)", fontsize=12)
ax.text(2.05, -0.45, "C (2, 0)", fontsize=12)
ax.text(5.1, 2.1, "D (5, 2)", fontsize=12)

ax.axhline(0, color="gray", linewidth=1, alpha=0.6)
ax.axvline(0, color="gray", linewidth=1, alpha=0.6)

ax.set_xlim(-2.5, 6.5)
ax.set_ylim(-1, 6.2)

ax.set_xticks(np.arange(-2, 7, 1))
ax.set_yticks(np.arange(-1, 7, 1))

ax.grid(
    True,
    color="#D9D9D9",
    linewidth=0.7,
    alpha=0.5
)

ax.set_axisbelow(True)
ax.set_aspect("equal")

for spine in ax.spines.values():
    spine.set_visible(False)

plt.tight_layout()

plt.savefig(
    "Viereck_Dreieckszerlegung.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()