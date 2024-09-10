from random import choice
from faker import Faker
from transliterate import translit


fake = Faker("ru_RU")


def faker_male_create():
    lastname_male = fake.last_name_male() #Генерация фейковой мужской фамилии
    firstname_male = fake.first_name_male() #Генерация фейкового мужского имени
    middlename_male = fake.middle_name_male() #Генерация фейкового мужского отчества
    dict_mail = ['@mail.ru', '@yandex.ru', '@rambler.ru', '@gmail.com', '@bk.ru']
    email_male = translit(str(lastname_male).lower(), language_code='ru', reversed=True) + choice(dict_mail)
    phone = fake.phone_number()
    users_male = (f"{lastname_male},{firstname_male},{middlename_male},{email_male},{phone}").replace(",",";")
    print(users_male)
    # with open('C:/Users/Evgeniy_S/Documents/person_faker_fkgs.csv', 'a', encoding='utf-8') as file:
    #         file.write(f'{users_male}\n')
    return users_male

def faker_female_create():
    lastname_female = fake.last_name_female() #Генерация фейковой женской фамилии
    firstname_female = fake.first_name_female() #Генерация фейкового женского имени
    middlename_female = fake.middle_name_female() #Генерация фейкового женского отчества
    dict_mail = ['@mail.ru', '@yandex.ru', '@rambler.ru', '@gmail.com', '@bk.ru']
    email_female = translit(str(lastname_female).lower(), language_code='ru', reversed=True) + choice(dict_mail)
    phone = fake.phone_number()
    users_female = (f"{lastname_female},{firstname_female},{middlename_female},{email_female},{phone}").replace(",",";")
    print(users_female)
    # with open('C:/Users/Evgeniy_S/Documents/person_faker_fkgs.csv', 'a', encoding='utf-8') as file:
    #         file.write(f'{users_female}\n')
    return users_female

            
def main():
    person_count = int(input('Введите количество личностей для генерации >>> '))
    for i in range(person_count):
        faker_male_create()
        faker_female_create()


if __name__ == "__main__":
    main()