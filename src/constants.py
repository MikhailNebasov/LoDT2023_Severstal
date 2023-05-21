from datetime import timedelta
import datetime


SENSOR_LIST = {
    "ЭКСГАУСТЕР 4. ТОК РОТОРА 1": {"BDName": "Э4.iР1", "DispName": ""},
    "ЭКСГАУСТЕР 4. ТОК РОТОРА2": {"BDName": "Э4.iР2", "DispName": ""},
    "ЭКСГАУСТЕР 4. ТОК СТАТОРА": {"BDName": "Э4.iС", "DispName": ""},
    "ЭКСГАУСТЕР 4. ДАВЛЕНИЕ МАСЛА В СИСТЕМЕ": {"BDName": "Э4.pМвС", "DispName": ""},
    "ЭКСГАУСТЕР 4. ТЕМПЕРАТУРА ПОДШИПНИКА НА ОПОРЕ 1": {"BDName": "Э4.tПО1", "DispName": ""},
    "ЭКСГАУСТЕР 4. ТЕМПЕРАТУРА ПОДШИПНИКА НА ОПОРЕ 2": {"BDName": "Э4.tПО2", "DispName": ""},
    "ЭКСГАУСТЕР 4. ТЕМПЕРАТУРА ПОДШИПНИКА НА ОПОРЕ 3": {"BDName": "Э4.tПО3", "DispName": ""},
    "ЭКСГАУСТЕР 4. ТЕМПЕРАТУРА ПОДШИПНИКА НА ОПОРЕ 4": {"BDName": "Э4.tПО4", "DispName": ""},
    "ЭКСГАУСТЕР 4. ТЕМПЕРАТУРА МАСЛА В СИСТЕМЕ": {"BDName": "Э4.tМвС", "DispName": ""},
    "ЭКСГАУСТЕР 4. ТЕМПЕРАТУРА МАСЛА В МАСЛОБЛОКЕ": {"BDName": "Э4.tМвМ", "DispName": ""},
    "ЭКСГАУСТЕР 4. ВИБРАЦИЯ НА ОПОРЕ 1": {"BDName": "Э4.vО1", "DispName": ""},
    "ЭКСГАУСТЕР 4. ВИБРАЦИЯ НА ОПОРЕ 2": {"BDName": "Э4.vО2", "DispName": ""},
    "ЭКСГАУСТЕР 4. ВИБРАЦИЯ НА ОПОРЕ 3": {"BDName": "Э4.vО3", "DispName": ""},
    "ЭКСГАУСТЕР 4. ВИБРАЦИЯ НА ОПОРЕ 3. ПРОДОЛЬНАЯ.": {"BDName": "Э4.vО3п", "DispName": ""},
    "ЭКСГАУСТЕР 4. ВИБРАЦИЯ НА ОПОРЕ 4": {"BDName": "Э4.vО4", "DispName": ""},
    "ЭКСГАУСТЕР 4. ВИБРАЦИЯ НА ОПОРЕ 4. ПРОДОЛЬНАЯ.": {"BDName": "Э4.vО4п", "DispName": ""},
    "ЭКСГАУСТЕР 5. ТОК РОТОРА 1": {"BDName": "Э5.iР1", "DispName": ""},
    "ЭКСГАУСТЕР 5. ТОК РОТОРА 2": {"BDName": "Э5.iР2", "DispName": ""},
    "ЭКСГАУСТЕР 5. ТОК СТАТОРА": {"BDName": "Э5.iС", "DispName": ""},
    "ЭКСГАУСТЕР 5. ДАВЛЕНИЕ МАСЛА В СИСТЕМЕ": {"BDName": "Э5.p", "DispName": ""},
    "ЭКСГАУСТЕР 5. ТЕМПЕРАТУРА ПОДШИПНИКА НА ОПОРЕ 1": {"BDName": "Э5.tПО1", "DispName": ""},
    "ЭКСГАУСТЕР 5. ТЕМПЕРАТУРА ПОДШИПНИКА НА ОПОРЕ 2": {"BDName": "Э5.tПО2", "DispName": ""},
    "ЭКСГАУСТЕР 5. ТЕМПЕРАТУРА ПОДШИПНИКА НА ОПОРЕ 3": {"BDName": "Э5.tПО3", "DispName": ""},
    "ЭКСГАУСТЕР 5. ТЕМПЕРАТУРА ПОДШИПНИКА НА ОПОРЕ 4": {"BDName": "Э5.tПО4", "DispName": ""},
    "ЭКСГАУСТЕР 5. ТЕМПЕРАТУРА МАСЛА В СИСТЕМЕ": {"BDName": "Э5.tМС", "DispName": ""},
    "ЭКСГАУСТЕР 5. ТЕМПЕРАТУРА МАСЛА В МАСЛОБЛОКЕ": {"BDName": "Э5.tММ", "DispName": ""},
    "ЭКСГАУСТЕР 5. ВИБРАЦИЯ НА ОПОРЕ 1": {"BDName": "Э5.vО1", "DispName": ""},
    "ЭКСГАУСТЕР 5. ВИБРАЦИЯ НА ОПОРЕ 2": {"BDName": "Э5.vО2", "DispName": ""},
    "ЭКСГАУСТЕР 5. ВИБРАЦИЯ НА ОПОРЕ 3": {"BDName": "Э5.vО3", "DispName": ""},
    "ЭКСГАУСТЕР 5. ВИБРАЦИЯ НА ОПОРЕ 3. ПРОДОЛЬНАЯ.": {"BDName": "Э5.vО3п", "DispName": ""},
    "ЭКСГАУСТЕР 5. ВИБРАЦИЯ НА ОПОРЕ 4": {"BDName": "Э5.vО4", "DispName": ""},
    "ЭКСГАУСТЕР 5. ВИБРАЦИЯ НА ОПОРЕ 4. ПРОДОЛЬНАЯ.": {"BDName": "Э5.vО4п", "DispName": ""},
    "ЭКСГАУСТЕР 6. ТОК РОТОРА 1": {"BDName": "Э6.iР1", "DispName": ""},
    "ЭКСГАУСТЕР 6. ТОК РОТОРА 2": {"BDName": "Э6.iР2", "DispName": ""},
    "ЭКСГАУСТЕР 6. ТОК СТАТОРА": {"BDName": "Э6.iС", "DispName": ""},
    "ЭКСГАУСТЕР 6. ДАВЛЕНИЕ МАСЛА В СИСТЕМЕ": {"BDName": "Э6.pМС", "DispName": ""},
    "ЭКСГАУСТЕР 6. ТЕМПЕРАТУРА ПОДШИПНИКА НА ОПОРЕ 1": {"BDName": "Э6.tПО1", "DispName": ""},
    "ЭКСГАУСТЕР 6. ТЕМПЕРАТУРА ПОДШИПНИКА НА ОПОРЕ 2": {"BDName": "Э6.tПО2", "DispName": ""},
    "ЭКСГАУСТЕР 6. ТЕМПЕРАТУРА ПОДШИПНИКА НА ОПОРЕ 3": {"BDName": "Э6.tПО3", "DispName": ""},
    "ЭКСГАУСТЕР 6. ТЕМПЕРАТУРА ПОДШИПНИКА НА ОПОРЕ 4": {"BDName": "Э6.tПО4", "DispName": ""},
    "ЭКСГАУСТЕР 6. ТЕМПЕРАТУРА МАСЛА В СИСТЕМЕ": {"BDName": "Э6.tМС", "DispName": ""},
    "ЭКСГАУСТЕР 6. ТЕМПЕРАТУРА МАСЛА В МАСЛОБЛОКЕ": {"BDName": "Э6.tММ", "DispName": ""},
    "ЭКСГАУСТЕР 6. ВИБРАЦИЯ НА ОПОРЕ 1": {"BDName": "Э6.vО1", "DispName": ""},
    "ЭКСГАУСТЕР 6. ВИБРАЦИЯ НА ОПОРЕ 2": {"BDName": "Э6.vО2", "DispName": ""},
    "ЭКСГАУСТЕР 6. ВИБРАЦИЯ НА ОПОРЕ 3": {"BDName": "Э6.vО3", "DispName": ""},
    "ЭКСГАУСТЕР 6. ВИБРАЦИЯ НА ОПОРЕ 3. ПРОДОЛЬНАЯ.": {"BDName": "Э6.vО3п", "DispName": ""},
    "ЭКСГАУСТЕР 6. ВИБРАЦИЯ НА ОПОРЕ 4": {"BDName": "Э6.vО4", "DispName": ""},
    "ЭКСГАУСТЕР 6. ВИБРАЦИЯ НА ОПОРЕ 4. ПРОДОЛЬНАЯ.": {"BDName": "Э6.vО4п", "DispName": ""},
    "ЭКСГАУСТЕР 7. ТОК РОТОРА 1": {"BDName": "Э7.iР1", "DispName": ""},
    "ЭКСГАУСТЕР 7. ТОК РОТОРА 2": {"BDName": "Э7.iР2", "DispName": ""},
    "ЭКСГАУСТЕР 7. ТОК СТАТОРА": {"BDName": "Э7.iС", "DispName": ""},
    "ЭКСГАУСТЕР 7. ДАВЛЕНИЕ МАСЛА В СИСТЕМЕ": {"BDName": "Э7.pМС", "DispName": ""},
    "ЭКСГАУСТЕР 7. ТЕМПЕРАТУРА ПОДШИПНИКА НА ОПОРЕ 1": {"BDName": "Э7.tПО1", "DispName": ""},
    "ЭКСГАУСТЕР 7. ТЕМПЕРАТУРА ПОДШИПНИКА НА ОПОРЕ 2": {"BDName": "Э7.tПО2", "DispName": ""},
    "ЭКСГАУСТЕР 7. ТЕМПЕРАТУРА ПОДШИПНИКА НА ОПОРЕ 3": {"BDName": "Э7.tПО3", "DispName": ""},
    "ЭКСГАУСТЕР 7. ТЕМПЕРАТУРА ПОДШИПНИКА НА ОПОРЕ 4": {"BDName": "Э7.tПО4", "DispName": ""},
    "ЭКСГАУСТЕР 7. ТЕМПЕРАТУРА МАСЛА В СИСТЕМЕ": {"BDName": "Э7.tМС", "DispName": ""},
    "ЭКСГАУСТЕР 7. ТЕМПЕРАТУРА МАСЛА В МАСЛОБЛОКЕ": {"BDName": "Э7.tММ", "DispName": ""},
    "ЭКСГАУСТЕР 7. ВИБРАЦИЯ НА ОПОРЕ 1": {"BDName": "Э7.vО1", "DispName": ""},
    "ЭКСГАУСТЕР 7. ВИБРАЦИЯ НА ОПОРЕ 2": {"BDName": "Э7.vО2", "DispName": ""},
    "ЭКСГАУСТЕР 7. ВИБРАЦИЯ НА ОПОРЕ 3": {"BDName": "Э7.vО3", "DispName": ""},
    "ЭКСГАУСТЕР 7. ВИБРАЦИЯ НА ОПОРЕ 3. ПРОДОЛЬНАЯ.": {"BDName": "Э7.vО3п", "DispName": ""},
    "ЭКСГАУСТЕР 7. ВИБРАЦИЯ НА ОПОРЕ 4": {"BDName": "Э7.vО4", "DispName": ""},
    "ЭКСГАУСТЕР 7. ВИБРАЦИЯ НА ОПОРЕ 4. ПРОДОЛЬНАЯ.": {"BDName": "Э7.v4п", "DispName": ""},
    "ЭКСГАУСТЕР 8. ТОК РОТОРА 1": {"BDName": "Э8.iР1", "DispName": ""},
    "ЭКСГАУСТЕР 8. ТОК РОТОРА 2": {"BDName": "Э8.iР2", "DispName": ""},
    "ЭКСГАУСТЕР 8. ТОК СТАТОРА": {"BDName": "Э8.iС", "DispName": ""},
    "ЭКСГАУСТЕР 8. ДАВЛЕНИЕ МАСЛА В СИСТЕМЕ": {"BDName": "Э8.pМС", "DispName": ""},
    "ЭКСГАУСТЕР 8. ТЕМПЕРАТУРА ПОДШИПНИКА НА ОПОРЕ 1": {"BDName": "Э8.tПО1", "DispName": ""},
    "ЭКСГАУСТЕР 8. ТЕМПЕРАТУРА ПОДШИПНИКА НА ОПОРЕ 2": {"BDName": "Э8.tПО2", "DispName": ""},
    "ЭКСГАУСТЕР 8. ТЕМПЕРАТУРА ПОДШИПНИКА НА ОПОРЕ 3": {"BDName": "Э8.tПО3", "DispName": ""},
    "ЭКСГАУСТЕР 8. ТЕМПЕРАТУРА ПОДШИПНИКА НА ОПОРЕ 4": {"BDName": "Э8.tПО4", "DispName": ""},
    "ЭКСГАУСТЕР 8. ТЕМПЕРАТУРА МАСЛА В СИСТЕМЕ": {"BDName": "Э8.tМС", "DispName": ""},
    "ЭКСГАУСТЕР 8. ТЕМПЕРАТУРА МАСЛА В МАСЛОБЛОКЕ": {"BDName": "Э8.tММ", "DispName": ""},
    "ЭКСГАУСТЕР 8. ВИБРАЦИЯ НА ОПОРЕ 1": {"BDName": "Э8.vО1", "DispName": ""},
    "ЭКСГАУСТЕР 8. ВИБРАЦИЯ НА ОПОРЕ 2": {"BDName": "Э8.vО2", "DispName": ""},
    "ЭКСГАУСТЕР 8. ВИБРАЦИЯ НА ОПОРЕ 3": {"BDName": "Э8.vО3", "DispName": ""},
    "ЭКСГАУСТЕР 8. ВИБРАЦИЯ НА ОПОРЕ 3. ПРОДОЛЬНАЯ.": {"BDName": "Э8.vО3п", "DispName": ""},
    "ЭКСГАУСТЕР 8. ВИБРАЦИЯ НА ОПОРЕ 4": {"BDName": "Э8.vО4", "DispName": ""},
    "ЭКСГАУСТЕР 8. ВИБРАЦИЯ НА ОПОРЕ 4. ПРОДОЛЬНАЯ.": {"BDName": "Э8.vО4п", "DispName": ""},
    "ЭКСГАУСТЕР 9. ТОК РОТОРА 1": {"BDName": "Э9.iР1", "DispName": ""},
    "ЭКСГАУСТЕР 9. ТОК РОТОРА 2": {"BDName": "Э9.iР2", "DispName": ""},
    "ЭКСГАУСТЕР 9. ТОК СТАТОРА": {"BDName": "Э9.iС", "DispName": ""},
    "ЭКСГАУСТЕР 9. ДАВЛЕНИЕ МАСЛА В СИСТЕМЕ": {"BDName": "Э9.pМС", "DispName": ""},
    "ЭКСГАУСТЕР 9. ТЕМПЕРАТУРА ПОДШИПНИКА НА ОПОРЕ 1": {"BDName": "Э9.tО1", "DispName": ""},
    "ЭКСГАУСТЕР 9. ТЕМПЕРАТУРА ПОДШИПНИКА НА ОПОРЕ 2": {"BDName": "Э9.tО2", "DispName": ""},
    "ЭКСГАУСТЕР 9. ТЕМПЕРАТУРА ПОДШИПНИКА НА ОПОРЕ 3": {"BDName": "Э9.tО3", "DispName": ""},
    "ЭКСГАУСТЕР 9. ТЕМПЕРАТУРА ПОДШИПНИКА НА ОПОРЕ 4": {"BDName": "Э9.tО4", "DispName": ""},
    "ЭКСГАУСТЕР 9. ТЕМПЕРАТУРА МАСЛА В СИСТЕМЕ": {"BDName": "Э9.tМС", "DispName": ""},
    "ЭКСГАУСТЕР 9. ТЕМПЕРАТУРА МАСЛА В МАСЛОБЛОКЕ": {"BDName": "Э9.tММ", "DispName": ""},
    "ЭКСГАУСТЕР 9. ВИБРАЦИЯ НА ОПОРЕ 1": {"BDName": "Э9.vО1", "DispName": ""},
    "ЭКСГАУСТЕР 9. ВИБРАЦИЯ НА ОПОРЕ 2": {"BDName": "Э9.vО2", "DispName": ""},
    "ЭКСГАУСТЕР 9. ВИБРАЦИЯ НА ОПОРЕ 3": {"BDName": "Э9.vО3", "DispName": ""},
    "ЭКСГАУСТЕР 9. ВИБРАЦИЯ НА ОПОРЕ 3. ПРОДОЛЬНАЯ.": {"BDName": "Э9.vО3п", "DispName": ""},
    "ЭКСГАУСТЕР 9. ВИБРАЦИЯ НА ОПОРЕ 4": {"BDName": "Э9.vО4", "DispName": ""},
    "ЭКСГАУСТЕР 9. ВИБРАЦИЯ НА ОПОРЕ 4. ПРОДОЛЬНАЯ.": {"BDName": "Э9.vО4п", "DispName": ""},
}

