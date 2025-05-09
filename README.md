# PyiHGS-Block

**PyiHGS-Block: Python Implementation of MHI-BLOCKS for In-Air Hand Gesture Signatures**

This repository contains a Python translation of the original MATLAB algorithm for processing In-Air Hand Gesture Signatures (iHGS) using Motion History Images (MHI) and BLOCKS technique.

## Overview

This custom image processing algorithm standardizes and preserves the full sequence of in-air hand gesture signatures. It processes 2000 samples across 100 classes, representing 100 individuals, ensuring the complete preservation of information within 10 frames using MHI and a specialized image processing technique. Each sample, with dimensions 640 x 480 x N, varies in frame count (N). This algorithm uniquely standardizes these varying frame counts, encapsulating all spatio-temporal information within a concise 10-frame format.

## Original Implementation

The original algorithm was developed in MATLAB 2021a without requiring any first-party toolboxes or third-party libraries. This Python implementation aims to faithfully translate the functionality while leveraging Python's ecosystem.

## Installation

To clone this repository and start exploring the Python implementation of this image processing algorithm on your local machine:

```bash
git clone https://github.com/alvinlimfangchuen/iHGS-MHI-BLOCKS.git
```

## Requirements

- Python 3.6+
- Dependencies: [list Python dependencies here]

## Dataset

The implementation of this project is based on the In-Air Hand Gesture Signature (iHGS) database, which is currently the only publicly available image-based dataset for in-air hand gesture signature recognition. For more information on the iHGS database and to access it for your research, please visit the following link and contact the corresponding author:

[In-Air Hand Gesture Signature (iHGS) Database](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10439358/)

Please ensure you adhere to the dataset's usage guidelines and cite it appropriately in your work.

## Citation

If you use this implementation in your research, please cite the original paper:

```
@article{lim2024inair,
    title={Revolutionizing Signature Recognition: A Contactless Method with Convolutional Recurrent Neural Networks},
    author={Alvin Fang Chuen Lim, Wee How Khoh, Ying Han Pang, Hui Yen Yap},
    doi = {(https://doi.org/10.14716/ijtech.v15i4.6744)},
    journal={International Journal of Technology},
    volume={15(4)},
    pages={pp. 1102-1117},
    year={2024}
}
```

## Reference to Original Implementation

This Python implementation is a translation of the original MATLAB algorithm available at:
[Original MATLAB Implementation](https://github.com/alvinlimfangchuen/iHGS-MHI-BLOCKS)
