# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    # draw_grid(canvas, scene_width, scene_height, 50)
    
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_grid(canvas, width, height, interval, color="blue"):
    # Draw a vertical line at every x interval.
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill=color)
        draw_text(canvas, x, label_y, f"{x}", fill=color)

    # Draw a horizontal line at every y interval.
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text(canvas, label_x, y, f"{y}", fill=color)

# function to draw the sky
def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 3,  scene_width, scene_height, width=0, fill='steelBlue1')
    draw_clouds(canvas, 600, 350, 75)
    draw_clouds(canvas, 475, 375, 65)
    draw_clouds(canvas, 700, 425, 50)

# repeatable function for drawing clouds
def draw_clouds(canvas, center_x, bottom, height):
    floof_width = (4 / 3) * height
    floof_height = (2 / 3) * height
    left_floof_first_x = center_x - height
    left_floof_first_y = bottom
    left_floof_second_x = left_floof_first_x + floof_width
    left_floof_second_y = left_floof_first_y + floof_height
    center_floof_first_x = center_x - (floof_width / 2)
    center_floof_first_y = bottom + (height - floof_height)
    center_floof_second_x = center_floof_first_x + floof_width
    center_floof_second_y = center_floof_first_y + floof_height
    right_floof_first_x = left_floof_second_x - (floof_width / 2)
    right_floof_first_y = bottom + (floof_height * .20)
    right_floof_second_x = right_floof_first_x + floof_width
    right_floof_second_y = right_floof_first_y + floof_height
    draw_oval(canvas, left_floof_first_x, left_floof_first_y, left_floof_second_x, left_floof_second_y, width=0, fill='white')
    draw_oval(canvas, center_floof_first_x, center_floof_first_y, center_floof_second_x, center_floof_second_y, width=0, fill='white')
    draw_oval(canvas, right_floof_first_x, right_floof_first_y, right_floof_second_x, right_floof_second_y, width=0, fill='white')

# function to drawn my ground. Including the call of the function for my mountains as I viewed them as an extension of the ground
def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0, scene_width, scene_height / 3, width=0, fill='lawnGreen')
    draw_mountains(canvas, 250, (scene_height / 3), 300)
    draw_mountains(canvas, 450, (scene_height / 3), 175)

# repeatable function for drawing mountains
def draw_mountains(canvas, center_x, bottom, height): 
    width = height * 1.5
    mountain_left = center_x - (width / 2)
    mountain_top = bottom + height
    mountain_right = center_x + (width / 2)
    draw_polygon(canvas, mountain_left, bottom, center_x, mountain_top, mountain_right, bottom, width=0, fill='saddleBrown')



# Call the main function so that
# this program will start executing.
main()