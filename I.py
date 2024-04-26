import os
import shutil

# Create a directory
directory = 'images'
os.makedirs(directory, exist_ok=True)

# Save images in the directory
image_data = b'...binary image data...'
with open(os.path.join(directory, 'image1.jpg'), 'wb') as f:
    f.write(image_data)

# Alternatively, using shutil.copy() to move images
shutil.copy('path_to_image/image2.jpg', os.path.join(directory, 'image2.jpg'))
