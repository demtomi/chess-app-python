# Chess Moves Suggestion App

This Python script generates a visual representation of a chessboard based on a sequence of moves and suggests the next move.

## Usage

1. Install the required library:

    ```bash
    pip install python-chess
    ```

2. Run the script:

    ```bash
    python chess_app.py
    ```

3. Example moves are provided in the script, and the suggested move is displayed.

## Customization

You can customize the script by modifying the `previous_moves` list in the script to represent your specific chess game sequence.

## Dependencies

- [python-chess](https://python-chess.readthedocs.io/): A pure Python chess library with move generation, move validation, and support for common formats.

## Visual Representation

The script generates SVG files for the current board and the next board with the suggested move. You can view these SVG files using a text editor, an SVG viewer, or a web browser.