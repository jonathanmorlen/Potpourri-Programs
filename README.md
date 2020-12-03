# Potpourri-Programs
Assorted programs that aren't a full project, similar to programming exercises

**Python**
- **Ackermann**: Computes the value of A(m, n) where A( ) is the [Ackermann function](https://en.wikipedia.org/wiki/Ackermann_function). Prints the value and the time it took to compute.
             
- **A_Star_Algorithm**: OOP implementation of the [A* search algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm). Computes the shortest path from a starting coordinate to an ending coordinate in a rectangular grid of 1's and 0's, where a 0 is traversable and a 1 is not. Prints the grid with the solution path as x's, the coordinates of the path elements, and the length of the path.

- **Collatz**: Finds the longest progression of the [Collatz Sequence](https://en.wikipedia.org/wiki/Collatz_conjecture) of integers 1 to n. Prints the starting number of the longest progression, the sequence length, and the time it took to compute.

- **Meepo_BlinkPoof**: Script for a combo in the game [DoTa 2](https://en.wikipedia.org/wiki/Dota_2) with the hero [Meepo](https://dota2.gamepedia.com/Meepo). Once running, uses the hotkeys 'F1' - 'F5' to set the number of Meepo clones from 1 - 5. When in game uses the hotkey '5' to tab through the appropriate number of clones and cast the ability "poof" at the location of the cursor, ending with a tab to the original meepo and a cast of "blink dagger" with the spacebar. I have never and will never use this in a game with human players, this was just a proof of concept and programming exercise.

- **backup.py**: Command line interface *daily* backup script with the format: `python.exe backup.py <source> <destination>` where `<source>` is the folder to be zipped and `<destination>` is the final location of the compressed file. Names the zip file after the current date (XX-XX-XXXX.zip). Created with the intention to use with batch files for automatic backing up of projects.

- **makeChange**: Given an amount of change 1 to 99 cents, computes the minimum number of coins needed to make that amount of change out of standard US coins (quarter, dime, nickel, penny). Prints the number of coins needed to make the amount of change.

- **orthogonal_projection**: Takes a vector and a subspace as input, computes the [orthogonal projection](https://en.wikipedia.org/wiki/Projection_(linear_algebra)) of the vector onto the subspace. Prints the projection vector.

- **playlist.py**: Interfaces with the [Spotify Developer Web API](https://developer.spotify.com/documentation/web-api/) through the [Spotipy](https://spotipy.readthedocs.io/en/2.16.1/) library in Python. Part of a growing personal project utilizing this API to implement various functionalities that I think are missing from vanilla Spotify. This program creates a public playlist or updates an existing playlist of user choice and populates it with all tracks in the "Liked Songs" section of the user's spotify account. Useful for easily and quickly sharing a user's personal "playlist" with the world. If the name for the playlist already exists, the program will update the existing one, overwriting previously stored songs while maintaining playlist followers. Automatically tags each pushed update with the current date and time in the playlist description.
