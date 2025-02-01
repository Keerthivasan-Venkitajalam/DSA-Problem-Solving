import os
from PIL import Image

# Path to your images folder
base_dir = "F:/Pragati_Frontend_2025/public/Images"

# Walk through the directory and find PNG files
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".png"):
            png_path = os.path.join(root, file)
            webp_path = os.path.splitext(png_path)[0] + ".webp"

            try:
                # Open PNG and save as WebP
                with Image.open(png_path) as img:
                    img.save(webp_path, "WEBP")
                os.remove(png_path)  # Remove original PNG
                print(f"Converted: {png_path} -> {webp_path}")
            except Exception as e:
                print(f"Error converting {png_path}: {e}")

print("All PNG files converted to WebP!")
