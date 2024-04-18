import json


def convert_base64_to_number(base64: str):
    number = ""

    splited_base64 = base64.split("/+")
    for split in splited_base64:
        length = str(len(split))
        number += length

    return number


def break_captcha(base64: dict):
    captcha_result = []
    base64_all = {}
    with open("data/base64l.json", "r") as lb64:
        base64_texts = json.load(lb64)

    with open("data/base64n.json", "r") as nb64:
        base64_numbers = json.load(nb64)

    base64_all.update(base64_numbers)
    base64_all.update(base64_texts)

    for i, b64 in enumerate(base64):
        converted_b64 = convert_base64_to_number(b64)
        print(converted_b64)
        b64_result = base64_texts.get(converted_b64)
        captcha_result.append(b64_result)

    return "".join(captcha_result)
