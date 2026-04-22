import streamlit as st
from PIL import Image
import io
import os

st.set_page_config(page_title="Product Customization", layout="centered")

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Title & Description
st.title("🧥 Product Customization System")
st.write("Upload your design and adjust it to preview how it looks on products.")

st.markdown("### How it works")
st.write("1. Upload your logo")
st.write("2. Choose a product")
st.write("3. Adjust size and position")
st.write("4. Download the final image")

st.info("Tip: Use transparent PNG logos for best results.")

# Upload
uploaded_logo = st.file_uploader("Upload your design (logo)", type=["png", "jpg", "jpeg"])

# Product selection
product = st.selectbox("Select product", ["T-Shirt", "Cap"])

# Load base image safely
if product == "T-Shirt":
    default_size = 230
    default_x = 260
    default_y = 190
    base_path = os.path.join(BASE_DIR, "input", "tshirt.png")

elif product == "Cap":
    default_size = 150
    default_x = 200
    default_y = 120
    base_path = os.path.join(BASE_DIR, "input", "cap.png")

base = Image.open(base_path).convert("RGBA")

# Sidebar controls
st.sidebar.title("Controls")
st.sidebar.markdown("Adjust logo size and position")

size = st.sidebar.slider("Logo Size", 50, 400, default_size)
x_pos = st.sidebar.slider("Horizontal Position", 0, 600, default_x)
y_pos = st.sidebar.slider("Vertical Position", 0, 600, default_y)


if uploaded_logo:
    logo = Image.open(uploaded_logo).convert("RGBA")

    # Remove white background
    new_logo = []
    for item in logo.getdata():
        if item[0] > 200 and item[1] > 200 and item[2] > 200:
            new_logo.append((255, 255, 255, 0))
        else:
            new_logo.append(item)
    logo.putdata(new_logo)

    # Resize
    logo.thumbnail((size, size))

    # Blend effect
    alpha = logo.split()[3]
    alpha = alpha.point(lambda p: int(p * 0.8))
    logo.putalpha(alpha)

    # Apply logo
    base.paste(logo, (x_pos, y_pos), logo)

    # Preview
    st.markdown("### Preview")
    st.image(base, width=400)

    # Download
    buf = io.BytesIO()
    base.save(buf, format="PNG")

    st.download_button(
        label="Download Customized Image",
        data=buf.getvalue(),
        file_name="customized.png",
        mime="image/png"
    )

# Footer
st.markdown("---")
st.markdown("Built using Python, Pillow, and Streamlit")
