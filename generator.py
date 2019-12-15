#     __________  ____  ____  ____
#    / ____/ __ \/ __ \/ __ \/ __ \
#   / __/ / /_/ / /_/ / / / / /_/ /
#  / /___/ _, _/ _, _/ /_/ / _, _/
# /_______/ ____/ _________________
#    / __ \/   | / ____/ ____/ ___/
#   / /_/ / /| |/ / __/ __/  \__ \
#  / ____/ ___ / /_/ / /___ ___/ /
# /_/   /_/  |_\____/_____//____/
#
# Copyright 2019, Hyungyo Seo
# generator.py - 템플릿을 바탕으로 오류페이지를 생성하는 스크립트입니다.

import json
import os
import shutil

# 템플릿 파일 열기
try:
    with open('template.html', encoding="utf-8") as data_file:
        template = data_file.read()
except Exception:
    print("template.html 파일 여는 중 오류.")
    exit(1)

# 메세지 파일 열기
try:
    with open('messages.json', encoding="utf-8") as data_file:
        messages = json.load(data_file)
except Exception:
    print("messages.json 파일 여는 중 오류.")
    exit(1)

# 이모지 파일 열기
try:
    with open('emojis.json', encoding="utf-8") as data_file:
        emojis = json.load(data_file)
except Exception:
    print("emojis.json 파일 여는 중 오류.")
    exit(1)

# dist 폴더 있으면 삭제 후 재생성
if os.path.exists("dist"):
    shutil.rmtree("dist")
os.mkdir("dist")

# 템플릿 치환 및 파일 만들기
for categories in messages:
    if categories in emojis:
        # 카테고리명으로 폴더 만들기
        os.mkdir("dist/" + categories)
        for codes in messages[categories]:
            # 치환자 목록
            filter = ["{{message}}", "{{emoji}}", "{{code_left}}", "{{code_right}}"]
            string = [messages[categories][codes], emojis[categories], codes[0], codes[2]]
            with open("dist/" + categories + "/" + codes + ".html", "w", encoding="utf-8") as data_file:
                html = template
                # 치환하기
                for loc in range(len(filter)):
                    html = html.replace(filter[loc], string[loc])
                data_file.write(html)