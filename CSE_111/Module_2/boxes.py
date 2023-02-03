import math # import math to be able to use the math.ceil

total_items = int(input('\nEnter the number of items: ')) # input to get the total number of items that need to be packed
items_per_box = int(input('Enter the number of items per box: ')) # input to get the number of items per box
boxes = math.ceil(total_items / items_per_box) # calculation to determine how many total boxes

print(f'\nFor {total_items} items, packing {items_per_box} items in each box, you will need {boxes} boxes.') # print out information
print() # printing line for white space