[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.201-blue.svg)](https://doi.org/10.25663/brainlife.app.201)

# app-convert-wmc2wmc
This App converts the White Matter Classification (WMC) structure deprecated datatype to the new WMC datatype. The main difference between the two datatypes is that, while the first one contains both the fiber indexes related to the original tractogram and the fiber coordinates (in the structure output.mat), the second one only contains the fiber indexes (in the structure classification.mat). For this reason, it is important that the new WMC datatype is always used in concomitance with the original tractogram, because it does not contain the fiber coordinates. 

### Authors
- [Giulia Bertò](giulia.berto.4@gmail.com)

### Contributors
- [Soichi Hayashi](hayashis@iu.edu)

### Funding Acknowledgement
brainlife.io is publicly funded and for the sustainability of the project it is helpful to Acknowledge the use of the platform. We kindly ask that you acknowledge the funding below in your publications and code reusing this code.

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)

### Citations
We kindly ask that you cite the following articles when publishing papers and code using this code. 

Avesani, P., McPherson, B., Hayashi, S. et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. Sci Data 6, 69 (2019). [https://doi.org/10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Running the App 

### On Brainlife.io

You can submit this App online at [https://doi.org/10.25663/bl.app.201](https://doi.org/10.25663/bl.app.201) via the "Execute" tab.

### Running Locally (on your machine)

1. git clone this repo.
2. Inside the cloned directory, create `config.json` with something like the following content with paths to your input files.

```json
{
        "segmentation": "./output.mat",
}
```

3. Launch the App by executing `main`

```bash
./main
```

## Output

The relevant output for this application is a classification structure. The classification structure is a .mat file which contains a matlab structure (entitled classification) with two fields: names and index. The names field lists the names of tracts which were identified by this process as strings. The index field is a 1 dimensional vector containing zeros for all unidentified streamlines, and integer index values corresponding to streamlines' membership in the corresponding structure of the names vector.

### Dependencies

This App only requires [singularity](https://www.sylabs.io/singularity/) to run.

#### MIT Copyright (c) 2020 brainlife.io The University of Texas at Austin and Indiana University
