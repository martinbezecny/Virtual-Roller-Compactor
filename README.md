# Virtual Roller Compactor

A simple GUI-based Python application to virtually simulate the maximum pressure for given process parameters of an Alexanderwerk roller compactor, and given compressibility factor of the powder. This Virtual Roller Compactor specifically models the Alexanderwerk WP 120 Pharma equipped with textured rolls of 250mm in diameter and 4mm in width. Built with Tkinter for the GUI and NumPy for numerical integration.


## Preview
![Screenshot of AUC Calculator](https://i.imgur.com/XtOcxgb.png)

## Requirements
- Python 3.7+
- NumPy: Used for AUC calculations via numerical integration.

## Installation
### Download executable for Windows
Download the .EXE file and run: [Virtual Roller Compactor v0.2](https://github.com/martinbezecny/Virtual-Roller-Compactor/releases/download/v0.2/Virtual.Roller.Compactor.v0.2.exe)
___
### Clone git repository
- Clone the Repository
```
git clone https://github.com/martinbezecny/Virtual-Roller-Compactor
cd Virtual-Roller-Compactor
```
- Install Dependencies
```
pip install numpy customtkinter scipy
```
- Run the Application
```
python main.py
```

## Usage
- **Input Coordinates**: Enter the processing parameters and compressibility factor of the powder.
- **Calculate Maximum Pressure**: Click the 'Calculate' button to calculate.


## Contributing
Feel free to submit issues or pull requests for improvements or bug fixes! Contributions are welcomed.

Based on the work of Chi So, Lap Y. Leung, Ariel R. Muliadi, Ajit S. Narang, Chen Mao.

© 2023 Martin Bezecný
