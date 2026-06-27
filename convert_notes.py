#!/usr/bin/env python3
"""
Convert all DMA notes markdown files to a single LaTeX document.
"""

import re
import os
from pathlib import Path

NOTES_DIR = Path("/Users/hechenyu/end-term/dma/notes")
OUTPUT_FILE = Path("/Users/hechenyu/end-term/dma/notes.tex")

# Ordering of files following README structure
FILE_ORDER = [
    # === Ch1 Logic & Proofs ===
    "Ch01-1.1-Propositional-Logic.md",
    "Ch01-1.3-Propositional-Equivalences.md",
    "Ch01-1.4-Predicates-and-Quantifiers.md",
    "Ch01-1.5-Nested-Quantifiers.md",
    "Ch01-1.6-Rules-of-Inference.md",
    "Ch01-1.7-Introduction-to-Proofs.md",
    "Ch01-1.8-Proof-Methods-and-Strategy.md",
    # === Ch2 Sets ===
    "Ch02-2.1-Sets.md",
    "Ch02-2.2-Set-Operations.md",
    "Ch02-2.3-Functions.md",
    "Ch02-2.4-Sequences-and-Summations.md",
    "Ch02-2.5-Cardinality-of-Sets.md",
    # === Ch3 Algorithms ===
    "Ch03-3.1-Algorithms.md",
    "Ch03-3.2-Growth-of-Functions.md",
    "Ch03-3.3-Complexity-of-Algorithms.md",
    # === Ch4 Number Theory ===
    "Ch04-4.1-Divisibility-and-Modular-Arithmetic.md",
    "Ch04-4.2-Integer-Representations.md",
    "Ch04-4.3-Primes-and-Greatest-Common-Divisors.md",
    "Ch04-4.4-Solving-Congruences.md",
    "Ch04-4.5-Cryptography.md",
    # === Ch5 Induction ===
    "Ch05-5.1-Mathematical-Induction.md",
    "Ch05-5.2-Strong-Induction.md",
    "Ch05-5.3-Recursive-Definitions.md",
    # === Ch6 Counting ===
    "Ch06-6.3-Permutations-and-Combinations.md",
    "Ch06-6.4-Binomial-Theorem-and-Pascal-Identity.md",
    "Ch06-6.5-Generalized-Permutations-and-Combinations.md",
    "Ch06-6.6-Generating-Permutations-and-Combinations.md",
    # === Ch8 Recurrence Relations ===
    "Ch08-8.1-Applications-of-Recurrence-Relations.md",
    "Ch08-8.2-Solving-Linear-Recurrence-Relations.md",
    "Ch08-8.3-Homogeneous-Recurrence-Relations.md",
    "Ch08-8.4-Nonhomogeneous-Recurrence-Relations.md",
    "Ch08-8.5-Generating-Functions.md",
    "Ch08-8.6-Inclusion-Exclusion.md",
    # === Ch9 Relations ===
    "Ch09-9.1-Relations-and-Their-Properties.md",
    "Ch09-9.2-n-ary-Relations.md",
    "Ch09-9.3-Representing-Relations.md",
    "Ch09-9.4-Closures-of-Relations.md",
    "Ch09-9.5-Equivalence-Relations.md",
    "Ch09-9.6-Partial-Orderings.md",
    # === Ch10 Graphs ===
    "Ch10-10.1-Graphs-and-Graph-Models.md",
    "Ch10-10.2-Graph-Terminology.md",
    "Ch10-10.3-Representing-Graphs-and-Isomorphism.md",
    "Ch10-10.4-Connectivity.md",
    "Ch10-10.5-Euler-and-Hamilton-Paths.md",
    "Ch10-10.6-Shortest-Path-Problems.md",
    "Ch10-10.7-Planar-Graphs.md",
    "Ch10-10.8-Graph-Coloring.md",
    # === Ch11 Trees ===
    "Ch11-11.1-Introduction-to-Trees.md",
    "Ch11-11.2-Applications-of-Trees.md",
    "Ch11-11.3-Tree-Traversal.md",
    "Ch11-11.4-Spanning-Trees.md",
    "Ch11-11.5-Minimum-Spanning-Trees.md",
    # === Network Flow ===
    "Network-Flow.md",
    # === Exam Reviews ===
    "Exam-Review-Ch1-3.md",
    "Exam-Review-Ch4-5.md",
    "Exam-Review-Ch6-8.md",
    "Exam-Review-Ch9-11.md",
    # === Practice ===
    "Practice-Exam.md",
    "Practice-Exam-Answers.md",
    # === Quiz Solutions ===
    "Quiz1-2022-Solutions.md",
    "Quiz1-2023-Solutions.md",
    "Quiz1-2024-Solutions.md",
    "Quiz1-2025-Solutions.md",
    "Quiz2-2022-Solutions.md",
    "Quiz2-2023-Solutions.md",
    "Quiz2-2024-Solutions.md",
    "Quiz3-2022-Solutions.md",
    "Quiz3-2024-Solutions.md",
    "Quiz4-2022-Solutions.md",
    "Quiz4-2024-Solutions.md",
    # === Final ===
    "Final-2022-Solutions.md",
    # === Meta ===
    "Study-Plan.md",
    "Weak-Points.md",
]

