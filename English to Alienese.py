def translate_to_alienese():
  input_string = input("Enter the word to translate: ")
  char_mapping = {
    'A': '@',
    'B': '8',
    'C': '(',
    'D': '|)',
    'E': '3',
    'F': '#',
    'G': '6',
    'H': '[-]',
    'I': '|',
    'J': '_|',
    'K': '|<',
    'L': '1',
    'M': '[]\/[]',
    'N': '[]\[]',
    'O': '0',
    'P': '|D',
    'Q': '(,)',
    'R': '|Z',
    'S': '$',
    'T': "']['",
    'U': '|_|',
    'V': '\/',
    'W': '\/\/',
    'X': '}{',
    'Y': '`/',
    'Z': '2'
  }

  translated_string = ""
  for char in input_string:
    if char == " ":
      translated_string += " "
    else:
      translated_char = char_mapping.get(char.upper(), char)
      translated_string += translated_char
  return translated_string

translated_message = translate_to_alienese()
print(translated_message)
