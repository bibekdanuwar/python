rows = 5
for i in range(1, rows + 1):
    # Uses full-width spaces to perfectly match the emoji width
    spaces = "　" * (rows - i)
    stars = "⭐" * (2 * i - 1)
    
    print(spaces + stars) 