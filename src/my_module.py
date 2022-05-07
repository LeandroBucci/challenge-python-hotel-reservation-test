#This is an scalable solution to the hotel reservation challange
#Feel free to add more hotels, it will worked as intendent
#Dictionary struct: Key = Hotel's name, Classification, week day no vip price ,week day vip price, weekend day no vip price, weekend day vip price
#Made by: Leandro Bucci
hotel_dic = {
        "Lakewood": [3,110,80,90,80],
        "Bridgewood": [4,160,110,60,50],
        "Ridgewood": [5,220,100,150,40]
        }
week_days = ["mon","thur","wed","tues","fri"]
weekend_days = ["sat","sun"]

def get_cheapest_hotel(number):#DO NOT change the function's name
    vip_client = 0
    result_dic = {}
    counter_weekdays = 0
    counter_weekend = 0
    actual_price = 0
    actual_classification = 0 
    
    #Define if the client is vip or not
    if "Rewards" in number:
        vip_client = 1

    #Occurrence of week and weekend days
    for day in week_days:
        counter_weekdays = counter_weekdays + number.count(day)
        
    for day in weekend_days:
        counter_weekend = counter_weekend + number.count(day)

    #Calculates the price and adds to the results dictionary
    if(vip_client == 0):
        for key, value in hotel_dic.items():
            price = counter_weekdays * hotel_dic[key][1]
            price = price + (counter_weekend * hotel_dic[key][3])
            aux = (hotel_dic[key][0], price)
            result_dic[key] = aux

    elif(vip_client == 1):

        for key, value in hotel_dic.items():
            price = counter_weekdays * hotel_dic[key][2]
            price = price + (counter_weekend * hotel_dic[key][4])
            aux = (hotel_dic[key][0], price)
            result_dic[key] = aux

    #Defines the best price with the best classification and returns it's name
    for key, value in result_dic.items():
        if (actual_price == 0):
            actual_price = value[1]
            actual_classification = value[0]
            cheapest_hotel = key
            
        if(value[1] == actual_price):
            if(value[0] > actual_classification):
                actual_price = value[1]
                actual_classification = value[0]
                cheapest_hotel = key
        if(value[1] < actual_price):
                actual_price = value[1]
                actual_classification = value[0]
                cheapest_hotel = key

    return cheapest_hotel








