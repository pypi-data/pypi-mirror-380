[![Binder](https://mybinder.org/badge_logo.svg)](
  https://mybinder.org/v2/gh/panschai/PyFV/main?labpath=notebooks%2FPyFV-lite.ipynb
)

# PyFV

PyFV is a modern, open-source rebirth of NASA’s classic FV (FITS Viewer.)

Rewritten in Python, PyFV provides astronomers, students, and enthusiasts with tools to explore 
and analyze FITS files in a clean, portable, and extensible way.  

Legacy preserved. Future enabled. Open to all.

---

## Features

- FITS Support — Open and explore FITS images and tables
- WCS Integration — Display world coordinate system (RA/Dec) when available
- Plotting — Visualize columns, histograms, and image slices
- Table Viewer — Inspect and filter FITS table HDUs
- Scalings — Linear, logarithmic, sqrt, asinh, and more
- Jupyter Support — Run PyFV Lite in the browser, no install required (via Binder/Colab, coming soon)

---

## Demo

Here is a quick look at PyFV in action:

![PyFV Demo](demo/pow.gif)

---

## Quick Start

### Local (Python)
   Clone the repository and install dependencies:

       git clone https://github.com/panchai/PyFV.git
       cd PyFV
       pip install -r requirements.txt

   (Option)

       pip install pyfv

   Run the FITS viewer:

      python src/pyfv/fv.py data/sample.image.fits

   In Jupyter (PyFV Lite)

      Notebook demos are available in the notebooks/ folder:

         jupyter notebook notebooks/PyFV-lite.ipynb

      Binder/Colab badges will be added soon for one-click browser runs.

         Examples
         FITS Image
         FITS Table

### Documentation

   Legacy FV help documentation is preserved in the doc/ folder (HTML format).  This includes explanations of FITS formats, plotting, and usage examples.

### History and Stewardship

The original FV (FITS Viewer) was developed at NASA in the late 1990s as part of the HEASARC mission tools suite. I have been its caretaker since 2001, ensuring it continued to serve astronomers, students, and researchers for more than two decades.

When my time at NASA came to a close, I am placing this Python-based FV, renamed as PyFV, on GitHub to preserve its legacy, ensure its survival, and open it to the future — even though there were efforts to quietly set it aside after it had already been demonstrated to succeed.

For the engineers and scientists who first created FV, PyFV is both a tribute to that history and a new beginning — lightweight, modern, and accessible to all.

### License

   This project is released under the BSD 3-Clause License.
   See the LICENSE file for details.
   © 2025 Pan S. Chai

### Acknowledgments

  - The original FV (FITS Viewer) developed and maintained at NASA since the 1990s
  - The Astropy Project for core FITS and WCS functionality
  - The astronomy community for keeping open science alive

### About the Author

  Pan S. Chai is a software engineer and scientist with a long history at NASA, where he worked on mission-critical astronomical tools. PyFV is his effort to ensure that the beloved FV viewer continues to live on for future generations.
