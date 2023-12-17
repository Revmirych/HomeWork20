import os.path
import csv

def First_String (User_Name, User_Sex, User_Age, User_Bill):
    #Готовим первую строку согласно шаблона домашнего задания.
    Gender = {}
    Gender[0] = {"male" : "мужского пола", "female" : "женского пола"}
    Gender[1] = {"male" : "", "female" : "а"}
    Return_String = f"Пользователь {User_Name} {Gender[0][User_Sex]}, {User_Age} лет совершил{Gender[1][User_Sex]} покупку на {User_Bill} у.е. с\n"
    return (Return_String)

def Second_String (User_Device, User_Browser, User_Region):
    #Готовим вторую строку согласно шаблона домашнего задания.
    Device = {"mobile" : "мобильного браузера", "tablet" : "планшета. И браузера:", "laptop" : "ноутбука. И браузера:", "desktop" : "десктопа. И браузера:"}
    if User_Region == "-":
        User_Region = "выявить не удалось"
    Return_String = f"{Device[User_Device]} {User_Browser}. Регион из которого совершалась покупка: {User_Region}\n"
    return (Return_String)

with open("web_clients_correct.csv", "r", encoding="utf-8") as CSV_File: 
    #Читаем построчно лог транзакций
    CSV_Rows = csv.DictReader(CSV_File)
    String = ""
    for Row in CSV_Rows:
        String += First_String (Row['name'], Row['sex'], Row['age'], Row['bill'])
        String += Second_String (Row['device_type'], Row['browser'], Row['region'])
    #print (String)

Log_Name = 'compleat_log.txt'
if os.path.exists(Log_Name) == True:
    Clear_Old_Log = open(Log_Name, 'w')
    Clear_Old_Log.close()

with open(Log_Name, 'w') as File_Output:
    #Пишем в файл получившийся лог (В задании не указано, что требуется писать построчно. Поэтому пишем сразу)
    File_Output.write(String)
