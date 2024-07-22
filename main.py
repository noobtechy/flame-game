def get_name_input():
    name1 = input("Enter the first name: ").lower().replace(" ", "")
    name2 = input("Enter the second name: ").lower().replace(" ", "")
    return name1, name2

def remove_common_letters(name1, name2):
    list1 = list(name1)
    list2 = list(name2)
    
    for letter in name1:
        if letter in list2:
            list1.remove(letter)
            list2.remove(letter)
    
    return len(list1) + len(list2)

def get_flames_result(count):
    flames = ["Friends", "Lovers", "Affection", "Marriage", "Enemies", "Siblings"]
    
    while len(flames) > 1:
        split_index = (count % len(flames)) - 1
        if split_index >= 0:
            right = flames[split_index + 1:]
            left = flames[:split_index]
            flames = right + left
        else:
            flames = flames[:len(flames) - 1]
    
    return flames[0]

def main():
    print("Welcome to the FLAMES Game!")
    
    name1, name2 = get_name_input()
    
    remaining_count = remove_common_letters(name1, name2)
    
    result = get_flames_result(remaining_count)
    
    print(f"The relationship between {name1.capitalize()} and {name2.capitalize()} is: {result}")

if __name__ == "__main__":
    main()