def snake_camel(word):
        import re
        return ''.join(x.capitalize() or '_' for x in word.split('_'))

print(snake_camel('python_exercises'))
