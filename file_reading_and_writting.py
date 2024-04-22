with open("names.txt") as file:
    data = file.readlines()
    print(data)

placeholder = "[name]"

with open("data.txt") as writte:
    read = writte.read()
    for name in data:
        name = name.strip() # Remove newline characters
        done = read.replace(placeholder, name)
        print(done)
        with open(f"{name}.txt", mode="w") as fille:
            fille.write("done")