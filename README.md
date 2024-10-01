# Snowman Interactive Program

This project is an interactive graphical program that allows the user to control the height of a snowman. The user can make the snowman taller or shorter using "Freeze" and "Melt" buttons, respectively, and a message will be displayed if the snowman reaches its maximum or minimum height.

## Features
- **Increase Height ("Freeze")**: Adds a snowball layer to make the snowman taller.
- **Decrease Height ("Melt")**: Removes a snowball layer to make the snowman shorter.
- **Quit**: Close the program with the "Quit" button.
- **Visual Feedback**: Displays a message when the snowman reaches its maximum or minimum height.

## Getting Started

### Prerequisites
- **Python**: Ensure that Python is installed on your system.
- **Graphics Library**: This program uses a custom `graphics.py` and `button.py` library to provide the graphical interface. Make sure both `graphics.py` and `button.py` are present in the same directory as the main script.

### Installation
1. Clone the repository or download the code files.
2. Ensure that the `graphics.py` and `button.py` files are available in the same directory as the main program file (`snowman.py`).

### Running the Application
To run the application, navigate to the directory containing the script and use the following command:

'''sh
python snowman.py

## How to Use
1. Start the Program: Run the script to see the initial snowman with three stacked circles.
2. Melt the Snowman: Click on the "Melt" button to reduce the height of the snowman by removing the top layer. The snowman can only go down to a single layer. If you try to melt further, a message saying "Is It Spring yet?" will appear.
3. Freeze the Snowman: Click on the "Freeze" button to add another layer to the snowman. The snowman can have a maximum of four layers. If you try to freeze beyond this, a message saying "Happy Holidays!" will appear.
4. Quit the Program: Click on the "Quit" button to close the application.

## Code Structure
Snowman Class: The main class that defines the snowman and handles the GUI.
1. __init__(): Initializes the snowman window and creates buttons, circles, and the snowman's face.
2. __createbuttons(): Creates the interactive buttons ("Melt", "Freeze", "Quit").
3. __createcircles(): Creates the snowball circles for the snowman, initially drawing three of them.
4. __createface(): Creates the face of the snowman, including the eyes, mouth, and nose.
5. getbutton(): Waits for the user to click a button and returns the label of the clicked button.
6. processButton(key): Handles the actions to be taken based on the button clicked.
7. run(): Main event loop to keep the snowman application running and handle user input.

## Important Notes
1. Dependencies: This code depends on a graphics.py library for GUI rendering and a button.py module for button creation. These libraries are not part of the Python standard library and must be provided.
2. Face Movement: As the snowman grows or shrinks, the face components also move up or down to stay on the top snowball.

## Potential Improvements
1. More Actions: Add additional features, such as hats or scarves, that can be added or removed.
2. Improved Messages: Provide more interactive messages and visual effects when the snowman reaches its limits.
3. Animation: Add animations when the snowman melts or freezes for a more dynamic experience.

## License
This project is provided as-is, without any warranty or guarantee of functionality. You are free to modify and distribute it as needed.

## Author
Alexander Harshman - Initial work for CS 135 Final

## Acknowledgements
graphics.py Library: For the GUI interface, allowing easy rendering of graphical elements.
Python Programming: The main language used for developing the snowman interactive program.
