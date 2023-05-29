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

with open("./讀取練習utf8.csv", 'r', encoding='utf-8') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    if row[1][3:5]:
        sex = '男' if row[0][1] == '1' else '女'
        result.append([row[0] , row[1] , row[2][0] + 'O' + row[2][1] , dep[row[1][3:5]], sex , city[row[0][0]]])
    index += 1

print(result)

with open("result.csv", "w", newline="", encoding='utf-8') as csvfile:
  writer = csv.writer(csvfile)
  for r in result:
    writer.writerow(r)