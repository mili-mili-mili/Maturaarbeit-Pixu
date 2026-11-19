import numpy as np
import matplotlib.pyplot as plt

pink = "#C40062"
mittelrosa = "#E36A9D"
hellrosa = "#F3B8D0"

radius = 2

winkel_kreis = np.linspace(0, 2 * np.pi, 1000)
x_kreis = radius * np.cos(winkel_kreis)
y_kreis = radius * np.sin(winkel_kreis)

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

for ax, n in zip(axes, [8, 40]):
    winkel = np.linspace(0, 2 * np.pi, n, endpoint=False)

    x = radius * np.cos(winkel)
    y = radius * np.sin(winkel)

    x_geschlossen = np.append(x, x[0])
    y_geschlossen = np.append(y, y[0])

    ax.fill(
        x_geschlossen,
        y_geschlossen,
        color=hellrosa,
        alpha=0.45
    )

    ax.plot(
        x_kreis,
        y_kreis,
        color=mittelrosa,
        linestyle="--",
        linewidth=2.2,
        zorder=2
    )

    ax.plot(
        x_geschlossen,
        y_geschlossen,
        color=pink,
        linewidth=2.5,
        zorder=3
    )

    ax.scatter(
        x,
        y,
        color=pink,
        s=42,
        zorder=4
    )

    ax.set_aspect("equal")
    ax.set_xlim(-2.3, 2.3)
    ax.set_ylim(-2.3, 2.3)
    ax.axis("off")

plt.tight_layout()

plt.savefig(
    "Polygonale_Annaeherung_Kreis.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()