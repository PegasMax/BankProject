import logging

from src.analytics import process_bank_search
from src.processing import filter_by_state, sort_by_date
from src.table_integration import get_transactions_from_csv_file, get_transactions_from_excel_file
from src.utils import get_transactions_from_json_file
from src.widget import get_date, mask_account_card

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/main.log")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def main() -> None:
    """Основная логика проекта"""
    # Выбор файла с данными
    logger.info("Начинает работу модуль main")

    loader_index = None
    is_ascending = None
    description_filter = ""

    logger.info("Пользователь выбирает файл для получения данных")

    loader = {
        "1": "Для обработки выбран JSON-файл.",
        "2": "Для обработки выбран CSV-файл.",
        "3": "Для обработки выбран XLSX-файл.",
    }

    while loader_index not in ("1", "2", "3"):
        if loader_index:
            print(f"Варианта {loader_index} не существует, начнем заново..")
        loader_index = input(
            """Привет! Добро пожаловать в программу работы с банковскими транзакциями. \nВыберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла\n2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла\n"""
        )
    print(loader[loader_index])
    logger.info(f"{loader[loader_index]}")

    logger.info("Получаем данные из файла")
    transaction_list = []
    if loader_index == "1":
        transaction_list = get_transactions_from_json_file("data/operations.json")
    elif loader_index == "2":
        transaction_list = get_transactions_from_csv_file("data/transactions.csv")
    else:
        transaction_list = get_transactions_from_excel_file("data/transactions_excel.xlsx")

    logger.info("Пользователь выбирает статус интересующих его операций.")

    user_input = None
    while user_input not in ("EXECUTED", "CANCELED", "PENDING"):
        if user_input:
            print(f"Статус операции {user_input} недоступен.", end="\n")

        user_input = input(
            """Введите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"""
        ).upper()

    filter_for_status = user_input

    logger.info("Фильтруем данные")
    transaction_list = filter_by_state(transaction_list, filter_for_status)
    print(f'Операции отфильтрованы по статусу "{filter_for_status}"')
    logger.info(f"Пользователь выбрал фильтрацию по статусу {filter_for_status}")

    logger.info("Пользователь выбирает сортировать ли операции по дате")
    user_input = None
    while user_input not in ("Да", "Нет"):
        if user_input:
            print(f"Вариант {user_input} недоступен.", end="\n")
        user_input = input("Отсортировать операции по дате? Да/Нет \n").capitalize()

    if user_input == "Нет":
        logger.info("Пользователь решил не производить сортировку операций по дате")
    else:
        logger.info("Пользователь решил произвести сортировку операций по дате")
        logger.info("Уточняем направление сортировки")

        user_input = None
        while user_input not in ("по возрастанию", "по убыванию"):
            if user_input:
                print(f"Вариант {user_input} недоступен.", end="\n")
            user_input = input("Отсортировать по возрастанию или по убыванию?\n").lower()

        if user_input == "по возрастанию":
            is_ascending = True
            transaction_list = sort_by_date(transaction_list, is_ascending)
            logger.info("Пользователь выбрал сортировку по возрастанию")
        else:
            is_ascending = False
            transaction_list = sort_by_date(transaction_list, is_ascending)
            logger.info("Пользователь выбрал сортировку по убыванию")

    logger.info("Узнаем нужны все транзакции или только рублевые")
    user_input = None
    while user_input not in ("Да", "Нет"):
        if user_input:
            print(f"Вариант {user_input} недоступен.", end="\n")
        user_input = input("Выводить только рублевые транзакции? Да/Нет \n").capitalize()

    if user_input == "Нет":
        logger.info("Выбраны все операции")
    else:
        transaction_list = [
            transaction
            for transaction in transaction_list
            if transaction["operationAmount"]["currency"]["code"] == "RUB"
        ]
        logger.info("Выбраны только рублевые операции")

    logger.info("Узнаем нужно ли фильтровать список транзакций по слову в описании")
    user_input = None
    while user_input not in ("Да", "Нет"):
        if user_input:
            print(f"Вариант {user_input} недоступен.", end="\n")
        user_input = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет \n").capitalize()

    if user_input == "Нет":
        logger.info("Решено не фильтровать операции")
    else:
        logger.info("Решено фильтровать операции")

        logger.info("Запрос слова для фильтрации операций")
        user_input = input("По какому слову в описании фильтровать операции?\n")

        description_filter = user_input
        transaction_list = process_bank_search(transaction_list, description_filter)
        logger.info(f"Пользователь выбрал оставить операции со словом {description_filter} в описании")

    print("Распечатываю итоговый список транзакций...\n")

    print(f"Всего банковских операций в выборке: {len(transaction_list)}\n")

    for transaction in transaction_list:
        print(f'{get_date(transaction["date"])} {transaction["description"]}')
        money_way_output = ""
        if "from" in transaction:
            money_way_output = f'{mask_account_card(transaction["from"])} -> '
        money_way_output += mask_account_card(transaction["to"])
        print(money_way_output)
        print(
            f'Сумма: {round(float(transaction["operationAmount"]["amount"]))} {transaction["operationAmount"]["currency"]["name"]}\n'
        )


if __name__ == "__main__":
    main()
