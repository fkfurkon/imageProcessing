from gui import GUI
from webcam import get_webcam_feed
from url_loader import load_image_from_url
from image_processing import apply_filter, adjust_brightness
from graph import plot_image_histogram
import cv2
import numpy as np

def main():
    # Initialize the GUI
    gui = GUI()

    # Get user input for webcam or URL
    source_type = gui.get_source_type()
    if source_type == 'webcam':
        feed = get_webcam_feed()
    else:
        url = gui.get_image_url()
        feed = load_image_from_url(url)

    while True:
        # Read a frame from the feed
        ret, frame = feed.read() if source_type == 'webcam' else (True, feed)

        if not ret:
            break

        # Get processing parameters from the GUI
        filter_type = gui.get_filter_type()
        brightness_adjustment = gui.get_brightness_adjustment()

        # Process the image
        processed_image = apply_filter(frame, filter_type)
        processed_image = adjust_brightness(processed_image, brightness_adjustment)

        # Display the processed image
        gui.display_image(processed_image)

        # Plot the histogram of the processed image
        histogram = plot_image_histogram(processed_image)
        gui.display_histogram(histogram)

        # Break the loop on user command
        if gui.should_exit():
            break

    # Release resources
    feed.release() if source_type == 'webcam' else None
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()