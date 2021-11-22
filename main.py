TICKETFAIR = 150
class Travel:
    def passenger1():
        Stations = ["Chennai Central Jn", "Tambaram","Arakonam", "Katpadi", "Jolarpet","Morappur", "Bommidi", "Salem Jn", "Erode Jn", "Tiruppur", "Coimbatore Jn"] 
        passengersList = ['Shriya','Ragu','Mukesh','Reshma','Vignesh','Rama']
        totalNoOfPassengers = len(passengersList)
        print("Total no of Passengers in the compartment are "+ str(totalNoOfPassengers))
        print("***********************************************")
        print("List of passengers")
        for index,i in enumerate(passengersList):
            print(index,i)
        print("\n")
        if "Ragu" in passengersList:
            print("Shriya's husband is inside")
        else:
            print("Shriya's husband is not inside")
        for station in Stations:
            if station == "Tambaram":
                passengersList.append("Dinesh")
                totalNoOfPassengers += 1
            if station == "Arakonam":
                passengersList.remove("Mukesh")
        print("List of passengers after updation")
        print("******************")
        for index,i in enumerate(passengersList):
            print(index,i)
        ticketfair = TICKETFAIR*totalNoOfPassengers
        print("Ticket fare for this family "+ str(ticketfair)) 
    passenger1() 
    print("\n")
    def passenger2():
        Stations = ["Chennai Central Jn", "Tambaram","Arakonam", "Katpadi", "Jolarpet","Morappur", "Bommidi", "Salem Jn", "Erode Jn", "Tiruppur", "Coimbatore Jn"] 
        data = {"Suriya":"Jyothika", "Ajith":"Shalini","Vijay":"Sangeetha"}
        totalNoOfPassengers = len(data)
        hubbies = []
        wives = []
        for station in Stations:
            if station == "Tambaram":
                data["Dhanush"] = "Aishwarya"
                totalNoOfPassengers += 1
        for keys, values in data.items():
            print(keys, values, end="\n")
        for keys in data.keys():
            hubbies.append(keys)
        print("Hubbies are " + str(hubbies))
        for values in data.values():
                wives.append(values)
        print("Wives are " + str(wives))
        ticketfair = TICKETFAIR*totalNoOfPassengers
        print("Ticket fare for this family "+ str(ticketfair))
    passenger2()
    print("\n")
    def ChennaiToCoimbatore(passengerList : list)-> list:
        stations = ["Coimbatore Jn", "Tiruppur", "Erode Jn", "Salem Jn", "Morappur", "Jolarpet", "Katpadi", "Arakonam", "Tambaram","ChennaiCentral"]
        print("The 4 friends in the train initially"+str(passengerList)) #Figuring all 4 friends at initial 
        totalNoOfPassengers = len(passengerList)
        for station in stations:
            if station == "Salem Jn":
                passengerList.append("naveenKumar")
                totalNoOfPassengers += 1
        print("The third friend is " + str(passengerList[2]))
        print("Total no of friends after the salem Junction "+ str(passengerList))
        ticketfair = TICKETFAIR*totalNoOfPassengers
        print("Ticket fare for this family "+ str(ticketfair))
    passengerList = ["dineshKumar","nawinKumar","mukeshKumar","vigeshKumar"] #List of passengers name
    ChennaiToCoimbatore(passengerList)
    favFoodOfEachPerson = ["Poori","Pongal","Chapati","Briyani","Idly"] #Considering the freinds having favorite food
    dictionary = dict(zip(passengerList,favFoodOfEachPerson))
    print(dictionary)
    def compartmentThree():
        passengers = ["Aravinth","Bharath","Chandru","Dinesh","Elangovan","Faraz","Ganesh","Hemanth","Illiyas","Jack","Kumar","Lokesh"]
        Stations = ["Chennai Central Jn", "Tambaram","Arakonam", "Katpadi", "Jolarpet","Morappur", "Bommidi", "Salem Jn", "Salem Market", "Erode Jn", "Tiruppur", "Coimbatore Jn"] 
        tup_Passengers = tuple(passengers)
        tup_Stations = tuple(Stations)
        return dict(zip(tup_Passengers,tup_Stations)) 
    print(compartmentThree())