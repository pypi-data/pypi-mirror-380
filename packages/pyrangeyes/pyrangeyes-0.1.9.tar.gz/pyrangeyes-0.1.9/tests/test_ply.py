import pyrangeyes as pre
import pyranges as pr
import os
import pytest
import plotly.graph_objects as go
import json
from deepdiff import DeepDiff
import numpy as np
from plotly.utils import PlotlyJSONEncoder


def normalize_plotly_json(obj):
    import numpy as np
    if isinstance(obj, dict):
        return {k: normalize_plotly_json(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [normalize_plotly_json(i) for i in obj]
    elif isinstance(obj, tuple):
        return list(normalize_plotly_json(i) for i in obj)
    elif isinstance(obj, np.ndarray):
        return normalize_plotly_json(obj.tolist())
    else:
        return obj

data1 = pr.PyRanges(
    {
        "Chromosome": ["1"] * 9,
        "Strand": ["+", "+", "-", "-", "-", "+", "+", "+", "-"],
        "Start": [i * 100 for i in [5, 35, 3, 13, 35, 45, 49, 56, 60]],
        "End": [i * 100 for i in [15, 37, 6, 17, 39, 47, 51, 57, 67]],
        "transcript_id": ["t1", "t1", "t2", "t2", "t2", "t3", "t3", "t3", "t4"],
        "second_id": ["a"] * 4 + ["b"] * 5,
    }
)

data2 = pr.PyRanges(
    {
        "Chromosome": ["1"] * 10 + ["2"] * 10 + ["4"],
        "Strand": ["+", "+", "+", "+", "-", "-", "-", "-", "+", "+"]
        + ["+", "+", "+", "+", "-", "-", "-", "-", "+", "+"]
        + ["+"],
        "Start": [90, 61, 104, 228, 9, 142, 52, 149, 218, 151]
        + [5, 27, 37, 47, 1, 7, 42, 37, 60, 80]
        + [20],
        "End": [92, 64, 113, 229, 12, 147, 57, 155, 224, 153]
        + [8, 32, 40, 50, 5, 10, 46, 40, 70, 90]
        + [50],
        "transcript_id": ["t1", "t1", "t1", "t1", "t2", "t2", "t2", "t2", "t3", "t3"]
        + ["t4", "t4", "t4", "t4", "t5", "t5", "t5", "t5", "t6", "t6", "t7"],
        "Feature": [
            "CDS",
            "exon",
            "exon",
            "exon",
            "exon",
            "exon",
            "exon",
            "exon",
            "exon",
            "exon",
        ]
        + ["exon"] * 8
        + ["exon"] * 3,
    }
)

data3 = pr.PyRanges(
    {
        "Chromosome": ["1", "1", "2", "2", "2", "2", "2", "3", "4", "4", "4", "5"],
        "Strand": ["+", "+", "-", "-", "+", "+", "+", "+", "-", "-", "-", "+"],
        "Start": [1, 40, 10, 70, 85, 110, 150, 140, 5, 170, 240, 100],
        "End": [11, 60, 25, 80, 100, 115, 180, 152, 150, 200, 260, 200],
        "transcript_id": [
            "t1",
            "t1",
            "T2",
            "T2",
            "T3",
            "T3",
            "T3",
            "T4",
            "T5",
            "T5",
            "T5",
            "T6",
        ],
        "Feature": ["exon"] * 12,
    }
)

data4 = pr.PyRanges(
    {
        "Start": [10, 30],
        "End": [40, 60],
        "Chromosome": [1, 1],
        "id": [1, 1],
        "depth": [0, 1],
    }
)

data5 = data4.copy()
data5["depth"] = [1, 0]

vcf = pr.PyRanges(
    {
        "Chromosome": ["1"] * 9,  # CHROM renamed to Chromosome
        "Start": [
            500,
            3500,
            300,
            1300,
            3500,
            4500,
            4900,
            5600,
            6000,
        ],  # POS column renamed to Start
        "End": [
            501,
            3501,
            301,
            1301,
            3501,
            4501,
            4901,
            5601,
            6001,
        ],  # End is calculated as Start + 1
        "ID": ["."] * 9,  # ID from the VCF file
        "REF": ["A"] * 9,  # REF column
        "ALT": ["T"] * 9,  # ALT column
        "QUAL": ["."] * 9,  # QUAL column
        "FILTER": ["PASS"] * 9,  # FILTER column
        "transcript_id": [
            "t1",
            "t2",
            "t3",
            "t4",
            "t5",
            "t6",
            "t7",
            "t8",
            "t9",
        ],  # Extracted from INFO
        "second_id": [
            "a",
            "a",
            "a",
            "a",
            "b",
            "b",
            "b",
            "b",
            "b",
        ],  # Extracted from INFO
        "Count": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    }
)

# Create a scatter plot trace with the adapted Start positions
aligned_traces = [
    (
        go.Scatter(
            x=[
                500,
                3500,
                300,
                1300,
                3500,
                4500,
                4900,
                5600,
                6000,
            ],  # Adapted Start positions
            y=[1, 2, 3, 4, 5, 6, 7, 8, 9],  # Arbitrary y-values for demonstration
            mode="markers",
        ),
        {"title": "VCF Scatter Plot"},
    )
]

aligned = pre.make_scatter(vcf, y="Count", engine="ply")
aligned1 = pre.make_scatter(
    vcf,
    y="Count",
    color_by="second_id",
    title="Human Variants",
    title_color="Magenta",
    title_size=18,
    engine="ply",
)
aligned2 = pre.make_scatter(
    vcf,
    y="Count",
    color_by="second_id",
    title="Human Variants",
    title_color="Magenta",
    title_size=18,
    height=0.5,
    y_space=0.5,
    engine="ply",
)

pre.set_engine("ply")
pre.set_id_col("transcript_id")

BASELINE_DIR = "tests/baseline_ply"

test_cases = [
    (
        "test01",
        pre.plot(
            data1,
            color_col="transcript_id",
            exon_border="black",
            sort=True,
            return_plot="fig",
        ),
    ),
    (
        "test02",
        pre.plot(
            data1,
            id_col="second_id",
            color_col="transcript_id",
            shrink=True,
            exon_border="black",
            sort=True,
            return_plot="fig",
        ),
    ),
    (
        "test03",
        pre.plot(
            data1,
            id_col=["transcript_id", "second_id"],
            color_col="transcript_id",
            packed=False,
            sort=True,
            return_plot="fig",
        ),
    ),
    (
        "test04",
        pre.plot(
            data1[data1["transcript_id"] == "t4"],
            id_col="transcript_id",
            shrink=True,
            return_plot="fig",
        ),
    ),
    (
        "test05",
        pre.plot(
            data1[data1["transcript_id"] == "t2"],
            id_col="transcript_id",
            shrink=True,
            return_plot="fig",
        ),
    ),
    (
        "test06",
        pre.plot(
            [data2, data3],
            color_col="transcript_id",
            sort=True,
            return_plot="fig",
        ),
    ),
    (
        "test07",
        pre.plot(
            [data2, data3],
            id_col="Feature",
            color_col="transcript_id",
            text="{Feature}",
            sort=True,
            return_plot="fig",
        ),
    ),
    (
        "test08",
        pre.plot(
            [data1, data2, data3],
            id_col="transcript_id",
            color_col="Feature",
            y_labels=[1, 2, 3],
            shrink=True,
            sort=True,
            return_plot="fig",
        ),
    ),
    (
        "test09",
        pre.plot(
            [data2, data2],
            id_col="transcript_id",
            packed=False,
            thick_cds=True,
            sort=True,
            return_plot="fig",
        ),
    ),
    (
        "test10",
        pre.plot(
            data2,
            thick_cds=True,
            limits=(75, 125),
            text="{Feature}",
            sort=True,
            return_plot="fig",
        ),
    ),
    (
        "test11",
        pre.plot(
            data3,
            id_col="transcript_id",
            limits={"1": (None, 1000), "2": (20, 40), "3": None, "4": (-1000, None)},
            return_plot="fig",
        ),
    ),
    (
        "test12",
        pre.plot(
            data2,
            id_col="transcript_id",
            limits=data3,
            arrow_size=0.1,
            arrow_color="red",
            sort=True,
            return_plot="fig",
        ),
    ),
    (
        "test13",
        pre.plot(
            [data2, data3],
            id_col="transcript_id",
            color_col="Feature",
            legend=True,
            title_chr="TITLE {chrom}",
            sort=True,
            return_plot="fig",
        ),
    ),
    (
        "test14",
        pre.plot(
            [data4, data5],
            id_col="id",
            color_col="depth",
            depth_col="depth",
            tooltip="{depth}",
            return_plot="fig",
        ),
    ),
    (
        "test15",
        pre.plot(
            [data4, data5],
            id_col="id",
            color_col="depth",
            depth_col="depth",
            tooltip="{depth}",
            theme="dark",
            return_plot="fig",
        ),
    ),
    (
        "test16",
        pre.plot(
            [data4, data5],
            id_col="id",
            color_col="depth",
            depth_col="depth",
            tooltip="{depth}",
            colormap={"0": "#505050", "1": "goldenrod"},
            return_plot="fig",
        ),
    ),
    (
        "test17",
        pre.plot(
            [data1, vcf],
            id_col="transcript_id",
            sort=True,
            return_plot="fig",
        ),
    ),
    (
        "test18",
        pre.plot(
            [data1, vcf],
            id_col="transcript_id",
            add_aligned_plots=[aligned],
            sort=True,
            return_plot="fig",
        ),
    ),
    (
        "test19",
        pre.plot(
            [data1, vcf],
            id_col="transcript_id",
            add_aligned_plots=[aligned1],
            sort=True,
            return_plot="fig",
        ),
    ),
    (
        "test20",
        pre.plot(
            [data1, vcf],
            id_col="transcript_id",
            add_aligned_plots=[aligned2],
            sort=True,
            return_plot="fig",
        ),
    ),
    (
        "test21",
        pre.plot(
            data1,
            id_col=["transcript_id", "second_id"],
            color_col="transcript_id",
            packed=False,
            return_plot="fig",
        ),
    ),
]

"""
for test_name, fig in test_cases:
    json_path = os.path.join(BASELINE_DIR, f"{test_name}.json")
    with open(json_path, "w") as f:
        json.dump(fig.to_plotly_json(), f, indent=2, cls=PlotlyJSONEncoder)
"""
@pytest.mark.parametrize("test_name, plot_func", test_cases)
# test id_col
def test_plot_comparison(test_name, plot_func):
    fig = plot_func    # JSON actual generat
    actual_json = normalize_plotly_json(fig.to_plotly_json())   # Ruta al baseline
    baseline_path = os.path.join(BASELINE_DIR, f"{test_name}.json")    # Carreguem JSON del baseline
    with open(baseline_path, "r") as f:
        expected_json = normalize_plotly_json(json.load(f))    # Compara
    diff = DeepDiff(expected_json, actual_json, ignore_order=True, report_repetition=True)
    assert diff == {}, f"{test_name} does not match baseline:\n{diff.pretty()}"