# Chapter boundaries for inserting \section-level chapter headers
CHAPTER_MARKERS = {
    "Ch01-1.1-Propositional-Logic.md": ("chapter", "Chapter 1: Logic \\& Proofs (逻辑与证明)"),
    "Ch02-2.1-Sets.md": ("chapter", "Chapter 2: Sets, Functions, Sequences (集合、函数、序列)"),
    "Ch03-3.1-Algorithms.md": ("chapter", "Chapter 3: Algorithms (算法)"),
    "Ch04-4.1-Divisibility-and-Modular-Arithmetic.md": ("chapter", "Chapter 4: Number Theory (数论)"),
    "Ch05-5.1-Mathematical-Induction.md": ("chapter", "Chapter 5: Induction \\& Recursion (归纳与递归)"),
    "Ch06-6.3-Permutations-and-Combinations.md": ("chapter", "Chapter 6: Counting (计数)"),
    "Ch08-8.1-Applications-of-Recurrence-Relations.md": ("chapter", "Chapter 8: Recurrence Relations (递推关系)"),
    "Ch09-9.1-Relations-and-Their-Properties.md": ("chapter", "Chapter 9: Relations (关系)"),
    "Ch10-10.1-Graphs-and-Graph-Models.md": ("chapter", "Chapter 10: Graphs (图论)"),
    "Ch11-11.1-Introduction-to-Trees.md": ("chapter", "Chapter 11: Trees (树)"),
    "Network-Flow.md": ("chapter", "Network Flow (网络流)"),
    "Exam-Review-Ch1-3.md": ("part", "历年真题考点分析"),
    "Practice-Exam.md": ("part", "模拟卷"),
    "Quiz1-2022-Solutions.md": ("part", "历年真题题解"),
    "Study-Plan.md": ("part", "附录"),
}


def parse_table_align(align_row):
    """Parse markdown table alignment row, return LaTeX column spec."""
    cols = [c.strip() for c in align_row.strip("|").split("|")]
    spec = ""
    for c in cols:
        c = c.strip()
        left = c.startswith(":")
        right = c.endswith(":")
        if left and right:
            spec += "c"
        elif left:
            spec += "l"
        elif right:
            spec += "r"
        else:
            spec += "c"
    return spec


