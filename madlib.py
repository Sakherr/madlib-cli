import re

print('''
In this exciting word game, you will be presented with a story template with some missing words such as nouns, verbs, adjectives, and more. Your task is to provide the missing words to complete the story.

To start playing, follow these simple steps:

Enter the path of the Madlib template file and press Enter.
You will be prompted to enter the specific types of words required to complete the story. Enter the words one by one and press Enter after each one.
After you have entered all the missing words, your completed Madlib story will be generated and displayed on the screen.

''')
def read_template(path):
    try:
        with open(path, 'r') as file:
            content = file.read().strip()
            return content
    except FileNotFoundError:
        print(" The file not found")
        raise

    

def parse_template(Str):
 
    strippe = re.sub(r"{[^}]*}", "{}", Str)
    parts = tuple(re.findall(r"{([^}]*)}", Str))
    return strippe , parts



def merge(temp, parts):
    return temp.format(*parts)



template_path = input("Enter the path of the Madlib template file please: ")

template_content = read_template(template_path)

template_text, template_parts = parse_template(template_content)


user_inputs = []
for part in template_parts:
    user_input = input(f" enter the {part}: ")
    user_inputs.append(user_input)

completed_text = merge(template_text, user_inputs)


print(completed_text)

output_path = "completed_madlib.txt"
with open(output_path, 'w') as file:
    file.write(completed_text)

print(f"Your madlib output in {output_path}! ")