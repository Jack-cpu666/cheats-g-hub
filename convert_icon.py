
from PIL import Image
import os

# Input path from previous step
input_path = "C:/Users/khjb/.gemini/antigravity/brain/a8020a7c-920e-4beb-b140-c293d201e98d/ascendancy_xmas_logo_1766288132065.png"
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.ico")

try:
    img = Image.open(input_path)
    # Save as ICO with multiple sizes for best scaling
    img.save(output_path, format='ICO', sizes=[(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)])
    print(f"Successfully converted to {output_path}")
except Exception as e:
    print(f"Error converting image: {e}")
