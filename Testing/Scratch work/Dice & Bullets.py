import arcade
import random
import time
import math


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SPRITE_SCALING = 1.5
BULLET_SCALING = 0.15
BULLET_SPEED =6

#sounds
DICE = arcade.load_sound("sounds/dice-142528.mp3")
THROW = arcade.load_sound("sounds/retro-game-shot-152052.mp3")
FAIL = arcade.load_sound("sounds/dead-8bit-41400.mp3")
WIN = arcade.load_sound("sounds/you-win-sequence-3-183950.mp3")
ZOMBIE_HURT = arcade.load_sound("sounds/retro-hurt-2-236675.mp3")
ELEVATOR_MUSIC = arcade.load_sound("sounds/jazz-lounge-elevator-music-332339.mp3")
HIGH_DAMAGE_LOST = arcade.load_sound("sounds/explosion-8-bit-11-314691.mp3")
DAMAGE_LOST = arcade.load_sound("sounds/hurt_c_08-102842.mp3")
HEAL = arcade.load_sound("sounds/classic-game-action-positive-10-224398.mp3")
UI = arcade.load_sound("sounds/confirm-tap-394001.mp3")
BULLETS_COLLIDING = arcade.load_sound("sounds/funny-boing-flexatone-wobble-352710.mp3")
EVADE = arcade.load_sound("sounds/classic-game-action-positive-1-224407.mp3")

#DRAWING THINGS

def draw_tutorial_objects():
    # TUTORIAL MENIU =========================

    # BUTON BACK
    arcade.draw_lrbt_rectangle_filled(930, 990, 530, 590, arcade.color.LIGHT_RED_OCHRE)
    arcade.draw_lrbt_rectangle_outline(930, 990, 530, 590, arcade.color.BLACK, 3)
    arcade.draw_text("BACK", 935, 554, arcade.color.BLACK, 17)

    # EXPLICATII
    arcade.draw_text("Bine ai venit la Dice & Bullet!", 220, 550, arcade.color.BLACK, 25)

    arcade.draw_text("GENERAL GAME KNOWLEDGE: ", 20, 460, arcade.color.BLACK, 20)

    arcade.draw_text("1. Scopul acestui joc este sa invingi zombi-ul (HP = 0), fara ca tu sa mori.", 20, 420,
                     arcade.color.BLACK, 17)
    arcade.draw_text(
        "2. Trebuie sa dai cu zarul apasand pe buton, daca ai nimerit un numar par, atunci in aceea tura vei da 2x DMG.",
        20, 390, arcade.color.BLACK, 17)
    arcade.draw_text("3. Si zombie-ul da cu zarul, asa ca fii atent cat de puternic te ataca!", 20, 360,
                     arcade.color.BLACK, 17)
    arcade.draw_text(
        "4. Misca, mouse-ul pentru a tinti, unde vrei sa tragi pe tasta \"F\" blochezi tinta, iar pe \"R\" deblochezi.",
        20, 330, arcade.color.BLACK, 17)
    arcade.draw_text("5. Dupa ce ai blocat tinta ATACA zombi-ul, sau bullet-ul acestuia pentru a bloca atacului lui!",
                     20, 300, arcade.color.BLACK, 17)
    arcade.draw_text("6. Ai o sansa de 10% de a evita complet atacul zombi-ului!", 20, 270, arcade.color.BLACK, 17)

    arcade.draw_text("ITEMS: ", 20, 230, arcade.color.BLACK, 20)

    arcade.draw_text("- Medkit: Ai o sansa de 10% ca sa se spawneze un Medkit pe harta. Acesta regenereaza 20 HP.", 20,
                     190, arcade.color.BLACK, 17)

    arcade.draw_text("TIPS: ", 20, 150, arcade.color.BLACK, 17)

    arcade.draw_text("1. Gandeste-te ce se merita mai mult! Sa ataci zombi-ul, bazandu-te ca poate eviti atacul?", 20,
                     120, arcade.color.BLACK, 17)
    arcade.draw_text(
        "   sau poate esti low, si se merita sa ataci bullet-ul zombi-ului pentru a fi sigur? sau de ce nu sa iei", 20,
        90, arcade.color.BLACK, 17)
    arcade.draw_text("   acel medkit... dar oare se merita? zarul iti va purta noroc?", 20, 60, arcade.color.BLACK, 17)
    arcade.draw_text("TU DECIZI ASTA! Mult noroc!", 300, 20, arcade.color.BLACK, 24)

