import arcade
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SPRITE_SCALING = 1


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "RPG")
        arcade.set_background_color(arcade.color.ASH_GREY)

        # Some coordinates for buttons
        self.left = 50
        self.right = 250
        self.top = 30
        self.bottom = 130

        self.text = ""

        # Sprites -------
        self.player_list = None
        self.player_sprite = None

        self.random_number = random.randint(1, 6)

    def setup(self):
        self.player_list = arcade.SpriteList()

        # Creăm sprite-ul dintr-o imagine (arcade are resurse test)
        self.player_sprite = arcade.Sprite("character_maleAdventurer_walk7.png",
            SPRITE_SCALING
        )
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 300
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        self.clear()

        # buton start
        arcade.draw_lrbt_rectangle_filled(self.left, self.right, self.top, self.bottom, arcade.color.PEAR)
        arcade.draw_text("Start", 110, 70, arcade.color.BLACK, 30)

        # buton zar
        arcade.draw_lrbt_rectangle_filled(self.left+self.right, self.right+self.right, self.top, self.bottom, arcade.color.PEAR)
        arcade.draw_text("Da cu zarul", 320, 70, arcade.color.BLACK, 27)

        # text
        arcade.draw_text(self.text, 300, 400, arcade.color.BLACK, 30)

        # sprite
        self.player_list.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        # verificăm dacă click-ul e în interiorul butonului "Start"
        if self.left < x < self.right and self.top < y < self.bottom:
            print("Buton Start apăsat!")

        # verificăm dacă click-ul e în interiorul butonului "Zar"
        if 300 < x < self.right*2 and self.top < y < self.bottom:
            self.text = f"Număr random: {random.randrange(1, 7)}"
            print("zar")

    def on_update(self, delta_time):
        pass


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
