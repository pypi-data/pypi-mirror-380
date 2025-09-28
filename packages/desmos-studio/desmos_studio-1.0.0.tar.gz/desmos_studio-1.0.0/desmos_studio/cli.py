#!/usr/bin/env python3
"""
image2curves - Convert images to mathematical curves
"""

import subprocess
import os
import argparse
import sys
from pathlib import Path
import matplotlib
matplotlib.use('Agg')  # for headless servers
import matplotlib.pyplot as plt
from svgpathtools import svg2paths


class Image2Curves:
    def __init__(self):
        self.temp_files = []
    
    def cleanup(self):
        """Remove temporary files"""
        for file in self.temp_files:
            if os.path.exists(file):
                os.remove(file)
    
    def jpeg_to_pbm(self, input_image, output_pbm, threshold=50):
        """Convert image to black and white bitmap"""
        if not os.path.exists(input_image):
            raise FileNotFoundError(f"Input image not found: {input_image}")

        try:
            subprocess.run([
                "convert", input_image,
                "-threshold", f"{threshold}%",
                output_pbm
            ], check=True, capture_output=True, text=True)
            print(f"✅ Converted to bitmap: {output_pbm}")
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"ImageMagick conversion failed: {e.stderr}")
        except FileNotFoundError:
            raise RuntimeError("ImageMagick 'convert' command not found. Please install ImageMagick.")

    def pbm_to_svg(self, pbm_file, svg_file):
        """Trace bitmap to SVG using Potrace"""
        if not os.path.exists(pbm_file):
            raise FileNotFoundError(f"PBM file not found: {pbm_file}")

        try:
            subprocess.run([
                "potrace", pbm_file,
                "-s",               # SVG output
                "-o", svg_file
            ], check=True, capture_output=True, text=True)
            print(f"✅ Traced to SVG: {svg_file}")
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Potrace tracing failed: {e.stderr}")
        except FileNotFoundError:
            raise RuntimeError("Potrace command not found. Please install potrace.")

    def export_matplotlib(self, svg_file, output_png, show_grid=True):
        """Export SVG as matplotlib plot"""
        if not os.path.exists(svg_file):
            raise FileNotFoundError(f"SVG file not found: {svg_file}")

        try:
            paths, _ = svg2paths(svg_file)
            total_curves = sum(len(path) for path in paths)

            plt.figure(figsize=(10, 10))
            
            for path in paths:
                for seg in path:
                    # Sample points along the segment
                    points = [seg.point(t/100.0) for t in range(101)]
                    x = [p.real for p in points]
                    y = [-p.imag for p in points]  # flip Y axis for standard orientation
                    plt.plot(x, y, 'k', linewidth=1)

            if show_grid:
                plt.grid(True, alpha=0.3)
            plt.axis('equal')
            plt.title(f'Traced Image ({total_curves} curves)')
            plt.tight_layout()
            plt.savefig(output_png, dpi=300, bbox_inches='tight')
            plt.close()  # Free memory
            
            print(f"✅ Matplotlib plot saved: {output_png} ({total_curves} curves)")
            
        except Exception as e:
            raise RuntimeError(f"Matplotlib export failed: {e}")

    def export_desmos(self, svg_file, output_file):
        """Export SVG as Desmos equations"""
        if not os.path.exists(svg_file):
            raise FileNotFoundError(f"SVG file not found: {svg_file}")

        try:
            paths, _ = svg2paths(svg_file)
            
            with open(output_file, "w") as f:
                curve_count = 0
                for path in paths:
                    for seg in path:
                        if seg.__class__.__name__ == "CubicBezier":
                            x0, y0 = seg.start.real, -seg.start.imag  # flip Y
                            x1, y1 = seg.control1.real, -seg.control1.imag
                            x2, y2 = seg.control2.real, -seg.control2.imag
                            x3, y3 = seg.end.real, -seg.end.imag

                            f.write(f"((1-t)^3*{x0} + 3*(1-t)^2*t*{x1} + 3*(1-t)*t^2*{x2} + t^3*{x3},"
                                   f"(1-t)^3*{y0} + 3*(1-t)^2*t*{y1} + 3*(1-t)*t^2*{y2} + t^3*{y3})\n")
                            curve_count += 1

                        else:
                            # Handle lines/other segments as degenerate cubic Béziers
                            x0, y0 = seg.start.real, -seg.start.imag
                            x3, y3 = seg.end.real, -seg.end.imag
                            x1, y1 = x0 + (x3-x0)/3, y0 + (y3-y0)/3
                            x2, y2 = x0 + 2*(x3-x0)/3, y0 + 2*(y3-y0)/3
                            
                            f.write(f"((1-t)^3*{x0}+3*(1-t)^2*t*{x1}+3*(1-t)*t^2*{x2}+t^3*{x3},"
                                   f"(1-t)^3*{y0}+3*(1-t)^2*t*{y1}+3*(1-t)*t^2*{y2}+t^3*{y3})\n")
                            curve_count += 1

            print(f"✅ Desmos equations exported: {output_file} ({curve_count} curves)")
            
        except Exception as e:
            raise RuntimeError(f"Desmos export failed: {e}")

    def process_image(self, input_image, output_mode, output_file=None, threshold=50, 
                     show_grid=True, keep_temp=False):
        """Main processing function"""
        input_path = Path(input_image)
        if not input_path.exists():
            raise FileNotFoundError(f"Input image not found: {input_image}")
        
        # Generate temporary file names
        base_name = input_path.stem
        pbm_file = f"{base_name}_temp.pbm"
        svg_file = f"{base_name}_temp.svg"
        
        self.temp_files = [pbm_file, svg_file]
        
        try:
            # Step 1: Convert to bitmap
            self.jpeg_to_pbm(input_image, pbm_file, threshold)
            
            # Step 2: Trace to SVG
            self.pbm_to_svg(pbm_file, svg_file)
            
            # Step 3: Export based on mode
            if output_mode == 'plot':
                if not output_file:
                    output_file = f"{base_name}_plot.png"
                self.export_matplotlib(svg_file, output_file, show_grid)
                
            elif output_mode == 'desmos':
                if not output_file:
                    output_file = f"{base_name}_equations.txt"
                self.export_desmos(svg_file, output_file)
                
            elif output_mode == 'both':
                plot_file = output_file or f"{base_name}_plot.png"
                desmos_file = f"{base_name}_equations.txt"
                
                if output_file and output_file.endswith('.png'):
                    plot_file = output_file
                    desmos_file = f"{base_name}_equations.txt"
                elif output_file and output_file.endswith('.txt'):
                    desmos_file = output_file  
                    plot_file = f"{base_name}_plot.png"
                
                self.export_matplotlib(svg_file, plot_file, show_grid)
                self.export_desmos(svg_file, desmos_file)
            
        finally:
            if not keep_temp:
                self.cleanup()


