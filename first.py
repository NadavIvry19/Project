def generate_table():
    print("|   x   |   0   |   1   |   2   |   3   |   4   |   5   |   6   |   7   |   8   |   9   |   10  |")
    print("|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|")
    
    for i in range(0, 11):
        row_values = [i * j for j in range(0, 11)]
        row_str = f"|   {i}   |" + "   |".join(f"  {value}"[-4:] for value in row_values) + "   |"
        print(row_str)

if __name__ == "__main__":
    generate_table()