# Проверим чтобы каждое название столбца для таблицы было использовано только один раз
for element in SENSOR_LIST.keys():
    counter = 0
    for test_element in SENSOR_LIST.keys():
        if SENSOR_LIST[test_element]["BDName"] == SENSOR_LIST[element]["BDName"]:
            counter += 1

    if counter > 1:
        print(f"Название столбца [{SENSOR_LIST[element]['BDName']}] для датчика [{element}], дублируется.")

for element in SENSOR_LIST.keys():
    # Если не указано название для вывода на экран,
    # то используем короткое имя, предназначенное
    # для названия столбца в таблице
    if SENSOR_LIST[element]["DispName"] == "":
        SENSOR_LIST[element]["DispName"] = SENSOR_LIST[element]["BDName"]

initual_data_PERIOD_TYPES = \
        {
            "table_name": "PERIOD_TYPES", "find_and_update_or_insert": True, "id_column": "id", "donot_commit": False,
                "data":
                [   {"id": 0, "period_name": "Один тик", "phidden": 1},
                    {"id": 1, "period_name": "Одна минута", "phidden": 1},
                    {"id": 2, "period_name": "5 минут", "phidden": 1},
                    {"id": 3, "period_name": "10 минут", "phidden": 1},
                    {"id": 4, "period_name": "15 минут", "phidden": 1},
                    {"id": 5, "period_name": "30 минут", "phidden": 1},
                    {"id": 6, "period_name": "Час", "phidden": 0},
                    {"id": 7, "period_name": "День", "phidden": 1},
                    {"id": 8, "period_name": "Неделя", "phidden": 1},
                    {"id": 9, "period_name": "Месяц", "phidden": 1}
                ]
        }

