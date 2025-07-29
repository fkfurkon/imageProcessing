# Image Processing Application

This project is an image processing application that allows users to open a webcam feed or load images from a URL, perform simple image processing tasks, customize parameters through a graphical user interface (GUI), and visualize the results with graphs.

## Features

- Access webcam feed or load images from a URL.
- Perform simple image processing tasks such as filtering and brightness adjustment.
- Customize image processing parameters via a user-friendly GUI.
- Display processed images and generate graphs based on image properties.

## Project Structure

```
image-processing-app
├── src
│   ├── main.py            # Entry point of the application
│   ├── gui.py             # GUI class for user interaction
│   ├── webcam.py          # Functions to access webcam feed
│   ├── url_loader.py      # Functions to load images from a URL
│   ├── image_processing.py # Functions for image processing tasks
│   ├── graph.py           # Functions to generate and display graphs
│   └── utils.py           # Utility functions for various tasks
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd image-processing-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python src/main.py
   ```

2. Use the GUI to select either the webcam feed or to input a URL for an image.

3. Adjust the image processing parameters as desired.

4. View the processed image and the corresponding graph displaying image properties.

## Dependencies

The project requires the following Python libraries:
- OpenCV
- NumPy
- Matplotlib
- Tkinter (for GUI)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.