#Task 1
# temperature = input("Please input the current temperature in Farenheit")

#Task 2

def farenheitToCelcius(temp):
    return (temp - 32) * 5/9

def celciusToFarenheit(temp):
    return (temp * 9/5) + 32

def mainLoop():
    while True:
        completed = 0
        print("Please choose to convert farenheit or celcius:\n(1) Farenheit\n(2) Celcius ")
        temp_metric = input("Metric:")
        print("Please input the current temperature: ")
        user_input = input("Temperature:")
        try:
            metric = int(temp_metric)
            temperature = float(user_input)
        except ValueError:
            print("Please make sure to input only numbers!")
        except:
            print("An unknown error has occured.")
        else:
            #Task 3
            converted_temp = ""
            first_metric = ""
            converted_metric = ""

            if metric == 1:
                first_metric = "F"
                converted_metric = "C"
                converted_temp = farenheitToCelcius(temperature)
            elif metric == 2:
                first_metric = "C"
                converted_metric = "F"
                converted_temp = celciusToFarenheit(temperature)
            
            if converted_temp != "":
                print(f"{temperature}{first_metric} is equal to {converted_temp}{converted_metric}")
                completed = 1
            else:
                print("Please choose either 1 or 2 as a metric!")
        finally:
            #Task 4
            if completed == 1:
                print("Thank you for using the weather forecast application!")
            else:
                print("Please try again!")
            print("--------------------------")
            
mainLoop()