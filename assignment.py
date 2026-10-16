range_below = 0
range_in = 0
range_above =0
def classify(test_width):
    if test_width<98:
        return "Below range"
    elif test_width>=98 and test_width<=102:
        return "In range"
    else:
        return "Above range"
def calculate_average(total, count):
    return total/count
total_width = 0
tiles = int(input("Enter the number of tiles: "))
    
for i in range(tiles):
    tile_width = int(input("Enter the tile width: ")) 
    total_width += tile_width
    print(classify(tile_width))
    if classify(tile_width) == "Below range":
        range_below+=1
    elif classify(tile_width) == "In range":
        range_in+=1
    else:
        range_above+=1
print(f"Total width: {total_width} mm")
print(f"Average width: {calculate_average(total_width, tiles)} mm")
print(f"Below range: {range_below}")
print(f"In range: {range_in}")
print(f"Above range: {range_above}")