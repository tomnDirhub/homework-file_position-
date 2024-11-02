def custom_write(file_name, string):
    file = open(file_name, "a", encoding="utf-8")
    dictionary = {}
    i = 0
    for st in string:
        dictionary[(i, file.tell())] = st
        file.write(f"{st}\n")
        i += 1
    file.close()
    return dictionary

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)