def draw_main_menu():
    # BUTON START
    arcade.set_background_color(arcade.color.YELLOW_GREEN)
    arcade.draw_lrbt_rectangle_filled(300, 700, 300, 380, arcade.color.LIGHT_BLUE)
    arcade.draw_lrbt_rectangle_outline(300, 700, 300, 380, arcade.color.BLACK, 3)
    arcade.draw_text("START", 420, 320, arcade.color.BLACK, 50)

    # TITLU
    arcade.draw_text("Dice & Bullets!", 224, 446, arcade.color.BLACK, 71)
    arcade.draw_text("Dice & Bullets!", 230, 450, arcade.color.ARCADE_GREEN, 70)

    # BUTON TUTORIAL
    arcade.set_background_color(arcade.color.YELLOW_GREEN)
    arcade.draw_lrbt_rectangle_filled(300, 700, 200, 280, arcade.color.LIGHT_RED_OCHRE)
    arcade.draw_lrbt_rectangle_outline(300, 700, 200, 280, arcade.color.BLACK, 3)
    arcade.draw_text("TUTORIAL", 373, 220, arcade.color.BLACK, 50)

    #BUTON BACK
    arcade.draw_lrbt_rectangle_filled(930, 990, 530, 590, arcade.color.LIGHT_RED_OCHRE)
    arcade.draw_lrbt_rectangle_outline(930, 990, 530, 590, arcade.color.BLACK, 3)
    arcade.draw_text("BACK", 935, 554, arcade.color.BLACK, 17)


    #DECORURI

    x = 850
    y = 100

    arcade.draw_circle_filled(x - 80, y, 35, arcade.color.BRITISH_RACING_GREEN, 3)
    arcade.draw_circle_filled(x + 50, y + 60, 50, arcade.color.CASTLETON_GREEN,3)
    arcade.draw_circle_filled(x, y, 65, arcade.color.BOTTLE_GREEN, 3, )

    arcade.draw_circle_outline(x - 80, y, 35, arcade.color.BLACK)
    arcade.draw_circle_outline(x + 50, y + 60, 50, arcade.color.BLACK)
    arcade.draw_circle_outline(x, y, 65, arcade.color.BLACK)



    x2 = 150
    y2 = 500



    arcade.draw_circle_outline(x2 - 80, y2- 90, 35, arcade.color.BLACK)
    arcade.draw_circle_outline(x2 + 20, y2 + 50, 50, arcade.color.BLACK)
    arcade.draw_circle_outline(x2- 60, y2- 10, 65, arcade.color.BLACK)

    arcade.draw_circle_filled(x2 - 80, y2 - 90, 35, arcade.color.BRITISH_RACING_GREEN)
    arcade.draw_circle_filled(x2 + 20, y2 + 50, 50, arcade.color.CASTLETON_GREEN)
    arcade.draw_circle_filled(x2 - 60, y2 - 10, 65, arcade.color.BOTTLE_GREEN)



