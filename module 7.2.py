def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    string_positions = {}
    pos_str = 1 #начальная позиция в строке
    pos_byte = 0 #начальная кол. байтов
    item = []
    for item in strings:
        file.write(item + '\n')
        string_positions[(pos_str,pos_byte)] = item
        pos_str += 1
        pos_byte = file.tell()
    file.close()
    return string_positions



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]



result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)