import numpy as np
import matplotlib.pyplot as plt

pink = "#C40062"
mittelrosa = "#E36A9D"
hellrosa = "#F3B8D0"

konvex = np.array([
    [0.8, 0.8],
    [3.6, 0.7],
    [4.4, 2.6],
    [2.4, 4.1],
    [0.5, 2.8]
])

konkav = np.array([
    [0.5, 0.8],
    [4.4, 0.8],
    [4.4, 4.0],
    [2.4, 2.1],
    [0.5, 4.0]
])

fig, axes = plt.subplots(1, 2, figsize=(9, 4.5))

polygone = [konvex, konkav]

for ax, punkte in zip(axes, polygone):
    geschlossen = np.vstack([punkte, punkte[0]])

    ax.fill(
        punkte[:, 0],
        punkte[:, 1],
        color=hellrosa,
        alpha=0.65
    )

    ax.plot(
        geschlossen[:, 0],
        geschlossen[:, 1],
        color=pink,
        linewidth=2.5
    )

    ax.scatter(
        punkte[:, 0],
        punkte[:, 1],
        color=pink,
        s=35,
        zorder=3
    )

    ax.set_xlim(0, 5)
    ax.set_ylim(0, 4.8)
    ax.set_aspect("equal")
    ax.axis("off")

plt.tight_layout()
plt.savefig("../Konvexe_und_konkave_Polygone.png", dpi=300, bbox_inches="tight")
plt.show()