def escape_latex(text):
    """Escape special LaTeX characters in plain text (not inside math)."""
    # Don't escape if it's a LaTeX command
    replacements = [
        ("&", r"\&"),
        ("%", r"\%"),
        ("#", r"\#"),
        ("_", r"\_"),
        # ("$", r"\$"),  # Don't escape $ as it's used for math
        # ("^", r"\^{}"), # Don't escape ^ as it's used in math
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def convert_inline_formatting(line):
    """Convert markdown inline formatting to LaTeX. Preserve math mode."""
    math_segments = []

    def save_math(m):
        math_segments.append(m.group(0))
        return f"<<<MATH{len(math_segments)-1}>>>"

    # Step 1: Protect display math $$...$$
    line = re.sub(r'\$\$.+?\$\$', save_math, line)

    # Step 2: Protect inline math $...$ (content between $ signs without another $)
    line = re.sub(r'\$[^$]+?\$', save_math, line)

    # Step 3: Escape any remaining lone $ signs (currency, etc.)
    # These are $ not part of a $...$ or $$...$$ pair
    line = line.replace('$', r'\$')

    # Step 4: Convert **bold** to \textbf{}
    line = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', line)

    # Step 5: Convert inline code `text` to \texttt{}
    line = re.sub(r'`([^`]+)`', r'\\texttt{\1}', line)

    # Step 6: Convert *italic* to \textit{}
    line = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'\\textit{\1}', line)

    # Step 7: Escape special LaTeX chars in text (BEFORE restoring math)
    line = line.replace(r'\_', '<<<US>>>')
    line = line.replace('_', r'\_')
    line = line.replace('<<<US>>>', r'\_')
    line = line.replace(r'\&', '<<<AMP>>>')
    line = line.replace('&', r'\&')
    line = line.replace('<<<AMP>>>', r'\&')
    line = line.replace('%', r'\%')
    line = line.replace('#', r'\#')
    line = line.replace('^', r'\^{}')

    # Step 8: Restore math
    for idx, m in enumerate(math_segments):
        line = line.replace(f"<<<MATH{idx}>>>", m)

    return line


def split_table_row(row):
    """Split a markdown table row by |, respecting $...$ math mode."""
    # Strip leading/trailing |
    row = row.strip().strip("|")
    cells = []
    current = ""
    in_math = False
    i = 0
    while i < len(row):
        ch = row[i]
        if ch == '$' and not in_math:
            # Check for $$
            if i + 1 < len(row) and row[i + 1] == '$':
                # Display math $$...$$
                j = row.find('$$', i + 2)
                if j != -1:
                    current += row[i:j + 2]
                    i = j + 2
                    continue
            in_math = True
            current += ch
        elif ch == '$' and in_math:
            in_math = False
            current += ch
        elif ch == '|' and not in_math:
            cells.append(current.strip())
            current = ""
        else:
            current += ch
        i += 1
    if current.strip():
        cells.append(current.strip())
    return cells


def convert_table(lines, i):
    """Convert a markdown table to LaTeX tabular. Returns (latex_str, new_i)."""
    if i + 1 >= len(lines):
        return None, i

    header_line = lines[i]
    align_line = lines[i + 1]

    # Check if this really looks like a table
    if not re.match(r'^\|.*\|$', header_line.strip()):
        return None, i
    if not re.match(r'^\|[\s\-:|\s]+\|$', align_line.strip()):
        return None, i

    col_spec = parse_table_align(align_line)
    num_cols = len(col_spec)

    # Read all table rows
    rows = []
    j = i + 2
    while j < len(lines):
        row = lines[j].strip()
        if re.match(r'^\|.*\|$', row):
            rows.append(row)
            j += 1
        else:
            break

    latex = f"\\begin{{tabular}}{{{col_spec}}}\n\\hline\n"

    # Header
    cells = split_table_row(header_line)
    cells = [convert_inline_formatting(c) for c in cells]
    latex += " & ".join(cells) + r" \\ \hline" + "\n"

    # Data rows
    for row in rows:
        cells = split_table_row(row)
        cells = [convert_inline_formatting(c) for c in cells]
        # Pad if fewer cells than columns
        while len(cells) < num_cols:
            cells.append("")
        latex += " & ".join(cells[:num_cols]) + r" \\" + "\n"

    latex += r"\hline" + "\n" + r"\end{tabular}" + "\n"
    return latex, j


def is_table_line(line):
    """Check if a line could be part of a markdown table."""
    return bool(re.match(r'^\|.*\|$', line.strip()))


