import os
import random
from PIL import Image

# Define the directory containing card images
image_directory = 'C:\card practical ai\image_directory'

# Create a list of image filenames
image_files = [f for f in os.listdir(image_directory) if f.endswith('.png')]

# Get the number of cards to shuffle from the user
num_cards = int(input("Enter the number of cards to shuffle and display: "))

# Check if the number of cards requested is valid
if num_cards > len(image_files):
    print(f"Error: There are only {len(image_files)} cards available.")
    num_cards = len(image_files)

# Shuffle the list of image filenames
random.shuffle(image_files)

# Select the specified number of cards
selected_files = image_files[:num_cards]

# Load images
images = [Image.open(os.path.join(image_directory, f)) for f in selected_files]

# Define the size for the final image
card_width, card_height = images[0].size
columns = 4  # Number of columns in the final image
rows = len(images) // columns + (1 if len(images) % columns != 0 else 0)
slide_width = columns * card_width
slide_height = rows * card_height

# Create a new blank image for the slide
slide = Image.new('RGB', (slide_width, slide_height))

# Paste each card image onto the slide
for index, image in enumerate(images):
    x = (index % columns) * card_width
    y = (index // columns) * card_height
    slide.paste(image, (x, y))

# Save or show the final slide
slide.save('shuffled_cards_slide.png')
slide.show()

print("Shuffling complete and all selected cards displayed on a single slide.")
