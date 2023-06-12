import json
from datetime import datetime


def read_json(file_path):
    """
    Считывает нужный файл в формате json
    :param file_path: Путь к json-файлу
    :return: Список словарей в нужном формате
    """
    with open(file_path, encoding='utf-8') as i:
        data = json.load(i)
    return data


def sort_data(data):
    """
    Выбирает успешно-выполненные операции и сортирует их по дате
    :param data: Список операций
    :return: Отсортированный список операций
    """
    sorted_data = []
    for operation in data:
        if "state" in operation.keys():
            if operation["state"] == "EXECUTED":
                sorted_data.append(operation)
    sorted_data.sort(key=lambda x: x["date"], reverse=True)
    return sorted_data


def correct_date(data: dict):
    """
    Изменяет формат даты в читаемый
    :param data: Отдельная операция из списка
    :return: Отформатированная дата из списка операций
    """
    return datetime.strptime(data['date'], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")


def hidden_card_number(data: dict):
    """
    Скрывает некоторые цифры номера карты
    :param data: Отдельная операция из списка
    :return: Номер карты со скрытыми цифрами
    """
    if 'from' in data.keys():
        if 'Счет' in data['from']:
            hiden_number = '**' + data['from'][-4::]
        else:
            hiden_number = f"{data['from'][:-12]} {data['from'][-12:-10]}** **** {data['from'][-4::]}"
    else:
        hiden_number = ''
    return hiden_number


def hidden_account(data: dict):
    """
    Скрывает некоторые цифры номера счета
    :param data: Отдельная операция из списка
    :return: Номер счета со скрытыми цифрами
    """
    if 'to' in data.keys():
        hidden_acc = '**' + data['to'][-4::]
    else:
        hidden_acc = ''
    return hidden_acc


def final_output(data: dict) -> str:
    """
   Выбирает из операции нужные данные и возвращает их
    :param data: Отдельная операция из списка
    :return str: Необходимая информация из операции
    """
    return f"{correct_date(data)} {data['description']}\n" \
           f" {hidden_card_number(data)} -> {hidden_account(data)}\n" \
           f" {data['operationAmount']['amount']} {data['operationAmount']['currency']['name']}"