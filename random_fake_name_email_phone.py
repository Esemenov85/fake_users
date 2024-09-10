from random import choice
from faker import Faker
from transliterate import translit


fake = Faker("ru_RU")


def faker_person_create():
    name = fake.name()
    name_male = fake.name_male() #Генерация мужского ФИО
    name_female = fake.name_female() #Генерация женского ФИО
    lastname_male = fake.last_name_male() #Генерация фейковой мужской фамилии
    lastname_female = fake.last_name_female() #Генерация фейковой женской фамилии
    firstname_male = fake.first_name_male() #Генерация фейкового мужского имени
    firstname_female = fake.first_name_female() #Генерация фейкового женского имени
    middlename_male = fake.middle_name_male() #Генерация фейкового мужского отчества
    middlename_female = fake.middle_name_female() #Генерация фейкового женского отчества
    dict_mail = ['@mail.ru', '@yandex.ru', '@rambler.ru', '@gmail.com', '@bk.ru']
    # email = translit(str(name).split()[0].lower(), language_code='ru', reversed=True) + choice(dict_mail)
    email_male = translit(str(lastname_male).lower(), language_code='ru', reversed=True) + choice(dict_mail)
    phone = fake.phone_number()
    # dict_person = {'name': name, 'email': email, 'phone': phone}
    # print(f"{dict_person['name'],dict_person['email'],dict_person['phone']}")
    # customers = (f"{dict_person['name'],dict_person['email'],dict_person['phone']}")
    # name_customer = customers.split()[0].replace("('", "") + ";" + \
    #                 customers.split()[1].replace("'", "") + ";" + \
    #                 customers.split()[2].replace("'", "").replace(",","") + ";" + \
    #                 customers.split()[3].replace("'", "").replace(",","") + ";" + \
    #                 phone.replace("'", "")
    # print(name_customer)
    users_male = (f"{lastname_male},{firstname_male},{middlename_male},{email_male},{phone}").replace(",",";")
    print(users_male)
    # with open('C:/Users/Evgeniy_S/Documents/person_faker_fkgs.txt', 'a', encoding='utf-8') as file:
    #         file.write(f'{name_customer}\n')
    return users_male

            
def main():
    person_count = int(input('Введите количество личностей для генерации >>> '))
    for i in range(person_count):
        faker_person_create()


if __name__ == "__main__":
    main()