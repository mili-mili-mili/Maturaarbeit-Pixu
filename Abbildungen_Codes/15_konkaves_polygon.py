import numpy as np
import matplotlib.pyplot as plt

pink = "#C40062"
hellrosa = "#F3B8D0"

A = np.array([0, 0])
B = np.array([4, 0])
C = np.array([4, 3])
D = np.array([2, 1])
E = np.array([0, 3])

punkte = np.array([A, B, C, D, E])
geschlossen = np.vstack([punkte, punkte[0]])

fig, ax = plt.subplots(figsize=(6, 5))

ax.fill(
    punkte[:, 0],
    punkte[:, 1],
    color=hellrosa,
    alpha=0.6
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
    s=40,
    zorder=3
)

ax.text(A[0] - 0.25, A[1] - 0.25, "A(0,0)", fontsize=12)
ax.text(B[0] + 0.05, B[1] - 0.25, "B(4,0)", fontsize=12)
ax.text(C[0] + 0.05, C[1] + 0.05, "C(4,3)", fontsize=12)
ax.text(D[0] + 0.08, D[1] - 0.3, "D(2,1)", fontsize=12)
ax.text(E[0] - 0.85, E[1] + 0.05, "E(0,3)", fontsize=12)

ax.axhline(0, color="gray", linewidth=1, alpha=0.6)
ax.axvline(0, color="gray", linewidth=1, alpha=0.6)

ax.set_xlim(-1, 5)
ax.set_ylim(-0.8, 4)
ax.set_xticks(np.arange(-1, 6, 1))
ax.set_yticks(np.arange(0, 5, 1))

ax.grid(True, color="#D9D9D9", linewidth=0.7, alpha=0.5)
ax.set_axisbelow(True)
ax.set_aspect("equal")

for spine in ax.spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.savefig("Konkaves_Polygon_Beispiel.png", dpi=300, bbox_inches="tight")
plt.show()