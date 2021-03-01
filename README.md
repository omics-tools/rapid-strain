Rapid-Strain
====
Rapid estimation of microbial strains from NGS data

## Requirement python packages
pandas (Test enviroment: Python 2.7)

## Requirement tools

・[MASH](https://mash.readthedocs.io/en/latest/index.html): Fast genome and metagenome distance estimation using MinHash

・[SeqKit](https://bioinf.shenwei.me/seqkit/): a cross-platform and ultrafast toolkit for FASTA/Q file manipulation

Please refer to the official site for details of the installation of these packages.

## Installation
Clone this repository into your local machine
`git clone https://github.com/omics-tools/rapid-strain.git`

Set up for requirement packages
`pip install pandas`

## Getting started

### Usage

`python rapid-strain.py -fa query.fa -t species/genus [-p threads ]`

**optional arguments:**

| Flag | Description | File type, Default, Example etc. |
|:-----------|:------------|:------------|
| **-fa**      | input FASTA (may be gzipped) |.fa/.fas/.fasta|
| **-fq**      | input FASTQ (may be gzipped) |.fq/fastq|
| **-t**       | target genus/species (See the list of supported genus/species names) (**required**) | (e.g.) -t campylobacter |
| **-p**       | Multi threads process for mash  | default: 1 |
| **-tmp**     | Temporary output directory | default: The directory in the input file |
| **-v**       | Program's version number and exit  | |
| **-h**       | Help message and exit         | |

## Version

0.0.1 (beta)

## Licence

[MIT] https://github.com/omics-tools/mitoimp/blob/master/LICENSE
