import arcade

# Dimensiunea ferestrei
arcade.open_window(600, 600, "A tall building")

# background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)



#Starting rendering
arcade.start_render()

#Drawing grass
arcade.draw_lrbt_rectangle_filled(0, 599, 0, 120, arcade.csscolor.GREEN)

#Drawing some mountains
arcade.draw_triangle_filled(110, 300, -100, 120, 330, 120, arcade.color.GRAY)
arcade.draw_triangle_filled(500, 400, 300, 120, 700, 120, arcade.color.GRAY)

#Drawing mountain peaks
arcade.draw_triangle_filled(110, 300, 100, 290, 120, 290, arcade.color.WHITE)

#Drawing the first piece of the sky scrapper
arcade.draw_lrbt_rectangle_filled(220, 360, 120, 400, arcade.csscolor.DIM_GRAY)
arcade.draw_lrbt_rectangle_filled(250, 330, 400, 490, arcade.csscolor.DIM_GRAY)
arcade.draw_lrbt_rectangle_filled(270, 310, 490, 550, arcade.csscolor.DIM_GRAY)
arcade.draw_lrbt_rectangle_filled(290, 295, 550, 570, arcade.csscolor.DIM_GRAY)

#Drawing a circle on top of the building
arcade.draw_circle_filled(293, 580, 10, arcade.color.RED)
arcade.draw_circle_outline(293, 580, 10, arcade.color.BLACK)

#Drawing the outlines
arcade.draw_lrbt_rectangle_outline(221, 361, 121, 400, arcade.color.BLACK)
arcade.draw_lrbt_rectangle_outline(251, 331, 400, 490, arcade.color.BLACK)
arcade.draw_lrbt_rectangle_outline(270, 311, 490, 550, arcade.color.BLACK)
arcade.draw_lrbt_rectangle_outline(291, 296, 550, 570, arcade.color.BLACK)






arcade.finish_render()









arcade.run()