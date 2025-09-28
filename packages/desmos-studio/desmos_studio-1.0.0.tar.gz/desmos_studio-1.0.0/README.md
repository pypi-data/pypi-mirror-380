# image2curves 🎨➡️📐

[![PyPI version](https://badge.fury.io/py/image2curves.svg)](https://badge.fury.io/py/image2curves)
[![Python versions](https://img.shields.io/pypi/pyversions/image2curves.svg)](https://pypi.org/project/image2curves/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Convert any image into mathematical curves! Transform JPEGs, PNGs, and other images into:
- **Desmos graphing calculator equations** (parametric Bézier curves)
- **Matplotlib plots** (publication-ready vector graphics)

Perfect for creating mathematical art, importing images into Desmos, or generating clean vector graphics from photos.

## ✨ Features

- 🖼️ **Multiple input formats**: JPEG, PNG, GIF, BMP, TIFF, and more
- 📈 **Desmos equations**: Copy-paste parametric equations directly into Desmos
- 📊 **Matplotlib plots**: High-quality vector graphics with customizable styling
- ⚡ **CLI interface**: Simple command-line tool with intuitive options
- 🎛️ **Customizable**: Adjust tracing threshold, grid display, and output formats
- 🔧 **Professional**: Built on industry-standard tools (Potrace, ImageMagick)

## 🚀 Quick Start

### Installation

```bash
pip install image2curves
```

**System Requirements:**
- [ImageMagick](https://imagemagick.org/script/download.php) - for image processing
- [Potrace](http://potrace.sourceforge.net/#downloading) - for curve tracing

**Install system dependencies:**

```bash
# Ubuntu/Debian
sudo apt-get install imagemagick potrace

# macOS (with Homebrew)
brew install imagemagick potrace

# Windows (with Chocolatey)
choco install imagemagick potrace
```

### Basic Usage

```bash
# Create a matplotlib plot
image2curves photo.jpg

# Generate Desmos equations
image2curves photo.jpg --mode desmos

# Create both outputs
image2curves photo.jpg --mode both

# Custom output filename
image2curves photo.jpg --output my_curves.png

# Adjust tracing sensitivity
image2curves photo.jpg --threshold 30
```

### Example Output

**Input Image:**
```
photo.jpg (your image file)
```

**Matplotlib Output:**
```
photo_plot.png - Clean vector graphic visualization
```

**Desmos Output:**
```
photo_equations.txt - Parametric equations like:
((1-t)^3*156.2 + 3*(1-t)^2*t*158.1 + 3*(1-t)*t^2*160.3 + t^3*162.1,(1-t)^3*89.4 + 3*(1-t)^2*t*91.2 + 3*(1-t)*t^2*93.8 + t^3*95.6)
```

## 📖 Usage Examples

### Create Mathematical Art
```bash
# High contrast tracing for clean curves
image2curves artwork.jpg --threshold 20 --output clean_art.png

# Multiple outputs for analysis
image2curves logo.png --mode both --keep-temp
```

### Desmos Graphing
```bash
# Generate equations optimized for Desmos
image2curves drawing.jpg --mode desmos --threshold 40

# Then copy equations from the output file into Desmos!
```

### Publication Graphics
```bash
# High-quality plot without grid
image2curves diagram.png --no-grid --output figure1.png
```

## 🛠️ Advanced Options

```bash
image2curves [INPUT_IMAGE] [OPTIONS]

Required:
  INPUT_IMAGE              Input image file

Options:
  -m, --mode {plot,desmos,both}
                          Output mode (default: plot)
  -o, --output OUTPUT     Custom output filename
  -t, --threshold N       Black/white threshold 0-100 (default: 50)
  --no-grid              Disable grid in matplotlib plots
  --keep-temp            Keep temporary PBM and SVG files
  --version              Show version information
  -h, --help             Show help message

Examples:
  image2curves image.jpg --mode plot
  image2curves image.jpg --mode desmos  
  image2curves image.jpg --mode both
  image2curves image.jpg --threshold 30 --no-grid
```

## 🔧 How It Works

1. **Image Processing**: Converts input image to black & white using ImageMagick
2. **Curve Tracing**: Uses Potrace to trace bitmap into smooth Bézier curves
3. **Export**: Converts SVG curves to your chosen format:
   - **Matplotlib**: Renders curves as publication-quality plots
   - **Desmos**: Exports parametric equations for direct import

## 🎨 Use Cases

- **Education**: Create mathematical representations of real-world objects
- **Art**: Generate algorithmic art from photographs  
- **Graphing**: Import complex shapes into Desmos graphing calculator
- **Research**: Convert diagrams into vector graphics for publications
- **Design**: Create clean, scalable graphics from bitmap images

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup
```bash
git clone https://github.com/yourusername/image2curves.git
cd image2curves
pip install -e .[dev]
```

### Running Tests
```bash
pytest tests/
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Potrace](http://potrace.sourceforge.net/) by Peter Selinger - excellent bitmap tracing
- [ImageMagick](https://imagemagick.org/) - powerful image processing
- [svgpathtools](https://github.com/mathandy/svgpathtools) - SVG path manipulation
- [matplotlib](https://matplotlib.org/) - plotting library

## 📊 Stats

![GitHub stars](https://img.shields.io/github/stars/yourusername/image2curves)
![PyPI downloads](https://img.shields.io/pypi/dm/image2curves)

---

**Created with ❤️ for the mathematical art community**