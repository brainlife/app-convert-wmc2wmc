<h1 align="center">Convert wmc-deprecated to wmc</h1>

<p align="center">
  A current white matter classification (<code>neuro/wmc</code>) from a classification stored in the deprecated <code>neuro/wmc-deprecated</code> datatype.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.201"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.201-blue.svg" alt="Run on brainlife.io"></a>
  <a href="https://github.com/brainlife/app-convert-wmc2wmc/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-MIT-lightgrey.svg" alt="MIT license"></a>
</p>

> 📍 **This branch, `1.0`, is the brainlife.io App Convert wmc-deprecated to wmc** ([doi:10.25663/brainlife.app.201](https://doi.org/10.25663/brainlife.app.201)).

## 🧠 At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Converts a deprecated white matter classification (wmc-deprecated, output.mat) into the current wmc datatype (classification.mat with tract JSONs and surfaces).**

Saves the classification structure from the old output.mat as classification.mat, copies any surfaces, and rewrites the tract JSON files with coordinates rounded to two decimals. The new datatype stores only streamline indices, so it must be used together with the original tractogram. Use it to make old classifications usable by current Apps. Utility App.

| | |
|---|---|
| 📥 **Inputs** | `neuro/wmc-deprecated` |
| 📤 **Outputs** | `neuro/wmc` |
| 🐳 **Container** | `brainlife/python:2.7.16` |
| ⚙️ **Resources** | 1 CPUs · 0.08 h walltime |
| 🔗 **Run it** | [doi.org/10.25663/brainlife.app.201](https://doi.org/10.25663/brainlife.app.201) |

#### 📥 Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `0` | `neuro/wmc-deprecated` | yes | Deprecated WMC classification (output.mat with tracts/ JSON files and optional surfaces/). |

#### 📤 Outputs

| Output | Datatype | Description |
|---|---|---|
| `wmc` | `neuro/wmc` | WMC classification (classification.mat with streamline indices, tracts/ JSONs and surfaces/). |

<!-- brainlife-app:end -->

## 🚀 Running the App

### ☁️ On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.201](https://doi.org/10.25663/brainlife.app.201), choose a `neuro/wmc-deprecated` dataset from your project and press **Execute**. The App archives a `neuro/wmc` dataset that current segmentation and tract-profile Apps can read.

The two datatypes differ in what they store. The deprecated one holds both the streamline indices into the original tractogram and the streamline coordinates (in `output.mat`); the new one holds only the indices (in `classification.mat`). Always use the converted classification together with the original tractogram.

### 💻 Locally

You need [Singularity/Apptainer](https://apptainer.org/). The App runs Python 2.7 with SciPy from the `brainlife/python:2.7.16` container.

1. Clone this repository and check out the App branch: `git checkout 1.0`.
2. Create `config.json` with the path to the old `output.mat`; its directory must also contain `tracts/` (and, optionally, `surfaces/`):

   ```json
   {
       "segmentation": "/input/wmc/output.mat"
   }
   ```

3. Run the App:

   ```bash
   ./main
   ```

## 📦 Outputs

```text
wmc/
├── classification.mat   MATLAB struct `classification` with `names` and `index`
├── tracts/              one JSON per tract (coordinates rounded to two decimals) and tracts.json
└── surfaces/            copied from the input when present
```

`names` lists the tracts identified; `index` is a vector with one entry per streamline of the original tractogram, zero for unassigned streamlines and otherwise the position of the streamline's tract in `names`.

## 🩺 Troubleshooting

- **`Conversion failed.`**: the `wmc` output directory is empty. Check that the input contains `output.mat` and `tracts/`.

## 📚 Citing

> [!TIP]
> If you use this App in your work, please cite the App, the software it builds on and brainlife.io (below). GitHub's **Cite this repository** button gives the App citation in APA and BibTeX.

- Convert wmc-deprecated to wmc. brainlife.io App. [doi:10.25663/brainlife.app.201](https://doi.org/10.25663/brainlife.app.201)
- Avesani P. et al. The open diffusion data derivatives. Sci Data 6, 69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)

## 👥 Authors

- Giulia Bertò

**Contributors:** Soichi Hayashi

## 💰 Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io is publicly funded, and acknowledging that support helps keep it running. This App was developed with support from Wellcome, the U.S. National Institutes of Health (including the BRAIN Initiative BRAIN CONNECTS program: The Axonal Projectome EXchange, U24NS140384, and the Center for Mesoscale Connectomics, UM1NS132207) and the U.S. National Science Foundation.</sub>

## ⚖️ License

MIT, Copyright (c) 2020 brainlife.io, The University of Texas at Austin and Indiana University.