def main():
    parser = argparse.ArgumentParser(
        description='Convert images to mathematical curves (Desmos equations or matplotlib plots)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s image.jpg --mode plot                    # Create matplotlib plot
  %(prog)s image.jpg --mode desmos                  # Create Desmos equations
  %(prog)s image.jpg --mode both                    # Create both outputs
  %(prog)s image.jpg --mode plot --output result.png # Custom output filename
  %(prog)s image.jpg --threshold 30 --no-grid      # Custom threshold, no grid
        """
    )
    
    parser.add_argument('input_image', 
                       help='Input image file (JPEG, PNG, etc.)')
    
    parser.add_argument('--mode', '-m', 
                       choices=['plot', 'desmos', 'both'], 
                       default='plot',
                       help='Output mode (default: plot)')
    
    parser.add_argument('--output', '-o',
                       help='Output filename (optional)')
    
    parser.add_argument('--threshold', '-t', 
                       type=int, default=50, 
                       metavar='N',
                       help='Black/white threshold 0-100 (default: 50)')
    
    parser.add_argument('--no-grid', 
                       action='store_true',
                       help='Disable grid in matplotlib plots')
    
    parser.add_argument('--keep-temp', 
                       action='store_true',
                       help='Keep temporary PBM and SVG files')
    
    parser.add_argument('--version', 
                       action='version', 
                       version='%(prog)s 1.0.0')

    args = parser.parse_args()
    
    # Validate threshold
    if not 0 <= args.threshold <= 100:
        print("Error: Threshold must be between 0 and 100")
        sys.exit(1)
    
    converter = Image2Curves()
    
    try:
        converter.process_image(
            input_image=args.input_image,
            output_mode=args.mode,
            output_file=args.output,
            threshold=args.threshold,
            show_grid=not args.no_grid,
            keep_temp=args.keep_temp
        )
        print("🎉 Conversion completed successfully!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()