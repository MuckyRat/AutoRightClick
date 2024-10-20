# Right Click Automation Script

This script allows you to automate right-click actions on your MacBook using the `Cmd + Z` key combination to start and stop the clicking. It uses the `pynput` library for keyboard and mouse control.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)

## Features

- Start and stop right-click automation with a simple keyboard shortcut (`Cmd + Z`).
- Lightweight and easy to use without a graphical user interface.

## Requirements

- Python 3.x
- `pynput` library

## Installation

1. **Clone the repository** or download the script directly.

   ```bash
   git clone https://github.com/muckyrat/AutoRightClick.git
   cd autorightclick
2. Install Python: Make sure you have Python 3 installed on your MacBook. You can download it from the official Python website.
3. Install the pynput library: Open a terminal and run the following command:
```bash
pip install pynput
```
## Usage

1. Open a terminal and navigate to the directory where you saved right_clicker.py:
```bash
cd path/to/your/script
```
2. Run the script using Python:
```bash
python AutoRightClick.py
```
3. Start and stop right-clicking:
- Press Cmd + Z to start or stop the right-clicking action.
- The terminal will display messages indicating whether clicking has started or stopped.
4. Exit the script:
- To stop the script entirely, use Ctrl + C in the terminal.