def convert_md_file(filepath):
    """Convert a single markdown file to LaTeX content."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.split("\n")
    output = []
    i = 0
    in_code_block = False
    in_display_math = False
    in_quote = False
    in_list = None  # 'itemize' or 'enumerate'

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Display math blocks $$...$$ (multi-line or single-line)
        if stripped.startswith("$$") and not in_code_block and not in_display_math:
            if stripped.endswith("$$") and len(stripped) > 4:
                # Single-line display math: $$...$$
                math_content = stripped[2:-2]
                output.append(r"\[")
                output.append(math_content)
                output.append(r"\]")
                output.append("")
            else:
                # Multi-line display math start
                output.append(r"\[")
                # Content after $$ on same line
                if len(stripped) > 2:
                    output.append(stripped[2:])
                in_display_math = True
            i += 1
            continue

        if in_display_math and stripped.endswith("$$"):
            # Closing $$ (possibly with content before it)
            if len(stripped) > 2:
                output.append(stripped[:-2])
            output.append(r"\]")
            output.append("")
            in_display_math = False
            i += 1
            continue

        if in_display_math:
            # Pass math content through unchanged
            output.append(line)
            i += 1
            continue

        # Code blocks
        if stripped.startswith("```"):
            if in_code_block:
                output.append(r"\end{verbatim}}")
                output.append("")
                in_code_block = False
            else:
                output.append(r"{\footnotesize\begin{verbatim}")
                in_code_block = True
            i += 1
            continue

        if in_code_block:
            output.append(line)
            i += 1
            continue

        # Skip empty lines
        if not stripped:
            if in_quote:
                output.append("")
            if in_list:
                output.append("")
            i += 1
            continue

        # Horizontal rule
        if stripped == "---" or stripped == "***" or stripped == "___":
            if in_quote:
                output.append(r"\end{quote}")
                in_quote = False
            if in_list:
                output.append(r"\end{" + in_list + "}")
                output.append("")
                in_list = None
            output.append(r"\vspace{-2pt}")
            output.append("")
            i += 1
            continue

        # Headers
        header_match = re.match(r'^(#{1,4})\s+(.+)$', stripped)
        if header_match:
            if in_quote:
                output.append(r"\end{quote}")
                output.append("")
                in_quote = False
            if in_list:
                output.append(r"\end{" + in_list + "}")
                output.append("")
                in_list = None

            level = len(header_match.group(1))
            title = convert_inline_formatting(header_match.group(2))
            # Remove trailing {#anchor} style tags
            title = re.sub(r'\s*\{#[^}]+\}$', '', title)

            if level == 1:
                output.append(r"\section{" + title + "}")
            elif level == 2:
                output.append(r"\subsection{" + title + "}")
            elif level == 3:
                output.append(r"\subsubsection{" + title + "}")
            else:
                output.append(r"\paragraph{" + title + "}")
            output.append("")
            i += 1
            continue

        # Blockquotes
        if stripped.startswith("> "):
            quote_content = stripped[2:]  # Remove '> '

            # Check for display math inside quote
            if quote_content.strip().startswith("$$"):
                if not in_quote:
                    if in_list:
                        output.append(r"\end{" + in_list + "}")
                        output.append("")
                        in_list = None
                    output.append(r"\begin{quote}")
                    in_quote = True

                if quote_content.strip().endswith("$$") and len(quote_content.strip()) > 4:
                    output.append(r"\[")
                    output.append(quote_content.strip()[2:-2])
                    output.append(r"\]")
                    output.append("")
                else:
                    output.append(r"\[")
                    if len(quote_content.strip()) > 2:
                        output.append(quote_content.strip()[2:])
                    in_display_math = True
                i += 1
                continue

            # Check for closing $$ inside quote while in display math
            if in_display_math and quote_content.strip().endswith("$$"):
                if len(quote_content.strip()) > 2:
                    output.append(quote_content.strip()[:-2])
                output.append(r"\]")
                output.append("")
                in_display_math = False
                i += 1
                continue

            if not in_quote:
                if in_list:
                    output.append(r"\end{" + in_list + "}")
                    output.append("")
                    in_list = None
                output.append(r"\begin{quote}")
                in_quote = True

            quote_text = convert_inline_formatting(quote_content)

            # Handle nested quotes
            while quote_text.startswith("> "):
                quote_text = quote_text[2:]

            if quote_text.startswith("**"):
                # Bold paragraph in quote
                quote_text = quote_text.strip()

            output.append(quote_text)
            i += 1
            continue
        elif in_quote and stripped:
            # Continuation of quote
            output.append(convert_inline_formatting(stripped))
            i += 1
            continue
        elif in_quote and not stripped:
            output.append("")
            i += 1
            continue

        # Table detection
        if is_table_line(stripped):
            if in_list:
                output.append(r"\end{" + in_list + "}")
                output.append("")
                in_list = None

            table_latex, new_i = convert_table(lines, i)
            if table_latex:
                output.append(r"\begin{center}")
                output.append(table_latex)
                output.append(r"\end{center}")
                output.append("")
                i = new_i
                continue

        # Unordered list
        if re.match(r'^[-*+]\s+', stripped):
            if not in_list:
                output.append(r"\begin{itemize}")
                in_list = "itemize"
            elif in_list != "itemize":
                output.append(r"\end{" + in_list + "}")
                output.append("")
                output.append(r"\begin{itemize}")
                in_list = "itemize"

            item_text = re.sub(r'^[-*+]\s+', '', stripped)
            item_text = convert_inline_formatting(item_text)
            output.append(r"\item " + item_text)
            i += 1
            continue

        # Ordered list
        ordered_match = re.match(r'^(\d+)\.\s+(.+)$', stripped)
        if ordered_match:
            if not in_list:
                output.append(r"\begin{enumerate}")
                in_list = "enumerate"
            elif in_list != "enumerate":
                output.append(r"\end{" + in_list + "}")
                output.append("")
                output.append(r"\begin{enumerate}")
                in_list = "enumerate"

            item_text = convert_inline_formatting(ordered_match.group(2))
            output.append(r"\item " + item_text)
            i += 1
            continue

        # Sub-list items (indented - item or 1. item)
        sub_list_match = re.match(r'^\s{2,4}[-*+]\s+(.+)$', stripped)
        if sub_list_match:
            if in_list:
                output.append(r"\end{" + in_list + "}")
                output.append("")
            output.append(r"\begin{itemize}")
            item_text = convert_inline_formatting(sub_list_match.group(1))
            output.append(r"\item " + item_text)

            # Read remaining sub-items
            j = i + 1
            while j < len(lines) and re.match(r'^\s{2,4}[-*+]\s+', lines[j].strip()):
                sub_text = convert_inline_formatting(re.sub(r'^\s{2,4}[-*+]\s+', '', lines[j].strip()))
                output.append(r"\item " + sub_text)
                j += 1

            output.append(r"\end{itemize}")
            output.append("")
            if in_list:
                output.append(r"\begin{" + in_list + "}")
            i = j
            continue

        # Indented line — continuation of list item
        if stripped and in_list and line.startswith("  "):
            output.append(convert_inline_formatting(stripped))
            output.append("")
            i += 1
            continue

        # Regular paragraph
        if in_quote:
            output.append(r"\end{quote}")
            output.append("")
            in_quote = False
        if in_list:
            output.append(r"\end{" + in_list + "}")
            output.append("")
            in_list = None

        # Check for images
        img_match = re.match(r'!\[.*\]\(.*\)', stripped)
        if img_match:
            i += 1
            continue

        # Remove HTML comments
        if stripped.startswith("<!--") and stripped.endswith("-->"):
            i += 1
            continue

        # Regular text line
        converted = convert_inline_formatting(stripped)
        # Remove markdown links — keep text
        converted = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', converted)
        output.append(converted)
        i += 1

    # Close any open environments
    if in_code_block:
        output.append(r"\end{verbatim}}")
    if in_quote:
        output.append(r"\end{quote}")
    if in_list:
        output.append(r"\end{" + in_list + "}")

    return "\n".join(output)


def main():
    latex_parts = []

    # Preamble
    latex_parts.append(r"""\documentclass[10pt,a4paper,openany]{ctexbook}

