import re

def create_password(pwd):
  try:  
    must_number_pattern = '\d'
    must_upper_pattern = '[A-Z]'
    must_lower_pattern = '[a-z]'

    if len(pwd) < 8:
      raise ValueError("密碼必須大於8位數")
    elif len(pwd) > 16:
      raise ValueError("密碼必須小於16位數")
    elif not re.findall(must_number_pattern, pwd):
        raise ValueError("密碼必須有數字")
    elif re.findall(must_upper_pattern, pwd) == []:
        raise ValueError("密碼必須有大寫英文字母")
    elif re.findall(must_lower_pattern, pwd) == []:
        raise ValueError("密碼必須有小寫英文字母")
    elif " " in pwd:
      raise Exception("密碼不能有空格")
    else:
       print('密碼設定成功')

  except ValueError as err:
    print(str(err))
  except Exception as e:
    print(str(e))
  
create_password("dAddddddd3")