import arcade

arcade.open_window(600, 600, "Drawing Examples")

arcade.set_background_color(arcade.csscolor.SKY_BLUE)

arcade.start_render()


arcade.draw_lrbt_rectangle_filled(0, 599, 0, 300, arcade.csscolor.GREEN)



#Cerc
arcade.draw_lrbt_rectangle_filled(80, 90, 300, 390, arcade.csscolor.BROWN)
arcade.draw_circle_filled(85, 380, 50, arcade.csscolor.DARK_GREEN)


#Elipsa
arcade.draw_lrbt_rectangle_filled(195, 205, 300, 390, arcade.csscolor.BROWN)
arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.csscolor.DARK_GREEN)


# Arc
arcade.draw_lrbt_rectangle_filled(290, 300, 300, 390, arcade.csscolor.BROWN)
arcade.draw_arc_filled(295, 330, 60, 160, arcade.csscolor.DARK_GREEN, 0, 180)


#Triunghi
arcade.draw_lrbt_rectangle_filled(410, 420, 300, 380, arcade.csscolor.BROWN)
arcade.draw_triangle_filled(420, 400, 380, 320, 460, 320, arcade.csscolor.DARK_GREEN)


#Poligon
arcade.draw_lrbt_rectangle_filled(495, 505, 300, 380, arcade.csscolor.BROWN)
arcade.draw_polygon_filled(((500, 400),
                            (480, 360),
                            (470, 320),
                            (530, 320),
                            (520, 360)
                            ),
                           arcade.csscolor.DARK_GREEN)


# Draw a sun
arcade.draw_circle_filled(500, 550, 40, arcade.color.YELLOW)

# Rays to the left, right, up, and down
arcade.draw_line(500, 550, 400, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 600, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 450, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 650, arcade.color.YELLOW, 3)

# Diagonal rays
arcade.draw_line(500, 550, 550, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 550, 500, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 500, arcade.color.YELLOW, 3)


arcade.draw_line(100, 200, 120, 300, arcade.color.YELLOW, 3)

arcade.draw_text("Desenam copacei!!", 200, 200, arcade.color.YELLOW, 24)

arcade.finish_render()



arcade.run()