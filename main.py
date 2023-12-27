# Converts PNG and WEBP files to jpeg.
# pip install Pillow
import os
from PIL import Image

# Create a directory named "jpeg" if it doesn't exist
output_directory = "Converted_To_JPEG"
os.makedirs(output_directory, exist_ok=True)

# Get a list of all PNG files in the current directory
image_files = [
    filename
    for filename in os.listdir()
    if filename.lower().endswith((".png", ".webp"))
]

# Loop through each PNG file, convert it to JPEG, and save it in the "jpeg" folder
for image_file in image_files:
    try:
        # Construct the output file path with a ".jpeg" extension
        jpeg_file = os.path.join(
            output_directory, os.path.splitext(image_file)[0] + ".jpeg"
        )

        # Check if jpeg_file already exists. Skips converting if it does.
        if os.path.exists(jpeg_file):
            print(f"Skipping {image_file}. {jpeg_file} already exists.")
            continue

        # Open the PNG file
        image = Image.open(image_file)
        # Save the image as JPEG
        image.convert("RGB").save(jpeg_file, "JPEG")
        print(f"Converted {image_file} to {jpeg_file}")
        image_stats = os.stat(image_file)
        jpeg_stats = os.stat(jpeg_file)
        size = 1024 * 1024
        print(
            f"File Size {round(image_stats.st_size / size, 2)}MB -> {round(jpeg_stats.st_size / size,2)}MB"
        )
    except Exception as e:
        print(f"Error converting {image_file}: {str(e)}")

print("Conversion completed.")
input("Press ENTER to close.")
