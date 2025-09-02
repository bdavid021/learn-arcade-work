import arcade


WIDTH = 20
HEIGHT = 20
MARGIN = 5

ROW_COUNT = 20
COLUMN_COUNT = 20



SCREEN_WIDTH = (WIDTH * COLUMN_COUNT + COLUMN_COUNT * MARGIN + 5  )
SCREEN_HEIGHT = (HEIGHT * ROW_COUNT + ROW_COUNT * MARGIN + 5)

#SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
#SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN




class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        # --- Create grid of numbers
        # Create an empty list
        self.grid = []
        # Loop for each row
        for row in range(ROW_COUNT):
            # For each row, create a list that will
            # represent an entire row
            self.grid.append([])
            # Loop for each column
            for column in range(COLUMN_COUNT):
                # Add a the number zero to the current row
                self.grid[row].append(0)


    def on_draw(self):
        """
        Render the screen.

        """
        self.clear()



        for row in range(0, ROW_COUNT):







            for column in range(0, COLUMN_COUNT):

                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                else:
                    color = arcade.color.WHITE

                arcade.draw_lrbt_rectangle_filled(MARGIN * (column * 5) + 5, WIDTH + MARGIN * (column * 5) + 5,
                                                  MARGIN * (row * 5) + 5, HEIGHT + MARGIN * (row * 5) + 5, color)





    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        column = int(x // (WIDTH + MARGIN))
        row = int(y // (HEIGHT + MARGIN))

        if self.grid[row][column] == 0:
            self.grid[row][column] = 1
        else:
            self.grid[row][column] = 0

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()