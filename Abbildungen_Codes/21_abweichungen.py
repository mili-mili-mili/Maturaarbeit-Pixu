
import matplotlib.pyplot as plt
import numpy as np

pink_dunkel = "#C40062"
pink_mittel = "#E36A9D"
pink_hell = "#F3B8D0"

versuche = [
    "F1 V1", "F1 V2", "F1 V3",
    "F2 V1", "F2 V2", "F2 V3",
    "F3 V1", "F3 V2", "F3 V3"
]

abweichungen = [
    -4.80, -7.28, -2.77,
    -5.64, -4.95, 6.45,
    -0.18, -9.56, -6.63
]

farben = (
    [pink_dunkel] * 3 +
    [pink_mittel] * 3 +
    ["#A04478"] * 3
)

x = np.arange(len(versuche))

fig, ax = plt.subplots(figsize=(11, 5.8))

ax.axhspan(
    -5, 5,
    color=pink_hell,
    alpha=0.40,
    zorder=0
)

balken = ax.bar(
    x,
    abweichungen,
    color=farben,
    width=0.58,
    zorder=3
)

ax.axhline(
    0,
    color="#777777",
    linewidth=1.1,
    zorder=2
)

ax.axhline(
    5,
    color=pink_mittel,
    linewidth=1,
    linestyle="--",
    alpha=0.6
)

ax.axhline(
    -5,
    color=pink_mittel,
    linewidth=1,
    linestyle="--",
    alpha=0.6
)

for balken, wert in zip(balken, abweichungen):
    xpos = balken.get_x() + balken.get_width() / 2
    beschriftung = f"{wert:+.2f}".replace(".", ",")

    if wert >= 0:
        ypos = wert + 0.35
        va = "bottom"
    else:
        ypos = wert - 0.35
        va = "top"

    ax.text(
        xpos,
        ypos,
        beschriftung,
        ha="center",
        va=va,
        fontsize=10.5,
        color="#333333"
    )

ax.set_xticks(x)
ax.set_xticklabels(versuche, fontsize=11)

ax.set_yticks([-10, -5, 0, 5])
ax.set_yticklabels(["-10 %", "-5 %", "0 %", "5 %"])

ax.set_ylim(-11.8, 9)
ax.set_xlim(-0.7, 8.7)

ax.set_title(
    "Prozentuale Abweichungen der neun Messungen",
    fontsize=16,
    pad=22
)

ax.grid(
    axis="y",
    color="#dddddd",
    linewidth=0.7,
    alpha=0.5,
    zorder=0
)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_color("#cccccc")

ax.tick_params(axis="both", length=0, pad=10)

fig.text(
    0.12,
    0.035,
    "Hellrosa Bereich: Genauigkeitsziel von −5 % bis +5 %. "
    "F = Referenzfläche, V = Versuch",
    fontsize=10,
    color="#666666"
)

plt.subplots_adjust(bottom=0.19, top=0.86)

plt.savefig(
    "prozentuale_abweichungen.png",
    dpi=300,
    bbox_inches="tight",
    facecolor="white"
)

plt.show()
