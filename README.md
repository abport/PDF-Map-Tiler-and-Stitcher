# PDF Map Tiler and Stitcher

Hey there, map enthusiasts and Python coders! 👋 This repo contains two nifty scripts that'll help you work with large PDF maps. Whether you're dealing with gigantic geological surveys, city plans, or just really, really big treasure maps, I've got you covered.

## What's in the Box?

1. `pdf_splitter.py`: This bad boy takes your massive PDF map and cuts it into manageable A0-sized tiles.
2. `tile_stitcher.py`: Once you're done working with your tiles, this script puts Humpty Dumpty back together again.

## Why Would I Need This?

Ever tried opening a 14GB PDF file? Yeah, it's not fun. These scripts let you:

- Work with sections of large maps without melting your computer
- Process or edit parts of a map independently
- Reassemble your map after making changes

## How to Use

### Prerequisites

Before you dive in, make sure you have these installed:
- Python 3.x
- PyMuPDF (fitz)
- Pillow (PIL)

You can install the required packages with:

```bash
pip install PyMuPDF Pillow
```

### Splitting a PDF Map

1. Open `pdf_splitter.py`
2. Scroll to the bottom and update these lines:
   ```python
   input_pdf = 'path/to/your/large_map.pdf'
   output_directory = 'path/to/output/tiles'
   ```
   
   Examples:
   - For Unix-based systems (macOS, Linux):
     ```python
     input_pdf = '/Users/yourusername/Documents/large_map.pdf'
     output_directory = '/Users/yourusername/Documents/map_tiles'
     ```
   - For Windows:
     ```python
     input_pdf = r'C:\Users\yourusername\Documents\large_map.pdf'
     output_directory = r'C:\Users\yourusername\Documents\map_tiles'
     ```
   Note for Windows users: The `r` before the string makes it a raw string, which treats backslashes as literal characters.

3. Run the script:
   ```bash
   python pdf_splitter.py
   ```
4. Watch as your map gets sliced and diced into A0-sized PNG tiles!

### Stitching Tiles Back Together

1. Open `tile_stitcher.py`
2. At the bottom, update these lines:
   ```python
   input_directory = 'path/to/input/tiles'
   output_file = 'path/to/output/stitched_map.png'
   ```

   Examples For Unix-based systems (macOS, Linux) and Windows are as mentioned above.

3. Run the script:
   ```bash
   python tile_stitcher.py
   ```
4. Marvel at your reassembled map!

## Features

- Handles ridiculously large PDF files (we're talking gigabytes)
- Splits maps into standard A0-sized tiles
- Stitches tiles back together, even if they're not all the same size
- Provides verbose output so you know exactly what's happening

## Limitations

- Currently works with single-page PDF maps
- Assumes your map is in the first page of the PDF
- Outputs tiles as PNG files (great quality, but can be large)

## Contributing

Found a bug? Have an idea for an improvement? Want to add support for A1 tiles because you think A0 is just showing off? Feel free to open an issue or submit a pull request!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Hat tip to the PyMuPDF and Pillow teams for their awesome libraries
- Thanks to caffeine for making this project possible

Happy mapping! 🗺️
