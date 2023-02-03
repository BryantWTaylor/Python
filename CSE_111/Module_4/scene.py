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

    # functional use for determining where to put my objects on the canvas will comment out before submission
    # draw_grid(canvas, scene_width, scene_height, 50)
    
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.

# functional use to see where to put objects on my canvas will comment out before submission
# def draw_grid(canvas, width, height, interval, color="blue"):
#     # Draw a vertical line at every x interval.
#     label_y = 15
#     for x in range(interval, width, interval):
#         draw_line(canvas, x, 0, x, height, fill=color)
#         draw_text(canvas, x, label_y, f"{x}", fill=color)

#     # Draw a horizontal line at every y interval.
#     label_x = 15
#     for y in range(interval, height, interval):
#         draw_line(canvas, 0, y, width, y, fill=color)
#         draw_text(canvas, label_x, y, f"{y}", fill=color)

# function to draw the sky
def draw_sky(canvas, scene_width, scene_height):
    '''Draw the sky of the picture
    parameters-
        canvas: indicates that this will draw to a canvas
        scene_width, scene_height: these give us the overall
            dimensions of the canvas we will be drawing to'''
    draw_rectangle(canvas, 0, scene_height / 3,  scene_width, scene_height, width=0, fill='steelBlue1')
    draw_cloud(canvas, 600, 350, 75)
    draw_cloud(canvas, 475, 375, 65)
    draw_cloud(canvas, 700, 425, 50)
    draw_cloud(canvas, 100, 400, 60)

# repeatable function for drawing clouds
def draw_cloud(canvas, center_x, bottom, height):
    '''Draw a single cloud.
    paramaters-
        canvas:indicates that this will draw to a canvas
        center_x, bottom: gives us the x and y coordinates
            needed to start the cloud in the correct location
        height: tells us how tall we want the cloud to be'''
    # my cloud is three ovals stacked on top so I have three draw_oval functions
    # floof was the term that I used as it just felt right when describing a cloud
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
    '''Draw the ground of the picture
    parameters-
        canvas: indicates that this will draw to a canvas
        scene_width, scene_height: these give us the overall
            dimensions of the canvas we will be drawing to'''
    draw_rectangle(canvas, 0, 0, scene_width, scene_height / 3, width=0, fill='lawnGreen')
    draw_mountain(canvas, 125, (scene_height / 3), 250)
    draw_mountain(canvas, 325, (scene_height / 3), 270)
    draw_mountain(canvas, 250, (scene_height / 3), 300)
    draw_mountain(canvas, 450, (scene_height / 3), 175)
    draw_mountain(canvas, 800, (scene_height / 3), 80)
    draw_tree(canvas, 35, 90, 65)
    draw_tree(canvas, 45, 160, 45)
    draw_tree(canvas, 75, 150, 50)
    draw_tree(canvas, 100, 50, 100)
    draw_tree(canvas, 115, 165, 30)
    draw_tree(canvas, 125, 160, 45)
    draw_tree(canvas, 140, 130, 60)
    draw_tree(canvas, 165, 80, 70)
    draw_tree(canvas, 170, 160, 45)
    draw_tree(canvas, 198, 160, 45)
    draw_tree(canvas, 207, 130, 60)
    draw_tree(canvas, 221, 160, 45)
    draw_tree(canvas, 230, 76, 80)
    draw_tree(canvas, 233, 165, 30)
    draw_tree(canvas, 248, 160, 45)
    draw_tree(canvas, 255, 150, 50)
    draw_tree(canvas, 269, 130, 60)
    draw_tree(canvas, 280, 160, 45)
    draw_tree(canvas, 300, 150, 50)
    draw_tree(canvas, 308, 160, 45)
    draw_tree(canvas, 323, 165, 30)
    draw_tree(canvas, 330, 75, 85)
    draw_tree(canvas, 348, 160, 45)
    draw_tree(canvas, 367, 160, 45)
    draw_tree(canvas, 373, 150, 50)
    draw_tree(canvas, 400, 130, 60)


# repeatable function for drawing mountains
def draw_mountain(canvas, center_x, bottom, height): 
    '''Draw a single mountain.
    paramaters-
        canvas:indicates that this will draw to a canvas
        center_x, bottom: gives us the x and y coordinates
            needed to start the mountain in the correct location
        height: tells us how tall we want the mountain to be'''
    # my function is a fairly simple triangle and only requires a single call to draw_polygon.
    width = height * 1.5
    mountain_left = center_x - (width / 2)
    mountain_top = bottom + height
    mountain_right = center_x + (width / 2)
    draw_polygon(canvas, mountain_left, bottom, center_x, mountain_top, mountain_right, bottom, width=0, fill='saddleBrown')


# repeatabe function for drawing pine trees
def draw_tree(canvas, center_x, bottom, height):
    '''Draw a single pine tree.
    parameters-
        canvas: indicates that this will draw to a canvas
        center_x, bottom: give us the x and y coordinates needed
            start the tree in the correct location
        height: tells us how tall we want the tree to be'''
    # my tree is three triangles stacked on top so I have three draw_polygon functions for the top section of the tree.
    tree_width = height / 2
    side_left = center_x - (tree_width / 2)
    tree_top = bottom + height
    side_right = center_x + (tree_width / 2)
    top_sec_low_y = tree_top - (height * .35)
    mid_sec_high_y = tree_top - (height * .25)
    mid_sec_low_y = mid_sec_high_y - (height * .35)
    low_sec_high_y = mid_sec_high_y - (height * .25)
    low_sec_low_y = low_sec_high_y - (height * .35)
    draw_polygon(canvas, side_left, low_sec_low_y, center_x, low_sec_high_y, side_right, low_sec_low_y, outline='forestGreen', width=0, fill='forestGreen')
    draw_polygon(canvas, side_left, mid_sec_low_y, center_x, mid_sec_high_y, side_right, mid_sec_low_y, outline='forestGreen', width=0, fill='forestGreen')
    draw_polygon(canvas, side_left, top_sec_low_y, center_x, tree_top, side_right, top_sec_low_y, outline='forestGreen', width=0, fill='forestGreen')
    # this is the part of the function where the trunk is drawn with a draw_rectangle function
    trunk_width = height * .10
    trunk_height = height * .15
    trunk_left = center_x - (trunk_width / 2)
    trunk_right = center_x + (trunk_width / 2)
    trunk_top = bottom + trunk_height
    draw_rectangle(canvas, trunk_left, bottom, trunk_right, trunk_top, outline='tan4', width=0, fill='tan4')

# Call the main function so that
# this program will start executing.
main()