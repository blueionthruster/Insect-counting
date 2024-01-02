file_path = 'INPUT DIRECTORY PATH TO YOUR FILE HERE, MAKE SURE TO HAVE YOUR FILE ITSELF IN THE PATH'

with open(file_path, 'r') as file:
    content = file.read()
    print(content)

with open(file_path, 'r') as f:
    beetles = 0
    mosquitoes = 0
    moths = 0
    for line in f:
        first_character = line[0]
        print(first_character)
        if first_character == "0":
            moths += 1
        elif first_character == "1":
            mosquitoes += 1
        elif first_character == "2":
            beetles += 1
        else:
            print("Error encountered, first_character was " + first_character)

print("Number of moths: " + str(moths))
print("Number of mosquitoes: " + str(mosquitoes))
print("Number of beetles: " + str(beetles))