initual_data_STOCKS = \
        {
            "table_name": "STOCKS", "find_and_update_or_insert": True, "id_column": "trade_kod", "donot_commit": False,
                "data":
                [   {"trade_kod": "GAZP", "mfd_id": 330, "full_name": 'ПАО "Газпром", акция обыкновенная', "short_name": "ГАЗПРОМ а/о", "order_field": 1, "phidden": 0},
                    {"trade_kod": "LKOH", "mfd_id": 632, "full_name": 'ПАО "Нефтяная компания "ЛУКОЙЛ", акция обыкновенная', "short_name": "ЛУКОЙЛ а/о", "order_field": 2, "phidden": 0},
                    {"trade_kod": "ROS", "mfd_id": 1373, "full_name": 'ПАО "Нефтяная компания "РОСНЕФТЬ", акция обыкновенная', "short_name": "РОСНЕФТЬ а/о", "order_field": 2, "phidden": 0},
                    {"trade_kod": "NLMK", "mfd_id": 913, "full_name": 'ПАО "Новолипецкий металлургический комбинат", акция обыкновенная', "short_name": "НЛМК", "order_field": 2, "phidden": 0},
                    {"trade_kod": "MMK", "mfd_id": 716, "full_name": 'ПАО "Магнитогорский металлургический комбинат", акция обыкновенная', "short_name": "ММК а/о", "order_field": 2, "phidden": 0}
                ]
        }

