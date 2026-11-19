import numpy as np
import matplotlib.pyplot as plt

pink = "#C40062"
mittelrosa = "#E36A9D"
hellrosa = "#F3B8D0"

A = np.array([0.2, 5.0])
B = np.array([-1.2, 2.0])
C = np.array([0.8, 0.4])
D = np.array([4.0, 1.2])
E = np.array([3.5, 4.2])

polygon = np.array([A, B, C, D, E, A])

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

ax.fill(
    [A[0], D[0], E[0]],
    [A[1], D[1], E[1]],
    color=pink,
    alpha=0.18
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

ax.plot(
    [A[0], D[0]],
    [A[1], D[1]],
    color=pink,
    linestyle="--",
    linewidth=2
)

punkte = np.array([A, B, C, D, E])

ax.scatter(
    punkte[:, 0],
    punkte[:, 1],
    color=pink,
    s=45,
    zorder=4
)

ax.text(A[0] + 0.08, A[1] + 0.18, "A", fontsize=13)
ax.text(B[0] - 0.28, B[1] - 0.2, "B", fontsize=13)
ax.text(C[0] + 0.08, C[1] - 0.28, "C", fontsize=13)
ax.text(D[0] + 0.08, D[1] - 0.08, "D", fontsize=13)
ax.text(E[0] + 0.08, E[1] + 0.08, "E", fontsize=13)

ax.axhline(0, color="gray", linewidth=1, alpha=0.6)
ax.axvline(0, color="gray", linewidth=1, alpha=0.6)

ax.set_xlim(-2, 5)
ax.set_ylim(-0.5, 5.8)

ax.set_xticks(np.arange(-2, 6, 1))
ax.set_yticks(np.arange(0, 6, 1))

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
plt.savefig("Fuenfeck_Dreieckszerlegung.png", dpi=300, bbox_inches="tight")
plt.show()