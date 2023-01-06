

import pandas as pd
from Modules.FoodModule import Food
from pathlib import Path


class User:
    global USER_DATA_DIR
    USER_DATA_DIR = Path(__file__).resolve(
    ).parent.parent.joinpath('Files\\data.csv')

    try:
        user_data_frame = pd.read_csv(USER_DATA_DIR)

    except:
        data = pd.DataFrame(columns=['Name', 'Family',
                                     'ID', 'Password', 'Balance', 'Foods'])
        data.to_csv(USER_DATA_DIR, mode='w', index=False)

    def register(name, family, password, ID):
        user_data_frame = pd.read_csv(USER_DATA_DIR)
        ID_list = [(x[1])[2] for x in user_data_frame.iterrows()]

        if int(ID) not in ID_list:
            data = pd.DataFrame({'Name': [name], 'Family': [family],
                                 'ID': [ID], 'Password': [password], 'Balance': 10000, 'Foods': ['بدون رزرو']})
            data.to_csv(USER_DATA_DIR, mode='a', index=False, header=False)

            return 'successful'

    def login(username, password):
        user_data_frame = pd.read_csv(USER_DATA_DIR)
        username = int(username) if username.isdigit() else username
        user_info = list(user_data_frame.loc[user_data_frame[user_data_frame['ID'] ==
                                                             username].index, 'Password'])

        if username == 'admin' and password == 'admin':
            return ('admin_login')
        elif password.isdigit():
            if int(password) in user_info:
                return ('successful')
        elif password in user_info:
            return ('successful')

        else:
            return ('failed')

    def remove(ID):
        user_data_frame = pd.read_csv(USER_DATA_DIR)
        user_data_frame[user_data_frame['ID'] == ID] = pd.DataFrame(
            {'Name': [], 'Family': [],
             'ID': [], 'Password': [], 'Balance': [], 'Foods': []})
        user_data_frame = user_data_frame.dropna()
        user_data_frame.to_csv(USER_DATA_DIR, index=False, float_format='%.0f')

    def getInfo_by_ID(ID):
        user_data_frame = pd.read_csv(USER_DATA_DIR)

        return user_data_frame[user_data_frame['ID'] == ID]

    def chargeBalance(value, ID):
        user_data_frame = pd.read_csv(USER_DATA_DIR)
        user_data_frame.loc[user_data_frame[user_data_frame['ID']
                                            == ID].index, 'Balance'] += value
        user_data_frame.to_csv(USER_DATA_DIR, index=False)

    def getBalance(ID):
        user_data_frame = pd.read_csv(USER_DATA_DIR)
        if ID != '':
            user_info = user_data_frame[user_data_frame['ID'] == int(ID)].index
            balance = user_data_frame.at[user_info[0], 'Balance']
            return int(balance)

    def getName_by_ID(ID):
        user_data_frame = pd.read_csv(USER_DATA_DIR)
        if ID != '':
            user_info = user_data_frame[user_data_frame['ID'] == int(ID)].index
            return user_data_frame.at[user_info[0], 'Name']

    def getID_by_Name(name):
        user_data_frame = pd.read_csv(USER_DATA_DIR)
        if name != '':
            user_info = user_data_frame[user_data_frame['Name'] == name].index
            return int(user_data_frame.at[user_info[0], 'ID'])

    def getNameAndFamily_by_ID(ID):
        user_data_frame = pd.read_csv(USER_DATA_DIR)
        if ID != '':
            user_info = user_data_frame[user_data_frame['ID'] == int(ID)].index
            name = user_data_frame.at[user_info[0], 'Name']
            family = user_data_frame.at[user_info[0], 'Family']
            return f'{name} {family}'

    def getFoodReserve_by_ID(ID):
        user_data_frame = pd.read_csv(USER_DATA_DIR)
        if ID != '':
            user_info = user_data_frame[user_data_frame['ID'] == int(ID)].index
            return user_data_frame.at[user_info[0], 'Foods']

    def userFoodReserve(userID, food):
        # this func get userID and foodName then manage reserve
        user_data_frame = pd.read_csv(USER_DATA_DIR)
        user_info = User.getInfo_by_ID(userID)
        user_food_list = [x for x in user_info['Foods']]
        if food in user_food_list:
            return 'food reserve'
        else:
            user_info = User.getInfo_by_ID(userID)
            data = pd.DataFrame(user_info)
            if User.getBalance(userID) < Food.getPrice(food):
                return 'BalanceNotEnough'
            else:
                data["Balance"] = User.getBalance(userID) - Food.getPrice(food)
                user_data_frame.update(data)
                data["Foods"] = food

                user_data_frame.update(data)
                user_data_frame.to_csv(
                    USER_DATA_DIR, index=False, float_format='%.0f')

    def getUsersFaHeader() -> pd.DataFrame:
        # this func return a dataframe with persian header
        user_data_frame = pd.read_csv(USER_DATA_DIR)
        data = pd.DataFrame({"نام": user_data_frame['Name'], "نام خانوادگی": user_data_frame['Family'],
                             "کدملی": user_data_frame['ID'], 'رمز ورود': user_data_frame['Password'], "موجودی": user_data_frame['Balance']})
        return data

    def getUsersFoodReserve():
        # this function return a list contain reserved food users
        user_data_frame = pd.read_csv(USER_DATA_DIR)
        user_data_frame = user_data_frame[user_data_frame['Foods']
                                          != 'بدون رزرو']
        dataframe = pd.DataFrame({'غذای رزور شده': user_data_frame['Foods'], "نام": user_data_frame['Name'], "نام خانوادگی": user_data_frame['Family']
                                  })
        return dataframe

    def getUsersList() -> list:
        Data = pd.read_csv(USER_DATA_DIR)
        return [(x[1])[0] for x in Data.iterrows()]
