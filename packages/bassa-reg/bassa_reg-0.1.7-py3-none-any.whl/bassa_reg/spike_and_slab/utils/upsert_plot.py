import io
from typing import List

import numpy as np
import pandas as pd
from upsetplot import UpSet, from_memberships
import matplotlib.pyplot as plt
import matplotlib as mpl
from PIL import Image
from matplotlib.lines import Line2D
import warnings

from bassa_reg.spike_and_slab.bassa_survival import SurvivalSample
from bassa_reg.spike_and_slab.utils.bassa_enums import SurvivalMetric
from bassa_reg.spike_and_slab.utils.can_use_latex import can_use_latex
from bassa_reg.spike_and_slab.utils.latex_featname import latex_features

warnings.filterwarnings("ignore", category=FutureWarning)


def generate_bassa_plot(data_survival: List[SurvivalSample], metric: SurvivalMetric, ratios: pd.DataFrame, path: str):
    """
    Orchestrates creating the plot by generating, cropping, and combining
    the main plot and its legend for perfect visual centering.
    """
    # 1. Generate plot image (in memory) and get legend info
    plot_buffer = io.BytesIO()
    legend_handles = generate_bassa_plot_base(data_survival, metric, ratios, path=plot_buffer)
    plot_buffer.seek(0)

    # 2. Generate legend image (in memory)
    legend_buffer = io.BytesIO()
    generate_legend_image(legend_handles, path=legend_buffer)
    legend_buffer.seek(0)

    # 3. Tightly crop both images to their actual content
    cropped_plot = crop_whitespace(Image.open(plot_buffer))
    cropped_legend = crop_whitespace(Image.open(legend_buffer))

    # 4. Combine the cropped images onto a new canvas
    padding = 40  # Pixels
    final_width = max(cropped_plot.width, cropped_legend.width) + (2 * padding)
    final_height = cropped_plot.height + cropped_legend.height + (3 * padding)
    final_image = Image.new('RGB', (final_width, final_height), 'white')

    # Paste plot, centered horizontally
    plot_x = (final_width - cropped_plot.width) // 2
    final_image.paste(cropped_plot, (plot_x, padding))

    # Paste legend, centered horizontally
    legend_x = (final_width - cropped_legend.width) // 2
    legend_y = padding + cropped_plot.height + padding
    final_image.paste(cropped_legend, (legend_x, legend_y))

    # Save the final masterpiece ✨
    final_plot_path = f"{path}/bassa_plot.png"
    final_image.save(final_plot_path)
    print(f"Final plot saved to {final_plot_path}")

    # Clean up
    plot_buffer.close()
    legend_buffer.close()

