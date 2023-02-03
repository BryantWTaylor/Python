# Work as a team to write a Python program named can_sizes.py that computes and prints the storage efficiency for each of the following 12 steel can sizes. Then visually examine the output and answer this question, “Which can size has the highest storage efficiency?”

# Name	Radius
# (centimeters)	Height
# (centimeters)	Cost per Can
# (U.S. dollars)
# #1 Picnic	6.83	10.16	$0.28
# #1 Tall	7.78	11.91	$0.43
# #2	8.73	11.59	$0.45
# #2.5	10.32	11.91	$0.61
# #3 Cylinder	10.79	17.78	$0.86
# #5	13.02	14.29	$0.83
# #6Z	5.40	8.89	$0.22
# #8Z short	6.83	7.62	$0.26
# #10	15.72	17.78	$1.53
# #211	6.83	12.38	$0.34
# #300	7.62	11.27	$0.38
# #303	8.10	11.11	$0.42

# If you separate your program into functions, this problem will be much easier to solve than if you don’t separate it into functions. You are free to write any functions that you choose in your program, but we strongly suggest that your program include at least these three functions:

# main
# compute_volume
# compute_surface_area

# Core Requirements
# Your program must compute the volume of all 12 can sizes.
# Your program must compute the surface area of all 12 can sizes.
# Your program must compute and print the storage efficiency of all 12 can sizes.

import math

name_list = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z", "#8Z short", "#10", "#211", "#300", "#303"]
radius_list = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.4, 6.83, 15.72, 6.83, 7.62, 8.1]
height_list = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
price_list = [0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42]

def main():
    for i, name in enumerate(name_list):
        volume = compute_volume(radius_list[i], height_list[i])
        surface_area = compute_surface_area(radius_list[i], height_list[i])
        storage_efficieny = compute_storage_efficiency(volume, surface_area)
        print(f"{name} {storage_efficieny:.2f}")
    return

def compute_volume(radius, height):
    volume = math.pi * (radius ** 2) * height
    return volume

def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def compute_storage_efficiency(volume, surface_area):
    storage_efficiency = volume / surface_area
    return storage_efficiency

main() 