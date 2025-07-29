import matplotlib.pyplot as plt
import numpy as np

def plot_image_histogram(image):
    if image is None:
        raise ValueError("Image cannot be None")

    # Convert the image to RGB if it's in BGR format
    if image.shape[2] == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Calculate the histogram for each color channel
    colors = ('r', 'g', 'b')
    plt.figure(figsize=(10, 5))
    
    for i, color in enumerate(colors):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    
    plt.title('Color Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.legend(['Red Channel', 'Green Channel', 'Blue Channel'])
    plt.show()