
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

pink = "#C40062"
tuerkis = "#1AA3A3"

fig, ax = plt.subplots(figsize=(10, 3.5))

x_pos = [0, 1.6, 3.2, 4.8, 6.4, 8.0]

oben = [
    r"$x_1$", r"$x_2$", r"$\cdots$",
    r"$x_{n-1}$", r"$x_n$", r"$x_1$"
]

unten = [
    r"$y_1$", r"$y_2$", r"$\cdots$",
    r"$y_{n-1}$", r"$y_n$", r"$y_1$"
]

for x, label in zip(x_pos, oben):
    ax.text(x, 1.2, label, fontsize=18,
            ha="center", va="center")

for x, label in zip(x_pos, unten):
    ax.text(x, 0.2, label, fontsize=18,
            ha="center", va="center")

for i in [0, 3, 4]:
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

for i in [0, 3, 4]:
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
        label=r"Addition: $x_i y_{i+1}$"
    ),
    Line2D(
        [0], [0],
        color=tuerkis,
        linewidth=2,
        linestyle="--",
        label=r"Subtraktion: $x_{i+1} y_i$"
    )
]

ax.legend(
    handles=legende,
    loc="lower center",
    ncol=2,
    frameon=False,
    fontsize=12,
    handlelength=2.8
)

ax.set_xlim(-0.5, 8.5)
ax.set_ylim(-0.9, 1.6)
ax.axis("off")

plt.tight_layout()

plt.savefig(
    "Shoelace_Illustration_allgemein.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
