import os


# 폴더 안에 있는 모든 파일들을 보여주는 소스코드
file_name_list = os.listdir()
for name in file_name_list:
    print(name)