class MyGame(arcade.Window):

    def __init__(self):

        # Call the parent class's init function
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Dice & Bullets!")
        arcade.set_background_color(arcade.color.LIGHT_BLUE)



        #STARTING MENU

        self.menu_choice = 1


        self.game_done = False



        #Some coordonates for buttons
        self.left = 50
        self.right = 250
        self.top = 30
        self.bottom = 130


        self.text = ""

        #Game State **************
        self.turn = "dice"
        self.dice_done = False
        self.player_done = False
        self.zombie_done = False

        #Sprites -------

        self.player_list = None
        self.player_sprite = None

        #player characteristics

        self.health = 100
        self.player_base_attack = 10
        self.player_double_damage_attack = self.player_base_attack
        self.dodge_chance = 10
        self.dodge_chance_bool = False
        self.double_damage_chance = False
        self.triple_damage_chance = False

        #Body damage

        self.head_damage = False
        self.body_damage = False
        self.foot_damage = False

        self.sprite_damage_chance = None




        self.health_less_than_last_turn = self.health


        #ZOMBIE SPRITE
        self.zombie_list = None
        self.zombie_sprite = None

        #zombie characteristics
        self.zombie_did_shoot = True
        self.zombie_did_not_missed = False

        self.zombie_base_attack = 0

        #Bulltet sprite

        self.bullet_list = None
        self.bullet_sprite = None

        self.zombie_bullet_list = None
        self.zombie_bullet_sprite = None
        self.bullet = None

        #MEDKIT SPRITE

        self.medkit_list = None
        self.medkit_sprite = None

        #DAMAGED BODY PARTS SPRITE

        self.head_damaged_list = None
        self.head_damaged_sprite = None

        self.body_damaged_list = None
        self.body_damaged_sprite = None

        self.foot_damaged_list = None
        self.foot_damaged_sprite = None

        #Aiming Arrow

        self.mouse_x = 400
        self.mouse_y = 200
        self.current_angle = 0
        self.is_locked = False
        self.locked_angle = None


        #Lock
        self.key = arcade.key.F
        self.key2 = arcade.key.R

        # Moving DICE

        self.dice_list = arcade.SpriteList()
        self.dice_sprite = arcade.Sprite("dice_question.png", SPRITE_SCALING+2)

        self.dice_sprite.position_y = 100
        self.dice_sprite.position_x = 100


        self.dice_list.append(self.dice_sprite)


    def draw_HUD(self):
        # =================AFISAZE (HUD)

        # Afisez viata zombie

        arcade.draw_text(f"{self.zombie_health} HP", 789, 349, arcade.color.BLACK, 25)
        arcade.draw_text(f"{self.zombie_health} HP", 790, 350, arcade.color.ARCADE_GREEN, 25)

        arcade.draw_text(f"{self.zombie_base_attack} DMG", 789, 389, arcade.color.BLACK, 25)
        arcade.draw_text(f"{self.zombie_base_attack} DMG", 790, 390, arcade.color.ARCADE_GREEN, 25)

        # Afisez viata om
        arcade.draw_text(f"{self.health} HP", 129, 349, arcade.color.BLACK, 25)
        arcade.draw_text(f"{self.health} HP", 130, 350, arcade.color.DARK_RED, 25)

        #Afisez damage om
        if self.triple_damage_chance == True and self.double_damage_chance == False:
            arcade.draw_text(f"{self.player_base_attack * 3} DMG", 129, 389, arcade.color.BLACK, 25)
            arcade.draw_text(f"{self.player_base_attack * 3} DMG", 130, 390, arcade.color.DARK_RED, 25)
        elif self.double_damage_chance == True:
            arcade.draw_text(f"{self.player_base_attack * 2} DMG", 129, 389, arcade.color.BLACK, 25)
            arcade.draw_text(f"{self.player_base_attack * 2} DMG", 130, 390, arcade.color.DARK_RED, 25)
        else:
            arcade.draw_text(f"{self.player_base_attack} DMG", 129, 389, arcade.color.BLACK, 25)
            arcade.draw_text(f"{self.player_base_attack} DMG", 130, 390, arcade.color.DARK_RED, 25)

        # Afisez statisitici importante, colt stanga sus =============

        arcade.draw_text(f"Aceasta tura te feresti: {self.dodge_chance_bool} ", 20, 570, arcade.color.FRENCH_LIME, 20)
        arcade.draw_text(f"Aceasta tura te feresti: {self.dodge_chance_bool} ", 19, 569, arcade.color.BLACK, 20)

        if self.triple_damage_chance == True:
            arcade.draw_text(f"Boosted Damage: {self.triple_damage_chance} ", 20, 540, arcade.color.CELADON_BLUE,
                             20)
            arcade.draw_text(f"Boosted Damage: {self.triple_damage_chance} ", 19, 539, arcade.color.BLACK,
                             20)
        else:
            arcade.draw_text(f"Boosted Damage: {self.double_damage_chance} ", 20, 540, arcade.color.CELADON_BLUE,
                             20)
            arcade.draw_text(f"Boosted Damage: {self.double_damage_chance} ", 19, 539, arcade.color.BLACK,
                         20)
        # Afisez numarul random
        arcade.draw_text(self.text, 20, 500, arcade.color.CAPUT_MORTUUM, 30)
        arcade.draw_text(self.text, 19, 499, arcade.color.BLACK, 30)

        #Afisez buton exit main-menu

        # BUTON BACK
        arcade.draw_lrbt_rectangle_filled(930, 990, 530, 590, arcade.color.LIGHT_RED_OCHRE)
        arcade.draw_lrbt_rectangle_outline(930, 990, 530, 590, arcade.color.BLACK, 3)
        arcade.draw_text("BACK", 935, 554, arcade.color.BLACK, 17)


    def draw_MAIN_GAME(self):

        # Peisaj in caz de lovitura mare

        # Scena
        if self.triple_damage_chance == True and self.zombie_base_attack >= 15:
            arcade.set_background_color(arcade.color.FLAX)
            arcade.draw_lrbt_rectangle_filled(500,1000,150,600, arcade.color.SLATE_GRAY)
            # Norisori
            x = 300
            y = 500

            arcade.draw_circle_filled(x - 70, y, 35, arcade.color.WHITE)
            arcade.draw_circle_filled(x, y, 60, arcade.color.WHITE)
            arcade.draw_circle_filled(x + 70, y, 35, arcade.color.WHITE)


            x2 = 700
            y2 = 420
            arcade.draw_circle_filled(x2 - 70, y2, 35, arcade.color.YANKEES_BLUE)
            arcade.draw_circle_filled(x2, y2, 60, arcade.color.YANKEES_BLUE)
            arcade.draw_circle_filled(x2 + 70, y2, 35, arcade.color.YANKEES_BLUE)
        elif self.triple_damage_chance == True:
            arcade.set_background_color(arcade.color.FLAX)

            # Norisori

            x = 300
            y = 500

            arcade.draw_circle_filled(x - 70, y, 35, arcade.color.WHITE)
            arcade.draw_circle_filled(x, y, 60, arcade.color.WHITE)
            arcade.draw_circle_filled(x + 70, y, 35, arcade.color.WHITE)

            x2 = 700
            y2 = 420
            arcade.draw_circle_filled(x2 - 70, y2, 35, arcade.color.WHITE)
            arcade.draw_circle_filled(x2, y2, 60, arcade.color.WHITE)
            arcade.draw_circle_filled(x2 + 70, y2, 35, arcade.color.WHITE)

        elif self.zombie_base_attack >= 15:
            arcade.set_background_color(arcade.color.SLATE_GRAY)

            x = 300
            y = 500

            arcade.draw_circle_filled(x - 70, y, 35, arcade.color.YANKEES_BLUE)
            arcade.draw_circle_filled(x, y, 60, arcade.color.YANKEES_BLUE)
            arcade.draw_circle_filled(x + 70, y, 35, arcade.color.YANKEES_BLUE)

            x2 = 700
            y2 = 420
            arcade.draw_circle_filled(x2 - 70, y2, 35, arcade.color.YANKEES_BLUE)
            arcade.draw_circle_filled(x2, y2, 60, arcade.color.YANKEES_BLUE)
            arcade.draw_circle_filled(x2 + 70, y2, 35, arcade.color.YANKEES_BLUE)





        else:
            arcade.set_background_color(arcade.color.LIGHT_BLUE)

            # Norisori

            x = 300
            y = 500

            arcade.draw_circle_filled(x - 70, y, 35, arcade.color.WHITE)
            arcade.draw_circle_filled(x, y, 60, arcade.color.WHITE)
            arcade.draw_circle_filled(x + 70, y, 35, arcade.color.WHITE)

            x2 = 700
            y2 = 420
            arcade.draw_circle_filled(x2 - 70, y2, 35, arcade.color.WHITE)
            arcade.draw_circle_filled(x2, y2, 60, arcade.color.WHITE)
            arcade.draw_circle_filled(x2 + 70, y2, 35, arcade.color.WHITE)

        # Copacei

        #boschet
        arcade.draw_circle_filled(570, 172, 35, arcade.color.BRITISH_RACING_GREEN)
        arcade.draw_circle_filled(640, 172,60, arcade.color.BRITISH_RACING_GREEN)
        arcade.draw_circle_filled(710, 152, 35, arcade.color.BRITISH_RACING_GREEN)

        arcade.draw_lrbt_rectangle_filled(70, 100, 161, 290, arcade.csscolor.BROWN)
        arcade.draw_lrbt_rectangle_outline(70, 100, 161, 290, arcade.csscolor.BLACK)
        arcade.draw_circle_filled(85, 290, 80, arcade.csscolor.DARK_GREEN)
        arcade.draw_circle_outline(85, 290, 80, arcade.csscolor.BLACK, 1)

        arcade.draw_lrbt_rectangle_filled(390, 420, 161, 290, arcade.csscolor.BROWN)
        arcade.draw_lrbt_rectangle_outline(390, 420, 161, 290, arcade.csscolor.BLACK)
        arcade.draw_triangle_filled(400, 390, 310, 220, 500, 220, arcade.csscolor.DARK_GREEN)
        arcade.draw_triangle_outline(400, 390, 310, 220, 500, 220, arcade.csscolor.BLACK)

        # Scena
        arcade.draw_lrbt_rectangle_filled(0, 1000, 150, 161, arcade.color.ARCADE_GREEN)
        arcade.draw_lrbt_rectangle_outline(0, 1001, 150, 161, arcade.color.BLACK, 1)

        arcade.draw_lrbt_rectangle_filled(0, 1000, 0, 150, arcade.color.BROWN_NOSE)



    def setup(self):

        self.player_list = arcade.SpriteList()

        self.player_sprite = arcade.Sprite("character_maleAdventurer_side.png", SPRITE_SCALING)

        self.player_sprite.center_x  = 162
        self.player_sprite.center_y  = 255
        self.player_list.append(self.player_sprite)


        self.head_damaged_list = arcade.SpriteList()
        self.head_damaged_sprite = arcade.Sprite("sprites/head_damaged_no_bg.png", SPRITE_SCALING-0.75)
        self.head_damaged_sprite.center_y = 465
        self.head_damaged_sprite.center_x = 40
        self.head_damaged_list.append(self.head_damaged_sprite)

        self.body_damaged_list = arcade.SpriteList()
        self.body_damaged_sprite = arcade.Sprite("sprites/body_damaged_no_bg.png", SPRITE_SCALING-0.75)
        self.body_damaged_sprite.center_y = 432
        self.body_damaged_sprite.center_x = 40
        self.body_damaged_list.append(self.body_damaged_sprite)

        self.foot_damaged_list = arcade.SpriteList()
        self.foot_damaged_sprite = arcade.Sprite("sprites/leg_damaged_no_bg (1).png", SPRITE_SCALING - 0.75)
        self.foot_damaged_sprite.center_y = 410
        self.foot_damaged_sprite.center_x = 45
        self.foot_damaged_list.append(self.foot_damaged_sprite)



        #ZOMBIE

        self.zombie_list = arcade.SpriteList()

        self.zombie_sprite = arcade.Sprite("character_zombie_attack0.png", SPRITE_SCALING)

        self.zombie_sprite.center_x = 820
        self.zombie_sprite.center_y = 255
        self.zombie_list.append(self.zombie_sprite)

        self.zombie_health = 150

        #BULLET

        self.bullet_list = arcade.SpriteList()

        #ZOMBIE BULLET

        self.zombie_bullet_list = arcade.SpriteList()

        # MEDKIT

        self.medkit_list = arcade.SpriteList()

        self.medkit_sprite = arcade.Sprite("health-red 32px.png", SPRITE_SCALING)

        self.medkit_sprite.center_x = random.randint(150, 990)
        self.medkit_sprite.center_y = random.randint(250, 580)

        self.medkit_list.append(self.medkit_sprite)

        self.spawn_medkit = False

        if self.menu_choice == 1 :
            player = arcade.play_sound(ELEVATOR_MUSIC, volume= 0.15, loop=True)



    def on_draw(self):

        self.clear()


        #MENIU ********************************************************************************************************


        if self.menu_choice == 1:

            #MAIN MENU

            draw_main_menu()
            self.game_done = False

            self.dice_list.draw()


        elif self.menu_choice == 2:

            #GAME

            self.draw_MAIN_GAME()


            self.draw_HUD()

    #==============================================




            #butoanele-------------
            if self.turn == "dice" and self.zombie_did_shoot == True:
                #time.sleep(0.9)

                arcade.draw_lrbt_rectangle_filled(self.left+self.right, self.right+self.right, self.top, self.bottom, arcade.color.WHITE)
                arcade.draw_lrbt_rectangle_outline(self.left+self.right, self.right+self.right, self.top, self.bottom, arcade.color.BLACK, 3)
                arcade.draw_text("Dă cu zarul", 320, 70, arcade.color.BLACK, 27)


            if self.turn == "player":
                arcade.draw_lrbt_rectangle_filled(self.left, self.right, self.top, self.bottom, arcade.color.PEAR)
                arcade.draw_lrbt_rectangle_outline(self.left, self.right, self.top, self.bottom, arcade.color.BLACK, 3)
                arcade.draw_text(f"Ataca!", 100, 70, arcade.color.BLACK, 30)

            else:
                ...



            arcade.draw_lrbt_rectangle_filled(self.left+self.right+self.right, self.right*3, self.top, self.bottom, arcade.color.LIGHT_BLUE)
            arcade.draw_text("Zombi, atac", 565, 70, arcade.color.BLACK, 27)



            #desenez player

            self.player_list.draw()

            if self.foot_damage == True:
                self.foot_damaged_list.draw()
            else:
                self.foot_damaged_sprite = arcade.SpriteList()

            if self.body_damage == True:
                self.body_damaged_list.draw()
            else:
                self.body_damaged_sprite = arcade.SpriteList()

            if self.head_damage == True:
                self.head_damaged_list.draw()
            else:
                self.head_damaged_sprite = arcade.SpriteList()




            #desenez zombie

            self.zombie_list.draw()

            #desenez bullet

            self.bullet_list.draw()

            #desenez zombie bullet

            self.zombie_bullet_list.draw()

            #Desenez medkit

            self.medkit_list.draw()



            # End game
            if self.zombie_health <= 0:

                arcade.play_sound(WIN)

                arcade.draw_text("Ai castigat! :)", 175, 305, arcade.color.BLACK, 110)
                arcade.draw_text("Ai castigat! :)", 180, 300, arcade.color.BLUEBERRY, 110)


                self.game_done = True
                self.menu_choice = 1

            if self.health <= 0:

                arcade.play_sound(FAIL)

                arcade.draw_text("Ai pierdut! :(", 175, 305, arcade.color.BLACK, 110)
                arcade.draw_text("Ai pierdut! :(", 180, 300, arcade.color.BLUEBERRY, 110)

                self.game_done = True
                self.menu_choice = 1


            # Arrow
            if self.is_locked and self.locked_angle is not None:
                # Use locked angle
                angle_to_use = self.locked_angle
            else:
                # Calculate angle from player to mouse position
                player_x = self.player_sprite.center_x + 60
                player_y = self.player_sprite.center_y - 25  # Adjust for better visual
                angle_to_use = math.atan2(self.mouse_y - player_y, self.mouse_x - player_x)


            self.current_angle = angle_to_use

            # Calculate end point of the aiming line
            line_length = 150
            start_x = self.player_sprite.center_x + 60
            start_y = self.player_sprite.center_y - 25
            end_x = start_x + math.cos(angle_to_use) * line_length
            end_y = start_y + math.sin(angle_to_use) * line_length

            if self.turn == "player":  # Only show aiming line during player turn
                color = arcade.color.RED if self.is_locked else arcade.color.YELLOW
                arcade.draw_line(start_x, start_y, end_x, end_y, color, 3)


        elif self.menu_choice == 3:

            # TUTORIAL

            draw_tutorial_objects()






    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.F:

            player_x = self.player_sprite.center_x + 60
            player_y = self.player_sprite.center_y - 25
            self.locked_angle = math.atan2(self.mouse_y - player_y, self.mouse_x - player_x)
            self.is_locked = True

        if symbol == arcade.key.R:
            self.locked_angle = None
            self.is_locked = False


    def on_mouse_motion(self, x, y, dx, dy):

        self.mouse_x = x
        self.mouse_y = y
        if self.menu_choice == 1 or self.menu_choice == 3:
            self.set_mouse_visible(True)
        else:
            if y <161:
                self.set_mouse_visible(True)
            else:
                self.set_mouse_visible(False)


        if x> 930 and y > 530 and x < 990 and y < 590:
            self.set_mouse_visible(True)

        # Daca nu vrem ca sa se vada cursorul mousului


    def on_mouse_press(self, x, y, button, modifiers):



        if x > 300 and x < 700 and y > 300 and y < 380:
            arcade.play_sound(UI)

            # RESET GAME TO START

            self.menu_choice = 2
            self.turn = "dice"
            self.dice_done = False
            self.player_done = False
            self.zombie_done = False
            self.health = 100
            self.zombie_health = 150
            self.triple_damage_chance = False
            self.zombie_base_attack = 10
            self.medkit_list.clear()
            self.zombie_bullet_list.clear()
            self.bullet_list.clear()

            self.zombie_did_shoot = True

            self.foot_damaged_sprite = arcade.SpriteList()
            self.body_damaged_sprite = arcade.SpriteList()
            self.head_damaged_sprite = arcade.SpriteList()

            self.text = None


        if x> 930 and x < 990 and y > 530 and y < 590 and self.menu_choice == 1:
            arcade.play_sound(UI)
            arcade.close_window()



        if x > 300 and x < 700 and y >200 and y< 280:
            arcade.play_sound(UI)
            self.menu_choice = 3


        if x> 930 and x < 990 and y > 530 and y < 590:
            arcade.play_sound(UI)
            self.menu_choice = 1







