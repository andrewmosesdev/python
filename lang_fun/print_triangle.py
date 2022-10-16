triangle_char = input('Enter a character:\n')
triangle_height = int(input('Enter triangle height:\n'))
print('')

def print_triangle(height):
    if height == 0:
        return
    else:
        print_triangle(height - 1)
        print(f'{triangle_char} '*height)
    


print_triangle(triangle_height)
