import random

def markov_chain_in_weather(wea):

    weather_type = ["晴天","雨天","多云"]

    weather_chance = {"晴天":["晴天","晴天","晴天","晴天","晴天","多云","多云","多云","多云","雨天"],
                      "雨天":["雨天","雨天","雨天","雨天","雨天","雨天","多云","多云","多云","晴天"],
                      "多云":["雨天","雨天","雨天","雨天","雨天","晴天","晴天","晴天","晴天","多云"]
                      }

    cho = random.choice(weather_chance[wea])

    return cho

def weather_forecast():

    while True:

        print("请输入当前的天气情况: ")
        print("1. 如果是\"晴天\", 请输入\"1\"")
        print("2. 如果是\"雨天\", 请输入\"2\"")
        print("3. 如果是\"多云\", 请输入\"3\"")

        inp = input("请输入: ")

        if inp == str(1):

            cho = markov_chain_in_weather("晴天")

            for i in range(1, 8):

                print("在 " + str(i) + " 天后可能是 " + cho + " 天")

                c = markov_chain_in_weather(cho)

                cho = c

            break

        elif inp == str(2):

            cho = markov_chain_in_weather("雨天")

            for i in range(1, 8):

                print("在 " + str(i) + " 天后可能是 " + cho + " 天")

                c = markov_chain_in_weather(cho)

                cho = c

            break

        elif inp == str(3):

            cho = markov_chain_in_weather("多云")

            for i in range(1, 8):

                print("在 " + str(i) + " 天后可能是 " + cho + " 天")

                c = markov_chain_in_weather(cho)

                cho = c

            break

        else:

            continue

if __name__=="__main__":

    weather_forecast()
