# Package Sorter

This project contains a Python script that simulates the sorting logic for packages in a robotic automation factory. The script classifies packages into three categories: `STANDARD`, `SPECIAL`, and `REJECTED` based on their dimensions and mass.

## Table of Contents
- [Description](#description)
- [Requirements](#requirements)
- [Usage](#usage)
- [Example Output](#example-output)

## Description

The `Package` class encapsulates the properties of a package such as width, height, length, and mass. The `sort()` method determines whether the package is `STANDARD`, `SPECIAL`, or `REJECTED` based on the following criteria:

- A package is **bulky** if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or if any one of its dimensions is greater than or equal to 150 cm.
- A package is **heavy** if its mass is greater than or equal to 20 kg.
- Packages are sorted into:
  - **STANDARD**: Neither bulky nor heavy.
  - **SPECIAL**: Either bulky or heavy.
  - **REJECTED**: Both bulky and heavy.

## Requirements

- Python 3.x

## Usage

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yashsavle/package-sort.git
    cd package-sort
    ```

2. Run the script:
    ```bash
    python3 main.py
    ```

The script is located in `main.py`, which contains the `Package` class and a `main()` function that runs example cases.

## Example Output

When you run the script, you will see output similar to the following:
```plaintext
SPECIAL
SPECIAL
STANDARD
REJECTED



