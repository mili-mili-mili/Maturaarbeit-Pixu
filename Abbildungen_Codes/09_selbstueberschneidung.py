import numpy as np
import matplotlib.pyplot as plt

pink = "#C40062"
mittelrosa = "#E36A9D"
hellrosa = "#F3B8D0"

polygon = np.array([
    [6.4, 5.2],
    [6.4, 2.2],
    [5.2, 3.1],
    [7.4, 2.6],
    [6.7, 0.25],
    [1.8, 0.9],
    [2.9, 5.55]
])

geschlossen = np.vstack([polygon, polygon[0]])

t = (6.4 - 5.2) / (7.4 - 5.2)
y_schnitt = 3.1 + t * (2.6 - 3.1)

dreieck = np.array([
    [6.4, 2.2],
    [5.2, 3.1],
    [6.4, y_schnitt]
])

fig, ax = plt.subplots(figsize=(6, 5))

ax.fill(
    polygon[:, 0],
    polygon[:, 1],
    color=hellrosa,
    alpha=0.25
)

ax.fill(
    dreieck[:, 0],
    dreieck[:, 1],
    color=mittelrosa,
    alpha=0.65,
    zorder=2
)

ax.plot(
    geschlossen[:, 0],
    geschlossen[:, 1],
    color=pink,
    linewidth=2.5,
    zorder=3
)

ax.scatter(
    polygon[:, 0],
    polygon[:, 1],
    color=pink,
    s=25,
    zorder=4
)

ax.set_xlim(0, 8)
ax.set_ylim(0, 6)
ax.set_aspect("equal")
ax.axis("off")

plt.tight_layout()
plt.savefig(
    "Selbstueberschneidendes_Polygon.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()