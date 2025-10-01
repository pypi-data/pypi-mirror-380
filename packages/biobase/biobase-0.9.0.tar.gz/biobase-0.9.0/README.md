# Biobase

[![Static Badge](https://img.shields.io/badge/Project_Name-Biobase-blue)](https://github.com/lignum-vitae/biobase)
[![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Flignum-vitae%2Fbiobase%2Fmain%2Fpyproject.toml)](https://github.com/lignum-vitae/biobase/blob/main/pyproject.toml)
[![PyPI version](https://img.shields.io/pypi/v/biobase.svg)](https://pypi.python.org/pypi/biobase)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub branch check runs](https://img.shields.io/github/check-runs/lignum-vitae/biobase/main)](https://github.com/lignum-vitae/biobase)

A Python package providing standardized biological constants and substitution matrices
for bioinformatics pipelines.
Biobase aims to eliminate the need to repeatedly recreate common biological data
structures and scoring systems in your code.

## Table of Contents

- [Quick Start](#quick-start)
  - [Access amino acid properties](#access-amino-acid-properties)
  - [Use substitution matrices](#use-substitution-matrices)
  - [Analyse DNA sequences](#analyse-dna-sequences)
  - [Find protein motifs](#find-protein-motifs)
  - [Parse FASTA](#parse-fasta)
- [Requirements](#requirements)
- [Installation](#installation)
  - [Regular Installation](#regular-installation)
  - [Development Installation](#development-installation)
- [Running Files](#running-files)
- [Data Files](#data-files)
- [Project Goals](#project-goals)
- [Contributing](#contributing)
- [License](#license)

## Quick Start

#### Access amino acid properties

```python
from biobase.constants import ONE_LETTER_CODES, MONO_MASS
print(ONE_LETTER_CODES)  # 'ACDEFGHIKLMNPQRSTVWY'
print(MONO_MASS['A'])    # 71.037113805
print(CODON_TABLE["AUG"])    # M
```

#### Use substitution matrices

```python
from biobase.matrix import Blosum
blosum62 = Blosum(62)
print(blosum62['A']['A'])  # 4
print(blosum62['W']['C'])  # -2
```

#### Analyse DNA sequences

```python
from biobase.analysis import Dna
sequence = "ATCGTAGC"
print(Dna.complement(sequence))               # 'TAGCATCG'
print(Dna.complement(sequence, reverse=True)) # 'GCTACGAT'
print(Dna.transcribe(sequence))               # 'AUCGUAGC'
print(Dna.translate(sequence))                # 'IV'
print(Dna.calculate_gc_content(sequence))     # 50.0
print(Dna.calculate_at_content(sequence))     # 50.0
print(Dna.entropy(sequence))                  # 2.0

seq = "ccatgccctaaatggggtag"
for start, end, orf in Dna.find_orfs(seq, include_seq=True)
    print(start, end, orf)
# 2, 11, "ATGCCCTAA"
# 11, 20, "ATGGGGTAG"
```

#### Analyse Nucleotides

```python
from biobase.analysis import Nucleotides

print(Nucleotides.molecular_weight("A"))               # 135.13
print(Nucleotides.cumulative_molecular_weight("ATCG")) # 523.48
print(Nucleotides.translate("AUGUUGUCGCCUU"))          # 'MLSP'
```

#### Find protein motifs

```python
from biobase.analysis import find_motifs
sequence = "ACDEFGHIKLMNPQRSTVWY"
print(find_motifs(sequence, "DEF"))
# [(1, 4)]

test_dict = {
    ">SP001": "ACDEFCDEFCDEFGHIKLMN",  # has matches for "CDE" that span indexes [(1, 4), (5, 8), (9, 12)]
    ">SP002": "MNPQRSTVWYACDEFGHIKL",  # has match for "CDE" that span indexes [(11, 14)]
    ">SP003": "AAAAAAAAAAAAAAAAAA12",  # invalid: contains "1", "2"
    ">SP004": "GGGGGGGGGGGGGGGGGGGG",  # no match
    ">SP005": "HHHHHHHHHHHHHHHHH@#$",  # invalid: contains "@", "#", "$"
    ">SP006": "DDDDDDDDDDDDDDDDDDDD",  # no match
    ">SP007": "CDEFGHCDEFKLCDEFPQRS",  # has matches for "CDE" that span indexes [(0, 3), (6, 9), (12, 15)]
    ">SP008": "LLLLLLLLLLLLLLLLLLLL",  # no match
    ">SP009": "KKKKKKKKKKKK123KKKKK",  # invalid: contains "1", "2", "3"
    ">SP010": "CDEACDEDCDEFAAAAAAAA",  # has matches for "CDE" that span indexes [(0, 3), (4, 7), (8, 11)]
}
matched, invalid, non_match = find_motifs(test_dict, "CDE")
print("Matches:")
for seq, matches in matched.items():
    print(f"{seq}")
    print(f"{"".join([f"{match[0]} to {match[1]}\n" for match in matches])}")
print(f"Invalid sequences:\n{"".join([f"{seq}: {invs}\n" for seq, invs in invalid.items()])}")
print(f"Sequences without matches:\n{"".join([f"- {nm}\n" for nm in non_match])}")

# Matches:
# >SP001
# 1 to 4
# 5 to 8
# 9 to 12

# >SP002
# 11 to 14

# >SP007
# 0 to 3
# 6 to 9
# 12 to 15

# >SP010
# 0 to 3
# 4 to 7
# 8 to 11

# Invalid sequences:
# >SP003: {'2', '1'}
# >SP005: {'$', '@', '#'}
# >SP009: {'2', '1', '3'}

# Sequences without matches:
# - >SP004
# - >SP006
# - >SP008
```

#### Parse FASTA

```python
from biobase.parser import FastaParser, fasta_parser
fasta = """>CAA39742.1 cytochrome b (mitochondrion) [Sus scrofa]
MTNIRKSHPLMKIINNAFIDLPAPSNISSWWNFGSLLGICLILQILTGLFLAMHYTSDTTTAFSSVTHIC"""

# Class that yields generator
records = list(FastaParser(fasta))
r: FastaRecord = records[0]
print(r.id) # CAA39742.1
print(r.seq) # MTNIRKSHPLMKIINNAFIDLPAPSNISSWWNFGSLLGICLILQILTGLFLAMHYTSDTTTAFSSVTHIC

# Function that returns list
records = fasta_parser(fasta)
for r in records:
    print(r.id) # CAA39742.1
    print(r.seq) # MTNIRKSHPLMKIINNAFIDLPAPSNISSWWNFGSLLGICLILQILTGLFLAMHYTSDTTTAFSSVTHIC

```

#### Parse FASTQ

```python
from biobase.parser import FastqParser, fastq_parser
fastq = """@2fa9ee19-5c51-4281-abdd-eac86
CGGTAGCCAGCTGCGTTCAGTATG
+
%%%+++'''@@@???<<<??????"""

# Class that yields generator
records = list(FastqParser(fastq))
r: FastqRecord = records[0]
print(r.id) # 2fa9ee19-5c51-4281-abdd-eac86
print(r.seq) # CGGTAGCCAGCTGCGTTCAGTATG

# Function that returns list
records = fastq_parser(fastq)
for r in records:
    print(r.id) # 2fa9ee19-5c51-4281-abdd-eac86
    print(r.seq) # CGGTAGCCAGCTGCGTTCAGTATG
```

## Requirements

- Python 3.10+
- pip (for installation)

## Installation

### Regular Installation

`pip install biobase`

### Development Installation

Clone the repository and install in editable mode:

```nginx
git clone https://github.com/lignum-vitae/biobase.git
cd biobase
uv pip install -e ".[dev]"
```

Files can be run using `uv run <file_name>` if in the same directory/folder
as the file.

If not using uv, to ensure that relative imports correctly work, run files using
the module path from the project root. To run the sub_matrix file, use the command
`python -m src.biobase.matrix.sub_matrix`

## Data Files

- `src/biobase/matrices/`: Scoring matrix data stored in JSON file format

## Project Goals

Biobase aims to provide Python-friendly versions of common biological constants
and tools for bioinformatics pipelines. Key objectives:

1. Standardize biological data structures
2. Provide efficient implementations of common scoring systems
3. Ensure type safety and validation
4. Maintain comprehensive documentation
5. Support modern Python practices

## Contributing

We welcome contributions! Please read our:

- [Code of Conduct](https://github.com/lignum-vitae/biobase/blob/main/docs/CODE_OF_CONDUCT.md)
- [Contribution Guidelines](https://github.com/lignum-vitae/biobase/blob/main/docs/CONTRIBUTING.md)

### Stability

This project is in the beta stage. APIs may change without warning until version
1.0.0.

## License

This project is licensed under the MIT License - see the
[LICENSE](https://github.com/lignum-vitae/biobase/blob/main/LICENSE) file for details.
