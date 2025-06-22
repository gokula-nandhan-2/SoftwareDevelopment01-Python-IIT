# Workshop 8

# 1
with open("input.txt", "r") as file_01:
    file = file_01.read()
    print(len(file))

#2
with open("greetings.txt","w") as file_02:
    file_02.write("Hello\n")
    file_02.write("World")

#3
with open("data.txt","r") as file_03:
    file = file_03.readlines()
    for line in file:
        print(f"Word- {line.strip()}, Letter Count- {len(line.strip())}")

#4
with open("story.txt","r") as file_04:
    lines = file_04.readlines()
    modified_lines = []
    for line in lines:
        modified_line = line.replace("python", "Pythons")
        modified_lines.append(modified_line)

with open("modified_story.txt", "w") as file_05:
    file_05.writelines(modified_lines)

#5
ratings = []
with open("reviews.txt", "r") as file_06:
    reviews = file_06.readlines()
    count = len(reviews)
    for line in file_06:
        line = line.strip()
        if ',' in line:
            parts = line.split(',', 1)


    

with open("summary.txt", "w") as file_07:
    file_07.write(f"Total Reviews: {count}\n")
