import csv

dep = {
    '66':'資訊管理系',
    '56':'應用外語系',
    '46':'多媒體設計系',
    '36':'會計資訊系',
    '26':'企業管理系',
    '16':'資訊工程系'
}

city ={
'A':'臺北市',
'B':'臺中市',
'C':'基隆市',
'D':'臺南市',
'E':'高雄市',
'F':'新北市',
'G':'宜蘭縣',
'H':'桃園市',
'J':'新竹縣',
'K':'苗栗縣',
'L':'臺中縣',
'M':'南投縣',
'N':'彰化縣',
'P':'雲林縣',
'Q':'嘉義縣',
'R':'臺南縣',
'S':'高雄縣',
'T':'屏東縣',
'U':'花蓮縣',
'V':'臺東縣',
'X':'澎湖縣',
'Y':'陽明山',
'W':'金門縣',
'Z':'連江縣',
'I':'嘉義市',
'O':'新竹市'
}

result = []
index = 0

import pandas as pd

url = "./讀取練習utf8.csv"

df = pd.read_csv(url, encoding='utf-8')
df['姓名'] = df['姓名'].str[0] + 'O' + df['姓名'].str[0][2]

def fill_depart(row):
    return dep[str(row['學號'])[3:5]]
 
df['科系'] = df.apply(fill_depart, axis=1)

def fill_gender(row):
    first_digit = int(row['身分證'][1])
    if first_digit == 1:
        return '男'
    elif first_digit == 2:
        return '女'
    else:
        return None

df['性別'] = df.apply(fill_gender, axis=1)

def fill_place(row):
    return city[row['身分證'][0]]

df['居住地'] = df.apply(fill_place, axis=1)


df.to_csv('result.csv', index=False, encoding='utf-8')

