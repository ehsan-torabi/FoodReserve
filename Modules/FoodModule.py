from random import randint
import pandas as pd
from pathlib import Path


class Food():
    global FOOD_DATA_DIR
    FOOD_DATA_DIR = Path(__file__).resolve(
    ).parent.parent.joinpath("Files\\food.csv")

    try:
        user_data_frame = pd.read_csv(FOOD_DATA_DIR)
    except:
        data = pd.DataFrame(columns=['Name', 'Price',
                                     'ID'])
        data.to_csv(FOOD_DATA_DIR, mode='w', index=False)

    def addFood(foodName, foodPrice):
        foodDataFrame = pd.read_csv(FOOD_DATA_DIR)
        foodList = [(x[1])[0] for x in foodDataFrame.iterrows()]
        randomID = len(foodList)+randint(0, 18)+10+randint(0, 10)
        if foodName not in foodList:
            data = pd.DataFrame(
                {'Name': [foodName], 'Price': [foodPrice], 'ID': [randomID]})
            data.to_csv(FOOD_DATA_DIR, mode='a', index=False, header=False)
            return

    def removeFood(foodID):
        foodDataFrame = pd.read_csv(FOOD_DATA_DIR)
        foodDataFrame[foodDataFrame['ID'] == int(foodID)] = pd.DataFrame(
            {'Name': [], 'Price': [], 'ID': []})
        foodDataFrame = foodDataFrame.dropna()
        foodDataFrame.to_csv(FOOD_DATA_DIR, index=False, float_format='%.0f')

    def foodList():
        foodDataFrame = pd.read_csv(FOOD_DATA_DIR)
        foodName = [(x[1])[0] for x in foodDataFrame.iterrows()]
        foodPrice = [(x[1])[1] for x in foodDataFrame.iterrows()]
        foodID = [(x[1])[2] for x in foodDataFrame.iterrows()]
        result = []
        for i in range(len(foodID)):
            result.append(
                f'{foodID[i]}: {foodName[i]}                {foodPrice[i]}تومان')
        return result

    def foodNameList():
        foodDataFrame = pd.read_csv(FOOD_DATA_DIR)
        name = [(x[1])[0] for x in foodDataFrame.iterrows()]
        price = [(x[1])[1] for x in foodDataFrame.iterrows()]
        result = []
        for i in range(len(name)):
            result.append(f'{name[i]} قیمت {price[i]}تومان')
        return result

    def listFaHeader():
        foodDataFrame = pd.read_csv(FOOD_DATA_DIR)
        data = pd.DataFrame(
            {'کد غذا': foodDataFrame['ID'], 'نام غذا': foodDataFrame['Name'],  "قیمت": foodDataFrame['Price']})
        return data

    def foodData(foodName):
        # This func get food name and return a row by dataframe type
        foodDataFrame = pd.read_csv(FOOD_DATA_DIR)
        return pd.DataFrame(Fdata[foodDataFrame['Name'] == foodName])

    def getPrice(food):
        foodDataFrame = pd.read_csv(FOOD_DATA_DIR)
        if food != '':
            indexs = foodDataFrame[foodDataFrame['Name'] == food].index
            return foodDataFrame.at[indexs[0], 'Price']

