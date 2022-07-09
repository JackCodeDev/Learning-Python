#TODO: Create a letter using starting_letter.docx
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
PLACE_HOLDER = "[name]"
with open("./input/Names/invited_names.txt") as names:
    list_names = names.readlines()
    print(list_names)
    for name in list_names:
        with open("./input/Letters/starting_letter.txt") as letter:
            new_name = name.strip()
            old_letter = letter.read()
            new_letter = old_letter.replace(PLACE_HOLDER, new_name)
            with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", mode="w") as completed_letter:
                completed_letter.write(new_letter)


