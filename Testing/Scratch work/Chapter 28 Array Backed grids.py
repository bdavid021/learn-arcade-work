import arcade


WIDTH = 20
HEIGHT = 20
MARGIN = 5

ROW_COUNT = 10
COLUMN_COUNT = 10



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

        


    def on_draw(self):
        """
        Render the screen.

        """
        self.clear()


        for column in range(0, COLUMN_COUNT):
            arcade.draw_lrbt_rectangle_filled(MARGIN* (column * 5)+ 5, WIDTH+MARGIN * (column * 5)+ 5, MARGIN, HEIGHT+MARGIN, arcade.color.WHITE)
            for row in range(0, ROW_COUNT):
                arcade.draw_lrbt_rectangle_filled(MARGIN * (column * 5) + 5, WIDTH + MARGIN * (column * 5) + 5, MARGIN * (row * 5) + 5,HEIGHT + MARGIN * (row*5)+ 5, arcade.color.WHITE)



    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()