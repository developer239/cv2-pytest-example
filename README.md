# Webcam Application with Face Detection

This application utilizes a webcam to display a live feed, draw a rectangle in the center, detect faces, and draw rectangles around detected faces. Additionally, it draws an arrow from the center rectangle to each detected face.

## Setup

### Prerequisites
- Ensure you have Conda installed on your system. If not, install it from [Conda's official site](https://www.conda.io).

### Installation
1. Clone the repository or download the source code.
2. Navigate to the project directory.
3. Create the Conda environment with the required dependencies:
   ```
   conda env create -f environment.yml
   ```
4. Activate the newly created environment:
   ```
   conda activate webcam-app
   ```
5. **(optional)** Configure PyCharm to use the Conda environment:
   - Search for current interpreter in the bottom right corner of the IDE and click the button name.
   - Select 'Add Interpreter' and 'Add Local Interpreter'.
   - Choose 'Conda Environment' and 'Use Existing' and select the newly created 'webcam-app' environment.

## Running the Application
To start the application, execute the following command in your terminal:
```
python src/main.py
```
The application window will open displaying the webcam feed. Press 'q' to quit the application.

## Running Tests
To ensure the functions are working as expected, run the unit tests with Pytest:
```
pytest tests/
```

## Features
- **Webcam Feed**: Shows live video from your webcam.
- **Center Rectangle**: Draws a green rectangle fixed at the center of the video frame.
- **Face Detection**: Detects faces in the video feed and outlines them with red rectangles.
- **Directional Arrow**: Draws a blue arrow from the center rectangle to each detected face, indicating the direction.

## Contributing
Feel free to fork the project and submit pull requests with enhancements or fixes. Make sure to write tests for new features or changes.

## License
Specify the license under which the project is released.

## Contact
For bugs, suggestions, or general questions, open an issue in the project repository or contact the maintainers directly.

This README provides detailed instructions on how to set up and run the project, along with information on the features and how to contribute to its development.