import arcade
import random

from arcade.camera import generate_view_matrix

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


class Ball:
    def __init__(self, position_x, position_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)


class GeneratedBalls:
    def __init__(self, position_x, position_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)





class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our ball
        self.ball = Ball(50, 50, 10, arcade.color.AUBURN)

        generated_x = random.randint(50, 750)
        generated_y = random.randint(50, 750)

        gene_ball = []

        for i in range(5):
            self.generated_ball = GeneratedBalls(generated_x, generated_y, 25, arcade.color.BLUE)

            gene_ball.append(self.generated_ball)


    score = 0


    def on_draw(self):
        """ Called whenever we need to draw the window. """
        self.clear()
        self.ball.draw()
        self.generated_ball.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.ball.position_x = x
        self.ball.position_y = y












def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")
    arcade.run()


main()