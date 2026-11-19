import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Polygon

pink = "#C40062"
mittelrosa = "#E36A9D"
hellrosa = "#F3B8D0"

A1 = np.array([0.0, 0.0])
A2 = np.array([3.3, -0.7])
A3 = np.array([2.3, 1.55])

punkte = np.array([A1, A2, A3])

fig, axes = plt.subplots(1, 2, figsize=(11, 5))

richtungen = [
    [0, 1, 2],
    [0, 2, 1]
]

for ax, reihenfolge, vorzeichen in zip(axes, richtungen, [1, -1]):

    ax.plot(
        [-0.65, 4.2],
        [0.14, -0.89],
        color="#B5B5B5",
        linewidth=1.2,
        zorder=0
    )

    ax.plot(
        [-0.35, 2.85],
        [-0.42, 2.05],
        color="#B5B5B5",
        linewidth=1.2,
        zorder=0
    )

    ax.plot(
        [0, 0],
        [-2.5, 2.8],
        color="#B5B5B5",
        linewidth=1.2,
        zorder=0
    )

    flaeche = Polygon(
        punkte,
        closed=True,
        facecolor=hellrosa,
        edgecolor=pink,
        linewidth=2.2,
        alpha=0.65,
        zorder=2
    )

    ax.add_patch(flaeche)

    for j in range(3):
        start = punkte[reihenfolge[j]]
        ende = punkte[reihenfolge[(j + 1) % 3]]

        p1 = start + 0.38 * (ende - start)
        p2 = start + 0.65 * (ende - start)

        pfeil = FancyArrowPatch(
            p1,
            p2,
            arrowstyle="-|>",
            mutation_scale=17,
            linewidth=2.5,
            color=pink,
            zorder=5
        )

        ax.add_patch(pfeil)

    ax.scatter(
        punkte[:, 0],
        punkte[:, 1],
        color=pink,
        s=55,
        zorder=6
    )

    ax.text(-0.32, 0.12, r"$A_1$", fontsize=14, fontweight="bold")
    ax.text(3.48, -0.82, r"$A_2$", fontsize=14, fontweight="bold")
    ax.text(2.35, 1.83, r"$A_3$", fontsize=14, fontweight="bold")

    ax.text(4.25, -0.94, "x", fontsize=13)
    ax.text(2.94, 2.07, "y", fontsize=13)
    ax.text(-0.28, 2.85, "z", fontsize=13)

    laenge = 2.15 * vorzeichen

    ax.annotate(
        "",
        xy=(0, laenge),
        xytext=(0, 0),
        arrowprops=dict(
            arrowstyle="-|>",
            color=pink,
            linewidth=3,
            mutation_scale=22
        ),
        zorder=7
    )

    if vorzeichen == 1:
        ax.text(
            0.22, 2.12, "+z",
            color=pink,
            fontsize=15,
            fontweight="bold"
        )
    else:
        ax.text(
            0.22, -2.3, "−z",
            color=pink,
            fontsize=15,
            fontweight="bold"
        )

    ax.set_xlim(-0.8, 4.6)
    ax.set_ylim(-2.65, 3.15)
    ax.set_aspect("equal")
    ax.axis("off")

plt.subplots_adjust(wspace=0.18)

plt.savefig(
    "Orientierung_Vektorprodukt_Dreieck.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()