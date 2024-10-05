import os
from PIL import Image
import re

def stitch_tiles(input_directory, output_file):
    tile_files = [f for f in os.listdir(input_directory) if f.endswith('.png')]
    
    if not tile_files:
        print("No PNG files found in the input directory.")
        return
    
    pattern = re.compile(r'tile_(\d+)_(\d+)\.png')
    tiles = {}
    max_x = max_y = 0
    min_x = min_y = float('inf')
    
    for file in tile_files:
        match = pattern.match(file)
        if match:
            x, y = map(int, match.groups())
            tiles[(x, y)] = os.path.join(input_directory, file)
            max_x, max_y = max(max_x, x), max(max_y, y)
            min_x, min_y = min(min_x, x), min(min_y, y)
    
    if not tiles:
        print("No valid tile files found.")
        return
    
    print(f"Tile coordinate ranges: X({min_x}-{max_x}), Y({min_y}-{max_y})")
    print(f"Total number of tiles found: {len(tiles)}")
    
    # Check tile dimensions and calculate column widths and row heights
    tile_sizes = {}
    column_widths = [0] * (max_x - min_x + 1)
    row_heights = [0] * (max_y - min_y + 1)
    
    for (x, y), file_path in tiles.items():
        with Image.open(file_path) as img:
            width, height = img.size
            tile_sizes[(x, y)] = (width, height)
            column_widths[x - min_x] = max(column_widths[x - min_x], width)
            row_heights[max_y - y] = max(row_heights[max_y - y], height)
    
    print("Tile sizes:")
    for coords, size in tile_sizes.items():
        print(f"Tile {coords}: {size[0]}x{size[1]}")
    
    # Calculate full image size
    full_width = sum(column_widths)
    full_height = sum(row_heights)
    stitched_image = Image.new('RGB', (full_width, full_height), color='lightgrey')
    
    print(f"Stitched image dimensions: {full_width}x{full_height}")
    
    # Place tiles
    y_offset = 0
    for y in range(max_y, min_y - 1, -1):
        x_offset = 0
        for x in range(min_x, max_x + 1):
            if (x, y) in tiles:
                with Image.open(tiles[(x, y)]) as tile:
                    stitched_image.paste(tile, (x_offset, y_offset))
                    print(f"Placed tile ({x}, {y}) at position ({x_offset}, {y_offset})")
            x_offset += column_widths[x - min_x]
        y_offset += row_heights[max_y - y]
    
    stitched_image.save(output_file, 'PNG')
    print(f"Stitched image saved as {output_file}")

# Usage
input_directory = 'path/to/input/tiles'
output_file = 'path/to/output/stitched_map.png'
stitch_tiles(input_directory, output_file)
