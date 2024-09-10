from random import choice, randint
from faker import Faker
from transliterate import translit
import csv


fake = Faker("ru_RU")

# lastname
# firstname
# middlename
# birthday
# email
# sex
# is_has_app
# driver_license_seria
# driver_license_number
# customer_id


def read_kindergarten():
    file_csv = 'C:/Users/Evgeniy_S/Documents/person_faker_kindergarten.csv'
    with open(file_csv, encoding='utf-8') as file:
            # file.read()
            reader = csv.reader(file)
            # for row in reader:
            #     print(row)
            reader = csv.DictReader(file)
            headers = next(reader)
            print('Headers: ', headers)
            for row in reader:
                print(row)
                print(row['surname_parent'], row['firstname_parent'])
                # row['surname_parent'], row['firstname_parent'], row['patronymic_parent'], row['dbirth_parrent'], row['email']

def faker_create():
    sex = 1
    is_has_app = randint(1,2)
    driver_license_seria = fake.plate_number_extra()
    driver_license_number = fake.plate_number_special()
    users_documents = (f"{sex},{is_has_app},{driver_license_seria},{driver_license_number}").replace(",",";")
    print(users_documents)
    # with open('C:/Users/Evgeniy_S/Documents/person_faker_users.csv', 'a', encoding='utf-8') as file:
    #         file.write(f'{users_documents}\n')
    return users_documents
    

def main():
    person_count = int(input('Введите количество личностей для генерации >>> '))
    for i in range(person_count):
        faker_create()
    read_kindergarten()


if __name__ == "__main__":
    main()