def generate_bassa_plot_base(data_survival: List[SurvivalSample], metric: SurvivalMetric, ratios: pd.DataFrame,
                        path: str = None):
    if can_use_latex():
        mpl.rcParams.update({
            "text.usetex": True,
            "font.family": "serif",
            "font.serif": ["Computer Modern Roman"],
        })

    if can_use_latex():
        for sample in data_survival:
            sample.feature_names = latex_features(sample.feature_names)
        for i in range(len(ratios)):
            ratios.at[i, "feature_name"] = latex_features([ratios.at[i, "feature_name"]])[0]

    bar_color = "black"
    text_color = "black"

    # ───────────────────  Data  ───────────────────
    data = {
        "Features": [
        ],
        "R2": [
        ],
        "Q2": [

        ],
        "MSE": [
        ],
        "MAE": [],
        "final_pct": []
    }

    ratio_map = dict(
        zip(ratios["feature_name"], ratios["relative_occurrence"])
    )

    for sample in data_survival:
        feat_labels = []
        for f in sample.feature_names:
            if f in ratio_map:
                perc = round(ratio_map[f] * 100, 1)
                if can_use_latex():
                    feat_labels.append(f"{f} (${{{perc}\\%}}$)")
                else:
                    feat_labels.append(f"{f} ({perc}%)")
            else:
                feat_labels.append(f)
        data["Features"].append(",".join(feat_labels))

        data["R2"].append(sample.r2)
        data["Q2"].append(sample.q2)
        data["MSE"].append(sample.mse)
        data["MAE"].append(sample.mae)

        first_value = sample.y_values[0]
        last_value = sample.y_values[-1]
        total_value = len(sample.y_values)
        if can_use_latex():
            data["final_pct"].append(fr"\begin{{center}}${first_value:.1f}\%$\\${last_value:.1f}\%$\\({total_value})\end{{center}}")
        else:
            data["final_pct"].append(f"{first_value:.1f}%\n{last_value:.1f}%\n({total_value})")


    df = pd.DataFrame(data)

    # ───────────────────  helper: raw → LaTeX  ───────────────────

    # memberships (LaTeX strings so tick labels look nice)
    memberships = [
        tuple(sorted(f.strip() for f in row.split(",")))
        for row in df["Features"]
    ]

    metric_name = r"$R^2$"
    combined_df = pd.DataFrame({'R2': df["R2"], 'Q2': df["Q2"], 'final_pct': df["final_pct"]})
    upset_combined = from_memberships(memberships, data=combined_df)

    if metric == SurvivalMetric.R2:
        upset_data = upset_combined['R2']
        metric_name = r"$R^2$"
    elif metric == SurvivalMetric.Q2:
        upset_data = upset_combined['Q2']
        metric_name = r"$Q^2$"
    else:
        upset_data = upset_combined['R2']
        metric_name = r"$R^2$"

    # ────────────────  Build the UpSet object first  ────────────────
    upset = UpSet(
        upset_data,
        show_counts="%.3f",
        sort_by="cardinality",
        totals_plot_elements=0,
        facecolor=bar_color,
        other_dots_color=0.12,
        shading_color=0.0,
        with_lines=False,
    )

    degrees = upset.intersections.index.to_frame().sum(axis=1).astype(int)
    unique_deg = sorted(degrees.unique())

    def is_grayish(rgba, threshold=0.05):
        r, g, b = rgba[:3]
        return abs(r - g) < threshold and abs(g - b) < threshold and abs(r - b) < threshold

    base_cmap = mpl.colormaps.get_cmap("Set2")
    norm = mpl.colors.Normalize(vmin=min(unique_deg), vmax=max(unique_deg))

    def pastel(rgba, w=1):
        r, g, b, _ = rgba
        return (1 - w) + w * r, (1 - w) + w * g, (1 - w) + w * b, 1.0

    valid_colors = [
        pastel(base_cmap(i / (base_cmap.N - 1)))
        for i in range(base_cmap.N)
        if not is_grayish(base_cmap(i / (base_cmap.N - 1)))
    ]

    for d, colour in zip(unique_deg, valid_colors):
        upset.style_subsets(
            min_degree=d,
            max_degree=d,
            facecolor=colour,
            edgecolor=colour,
        )

    upset.plot()
    fig = plt.gcf()
    height = 8
    if len(upset_data) > 10:
        height = 10
    fig.set_size_inches(10 + 0.5 * max(len(upset_data), 8), height)

    # ────────────────  Add final_pct values at bottom of bars  ────────────────
    # Find the intersection axis (the one with the bars)
    intersection_ax = None
    for ax in fig.get_axes():
        if ax.get_ylabel() == "Intersection size":
            intersection_ax = ax
            break

    if intersection_ax is not None:
        # Create mapping from metric values to final_pct values
        if metric == SurvivalMetric.R2:
            metric_values = df["R2"]
        elif metric == SurvivalMetric.Q2:
            metric_values = df["Q2"]
        else:
            metric_values = df["R2"]

        value_to_final_pct = dict(zip(metric_values, df["final_pct"]))

        # Get final_pct values by matching the actual metric values
        sorted_final_pct_values = [value_to_final_pct.get(val, 'N/A') for val in upset.intersections.values]

        # Get bar positions
        bars = intersection_ax.patches

        # Add text at the bottom of each bar
        y_min = intersection_ax.get_ylim()[0]
        text_y_offset = (intersection_ax.get_ylim()[1] - intersection_ax.get_ylim()[0]) * 0.02  # 2% of y-range

        for i, (bar, final_pct_val) in enumerate(zip(bars, sorted_final_pct_values)):
            x_center = bar.get_x() + bar.get_width() / 2
            # Position text below the x-axis
            intersection_ax.text(x_center, y_min - text_y_offset, final_pct_val,
                                 ha='center', va='top', color=text_color, fontsize=8)

        if bars:  # Make sure there are bars
            first_bar = bars[0]

            # Position the header to align with the text below the bars
            x_left_margin = first_bar.get_x() - (first_bar.get_width() * 1.2)

            # Use the EXACT same positioning as the data text
            y_min = intersection_ax.get_ylim()[0]
            text_y_offset = (intersection_ax.get_ylim()[1] - intersection_ax.get_ylim()[0]) * 0.02

            # Create the header text with the same formatting as data text
            if can_use_latex():
                header_text = r"\begin{flushleft}\% Start\\\% End\\Total Points\end{flushleft}"
            else:
                header_text = "% Start\n% End\nTotal Points"


            intersection_ax.text(x_left_margin, y_min - text_y_offset, header_text,
                                 ha='right', va='top', color=text_color, fontsize=8)

    for ax in fig.get_axes():
        if ax.get_ylabel() == "Intersection size":
            if can_use_latex():
                ax.set_ylabel(fr"Model {metric_name} Value", color=text_color)
            else:
                ax.set_ylabel(f"Model {metric_name} Value", color=text_color)
            ax.grid(False)
            ax.set_yticks([])
        ax.tick_params(axis="x", colors=text_color)
        ax.tick_params(axis="y", colors=text_color)
        for line in ax.lines:
            line.set_color(text_color)
        for txt in ax.texts:
            txt.set_color(text_color)
        for spine in ax.spines.values():
            spine.set_edgecolor(text_color)

    plt.subplots_adjust(bottom=0.1, left=0.05)  # Increased bottom margin for final_pct text
    # --- Create Legend Handles (but don't draw the legend) ---
    legend_handles = [
        Line2D([0], [0], marker='o', linestyle='None',
               markerfacecolor=color, markeredgecolor='none', markersize=10,
               label=str(degree))
        for degree, color in zip(unique_deg, valid_colors)
    ]

    # --- Save the plot to the provided path/buffer and clean up ---
    fig = plt.gcf()
    plt.savefig(path, dpi=300, bbox_inches='tight', pad_inches=0.1)
    plt.close(fig)

    # --- Return the handles for later use ---
    return legend_handles



def crop_whitespace(image: Image.Image) -> Image.Image:
    """Crops an image by finding the bounding box of non-white pixels."""
    img_array = np.array(image.convert('RGB'))
    non_white_pixels = np.any(img_array != [255, 255, 255], axis=2)
    non_white_coords = np.argwhere(non_white_pixels)

    if non_white_coords.size == 0: return image

    top, left = non_white_coords.min(axis=0)
    bottom, right = non_white_coords.max(axis=0)

    return image.crop((left, top, right + 1, bottom + 1))


def generate_legend_image(handles: List[Line2D], path):
    """Creates a new figure containing ONLY the legend and saves it."""
    fig_legend = plt.figure(figsize=(5, 0.5))
    fig_legend.legend(
        handles=handles,
        title="Number of Features",
        loc='center',
        ncol=len(handles),
        frameon=False,
    )
    fig_legend.savefig(path, dpi=300, bbox_inches='tight', pad_inches=0.05)
    plt.close(fig_legend)
