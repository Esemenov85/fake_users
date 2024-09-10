from random import choice
from faker import Faker
from transliterate import translit


fake = Faker("ru_RU")

name_male = []
name_female = []
lastname_male = []
lastname_female = []
firstname_male = []
firstname_female = []
middlename_male = []
middlename_female = []
email = []
phone = []

name_male = fake.name_male() #Генерация мужского ФИО
name_female = fake.name_female() #Генерация женского ФИО

lastname_male = fake.last_name_male() #Генерация фейковой мужской фамилии
lastname_female = fake.last_name_female() #Генерация фейковой женской фамилии
firstname_male = fake.first_name_male() #Генерация фейкового мужского имени
firstname_female = fake.first_name_female() #Генерация фейкового женского имени
# middlename_male = 
# middlename_female = 
phone = fake.phone_number() #Генерация фейкового номера телефона
email = fake.ascii_free_email() #Генерация фейкового емейла



def faker_person_create():
    name_f = fake.name()
    phone_f = fake.phone_number()
    dict_mail = ['@mail.ru', '@yandex.ru', '@rambler.ru', '@gmail.com', '@bk.ru']
    email_f = translit(str(name_f).split()[0].lower(), language_code='ru', reversed=True) + choice(dict_mail)
    dict_person = {'Ф.И.О.': name_f, 'Телефон': phone_f, 'E-mail': email_f}
    return dict_person


# def print_person_data(dict_person, i):
#     for item in dict_person:
#         print(f'{item}: {dict_person[item]}')
#         with open('C:/Users/Evgeniy_S/Documents/person_faker.txt', 'a', encoding='utf-8') as file:
#             file.write(f'{item}: {dict_person[item]}\n')
            
def print_person_data(dict_person, i):
    for item in dict_person:
        print(f'{dict_person[item]}')
        with open('C:/Users/Evgeniy_S/Documents/person_faker_name.txt', 'a', encoding='utf-8') as file:
            file.write(f'{dict_person[item]}\n')


def main():
    person_count = int(input('Введите количество личностей для генерации >>> '))
    for i in range(person_count):
        dict_person = faker_person_create()
        print_person_data(dict_person, i)


if __name__ == "__main__":
    main()

