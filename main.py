# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("Input/Names/invited_names.txt", "r") as names:
    name_list = names.readlines()

for num in range(8):
    with open("Input/Letters/starting_letter.txt", "r") as letter:
        contents = letter.read()
    name = name_list[num].strip()
    contents = contents.replace("[name]", name)
    with open(f"Output/ReadyToSend/Letter_For_{name}", "w")as new_letter:
        new_letter.write(contents)
