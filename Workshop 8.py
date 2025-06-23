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
    for line in reviews:
        line = line.strip()
        if ',' in line:
            parts = line.split(',', 1)
            rating = int(parts[1].strip())
            ratings.append(rating)

    total_reviews = len(ratings)
    average_rating = sum(ratings) / total_reviews if total_reviews > 0 else 0

with open("summary.txt", "w") as file_07:
    file_07.write(f"Total Reviews: {total_reviews}\n")
    file_07.write(f"Average Rating: {average_rating:.2f}\n")

#6
def capitalize_sentences(text):
    import re #regular expressions
    sentences = re.split('(?<=[.!?]) +', text)
    return ' '.join(sentence.strip().capitalize() for sentence in sentences)


with open("article.txt", "r") as file_08:
    raw_lines = file_08.readlines()
    content = [line.strip() for line in raw_lines]

print("\n Article Loaded!")

while True:
    print("\nMenu:")
    print("1 -> Replace Word")
    print("2 -> Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        input_word = input("Enter a word to search: ")
        replace_word = input("Enter a word to replace it with: ")

        modified_content = []
        for line in content:
            modified_line = line.replace(input_word, replace_word)
            capitalized = capitalize_sentences(modified_line)
            modified_content.append(capitalized + '\n')
    
        with open("formatted_article.txt", "w") as file_09:
            file_09.writelines(modified_content)
            print("Word replaced and saved to formatted_article.txt")
    elif choice == '2':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")

    

    
