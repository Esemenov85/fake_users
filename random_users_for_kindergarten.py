from random import choice
from faker import Faker
from transliterate import translit


fake = Faker("ru_RU")

# kod_doo	
# surname_child	
# firstname_child	
# patronymic_child	
# dbirth_child	
# snils_child	
# "табельный номер"	
# "дата рождения"	
# "ФИО ребенка"	
# customer_id	
# children_snils	
# email
# surname_parent
# firstname_parent
# patronymic_parent
# full_name_parent
# dbirth_parrent


def faker_male_create():
    kod_doo = fake.bic() #Генерация фейкового кода ДОО (по генерации БИК)
    
    surname_parent = fake.last_name_male() #fake.last_name_male() #Генерация фейковой мужской фамилии
    firstname_parent = fake.first_name_male() #Генерация фейкового мужского имени
    patronymic_parent = fake.middle_name_male() #Генерация фейкового мужского отчества
    full_name_parent = surname_parent +" "+ firstname_parent +" "+ patronymic_parent
    dbirth_parrent = fake.date_of_birth(minimum_age=20,maximum_age=40)
    
    surname_child = surname_parent 
    firstname_child = fake.first_name_male()
    patronymic_child = firstname_parent+'ович'
    dbirth_child = fake.date_of_birth(minimum_age=2,maximum_age=6)
    snils_child = fake.individuals_inn()
    tab_numb = kod_doo
    birthday = dbirth_child
    names_child = surname_child +" "+ firstname_child +" "+ patronymic_child
    customer_id = fake.postcode()
    children_snils = snils_child
    
    
    
    dict_mail = ['@mail.ru', '@yandex.ru', '@rambler.ru', '@gmail.com', '@bk.ru']
    email = translit(str(surname_parent).lower(), language_code='ru', reversed=True) + choice(dict_mail)
    

    users_male = (f"{kod_doo},{surname_child},{firstname_child},{patronymic_child},{dbirth_child},{snils_child},{tab_numb},{birthday},{names_child},{customer_id},{children_snils},{email},{surname_parent},{firstname_parent}, {patronymic_parent},{full_name_parent},{dbirth_parrent}").replace(",",";")
    print(users_male)
    with open('C:/Users/Evgeniy_S/Documents/person_faker_kindergarten.csv', 'a', encoding='utf-8') as file:
            file.write(f'{users_male}\n')
    return users_male


def faker_female_create():
    kod_doo = fake.bic() #Генерация фейкового кода ДОО (по генерации БИК)
    
    surname_parent = fake.last_name_male() #fake.last_name_male() #Генерация фейковой мужской фамилии
    firstname_parent = fake.first_name_male() #Генерация фейкового мужского имени
    patronymic_parent = fake.middle_name_male() #Генерация фейкового мужского отчества
    full_name_parent = surname_parent +" "+ firstname_parent +" "+ patronymic_parent
    dbirth_parrent = fake.date_of_birth(minimum_age=20,maximum_age=40)
    
    surname_child = surname_parent+'а' 
    firstname_child = fake.first_name_female()
    patronymic_child = firstname_parent+'овна'
    dbirth_child = fake.date_of_birth(minimum_age=2,maximum_age=6)
    snils_child = fake.individuals_inn()
    tab_numb = kod_doo
    birthday = dbirth_child
    names_child = surname_child +" "+ firstname_child +" "+ patronymic_child
    customer_id = fake.postcode()
    children_snils = snils_child
    
    
    
    dict_mail = ['@mail.ru', '@yandex.ru', '@rambler.ru', '@gmail.com', '@bk.ru']
    email = translit(str(surname_parent).lower(), language_code='ru', reversed=True) + choice(dict_mail)
    

    users_female = (f"{kod_doo},{surname_child},{firstname_child},{patronymic_child},{dbirth_child},{snils_child},{tab_numb},{birthday},{names_child},{customer_id},{children_snils},{email},{surname_parent},{firstname_parent}, {patronymic_parent},{full_name_parent},{dbirth_parrent}").replace(",",";")
    print(users_female)
    with open('C:/Users/Evgeniy_S/Documents/person_faker_kindergarten.csv', 'a', encoding='utf-8') as file:
            file.write(f'{users_female}\n')
    return users_female

            
def main():
    person_count = int(input('Введите количество личностей для генерации >>> '))
    for i in range(person_count):
        faker_male_create()
        faker_female_create()


if __name__ == "__main__":
    main()