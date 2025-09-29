# polychromy

## Release Notes - Version 1.1.1

- Updated to support the latest `textlinebreaker` API:  
  Replaced the old `split_line` function with the new `TextLineBreaker` class.

### Release Notes - Version 1.1.0

- Colors are now fetched from a remote .json file that can be updated in real time with new color names.
- Optimized algorithm to check validity of the color.

### Release Notes - Version 1.0.2

- Fixed compatibility issue when color is defined by an integer.

### Release Notes - Version 1.0.1

- Removed ```(System Color)``` from unique color names (e.g., "Bright Blue (System Color)" --> "Bright Blue").

### Release Notes - Version 1.0.0

- Function ```colorate``` is now fully functional and can format any string in any color for background and foreground.[^Note]

[^Note]: The output color might differ from the desired one depending on terminal used.

### Release Notes - Version 0.0.2

- Color list is now stored in the additional file ```colors.json```
