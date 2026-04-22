from PIL import Image

# Load images
tshirt = Image.open("input/tshirt.png").convert("RGBA")
logo = Image.open("input/logo.png").convert("RGBA")

# Remove white background from logo
new_logo = []
for item in logo.getdata():
    # If pixel is almost white → make transparent
    if item[0] > 200 and item[1] > 200 and item[2] > 200:
        new_logo.append((255, 255, 255, 0))  # transparent
    else:
        new_logo.append(item)

logo.putdata(new_logo)

# Resize logo
logo = logo.resize((250, 250))

# ✅ SAFE blending (reduce opacity properly)
alpha = logo.split()[3]          # get alpha channel
alpha = alpha.point(lambda p: p * 0.8)  # reduce opacity to 80%
logo.putalpha(alpha)

# Position
position = (295, 205)

# Paste with transparency
tshirt.paste(logo, position, logo)

# Save & show
tshirt.save("output/result.png")
tshirt.show()
