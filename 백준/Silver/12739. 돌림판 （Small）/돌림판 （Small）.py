def get_next_color(left, current, right):
    if (left == current == right) or (left != current and current != right and left != right):
        return 'B'
    
    colors = [left, current, right]
    color_count = {}
    for color in colors:
        color_count[color] = color_count.get(color, 0) + 1
    
    majority_color = None
    minority_color = None
    for color, count in color_count.items():
        if count == 2:
            majority_color = color
        elif count == 1:
            minority_color = color
    
    if ((majority_color == 'R' and minority_color == 'G') or 
        (majority_color == 'G' and minority_color == 'B') or 
        (majority_color == 'B' and minority_color == 'R')):
        return 'R'
    return 'G'

def transform_colors(colors, K):
    N = len(colors)
    current_colors = list(colors)
    
    for _ in range(K):
        new_colors = [''] * N
        for i in range(N):
            left = current_colors[(i - 1) % N]
            right = current_colors[(i + 1) % N]
            new_colors[i] = get_next_color(left, current_colors[i], right)
        current_colors = new_colors
    
    return current_colors

N, K = map(int, input().split())
initial_colors = input().strip()

final_colors = transform_colors(initial_colors, K)

red_count = final_colors.count('R')
green_count = final_colors.count('G')
blue_count = final_colors.count('B')

print(red_count, green_count, blue_count)