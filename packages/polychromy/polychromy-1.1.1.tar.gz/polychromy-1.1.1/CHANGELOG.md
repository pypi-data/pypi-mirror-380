# polychromy
<!--
## [version] - YYYY-MM-DD

- **Added**
  - 
- **Changed**
  -
- **Fixed**
  -
-->
## [1.1.1] - 2025-09-28

- **Changed**

  - Updated to support the latest version of `textlinebreaker`:
    - Replaced deprecated `split_line` function with the `TextLineBreaker` class.

### [1.1.0] - 2024-04-10

- **Changed**
  - Colors are now fetched from a remote .json file that can be updated in real time with new color names.

- **Fixed**
  - Optimized algorithm to check validity of the color.

### [1.0.2] - 2023-12-29

- **Fixed:**
  - Resolved compatibility issue when color is defined by an integer.

### [1.0.1] - 2023-12-27

- **Changed:**
  - Removed ```(System Color)``` from unique color names (e.g., "Bright Blue (System Color)" --> "Bright Blue").

### [1.0.0] - 2023-12-17

- **Added:**
  - Function ```Colorate``` to print any string using any color for background and for text.

### [0.0.2] - 2023-12-04

- **Added:**
  - Json file with list of colors.
- **Changed:**
  - Color list imported from json file

### [0.0.1] - 2023-12-01

- **First version**