% === Packages ===
\usepackage{amsmath,amssymb,amsthm}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{geometry}
\usepackage{fancyhdr}
\usepackage{enumitem}
\usepackage{booktabs}
\usepackage{array}
\usepackage{xcolor}
\usepackage{tikz}
\usepackage{listings}
\usepackage{longtable}

\geometry{margin=1cm,footskip=0.6cm,headsep=0.3cm}
\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    urlcolor=cyan,
}

% === Theorem environments ===
\theoremstyle{definition}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{definition}{Definition}[section]
\newtheorem{example}{Example}[section]
\theoremstyle{remark}
\newtheorem*{remark}{Remark}

% === Compact spacing ===
\setlength{\parskip}{0pt plus 0.1pt}
\setlength{\parindent}{0pt}
\setlength{\abovedisplayskip}{2pt plus 1pt minus 1pt}
\setlength{\belowdisplayskip}{2pt plus 1pt minus 1pt}
\setlength{\abovedisplayshortskip}{0pt plus 0.5pt}
\setlength{\belowdisplayshortskip}{1pt plus 0.5pt minus 0.5pt}
\setlist{nosep,leftmargin=1.2em,itemsep=0pt,topsep=0pt,partopsep=0pt,parsep=0pt}
\renewcommand{\arraystretch}{0.85}
% Compact quote environment (minimal whitespace)
\renewenvironment{quote}
  {\list{}{\leftmargin=1em\rightmargin=0pt\topsep=0.5pt\partopsep=0pt}\item[]}
  {\endlist}
