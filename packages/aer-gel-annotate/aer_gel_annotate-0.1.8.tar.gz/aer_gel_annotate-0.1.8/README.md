# Gel Annotate

**Gel Annotate** is a Python package + GUI tool for automated detection and annotation of gel electrophoresis wells, ladders, and PCR bands.  
It was developed for lab workflows to speed up gel image analysis and make the results reproducible and easy to share.

---

## Features

- Automatic detection of **sample wells** and **ladder wells** from gel images (TIFF, PNG, JPG, etc.).
- **PCR band detection** with adjustable thresholds.
- Interactive **PyQt5 GUI**:
  - View annotated gels with labeled wells/bands.
  - Edit probable wells manually by typing coordinates.
  - Save and reload results (`.json`).
  - Export results to CSV or JSON.
  - Save annotated PNGs for reports.
- Command-line interface for batch processing.
- Cross-platform (Windows, Linux, macOS).
- Optional desktop/start menu shortcuts for quick access.

---

## Installation

You can install from PyPI:

```bash
pip install aer-gel-annotate
````

On Windows (to allow shortcut creation), install with:

```bash
pip install aer-gel-annotate[windows]
```

---

## Usage

### Run the GUI

After installation:

```bash
gel-annotate
```

This opens the GUI application.

### Run the CLI

For quick batch analysis:

```bash
gel-annotate-cli path/to/gel_image.tif --ladder --detect_bars
```

---

## GUI Overview

* **Top row**:

  * Select an image file.
  * Set detection parameters (comb size, combs per row, ladder/band detection).
  * Run detection.

* **Left sidebar**:

  * Manual overrides (force YES/NO for PCR bands).
  * Detected wells and ladder wells (read-only).
  * Probable wells (editable — add/modify coordinates).
  * Save/export options (PNG, CSV, JSON).
  * Load JSON results.

* **Main area**:

  * Annotated gel image with labeled wells and bands.

---

## Export & Reload Results

* **CSV**: table of wells, ladder wells, bands.
* **JSON**: full structured result (including probable wells, ladder bands, etc.).

You can later reload a JSON file into the GUI, edit probable wells, and re-run detection.

---

##  Application Shortcuts

* To create a desktop/start menu shortcut (after installation):

```bash
gel-annotate-shortcut
```

* On Linux, this creates a `.desktop` entry under `~/.local/share/applications` and your Desktop.
* On Windows, it creates `Gel Annotate.lnk` on Desktop and in the Start Menu.
* On macOS, it creates a `Gel Annotate.command` launcher on the Desktop.


---

## ️ Development

Clone the repository and install in editable mode:

```bash
git clone https://github.com/your-org/aer-gel-annotate
cd aer-gel-annotate
pip install -e .[windows]  # add [windows] on Windows
```

Run the GUI locally:

```bash
python -m annotation.gui.gel_gui_wrapper
```

---

##  License

MIT License © 2025 Manan Shah
