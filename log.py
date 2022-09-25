def print_result(name1, telephone1):
    with open ('result.txt', 'a+', encoding='UTF-8') as file:
        file.write(f'ФИО Абонента:{name1}, Номер телефона:{telephone1}\n')

def search_result(info):
    path = 'result.txt'
    data = open(path, 'r')
    for line in data:
        if line.partition(info):
            print(line)

   
