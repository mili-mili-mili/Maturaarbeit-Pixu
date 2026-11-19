import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

pink_dunkel = "#C40062"
pink_mittel = "#E36A9D"
pink_hell = "#F3B8D0"

fig, ax = plt.subplots(figsize=(10, 5.5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis("off")

rahmen = FancyBboxPatch(
    (0.4, 0.6), 9.2, 8.8,
    boxstyle="round,pad=0.25",
    linewidth=1.2,
    edgecolor="#dddddd",
    facecolor="white"
)
ax.add_patch(rahmen)

box1 = FancyBboxPatch(
    (1.6, 6.6), 6.8, 2.2,
    boxstyle="round,pad=0.18",
    linewidth=1.5,
    edgecolor=pink_mittel,
    facecolor=pink_hell,
    alpha=0.35
)
ax.add_patch(box1)

box2 = FancyBboxPatch(
    (1.6, 1.2), 6.8, 2.5,
    boxstyle="round,pad=0.18",
    linewidth=1.5,
    edgecolor=pink_mittel,
    facecolor=pink_hell,
    alpha=0.35
)
ax.add_patch(box2)

ax.text(5, 7.95, "Pixu (mBot2)", ha="center", va="center",
        fontsize=19, fontweight="bold", color="#333333")

ax.text(5, 7.15, "Motorencoder und Gyrosensor", ha="center", va="center",
        fontsize=14.5, color="#666666")

ax.text(5, 5.9, "↓", ha="center", va="center",
        fontsize=22, color=pink_dunkel)

ax.text(5, 5.2, "Übertragung der Messwerte über WLAN/TCP",
        ha="center", va="center", fontsize=14.5, color="#666666")

ax.text(5, 4.35, "↓", ha="center", va="center",
        fontsize=22, color=pink_dunkel)

ax.text(5, 2.7, "Laptop – Python", ha="center", va="center",
        fontsize=18, fontweight="bold", color="#333333")

ax.text(5, 1.95, "Positionsberechnung, Trajektorie, Flächeninhalt",
        ha="center", va="center", fontsize=14.5, color="#666666")

plt.tight_layout()
plt.savefig("systemschema.png", dpi=300, bbox_inches="tight")
plt.show()