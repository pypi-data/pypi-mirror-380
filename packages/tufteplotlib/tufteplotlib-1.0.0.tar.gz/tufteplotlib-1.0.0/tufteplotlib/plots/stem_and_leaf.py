import numpy as np
import warnings
from collections import defaultdict

####################################################################################################
#                                         Core function                                            #
####################################################################################################
def stem_and_leaf_plot(data=None, output="plain", round_decimals=2):
    """
    Generate an horizontal histogram in which significant digits are used as categorical labels.
    Best used for sparse data. For dense data, consider using the density plot.

    Parameters
    ----------
    data : array-like
        List or array of numbers. If None, raises ValueError.
    output : str
        'plain', 'Markdown', 'LaTeX', 'CSV'.
    round_decimals : int
        Number of decimal places for floats.

    Returns
    -------
    output_str : str
        The textual representation of the stem-and-leaf table.
    """
    if data is None:
        raise ValueError("No data provided.")

    data = sorted(data)
    stems = defaultdict(list)

    # --- Organize stems and leaves ---
    if all(isinstance(x, (int, np.integer)) for x in data):
        # integer-only handling
        for value in data:
            s = str(value)
            if len(s) == 1:
                stem, leaf = "0", s[-1]
            else:
                stem, leaf = s[:-1], s[-1]
            stems[int(stem)].append(leaf)
        min_stem, max_stem = int(min(stems)), int(max(stems))
        for stem in range(min_stem, max_stem + 1):
            stems.setdefault(stem, [])

    elif all(isinstance(x, (float, np.floating)) for x in data) or all(isinstance(x, (int, np.integer)) for x in data):
        # float (or mixed int/float) handling
        for value in data:
            stem = int(np.floor(value))
            leaf_val = value - stem
            leaf_str = "." + f"{leaf_val:.{round_decimals}f}".split(".")[1]
            stems[stem].append(leaf_str)
        min_stem = int(np.floor(min(data)))
        max_stem = int(np.floor(max(data)))
        for stem in range(min_stem, max_stem + 1):
            stems.setdefault(stem, [])


    else:
        warnings.warn("Mixed or unsupported data types detected. Only int or float arrays are supported.")
        return None

    # --- Build table data ---
    table_data = [["Stem", "Leaves"]]
    for stem in sorted(stems):
        leaves = " ".join(str(l) for l in stems[stem])
        table_data.append([str(stem), leaves])

    # --- Prepare textual output ---
    output_str = ""
    if output == "plain":
        lines = [f"{row[0].rjust(5)} | {row[1]}" for row in table_data]
        output_str = "\n".join(lines)

    elif output == "Markdown":
        lines = ["|  Stem | Leaves |", "|------:|:-------|"]
        for row in table_data[1:]:
            lines.append(f"| {row[0].rjust(5)} | {row[1]} |")
        output_str = "\n".join(lines)

    elif output == "CSV":
        lines = ["Stem,Leaves"]
        for row in table_data[1:]:
            lines.append(f"{row[0]},{row[1]}")
        output_str = "\n".join(lines)

    elif output == "LaTeX":
        max_leaves = max(len(row[1].split()) for row in table_data[1:]) if len(table_data) > 1 else 0
        col_format = "r|" + "l" * max_leaves
        lines = [f"\\begin{{tabular}}{{{col_format}}}",
                 f"Stem & \\multicolumn{{{max_leaves}}}{{l}}{{Leaves}} \\\\ \\hline"]
        for row in table_data[1:]:
            leaves = row[1].split()
            leaves += [""] * (max_leaves - len(leaves))
            lines.append(f"{row[0]} & " + " & ".join(leaves) + " \\\\")
        lines.append("\\end{tabular}")
        output_str = "\n".join(lines)

    elif output is not None:
        raise ValueError(f"Unknown output '{output}'")

    return output_str

####################################################################################################
#                                          Test / example code                                     #
####################################################################################################  
def main():
    data = np.random.randint(5, 15, size=20) + np.random.rand(20)

    print("\nPlain text:\n")
    print(stem_and_leaf_plot(data, output="plain"))
    
    print("\nMarkdown:\n")
    print(stem_and_leaf_plot(data, output="Markdown"))
    
    print("\nLaTeX:\n")
    print(stem_and_leaf_plot(data, output="LaTeX"))
    
    print("\nCSV:\n")
    print(stem_and_leaf_plot(data, output="CSV"))

if __name__ == "__main__":
    main()
