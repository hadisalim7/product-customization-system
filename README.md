# Product Customization System

## Description
This project allows placing a user-uploaded design onto a product image (T-shirt or cap). It also provides an interactive interface to adjust the design and preview the final result.

## Live Demo
https://customizationsystem.streamlit.app/

## Features
- Loads base product image  
- Removes background from logo  
- Resizes and places logo in print area  
- Allows adjustment of size and position  
- Applies slight blending for realistic effect  
- Generates downloadable output  

## How to Run
- Place images inside the `input` folder  
- Run the application:
  streamlit run app.py  
- The customized output can be previewed and downloaded  

## Limitations
- No perspective transformation  
- No wrinkle simulation  
- Basic blending only  

## Approach
The problem was broken down into smaller steps:
- Load base product image and user design  
- Remove background from design using pixel filtering  
- Resize and position the design in the print area  
- Blend the design slightly to match the product surface  
- Generate and display the final customized image  

This approach focuses on building a clean and functional pipeline rather than complex rendering.
