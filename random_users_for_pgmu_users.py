from random import choice, randint
from faker import Faker
from transliterate import translit
import csv


fake = Faker("ru_RU")

# [0] = {kod_doo}, 
# [1] = {surname_child}, 
# [2] = {firstname_child}, 
# [3] = {patronymic_child}, 
# [4] = {dbirth_child}, 
# [5] = {snils_child}, 
# [6] = {"табельный номер"}, 
# [7] = {"дата рождения"}, 
# [8] = {"ФИО ребенка"}, 
# [9] = {customer_id}, 
# [10] = {children_snils}, 
# [11] = {email}, 
# [12] = {surname_parent}, 
# [13] = {firstname_parent}, 
# [14] = {patronymic_parent}, 
# [15] = {full_name_parent}, 
# [16] = {dbirth_parrent}


# def read_kindergarten():
#     infile = 'C:/Users/Evgeniy_S/Documents/person_faker_kindergarten.csv'
#     outfile = 'C:/Users/Evgeniy_S/Documents/person_faker_users.csv'
    # with open(infile, encoding='utf-8') as infile, open(outfile, 'a', encoding='utf-8') as outfile:
    #     csv_reader = csv.reader(infile, delimiter=';')
    #     headers = next(csv_reader)
    #     new_headers = str(f'{headers[12],headers[13],headers[14],headers[15],headers[16],headers[11]}').replace(",",";").replace("'","").replace("(","").replace(")","")
    #     print(new_headers)
    #     # outfile.write(f'{new_headers}') # Записываем заголовки в файл
        
    #     csv_reader = csv.DictReader(infile, delimiter=";")
    #     for row in csv_reader:
    #         new_reader = str((row['surname_parent'],row['firstname_parent'],row['patronymic_parent'],row['dbirth_parrent'],row['email'])).replace(",",";").replace("'","").replace("(","").replace(")","")
    #         print(new_reader)
    #         # outfile.write(f'{new_reader}\n') # Записываем строки без заголовка в файл
    
    
    
    # with open(file_csv, encoding='utf-8') as file:
    #         reader = csv.reader(file, delimiter=";")
    #         headers = next(reader)
    #         print('Headers: ', headers)
    #         # for row in reader:
    #             # print(row)
    #         #     file.write(f'{new_reader}\n')
    # with open(file_csv, encoding='utf-8') as file:
    #         reader = csv.DictReader(file, delimiter=";")
    #         for row in reader:
    #             new_reader = str((row['surname_parent'],row['firstname_parent'],row['patronymic_parent'],row['dbirth_parrent'],row['email'])).replace(",",";").replace("'","").replace("(","").replace(")","")
    #             print(new_reader)
    #             #     file.write(f'{new_reader}\n')
    

 
    # with open(infile, encoding='utf-8') as infile, open(outfile, 'a', encoding='utf-8') as outfile:
    #     csv_reader = csv.reader(infile, delimiter=';')
    #     headers = next(csv_reader)
    #     # res = dict((i, headers.count(i)) for i in headers)
    #     # print(f'{res['surname_parent'],res['firstname_parent'],res['patronymic_parent'],res['dbirth_parrent'],res['email']}')
    #     # print(headers)
    #     new_headers = str(f'{headers[12],headers[13],headers[14],headers[15],headers[16],headers[11]}').replace(",",";").replace("'","").replace("(","").replace(")","")
    #     print(new_headers)
    #     # outfile.write(f'{new_headers}') # Записываем заголовки в файл
        

    # with open(infile, encoding='utf-8') as infile, open(outfile, 'a', encoding='utf-8') as outfile:
    #         reader = csv.DictReader(infile, delimiter=";")
    #         for row in reader:
    #             new_reader = str((row['surname_parent'],row['firstname_parent'],row['patronymic_parent'],row['dbirth_parrent'],row['email'])).replace(",",";").replace("'","").replace("(","").replace(")","")
    #             print(new_reader)
    #             # outfile.write(f'{new_reader}\n') # Записываем строки без заголовка в файл
    
def get_header():
    infile = 'C:/Users/Evgeniy_S/Documents/person_faker_kindergarten.csv'
    outfile = 'C:/Users/Evgeniy_S/Documents/person_faker_users_1.csv'
    with open(infile, encoding='utf-8') as infile, open(outfile, 'a', encoding='utf-8') as outfile:
        csv_reader = csv.reader(infile, delimiter=';')
        headers = next(csv_reader)
        new_headers = str(f'{headers[12],headers[13],headers[14],headers[15],headers[16],headers[11],headers[9]}'+";").replace(",",";").replace("'","").replace("(","").replace(")","").replace(" ","")
        print(new_headers)
        outfile.write(f'{new_headers}\n') # Записываем заголовки в файл

def get_row():
    infile = 'C:/Users/Evgeniy_S/Documents/person_faker_kindergarten.csv'
    outfile = 'C:/Users/Evgeniy_S/Documents/person_faker_users_1.csv'
    with open(infile, encoding='utf-8') as infile, open(outfile, 'a', encoding='utf-8') as outfile:
            reader = csv.DictReader(infile, delimiter=";")
            for row in reader:
                new_reader = str((row['surname_parent'],row['firstname_parent'],row['patronymic_parent'],row['dbirth_parrent'],row['email'],row['customer_id']+";")).replace(",",";").replace("'","").replace("(","").replace(")","").replace(" ","")
                print(new_reader)
                outfile.write(f'{new_reader}\n') # Записываем строки без заголовка в файл


def faker_create():
    sex = 1
    is_has_app = randint(1,2)
    driver_license_seria = fake.plate_number_extra()
    driver_license_number = fake.plate_number_special()
    users_documents = (f"{sex},{is_has_app},{driver_license_seria},{driver_license_number}").replace(",",";")
    print(users_documents)
    with open('C:/Users/Evgeniy_S/Documents/person_faker_users_2.csv', 'a', encoding='utf-8') as file:
            file.write(f'{users_documents}\n')
    return users_documents
    

def main():
    person_count = int(input('Введите количество личностей для генерации >>> '))
    for i in range(person_count):
        faker_create()
    get_header()
    get_row()


if __name__ == "__main__":
    main()