#******************** Buton DICE **************

        if self.turn == "dice" and self.zombie_did_shoot == True:

            if 300 < x < self.right * 2 and y > self.top and y < self.bottom or arcade.key.SPACE == True:


                arcade.play_sound(DICE)

                #Dice going
                self.random_number = random.randint(1, 6)
                #dodge calculating

                self.dodge_chance = random.randint(1, 10)
                if self.dodge_chance == 1:
                    self.dodge_chance_bool = True
                    arcade.play_sound(EVADE)

                self.text = f"Numar random: {self.random_number}"
                if self.random_number % 2 == 0:
                    self.double_damage_chance = True
                    self.player_double_damage_attack = self.player_base_attack * 2
                else:
                    self.double_damage_chance = False


                if self.random_number == 6:
                    self.triple_damage_chance = True
                    self.double_damage_chance = False
                    self.player_triple_damage_attack = self.player_base_attack * 3
                else:
                    self.triple_damage_chance = False

                self.dice_done = True
                self.player_done = False


                # MEDKIT SPAWN CHANCE

                medkit_spawn_change = random.randint(1, 10)

                if medkit_spawn_change == 1:
                    self.spawn_medkit = True
                    medkit = arcade.Sprite("health-red 32px.png", SPRITE_SCALING)

                    medkit.center_x = random.randint(150, 800)
                    medkit.center_y = random.randint(250, 580)

                    self.medkit_list.append(medkit)

                self.zombie_did_shoot = False
                self.zombie_base_attack = random.randint(10, 20)












        #Buronul din stanga de atac ------

        if self.turn == "player":
            if self.left < x < self.right and y > self.top and y < self.bottom:

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







        #Butonul din dreapta de zombi (pt test)

        if x > 550 and x < 750 and y > self.top and y < self.bottom:
            print("Esti slaaaab")




    def on_update(self, delta_time):

        if self.menu_choice == 1:
            self.dice_list.update()
            self.dice_sprite.center_x = 150
            self.dice_sprite.center_y = 120

            self.dice_sprite.angle += 2

        #game timer after end game
        if self.game_done == True:
            for i in range(1,5):
                time.sleep(1)




        self.bullet_list.update()
        self.zombie_list.update()

        for self.bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(self.bullet, self.zombie_list)



            if len(hit_list) > 0:
                self.bullet.remove_from_sprite_lists()
                if self.triple_damage_chance == True:
                    self.zombie_health -= self.player_triple_damage_attack
                    arcade.play_sound(ZOMBIE_HURT)
                    self.zombie_did_not_missed = True



                elif self.double_damage_chance == True:
                    self.zombie_health -= self.player_double_damage_attack
                    arcade.play_sound(ZOMBIE_HURT)
                    self.zombie_did_not_missed = True
                else:
                    self.zombie_health -= self.player_base_attack
                    arcade.play_sound(ZOMBIE_HURT)
                    self.zombie_did_not_missed = True





        for zombie_bullet in self.zombie_bullet_list:


            if self.dodge_chance == 1:

                self.dodge_chance_bool = True
                self.zombie_did_shoot = True

            else:
                hit_list = arcade.check_for_collision_with_list(zombie_bullet, self.player_list)
                self.dodge_chance_bool = False



                if len(hit_list) > 0:
                    self.zombie_did_shoot = True
                    self.zombie_did_not_missed = True
                    zombie_bullet.remove_from_sprite_lists()

                    self.health -= self.zombie_base_attack

                    if self.zombie_base_attack >= 15:
                        arcade.play_sound(HIGH_DAMAGE_LOST)
                    else:
                        arcade.play_sound(DAMAGE_LOST, volume = 1.5)





            player_hit_list = arcade.check_for_collision_with_list(zombie_bullet, self.bullet_list)


            if len(player_hit_list) > 0:
                self.zombie_did_shoot = True
                arcade.play_sound(BULLETS_COLLIDING)

                self.zombie_did_not_missed = True

                zombie_bullet.remove_from_sprite_lists()
                self.bullet.remove_from_sprite_lists()



        self.zombie_bullet_list.update()


        #MEDKIT ------ HITBOX

        for medkitlist in self.medkit_list:

            hit_list = arcade.check_for_collision_with_list(medkitlist, self.bullet_list)

            if len(hit_list) > 0:
                self.body_damage = False
                self.foot_damage = False
                self.head_damage = False


                arcade.play_sound(HEAL)
                self.health = self.health + 20
                self.bullet.remove_from_sprite_lists()
                medkitlist.remove_from_sprite_lists()






        if self.dice_done == True:
            self.turn = "player"


        if self.player_done == True:
            self.turn = "zombie"

        if self.zombie_done == True and self.player_done == True:
            self.turn = "dice"





        if self.turn == "zombie":


            zombie_bullet = arcade.Sprite("ballBlue_07.png", BULLET_SCALING)

            zombie_bullet.center_x = self.zombie_sprite.center_x - 50
            zombie_bullet.center_y = 190 + random.randint(10,100) - random.randint(10,60)
            zombie_bullet.change_x = -random.randint(2,8)

            # Damaged Zone calculation
            if self.health_less_than_last_turn > self.health and self.dodge_chance_bool == False:
                print("less health")


            if self.health_less_than_last_turn > self.health:
                self.zombie_did_not_missed = False
                if zombie_bullet.center_y < 190 and zombie_bullet.center_y >= 161:
                    print("foot")
                    self.sprite_damage_chance = random.randint(1,1)
                    if self.sprite_damage_chance == 1:
                        self.foot_damage = True
                        print("feet damaged")
                elif zombie_bullet.center_y <230 and zombie_bullet.center_y >= 190:
                    print("body")
                    self.sprite_damage_chance = random.randint(1, 1)
                    if self.sprite_damage_chance == 1:
                        self.body_damage = True
                        print("body damaged")
                elif zombie_bullet.center_y <290 and zombie_bullet.center_y >= 230:
                    print("head")
                    self.sprite_damage_chance = random.randint(1, 1)
                    if self.sprite_damage_chance == 1:
                        self.head_damage = True
                        print("head damaged")
            else:
                print("missed")
            self.zombie_bullet_list.append(zombie_bullet)
            self.zombie_done = True
            self.health_less_than_last_turn = self.health
            print(self.health_less_than_last_turn)



def main():
    window = MyGame()
    window.setup()

    arcade.run()

if __name__ == "__main__":
    main()