% Compact center/table spacing
\setlength{\intextsep}{1pt plus 0.5pt minus 0.5pt}
\setlength{\textfloatsep}{1pt plus 0.5pt minus 0.5pt}
% Compact sections
\usepackage{titlesec}
\titlespacing{\chapter}{0pt}{-10pt plus 2pt}{4pt plus 1pt}
\titlespacing{\section}{0pt}{4pt plus 1pt}{2pt plus 0.5pt}
\titlespacing{\subsection}{0pt}{3pt plus 1pt}{1pt plus 0.5pt}
\titlespacing{\subsubsection}{0pt}{2pt plus 0.5pt}{0pt plus 0.5pt}
\pagestyle{plain}

\title{\Huge \textbf{DMA 离散数学复习笔记}}
\author{
    \Large 郑文庭老师班 \\
    \large Rosen, \textit{Discrete Mathematics and Its Applications}, 8th Edition
}
\date{\large \today}

\begin{document}

\maketitle
{\small\tableofcontents}
\newpage
\small

""")

    # Process each file
    missing_files = []
    for filename in FILE_ORDER:
        filepath = NOTES_DIR / filename
        if not filepath.exists():
            missing_files.append(filename)
            continue

        # Check if we need to insert a chapter/part header
        is_chapter_start = filename in CHAPTER_MARKERS
        if is_chapter_start:
            marker_type, title = CHAPTER_MARKERS[filename]
            if marker_type == "chapter":
                latex_parts.append(f"\n\\chapter{{{title}}}\n")
            elif marker_type == "part":
                latex_parts.append(f"\n\\part{{{title}}}\n")

        print(f"Converting: {filename}")
        try:
            content = convert_md_file(filepath)
            latex_parts.append(content)
            # Only newpage at chapter/part boundaries, not between sections
            if is_chapter_start:
                latex_parts.append("\n\\newpage\n")
            else:
                latex_parts.append("\n")
        except Exception as e:
            print(f"  ERROR converting {filename}: {e}")
            missing_files.append(filename)

    latex_parts.append(r"\end{document}")

    if missing_files:
        print(f"\nMissing/failed files ({len(missing_files)}):")
        for f in missing_files:
            print(f"  - {f}")

    # Write output
    output = "\n".join(latex_parts)

    # Post-processing: fix common issues
    # Remove empty itemize/enumerate blocks
    output = re.sub(r'\\begin\{(itemize|enumerate)\}\s*\\end\{\1\}', '', output)
    # Remove empty quote blocks
    output = re.sub(r'\\begin\{quote\}\s*\\end\{quote\}', '', output)
    # Remove empty center blocks
    output = re.sub(r'\\begin\{center\}\s*\\end\{center\}', '', output)
    # Reduce excessive newlines
    output = re.sub(r'\n{4,}', '\n\n', output)
    # Remove extra blank lines
    output = re.sub(r'\n{4,}', '\n\n', output)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"\nOutput written to: {OUTPUT_FILE}")
    print(f"Total size: {len(output):,} bytes, {output.count(chr(10)):,} lines")


if __name__ == "__main__":
    main()
