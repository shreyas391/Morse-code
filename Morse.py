from Data import code

keep_running = True
while keep_running:
    ende = input("Do you want to encode or decode: ").lower()
    text = ""

    def encode():
        global text
        get_data = input("Enter the text that you want to encode into morse. \n").lower()
        for i in get_data:
            if i == " ":
                text += "| "
            else:
                text += code[i]
                text += " "
        print(f"Your encoded morse is here: {text}")

    def decode():
        global text
        get_data = input("Enter the morse code that you want to decode. \n")
        words = get_data.split("|")
        for items in words:
            one_word = items.split()
            for each_code in one_word:
                for key, value in code.items():
                    if each_code == value:
                        text += key
            text += " "
        print(f"Your decoded text is here: {text}")

    if ende == "encode":
        encode()
    elif ende == "decode":
        decode()
    elif ende == "end":
        keep_running = False