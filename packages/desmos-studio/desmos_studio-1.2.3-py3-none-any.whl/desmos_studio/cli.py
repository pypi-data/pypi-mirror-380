#!/usr/bin/env python3
"""
image2curves - Convert images to mathematical curves
"""

import subprocess
import os
import argparse
import sys
from pathlib import Path
import numpy as np
import cv2
import matplotlib
matplotlib.use('Agg')  # for headless servers
import matplotlib.pyplot as plt
from svgpathtools import svg2paths
import tempfile
import shutil


class Image2Curves:
    def __init__(self):
        self.temp_files = []
    
    def extract_frames(self, video_path, output_dir, max_frames=None, fps=None):
        """Extract frames from video"""
        if not os.path.exists(video_path):
            raise FileNotFoundError(f"Video file not found: {video_path}")
        
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        
        # Open video
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            raise RuntimeError(f"Could not open video: {video_path}")
        
        # Get video properties
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        video_fps = cap.get(cv2.CAP_PROP_FPS)
        
        print(f"📹 Video info: {total_frames} frames at {video_fps:.2f} FPS")
        
        # Calculate frame skip for target FPS
        frame_skip = 1
        if fps and fps < video_fps:
            frame_skip = int(video_fps / fps)
        
        # If max_frames is None, process all frames
        if max_frames:
            frame_skip = max(frame_skip, total_frames // max_frames)
            print(f"   Limiting to {max_frames} frames, skipping every {frame_skip} frames")
        else:
            print(f"   Processing all {total_frames} frames")
        
        frame_count = 0
        saved_count = 0
        frame_paths = []
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Skip frames based on target FPS or max_frames
            if frame_count % frame_skip == 0:
                frame_filename = f"frame_{saved_count:06d}.png"
                frame_path = os.path.join(output_dir, frame_filename)
                cv2.imwrite(frame_path, frame)
                frame_paths.append(frame_path)
                saved_count += 1
                
                if max_frames and saved_count >= max_frames:
                    break
            
            frame_count += 1
        
        cap.release()
        print(f"✅ Extracted {saved_count} frames to {output_dir}")
        return frame_paths, video_fps

    def process_video_frames(self, frame_paths, output_dir, canny_low=50, canny_high=150, 
                           blur_kernel=5, show_grid=True):
        """Process each frame to create mathematical plots"""
        os.makedirs(output_dir, exist_ok=True)
        plot_paths = []
        
        total_frames = len(frame_paths)
        print(f"🎬 Processing {total_frames} frames...")
        
        for i, frame_path in enumerate(frame_paths):
            try:
                # Create temporary files for this frame
                base_name = f"frame_{i:06d}"
                temp_pbm = f"{base_name}_temp.pbm"
                temp_svg = f"{base_name}_temp.svg"
                plot_path = os.path.join(output_dir, f"{base_name}_plot.png")
                
                # Process frame through edge detection and tracing
                self.image_to_edges(frame_path, temp_pbm, canny_low, canny_high, blur_kernel)
                self.pbm_to_svg(temp_pbm, temp_svg)
                self.export_matplotlib(temp_svg, plot_path, show_grid)
                
                plot_paths.append(plot_path)
                
                # Clean up temp files
                for temp_file in [temp_pbm, temp_svg]:
                    if os.path.exists(temp_file):
                        os.remove(temp_file)
                
                # Progress indicator
                if (i + 1) % 10 == 0 or i == total_frames - 1:
                    print(f"   Progress: {i + 1}/{total_frames} frames processed")
                    
            except Exception as e:
                print(f"⚠️  Error processing frame {i}: {e}")
                # Create a blank frame to maintain video continuity
                plot_path = os.path.join(output_dir, f"frame_{i:06d}_plot.png")
                plt.figure(figsize=(10, 10))
                plt.text(0.5, 0.5, f"Error processing frame {i}", 
                        ha='center', va='center', fontsize=16)
                plt.axis('equal')
                plt.savefig(plot_path, dpi=150, bbox_inches='tight')
                plt.close()
                plot_paths.append(plot_path)
        
        print(f"✅ Processed all frames, saved to {output_dir}")
        print(f"📁 Sample plot files: {plot_paths[:3]} ...")
        return plot_paths

    def create_video_from_plots(self, plot_paths, output_video, input_video,fps=30):
        """Combine matplotlib plots into a video"""
        if not plot_paths:
            raise RuntimeError("No plot images to create video from")
        
        print(f"🎬 Creating video from {len(plot_paths)} frames at {fps} FPS...")
        
        # Method 1: Try using image sequence input (more reliable)
        try:
            # Create a pattern-based input for ffmpeg
            # Assumes plot files are named consistently (frame_000000_plot.png, etc.)
            first_plot = plot_paths[0]
            plot_dir = os.path.dirname(first_plot)
            
            # Use glob pattern for input
            # In Method 1 (add these parameters):
            subprocess.run([
                "ffmpeg", "-y",
                "-i", input_video,  # Add original video as input
                "-framerate", str(fps),
                "-pattern_type", "glob", 
                "-i", f"{plot_dir}/frame_*_plot.png",
                "-c:v", "libx264",
                "-c:a", "copy",  # Copy audio from original
                "-pix_fmt", "yuv420p",
                "-r", str(fps),
                "-shortest",  # Stop when shortest input ends
                output_video
            ], check=True, capture_output=True, text=True)
            
            print(f"🎥 Created video: {output_video}")
            return
            
        except subprocess.CalledProcessError as e:
            print(f"⚠️ Method 1 failed, trying alternative method: {e.stderr}")
        
        # Method 2: Create numbered symlinks and use image sequence
        try:
            temp_dir = "temp_numbered_frames"
            os.makedirs(temp_dir, exist_ok=True)
            
            # Create numbered symlinks/copies
            for i, plot_path in enumerate(plot_paths):
                link_path = os.path.join(temp_dir, f"frame_{i:06d}.png")
                if os.path.exists(link_path):
                    os.remove(link_path)
                # Use copy instead of symlink for better compatibility
                shutil.copy2(plot_path, link_path)
            
            # Use numbered sequence input
            subprocess.run([
                "ffmpeg", "-y",
                "-framerate", str(fps),
                "-i", f"{temp_dir}/frame_%06d.png",
                "-c:v", "libx264",
                "-pix_fmt", "yuv420p",
                "-r", str(fps),
                output_video
            ], check=True, capture_output=True, text=True)
            
            # Clean up temp directory
            shutil.rmtree(temp_dir)
            print(f"🎥 Created video: {output_video}")
            return
            
        except subprocess.CalledProcessError as e:
            print(f"⚠️ Method 2 failed, trying concat method: {e.stderr}")
        
        # Method 3: Fallback to concat method (original)
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            for plot_path in plot_paths:
                # Use duration per frame based on FPS
                duration = 1.0 / fps
                f.write(f"file '{os.path.abspath(plot_path)}'\n")
                f.write(f"duration {duration}\n")
            # Add the last frame again to ensure proper ending
            if plot_paths:
                f.write(f"file '{os.path.abspath(plot_paths[-1])}'\n")
            input_list = f.name
        
        try:
            subprocess.run([
                "ffmpeg", "-y",
                "-f", "concat",
                "-safe", "0",
                "-i", input_list,
                "-vsync", "vfr",  # Variable frame rate
                "-pix_fmt", "yuv420p",
                "-c:v", "libx264",
                output_video
            ], check=True, capture_output=True, text=True)
            
            print(f"🎥 Created video: {output_video}")
            
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"All FFmpeg methods failed. Last error: {e.stderr}")
        finally:
            if os.path.exists(input_list):
                os.remove(input_list)

    def process_video(self, input_video, output_video=None, max_frames=None, target_fps=None,
                     canny_low=50, canny_high=150, blur_kernel=5, show_grid=True, 
                     keep_temp=False):
        """Main video processing function"""
        
        if not os.path.exists(input_video):
            raise FileNotFoundError(f"Video file not found: {input_video}")
        
        # Set up output paths
        if not output_video:
            base_name = Path(input_video).stem
            output_video = f"{base_name}_curves_animation.mp4"
        
        # Create temporary directories
        frames_dir = "temp_frames"
        plots_dir = "temp_plots"
        
        try:
            # Step 1: Extract frames
            frame_paths, original_fps = self.extract_frames(
                input_video, frames_dir, max_frames, target_fps
            )
            
            # Step 2: Process frames to mathematical plots
            plot_paths = self.process_video_frames(
                frame_paths, plots_dir, canny_low, canny_high, blur_kernel, show_grid
            )
            
            # Step 3: Create final video
            final_fps = target_fps if target_fps else original_fps
            self.create_video_from_plots(plot_paths, output_video, input_video ,final_fps)
            
            print(f"🎉 Video conversion completed: {output_video}")
            
        finally:
            # Clean up temporary files
            if not keep_temp:
                for temp_dir in [frames_dir, plots_dir]:
                    if os.path.exists(temp_dir):
                        shutil.rmtree(temp_dir)
    
    def image_to_edges(self, input_image, output_pbm, canny_low=50, canny_high=150, blur_kernel=5):
        """Convert image to edge-detected bitmap using OpenCV Canny"""
        if not os.path.exists(input_image):
            raise FileNotFoundError(f"Input image not found: {input_image}")

        try:
            # Read image
            img = cv2.imread(input_image)
            if img is None:
                raise ValueError(f"Could not read image: {input_image}")
            
            # Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            # Apply Gaussian blur to reduce noise
            if blur_kernel > 0:
                gray = cv2.GaussianBlur(gray, (blur_kernel, blur_kernel), 0)
            
            # Apply Canny edge detection
            edges = cv2.Canny(gray, canny_low, canny_high)
            
            # Invert so edges are white on black background (for Potrace)
            edges_inverted = cv2.bitwise_not(edges)
            
            # Save as bitmap
            cv2.imwrite(output_pbm, edges_inverted)
            
            print(f"✅ Edge detection completed: {output_pbm}")
            print(f"   Canny thresholds: {canny_low}-{canny_high}, Blur: {blur_kernel}px")
            
        except Exception as e:
            raise RuntimeError(f"OpenCV edge detection failed: {e}")

    def jpeg_to_pbm(self, input_image, output_pbm, threshold=50):
        """Convert image to black and white bitmap (fallback method)"""
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
                    y = [p.imag for p in points]  # Keep original orientation (don't flip)
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
                            x0, y0 = seg.start.real, seg.start.imag  # Keep original orientation
                            x1, y1 = seg.control1.real, seg.control1.imag
                            x2, y2 = seg.control2.real, seg.control2.imag
                            x3, y3 = seg.end.real, seg.end.imag

                            f.write(f"((1-t)^3*{x0} + 3*(1-t)^2*t*{x1} + 3*(1-t)*t^2*{x2} + t^3*{x3},"
                                   f"(1-t)^3*{y0} + 3*(1-t)^2*t*{y1} + 3*(1-t)*t^2*{y2} + t^3*{y3})\n")
                            curve_count += 1

                        else:
                            # Handle lines/other segments as degenerate cubic Béziers
                            x0, y0 = seg.start.real, seg.start.imag
                            x3, y3 = seg.end.real, seg.end.imag
                            x1, y1 = x0 + (x3-x0)/3, y0 + (y3-y0)/3
                            x2, y2 = x0 + 2*(x3-x0)/3, y0 + 2*(y3-y0)/3
                            
                            f.write(f"((1-t)^3*{x0}+3*(1-t)^2*t*{x1}+3*(1-t)*t^2*{x2}+t^3*{x3},"
                                   f"(1-t)^3*{y0}+3*(1-t)^2*t*{y1}+3*(1-t)*t^2*{y2}+t^3*{y3})\n")
                            curve_count += 1

            print(f"✅ Desmos equations exported: {output_file} ({curve_count} curves)")
            
        except Exception as e:
            raise RuntimeError(f"Desmos export failed: {e}")

    def cleanup(self):
        """Remove temporary files"""
        for file in self.temp_files:
            if os.path.exists(file):
                os.remove(file)

    def process_image(self, input_image, output_mode, output_file=None, 
                     canny_low=50, canny_high=150, blur_kernel=5, 
                     show_grid=True, keep_temp=False, use_canny=True):
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
            # Step 1: Convert to bitmap (either edge detection or threshold)
            if use_canny:
                self.image_to_edges(input_image, pbm_file, canny_low, canny_high, blur_kernel)
            else:
                # Fallback to simple threshold (for backwards compatibility)
                threshold = 50  # Default threshold for fallback
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
        description='Convert images or videos to mathematical curves (Desmos equations or matplotlib plots)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Images
  %(prog)s image.jpg --mode plot                    # Create matplotlib plot with edge detection
  %(prog)s image.jpg --mode desmos                  # Create Desmos equations from edges
  %(prog)s image.jpg --canny-low 30 --canny-high 100 # Custom edge detection
  
  # Videos  
  %(prog)s video.mp4 --video                       # Convert entire video to mathematical animation
  %(prog)s video.mp4 --video --max-frames 50       # Limit to first 50 frames
  %(prog)s video.mp4 --video --fps 15              # Target 15 FPS output
        """
    )
    
    parser.add_argument('input', 
                       help='Input image file or video file')
    
    parser.add_argument('--video', 
                       action='store_true',
                       help='Process as video (creates animated mathematical curves)')
    
    parser.add_argument('--mode', '-m', 
                       choices=['plot', 'desmos', 'both'], 
                       default='plot',
                       help='Output mode for images (default: plot, ignored for videos)')
    
    # Video-specific options
    parser.add_argument('--max-frames', 
                       type=int,
                       help='Maximum number of frames to process (default: process all frames)')
    
    parser.add_argument('--fps', 
                       type=int,
                       help='Target frames per second for output video (default: use original)')
    
    parser.add_argument('--output', '-o',
                       help='Output filename (optional)')
    
    parser.add_argument('--canny-low', 
                       type=int, default=50, 
                       metavar='N',
                       help='Canny edge detection lower threshold (default: 50)')
    
    parser.add_argument('--canny-high', 
                       type=int, default=150, 
                       metavar='N',
                       help='Canny edge detection upper threshold (default: 150)')
    
    parser.add_argument('--blur', 
                       type=int, default=5, 
                       metavar='N',
                       help='Gaussian blur kernel size for noise reduction (default: 5, 0 to disable)')
    
    parser.add_argument('--threshold', '-t', 
                       type=int, default=50, 
                       metavar='N',
                       help='Black/white threshold 0-100 (only used with --no-canny, default: 50)')
    
    parser.add_argument('--no-canny', 
                       action='store_true',
                       help='Use simple threshold instead of Canny edge detection')
    
    parser.add_argument('--no-grid', 
                       action='store_true',
                       help='Disable grid in matplotlib plots')
    
    parser.add_argument('--keep-temp', 
                       action='store_true',
                       help='Keep temporary PBM and SVG files')
    
    parser.add_argument('--version', 
                       action='version', 
                       version='%(prog)s 1.2.2')

    args = parser.parse_args()
    
    # Validate thresholds
    if not 0 <= args.threshold <= 100:
        print("Error: Threshold must be between 0 and 100")
        sys.exit(1)
    
    if args.canny_low >= args.canny_high:
        print("Error: Canny low threshold must be less than high threshold")
        sys.exit(1)
        
    if args.blur < 0:
        print("Error: Blur kernel size must be >= 0")
        sys.exit(1)
    
    if args.video and args.max_frames and args.max_frames <= 0:
        print("Error: Max frames must be > 0")
        sys.exit(1)
    
    converter = Image2Curves()
    
    try:
        if args.video:
            # Process video
            converter.process_video(
                input_video=args.input,
                output_video=args.output,
                max_frames=args.max_frames,
                target_fps=args.fps,
                canny_low=args.canny_low,
                canny_high=args.canny_high,
                blur_kernel=args.blur,
                show_grid=not args.no_grid,
                keep_temp=args.keep_temp
            )
        else:
            # Process single image
            converter.process_image(
                input_image=args.input,
                output_mode=args.mode,
                output_file=args.output,
                canny_low=args.canny_low,
                canny_high=args.canny_high,
                blur_kernel=args.blur,
                show_grid=not args.no_grid,
                keep_temp=args.keep_temp,
                use_canny=not args.no_canny
            )
        print("🎉 Conversion completed successfully!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()