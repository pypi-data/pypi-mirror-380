"""Generate weighting scheme comparison grid for documentation.

This script recreates the weighting_schemes_grid.png asset while sharing the
Y-axis for comparable visual scaling across scenarios. It relies on the
portfolio sizing helper from the core package to ensure logic parity with the
application.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from cc_liquid.portfolio import weights_from_ranks


def _build_rank_scores(universe_size: int) -> dict[str, float]:
    """Create monotonically decreasing scores for a synthetic ranking."""

    ranks = np.arange(universe_size, 0, -1, dtype=float)
    # Scale highest score to 1.0 and tail near zero for smooth taper.
    scores = ranks / ranks.max()
    return {f"#{i}": score for i, score in enumerate(scores, start=1)}


def _render_axis(ax, title: str, ids: list[str], weights_equal, weights_p05, weights_p15):
    x = np.arange(len(ids))

    ax.bar(x - 0.2, weights_equal, width=0.2, label="Equal Weight", color="#2E7D32")
    ax.bar(x, weights_p05, width=0.2, label="Rank Power 0.5", color="#1976D2")
    ax.bar(x + 0.2, weights_p15, width=0.2, label="Rank Power 1.5", color="#E65100")

    ax.set_title(title, fontsize=11, fontweight='bold')
    
    # Show every 5th label for readability, plus first and last
    step = 5 if len(ids) > 20 else 3 if len(ids) > 10 else 2
    tick_indices = list(range(0, len(ids), step))
    if (len(ids) - 1) not in tick_indices:
        tick_indices.append(len(ids) - 1)
    
    ax.set_xticks(tick_indices)
    ax.set_xticklabels([ids[i] for i in tick_indices], fontsize=8)
    ax.set_xlabel("Position Rank", fontsize=9)
    ax.set_ylabel("Weight (% of NAV)", fontsize=9)
    ax.grid(axis="y", linestyle="--", linewidth=0.4, alpha=0.6)
    
    # Add top position percentages for context
    for i in range(min(3, len(ids))):
        if i < len(weights_p15):
            ax.text(i + 0.2, weights_p15[i] + 0.1, f'{weights_p15[i]:.1f}%', 
                   ha='center', fontsize=7, color='#E65100')


def generate_grid(output_path: Path) -> None:
    scenarios = [
        {"long": 60, "short": 50, "leverage": 4.0},
        {"long": 80, "short": 20, "leverage": 2.0},
        {"long": 30, "short": 30, "leverage": 3.0},
    ]

    rank_scores = _build_rank_scores(100)

    fig, axes = plt.subplots(2, 3, figsize=(18, 10), sharey="row")
    fig.suptitle("Position Weighting Schemes: Impact on Portfolio Concentration", fontsize=16)

    for col, scenario in enumerate(scenarios):
        long_ids = list(rank_scores.keys())[: scenario["long"]]
        short_ids = list(rank_scores.keys())[: scenario["short"]]

        for row, (ids, direction) in enumerate(((long_ids, "LONG"), (short_ids, "SHORT"))):
            if not ids:
                axes[row, col].set_visible(False)
                continue

            weights_equal = _weights_as_pct(
                weights_from_ranks(
                    [(i, rank_scores[i]) for i in ids],
                    long_assets=ids if direction == "LONG" else [],
                    short_assets=[] if direction == "LONG" else ids,
                    target_gross=scenario["leverage"],
                    scheme="equal",
                ),
                scenario["leverage"],
            )

            weights_p05 = _weights_as_pct(
                weights_from_ranks(
                    rank_scores,
                    long_assets=ids if direction == "LONG" else [],
                    short_assets=[] if direction == "LONG" else ids,
                    target_gross=scenario["leverage"],
                    scheme="rank_power",
                    power=0.5,
                ),
                scenario["leverage"],
            )

            weights_p15 = _weights_as_pct(
                weights_from_ranks(
                    rank_scores,
                    long_assets=ids if direction == "LONG" else [],
                    short_assets=[] if direction == "LONG" else ids,
                    target_gross=scenario["leverage"],
                    scheme="rank_power",
                    power=1.5,
                ),
                scenario["leverage"],
            )

            _render_axis(
                axes[row, col],
                f"{scenario['long']}L/{scenario['short']}S @ {scenario['leverage']}x - {direction}"
                f" ({len(ids)} positions)",
                ids,
                weights_equal,
                weights_p05,
                weights_p15,
            )

    # Place legend only once to avoid clutter - put it in the top-left subplot
    handles, labels = axes[0, 0].get_legend_handles_labels()
    axes[0, 0].legend(handles, labels, loc="upper right", fontsize=9, framealpha=0.9)
    
    fig.tight_layout()
    fig.savefig(output_path, dpi=200)
    plt.close(fig)


def _weights_as_pct(weights: dict[str, float], leverage: float) -> list[float]:
    return [abs(w) / leverage * 100 for w in weights.values()]


if __name__ == "__main__":
    target = Path(__file__).parent / "assets" / "weighting_schemes_grid.png"
    generate_grid(target)

