# Product Customization System

## Description
This project allows placing a user-uploaded design onto a product image (t-shirt).

## Features
- Loads base product image
- Removes background from logo
- Resizes and places logo in print area
- Applies slight blending for realistic effect

## How to Run
1. Place images inside input folder
2. Run main.py
3. Output will be saved in output folder

## Limitations
- No perspective transformation
- No wrinkle simulation
- Basic blending only

## Approach
The problem was broken down into smaller steps:
1. Load base product image and user design
2. Remove background from design using pixel filtering
3. Resize and position the design in the print area
4. Blend the design slightly to match the product surface
5. Save the final customized image

This approach focuses on building a clean and functional pipeline rather than complex rendering.
