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

