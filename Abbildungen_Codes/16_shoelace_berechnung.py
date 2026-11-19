import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

pink = "#C40062"
tuerkis = "#1AA3A3"

x_pos = [0, 1.6, 3.2, 4.8, 6.4, 8.0]
x_labels = ["0", "4", "4", "2", "0", "0"]
y_labels = ["0", "0", "3", "1", "3", "0"]

fig, ax = plt.subplots(figsize=(10, 3.8))

for x, label in zip(x_pos, x_labels):
    ax.text(x, 1.2, label, fontsize=18, ha="center", va="center")

for x, label in zip(x_pos, y_labels):
    ax.text(x, 0.2, label, fontsize=18, ha="center", va="center")

for i in range(len(x_pos) - 1):
    ax.annotate(
        "",
        xy=(x_pos[i + 1] - 0.12, 0.32),
        xytext=(x_pos[i] + 0.12, 1.08),
        arrowprops=dict(
            arrowstyle="->",
            color=pink,
            linewidth=2.2
        )
    )

for i in range(len(x_pos) - 1):
    ax.annotate(
        "",
        xy=(x_pos[i] + 0.12, 0.32),
        xytext=(x_pos[i + 1] - 0.12, 1.08),
        arrowprops=dict(
            arrowstyle="->",
            color=tuerkis,
            linewidth=2,
            linestyle="--"
        )
    )

legende = [
    Line2D(
        [0], [0],
        color=pink,
        linewidth=2.2,
        label="Addition: 0·0 + 4·3 + 4·1 + 2·3 + 0·0"
    ),
    Line2D(
        [0], [0],
        color=tuerkis,
        linewidth=2,
        linestyle="--",
        label="Subtraktion: 0·4 + 0·4 + 3·2 + 1·0 + 3·0"
    )
]

ax.legend(
    handles=legende,
    loc="lower center",
    ncol=1,
    frameon=False,
    fontsize=11,
    handlelength=2.8
)

ax.set_xlim(-0.5, 8.5)
ax.set_ylim(-1.1, 1.6)
ax.axis("off")

plt.tight_layout()
plt.savefig("Shoelace_Beispiel_konkav.png", dpi=300, bbox_inches="tight")
plt.show()