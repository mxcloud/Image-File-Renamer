# Image File Renamer

## Overview
The `orderer.py` script is designed to rename all image files in a specified folder to a unique 10-character ID. This can be particularly useful for organizing and managing large collections of images where a standardized naming convention is desired.

## Features
- Renames all image files in a specified directory.
- Generates a unique 10-character alphanumeric ID for each file.
- Preserves the original file extension.
- Supports common image formats such as JPG, PNG, GIF, and BMP.

## Prerequisites
- Python 3.x installed on your system.
- Basic knowledge of running Python scripts and navigating directories in your system's command line interface.

## Setup
1. **Clone or Download the Script**
   - Obtain a copy of `orderer.py` and place it in a convenient directory on your system.

2. **Prepare Your Images**
   - Ensure all images you wish to rename are placed in a single directory.
   - Back up your images to prevent accidental data loss.

## Usage
1. **Open Command Line:**
   - Open a command line interface (CLI) such as Command Prompt on Windows or Terminal on macOS/Linux.

2. **Navigate to the Script Directory:**
   - Use the `cd` command to navigate to the directory containing `orderer.py`.
   - Example: `cd C:\Users\dude\Documents\Development`

3. **Run the Script:**
   - Execute the script with Python and provide the path to your image directory.
   - Command: `python orderer.py`
   - Replace `'path_to_your_folder'` inside the script with the actual path to your image folder before running.

## Important Notes
- **Backup**: Always ensure you have a backup of your images before running the script.
- **Collision Risk**: With a 10-character limit, there's a small risk of ID collisions. Ensure this risk is acceptable for your use case.
- **File Extensions**: By default, the script looks for `.png`, `.jpg`, `.jpeg`, `.gif`, and `.bmp` files. Modify the script if you have images with different extensions.

## Troubleshooting
- **File Not Found**: If you encounter a 'File Not Found' error, double-check the path you provided to the script and ensure it is correct and accessible.
- **Permission Issues**: Ensure you have the necessary permissions to read and write files in the target directory.

## Contributing
Feel free to fork the project, make improvements, and submit pull requests. Any contributions to enhance the functionality or efficiency of the script are welcome!
