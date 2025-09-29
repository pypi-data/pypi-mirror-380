<div align="center">

<!-- omit in toc -->
# RNA-SyntHub 🧬
<strong>Meta-scoring pipeline to prepare curated synthetic RNA structure data</strong>

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Python](https://img.shields.io/pypi/pyversions/tensorflow.svg)](https://badge.fury.io/py/tensorflow)

</div>

![](data/img/figures/pipeline.png)

RNA-SyntHub is a pipeline applied to create curated RNA structures data. 
It has been applied to a set of [447,402 synthetic RNA](https://www.kaggle.com/datasets/andrewfavor/uw-synthetic-rna-structures) structures 
and enforced by predictions from [RNAComposer](https://rnacomposer.cs.put.poznan.pl/) and [Boltz-1](https://github.com/jwohlwend/boltz). 

# Repo structure:

To download the data of RNA-SyntHub (structures from RFDiffusion, RNAComposer and Boltz-1), you can find the data on this [link]().
The repo is structured as follows:

- `data/`: folder containing the data used in the repo (figures, example pdb files, etc.) as well as the `.pdb` structures
  - `img/`: folder containing the figures used in the README
  - `pdb/`: folder containing example `.pdb` files
  - `examples`: folder containing example output files of the different steps of the pipeline
  - `metadata`: folder containing example extracted information from the RNA-SyntHub dataset
  - `times`: folder containing times benchmark on the subset of 1000 structures
- `src/`: folder containing the source code of the pipeline and the visualisation
- `Makefile`: file to run the different steps of the pipeline and visualisation

# Installation

To compute molprobity scores, you need to install [RNAqua](https://github.com/mantczak/rnaqua) using: 
```bash
make install_rnaqua
```
To compute alignment, you need to install [mlocarna](https://github.com/s-will/LocARNA) and [cd-hit](https://sites.google.com/view/cd-hit).
You can go to `src/rna_synthub/locarna_helper.py` to change the path of the binaries if needed.
For `cd-hit`, you need to compile it first using:
```bash
make install_cd_hit
```

You can install the visualisation using pip:
```bash
pip install rna_synthub
```

# Usage

## Pipeline steps
If you want to reproduce the pipeline, please go the the `src/analyze/script_example.py` where there is a step-by-step example of the pipeline usage.
You just need to uncomment the main function and run the script you want. 
Examples are provided with 10 `.pdb` files.
The different steps of the pipeline are as follows:

```python
def main():
    ScriptExample.compute_n_meta()
    ScriptExample.compute_filter()
    ScriptExample.compute_2d()
    ScriptExample.compute_clustering()
```

You can run the script using:
```bash
make run_example
```
or, if you installed the library using pip:
```bash
python synt_example
```


## Viz steps

To run the code to obtain the different visualisation, you can use: 
```bash
make run_viz
```
or, if you installed the library using pip: 
```bash
python viz_cli
```

You can also have a look at the `src/viz/viz_cli.py` to choose which visualisation you want to run.

```python
def main():
    VizCLI.viz_funnel()
    VizCLI.viz_filter()
    VizCLI.viz_best_worst()
    VizCLI.viz_distance()
    VizCLI.viz_sf()
    VizCLI.viz_times()
    VizCLI.viz_angles()
```


## Citation

## Authors
- Clement Bernard
- Marek Justyna
- Guillaume Postic
- Maciej Antczak
- Fariza Tahi
- Marta Szachniuk