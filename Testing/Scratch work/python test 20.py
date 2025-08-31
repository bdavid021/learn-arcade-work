import arcade
import random
import math

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SPRITE_SCALING = 1.5
BULLET_SCALING = 0.20
BULLET_SPEED = 6

# sounds
DICE = arcade.load_sound("sounds/dice-142528.mp3")
THROW = arcade.load_sound("sounds/fireball-whoosh-1-179125.mp3")
FAIL = arcade.load_sound("sounds/cartoon-fail-trumpet-278822.mp3")
WIN = arcade.load_sound("sounds/you-win-sequence-3-183950.mp3")
ZOMBIE_HURT = arcade.load_sound("sounds/retro-hurt-2-236675.mp3")


class MyGame(arcade.Window):

    def __init__(self):
        # Call the parent class's init function
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "RPG")
        arcade.set_background_color(arcade.color.LIGHT_BLUE)

        # Some coordonates for buttons
        self.left = 50
        self.right = 250
        self.top = 30
        self.bottom = 130

        self.text = ""

        # Game State **************
        self.turn = "dice"
        self.dice_done = False
        self.player_done = False
        self.zombie_done = False

        # Sprites -------
        self.player_list = None
        self.player_sprite = None

        # player characteristics
        self.health = 100
        self.player_base_attack = 10
        self.player_double_damage_attack = self.player_base_attack
        self.dodge_chance = 10
        self.double_damage_chance = False

        # ZOMBIE SPRITE
        self.zombie_list = None
        self.zombie_sprite = None

        # zombie characteristics
        self.zombie_base_attack = random.randint(5, 15)

        # Bullet sprite
        self.bullet_list = None
        self.bullet_sprite = None

        self.zombie_bullet_list = None
        self.zombie_bullet_sprite = None

        # Aiming Arrow - FIXED
        self.mouse_x = 400
        self.mouse_y = 200
        self.current_angle = 0
        self.is_locked = False
        self.locked_angle = None

        # Lock keys
        self.key = arcade.key.F
        self.key2 = arcade.key.R

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite("character_maleAdventurer_walk7.png", SPRITE_SCALING)
        self.player_sprite.center_x = 162
        self.player_sprite.center_y = 255
        self.player_list.append(self.player_sprite)

        # ZOMBIE
        self.zombie_list = arcade.SpriteList()
        self.zombie_sprite = arcade.Sprite("character_zombie_attack0.png", SPRITE_SCALING)
        self.zombie_sprite.center_x = 820
        self.zombie_sprite.center_y = 255
        self.zombie_list.append(self.zombie_sprite)
        self.zombie_health = 150

        # BULLET
        self.bullet_list = arcade.SpriteList()

        # ZOMBIE BULLET
        self.zombie_bullet_list = arcade.SpriteList()

    def on_draw(self):
        self.clear()

        # Scena
        arcade.draw_lrbt_rectangle_filled(0, 1000, 150, 161, arcade.color.ARCADE_GREEN)
        arcade.draw_lrbt_rectangle_filled(0, 1000, 1, 150, arcade.color.BROWN_NOSE)

        # Copacei
        arcade.draw_lrbt_rectangle_filled(70, 100, 161, 290, arcade.csscolor.BROWN)
        arcade.draw_circle_filled(85, 290, 80, arcade.csscolor.DARK_GREEN)

        arcade.draw_lrbt_rectangle_filled(390, 420, 161, 290, arcade.csscolor.BROWN)
        arcade.draw_triangle_filled(400, 390, 310, 220, 500, 220, arcade.csscolor.DARK_GREEN)

        # butoanele-------------
        if self.turn == "dice":
            arcade.draw_lrbt_rectangle_filled(self.left + self.right, self.right + self.right, self.top, self.bottom,
                                              arcade.color.LIGHT_BLUE)
            arcade.draw_text("Da cu zarul", 320, 70, arcade.color.BLACK, 27)
        if self.turn == "player":
            arcade.draw_lrbt_rectangle_filled(self.left, self.right, self.top, self.bottom, arcade.color.PEAR)
            arcade.draw_text(f"Ataca!", 110, 70, arcade.color.BLACK, 30)

        arcade.draw_lrbt_rectangle_filled(self.left + self.right + self.right, self.right * 3, self.top, self.bottom,
                                          arcade.color.LIGHT_BLUE)
        arcade.draw_text("Zombi, atac", 565, 70, arcade.color.BLACK, 27)

        # =================AFISAZE (HUD)
        # Afisez viata zombie
        arcade.draw_text(f"{self.zombie_health} HP", 790, 350, arcade.color.ARCADE_GREEN, 25)
        arcade.draw_text(f"{self.zombie_base_attack} Damage", 790, 390, arcade.color.ARCADE_GREEN, 25)

        # Afisez viata om
        arcade.draw_text(f"{self.health} HP", 130, 350, arcade.color.DARK_RED, 25)
        arcade.draw_text(self.text, 300, 400, arcade.color.BLACK, 30)

        # Afisez statisitici importante, colt stanga sus =============
        if self.double_damage_chance == True:
            arcade.draw_text(f"Ataci cu {self.player_base_attack * 2} damage", 20, 570, arcade.color.BLACK, 20)
        else:
            arcade.draw_text(f"Ataci cu {self.player_base_attack} damage", 20, 570, arcade.color.BLACK, 20)

        arcade.draw_text(f"Sansa ta de a te ferii este {self.dodge_chance} ", 20, 540, arcade.color.BLACK, 20)
        arcade.draw_text(f"Tura aceasta dai damaga dublu: {self.double_damage_chance} ", 20, 510, arcade.color.BLACK,
                         20)

        # desenez player
        self.player_list.draw()

        # desenez zombie
        self.zombie_list.draw()

        # desenez bullet
        self.bullet_list.draw()

        # desenez zombie bullet
        self.zombie_bullet_list.draw()

        # End gamea
        if self.zombie_health <= 0:
            arcade.draw_text("Ai castigat", 230, 300, arcade.color.BLUEBERRY, 110)

        if self.health <= 0:
            arcade.draw_text("Ai pierdut", 230, 300, arcade.color.BLUEBERRY, 110)

        # FIXED: Arrow drawing and aiming
        # Calculate the angle for aiming
        if self.is_locked and self.locked_angle is not None:
            # Use locked angle
            angle_to_use = self.locked_angle
        else:
            # Calculate angle from player to mouse position
            player_x = self.player_sprite.center_x + 60
            player_y = self.player_sprite.center_y - 25  # Adjust for better visual
            angle_to_use = math.atan2(self.mouse_y - player_y, self.mouse_x - player_x)

        # Store the current angle for bullet shooting
        self.current_angle = angle_to_use

        # Calculate end point of the aiming line
        line_length = 150
        start_x = self.player_sprite.center_x + 60
        start_y = self.player_sprite.center_y - 25
        end_x = start_x + math.cos(angle_to_use) * line_length
        end_y = start_y + math.sin(angle_to_use) * line_length

        # Draw the aiming line
        if self.turn == "player":  # Only show aiming line during player turn
            color = arcade.color.RED if self.is_locked else arcade.color.YELLOW
            arcade.draw_line(start_x, start_y, end_x, end_y, color, 3)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.F:
            # Lock the current aiming direction
            player_x = self.player_sprite.center_x + 60
            player_y = self.player_sprite.center_y - 25
            self.locked_angle = math.atan2(self.mouse_y - player_y, self.mouse_x - player_x)
            self.is_locked = True
            print(f"Locked angle: {self.locked_angle}")

        if symbol == arcade.key.R:
            # Release the lock
            self.locked_angle = None
            self.is_locked = False
            print("Angle unlocked")

    def on_mouse_motion(self, x, y, dx, dy):
        # Update mouse position for aiming
        self.mouse_x = x
        self.mouse_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        if self.turn == "dice":
            if 300 < x < self.right * 2 and y > self.top and y < self.bottom:
                arcade.play_sound(DICE)
                self.random_number = random.randint(1, 6)
                self.text = f"Numar random: {self.random_number}"
                if self.random_number % 2 == 0:
                    self.double_damage_chance = True
                    self.player_double_damage_attack = self.player_base_attack * 2
                else:
                    self.double_damage_chance = False

                self.dice_done = True
                self.player_done = False
                print(self.turn)

        # FIXED: Player attack button
        if self.turn == "player":
            if self.left < x < self.right and y > self.top and y < self.bottom:
                print("Buton apăsat!", self.turn)

                # Create bullet
                bullet = arcade.Sprite("ballBlack_04.png", BULLET_SCALING)
                arcade.play_sound(THROW)

                # Set bullet starting position
                bullet.center_x = self.player_sprite.center_x + 60
                bullet.center_y = self.player_sprite.center_y - 25

                # FIXED: Set bullet velocity using the current aiming angle
                bullet.change_x = math.cos(self.current_angle) * BULLET_SPEED
                bullet.change_y = math.sin(self.current_angle) * BULLET_SPEED

                self.bullet_list.append(bullet)
                self.player_done = True
                self.zombie_done = False

        # Butonul din dreapta de zombi (pt test)
        if x > 550 and x < 750 and y > self.top and y < self.bottom:
            pass

    def on_update(self, delta_time):
        self.bullet_list.update()
        self.zombie_list.update()

        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet, self.zombie_list)

            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
                if self.double_damage_chance == True:
                    self.zombie_health -= self.player_double_damage_attack
                    arcade.play_sound(ZOMBIE_HURT)
                else:
                    self.zombie_health -= self.player_base_attack
                    arcade.play_sound(ZOMBIE_HURT)

        self.zombie_bullet_list.update()

        for zombie_bullet in self.zombie_bullet_list:
            if self.dodge_chance == 1:
                print("evade")
            else:
                hit_list = arcade.check_for_collision_with_list(zombie_bullet, self.player_list)
                self.zombie_base_attack = random.randint(10, 20)
                if len(hit_list) > 0:
                    zombie_bullet.remove_from_sprite_lists()
                    if self.double_damage_chance == True:
                        self.health -= self.zombie_base_attack
                    else:
                        self.health -= self.zombie_base_attack

        if self.dice_done == True:
            self.turn = "player"

        if self.player_done == True:
            self.turn = "zombie"

        if self.zombie_done == True and self.player_done == True:
            self.turn = "dice"

        if self.turn == "zombie":
            print("merge")

            zombie_bullet = arcade.Sprite("ballBlue_07.png", BULLET_SCALING)
            zombie_bullet.center_x = self.zombie_sprite.center_x - 50
            zombie_bullet.center_y = 190
            zombie_bullet.change_x = -BULLET_SPEED + 1.5
            self.zombie_bullet_list.append(zombie_bullet)
            self.dodge_chance = random.randint(1, 10)

            self.zombie_done = True
            print(self.turn)


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()