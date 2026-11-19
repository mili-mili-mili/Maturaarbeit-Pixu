import numpy as np
import matplotlib.pyplot as plt

pink = "#C40062"
pink_hell = "#E36A9D"
pink_sehr_hell = "#F3B8D0"

def f(x):
    return 2 + 0.35 * x + 0.7 * np.sin(0.6 * x)

x = np.linspace(-2, 10, 1200)
y = f(x)

a = 2
b = 8

n_werte = [5, 20, 100]

dateinamen = [
    "../rechteckregel_1.png",
    "../rechteckregel_2.png",
    "../rechteckregel_3.png"
]

for n, dateiname in zip(n_werte, dateinamen):

    delta_x = (b - a) / n

    x_grenzen = np.linspace(a, b, n + 1)

    x_mitte = a + (np.arange(n) + 0.5) * delta_x

    hoehen = f(x_mitte)

    fig, ax = plt.subplots(figsize=(9, 6))

    ax.bar(
        x_mitte,
        hoehen,
        width=delta_x,
        align="center",
        color=pink_sehr_hell,
        edgecolor=pink_hell,
        linewidth=1.0,
        zorder=2
    )

    ax.plot(
        x,
        y,
        color=pink,
        linewidth=2.5,
        zorder=5
    )

    ax.annotate(
        "",
        xy=(10.25, 0),
        xytext=(-2.2, 0),
        arrowprops=dict(
            arrowstyle="->",
            color="black",
            linewidth=1.2
        )
    )

    ax.annotate(
        "",
        xy=(0, 6.05),
        xytext=(0, -0.65),
        arrowprops=dict(
            arrowstyle="->",
            color="black",
            linewidth=1.2
        )
    )

    if n == 5:
        beschriftungen = [
            r"$x_0=a$",
            r"$x_1$",
            r"$x_2$",
            r"$x_3$",
            r"$x_4$",
            r"$x_5=b$"
        ]

        for wert, beschriftung in zip(x_grenzen, beschriftungen):
            ax.text(
                wert,
                -0.18,
                beschriftung,
                ha="center",
                va="top",
                fontsize=13,
                color=pink
            )

    else:
        ax.text(
            a,
            -0.18,
            "a",
            ha="center",
            va="top",
            fontsize=17,
            color=pink
        )

        ax.text(
            b,
            -0.18,
            "b",
            ha="center",
            va="top",
            fontsize=17,
            color=pink
        )

    ax.text(
        8.9,
        5.2,
        "f(x)",
        fontsize=18,
        color=pink
    )

    ax.text(
        5,
        1.15,
        f"n = {n}",
        ha="center",
        va="center",
        fontsize=20,
        color=pink
    )

    ax.text(
        10.15,
        -0.27,
        "x",
        fontsize=16,
        ha="right",
        va="top"
    )

    ax.text(
        -0.18,
        5.95,
        "y",
        fontsize=16,
        ha="right",
        va="top"
    )

    ax.set_xticks([])
    ax.set_yticks([])

    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.set_xlim(-2.25, 10.3)
    ax.set_ylim(-0.65, 6.1)

    plt.savefig(
        dateiname,
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()