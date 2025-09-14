#!/usr/bin/env python3
"""
Create a simple test image for testing
"""

from PIL import Image, ImageDraw
import numpy as np
import os

# Create a simple test image
width, height = 300, 300
image = Image.new('RGB', (width, height), color='white')
draw = ImageDraw.Draw(image)

# Draw a red circle
draw.ellipse((50, 50, 250, 250), fill='red')

# Draw a green rectangle
draw.rectangle((100, 100, 200, 200), fill='green')

# Save the image
image.save('test_input.jpg')
print("Test image created: test_input.jpg")

# Check if the image was created
if os.path.exists('test_input.jpg'):
    print("✓ Test image created successfully")
else:
    print("✗ Failed to create test image")