# Сгенерируем словарь с типами периодов:
PERIOD_TYPES = {
                initual_data_PERIOD_TYPES["data"][j]["period_name"]: initual_data_PERIOD_TYPES["data"][j]["id"]
                    for j in range(1, len(initual_data_PERIOD_TYPES["data"]))
               }

DEFAULT_PERIOD_TYPE = PERIOD_TYPES["Час"]

API_URL = "https://mfd.ru/export/handler.ashx/DataFile.txt?"
API_PARAMS = {
    "TickerGroup": "16",
    "Tickers": "330",
    "Alias": "False",
    "Period": "7",
    "timeframeValue": "1,",
    "timeframeDatePart": "day",
    "StartDate": "01.06.2019",
    "EndDate": "09.06.2019",
    "SaveFormat": "0",
    "SaveMode": "0",
    "FileName": "FileWithData.txt",
    "FieldSeparator": ";",
    "DecimalSeparator": ".",
    "DateFormat": "yyyyMMdd",
    "TimeFormat": "HHmmss",
    "DateFormatCustom": "",
    "TimeFormatCustom": "",
    "AddHeader": "true",
    "RecordFormat": "0",
    "Fill": "false"
}
API_PARAMS_DATE_FORMAT = "%d.%m.%Y"

DATE_FORMAT_SLASH = "%Y/%m/%d"
DATETIME_FORMAT_SLASH = "%Y/%m/%d %H:%M:%S"
DATETIME_FORMAT_DASH = "%Y-%m-%d %H:%M:%S"
DATETIME_FORMAT_IN_DB = DATETIME_FORMAT_DASH

FIRST_DAY_OF_PREDICTION_DATASET = (datetime.date.today() - datetime.timedelta(days=170)).strftime(DATE_FORMAT_SLASH)
FIRST_DAY_OF_PLOT = (datetime.date.today() - datetime.timedelta(days=7)).strftime(DATE_FORMAT_SLASH)

FIRST_DAY_IN_HISTORY = FIRST_DAY_OF_PREDICTION_DATASET
FIRST_DATETIME_IN_HISTORY = FIRST_DAY_OF_PREDICTION_DATASET + " 9:00:00"

MAX_LAG_FOR_PREDICTION = 9*100
DEPTH_OF_PREDICTION = 9*2 # Два дня
PREDICTION_STEP = timedelta(hours=1)
NEXT_DAY_AFTER_PREDICTION = datetime.datetime.today()+timedelta(hours=DEPTH_OF_PREDICTION+1)

MODULES_PARAM_GROUPS = {
    "initdb": ["db", "constants", "utils"],
    "start": ["db", "constants", "utils", "prediction"],
    "update": ["db", "constants", "utils"],
    "predict": ["db", "constants", "utils", "prediction"]
}
