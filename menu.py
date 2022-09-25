from log import print_result
from log import search_result

var = input('Добро пожаловать! Это Телефонный справочник с возможностью импорта и экспорта данных \n Вы хотите добавить данные в систему -1 \n Вы хотите загрузить данные из системы -2 ')
if var =='1': #Добавление в справочник
    name1=input('Введите ФИО абонента: ')
    telephone1= input("Введите телефон абонента: ")
    print_result(name1, telephone1)
if var =='2': #Загрузка из системы
    name2=input('Введите ФИО абонента: ')
    telephone2= input("Введите телефон абонента: ")
    search_result(name2) 
    search_result(telephone2) 
    if name2=="":
        telephone2= input("Введите телефон абонента: ")
        search_result(telephone2)
    if telephone=="":
        search_result(name2)
