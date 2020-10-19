ru_translate_char = {
 'а': 'a',
 'б': 'b',
 'в': 'v',
 'г': 'g',
 'д': 'd',
 'ж': 'zh',
 'з': 'z',
 'и': 'i',
 'й': 'y',
 'к': 'k',
 'л': 'l',
 'м': 'm',
 'н': 'n',
 'о': 'o',
 'п': 'p',
 'р': 'r',
 'с': 's',
 'т': 't',
 'у': 'u',
 'ф': 'f',
 'х': 'x',
 'ц': 'c',
 'ч': 'ch',
 'ш': 'sh',
 'щ': 'shch',
 'ъ': '"',
 'ы': 'y',
 'ь': '\'',
 'э': 'e',
 'ю': 'yu',
 'я': 'ya',
}

def generateTranslate(input):
  for key in ru_translate_char:
    input = input.lower().replace(key, ru_translate_char[key])
  
  print(input)

generateTranslate(input("Введите исходный текст на русском: "))