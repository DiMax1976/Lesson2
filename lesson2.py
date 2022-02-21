from random import uniform
# Task 1.
print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 2))
print(type(15 ** 2))
#
my_list=list()
my_list=['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print("Данные на входе:")
print(my_list)
print("Добавляем кавычки:")
def convert_list_in_str (dataset: list) ->list:
# добавлем кавычки через одну

    my_list2=list()
    for num_s in range(len(dataset)):
        try:
            simbol=int(dataset[num_s])//10

            if simbol==0:
                if len(dataset[num_s])==2:
                    my_list2.append(chr(34))
                    my_list2.append("+"+"0"+str(int(dataset[num_s])))
                    my_list2.append(chr(34))
                else:
                    my_list2.append(chr(34))
                    my_list2.append("0" + str(int(dataset[num_s])))
                    my_list2.append(chr(34))
            else:
                my_list2.append(chr(34))
                my_list2.append(dataset[num_s])
                my_list2.append(chr(34))
        except ValueError:

            my_list2.append(dataset[num_s])

    return my_list2
def New_String (dataset1: list)-> str:
    Single_s=""
    for num_s in range(len(dataset1)):

        if dataset1[num_s]==chr(34):
            if num_s==1 :
                Single_s =  Single_s+dataset1[num_s]
            elif num_s==3:
                Single_s = Single_s + dataset1[num_s]+ chr(32)
            elif num_s == 5:
                Single_s = Single_s + dataset1[num_s]
            elif num_s == 7:
                Single_s = Single_s + dataset1[num_s] + chr(32)
            elif num_s == 12:
                Single_s = Single_s + dataset1[num_s]
            elif num_s == 14:
                Single_s = Single_s + dataset1[num_s] + chr(32)
        else:
                Single_s = Single_s +dataset1[num_s]+  chr(32)
    Single_s=Single_s.replace(' " ', '" ', )
    return Single_s

print(convert_list_in_str(my_list))
my_list3=convert_list_in_str(my_list)
print("Выводим в строку полученный список:")
print(New_String(my_list3))


def convert_name_extract(list_in: list) -> list:
    """Извлекает имена из элементов и формирует список приветствий."""
    list_out = []
    for i in range(len(list_in)):
        get_first_person = list_in.pop()  # забираем последний индекс из списка list_in
        # print(get_first_person, type(get_first_person))
        first_item_split = get_first_person.split()  # делаем сплит get_first_person, получаем новый список first_item_split
        # print(get_item_2, type(get_item_2))
        get_position = ' '.join(first_item_split[0:-1:1]).lower()  # получаем должность с помощью среза, приводим к нижнему регистру
        # print(get_position, type(get_position))
        get_name = first_item_split.pop().lower().capitalize()  # забираем имя и приводим его к нижнему регистру и "поднимаем" первую букву
        # print(get_name, type(get_name))
        new_person = ' '.join([get_position, get_name])  # в новый список заносим дожность и имя сотрудника
        # print(new_item, type(new_item))
        list_out.insert(0, new_person)  # добавляем итем в список list_out
    #list_out = ["здесь должены оказаться результирующие строковые приветствия"]
    return list_out

my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
print(f'Входящий список: {my_list}')
result = convert_name_extract(my_list)
print(f'Обработанный список: {result}')

def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
        формирует из них единую строковую переменную разделяя значения запятой."""
    inner_list_begin = list_in.copy() # Если копию не делать, то затрётся изначальный список и не будут работать последующие функции
    inner_list = []
    for i in range(len(inner_list_begin)):
        get_item = str(inner_list_begin.pop()).split('.', -1) # забираем последний элемент списка и делаем его списком  с двумя элементами через метод .split
        # print(get_item, type(get_item))
        get_ruble = get_item[0] # Получаем первый элемент (рубли)
        get_kopek = get_item[-1] # Получаем второй элемент (копейки)
        # print(get_ruble, type(get_ruble), get_kopek, type(get_kopek))
        price = f'{get_ruble} руб {get_kopek} коп' # собираем нужную строку
        # print(price, type(price))
        inner_list.append(price) # добавялем строку price в список
    inner_list.reverse()# реверс списка
    format_inner_list = ', '.join(inner_list) # склеиваем список inner_list
    str_out = f'Преобразованная строка: {format_inner_list}' #"здесь итоговая строка"
    return str_out

my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список вещественных чисел (float): {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)

def sort_prices(list_in: list) -> list:
    """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
    list_in.sort()  # сортируем список по возврастанию (дефолт для sort())
    return list_in  # ["отсортированный результирующий список"]

print(f'\n{id(my_list)} -> Адрес начального списка') # зафиксируйте здесь информацию по исходному списку my_list
result_2 = sort_prices(my_list)
print(f'{id(result_2)} -> Адрес того же списка, но отсортированного по возрастанию') # зафиксируйте здесь доказательство, что результат result_2 остался тем же объектом
print(f'Список, сортированный по возрастанию: {result_2}\n')

def sort_price_adv(list_in: list) -> list:
    """Создаёт новый список и возвращает список с элементами по убыванию"""
    list_out = sorted(list_in, reverse=True) # ["список элементов в списке по убыванию"]
    return list_out

print(f'\n{id(my_list)} -> Адрес начального списка')
result_3 = sort_price_adv(my_list)
print(f'{id(result_3)} -> Адрес списка, отсортированного по убыванию. Ух ты, адрес то поменялся.')
print(result_3)

def check_five_max_elements(list_in: list) -> list:
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""
    list_in.sort(reverse=True) # сортируем список в обратном порядке
    list_out = list_in[0:5]  # получаем первые ПЯТЬ элементов, т.е. первые 5 самых больших значений["список из пяти самых больших элементов"]
    return list_out
result_4 = check_five_max_elements(my_list)
print(f'\nА вот и самые большие числа (целых ПЯТЬ штук) в нашем списке: {result_4}')