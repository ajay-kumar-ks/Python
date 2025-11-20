def print_alternate(text, index=0):
    if index >= len(text):
        return
    
    print(text[index], end="")
    print_alternate(text, index + 2)

line = input("Enter a line of text: ")
print("Alternate characters: ", end="")
print_alternate(line)
