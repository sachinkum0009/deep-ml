from typing import List

def calculate_brightness(img: List[List[int]]) -> float:
	# Write your code here
    row_size = len(img)
    if row_size == 0:
        return -1
    col_size = len(img[0])
    if row_size != col_size:
        return -1
    total_sum = 0
    for row in img:
        # check if the value exceeds greater than 255
        if len(row) != row_size:
            return -1
        if any(val > 255 for val in row):
            return -1
        total_sum += sum(row)
    
    return total_sum / (row_size * col_size)


# img = [
#     [100, 200],
#     [50, 150]
# ]
img = [[100, 200], [150]]
print(calculate_brightness(img))