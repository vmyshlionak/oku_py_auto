import os



base_path = os.path.dirname(__file__)
print(base_path)
file_path1 = os.path.join(base_path, 'data.txt')
file_path2 = os.path.join(base_path, 'data2.txt')
print(file_path1)

# def read_file():
#  with open(file_path1) as data_file: #with - менеджер контекста, гарантирующий, что файл будет закрыт
#     for line in data_file.readlines():
#         yield line
#
# for data_line in read_file():
#     with open(file_path2, 'a') as data_file: #режим 'a' добавляет новые записи в конец файла, 'w' - перезаписывает
#         data_line = data_line.replace('.', '').replace(',', '')
#         data_file.write(data_line)

homework_path = os.path.dirname(base_path) #дает путь к папке, в которой лежит кончик base_path, то есть уровень выше. Можно сделать еще выше: os.path.dirname(os.path.dirname(base_path))
vika_file_path = os.path.join(homework_path, 'test_file')
print(vika_file_path)

with open(vika_file_path) as f:
    print(f.read())


