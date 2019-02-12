f = open("reservations")

for reservation in f:
    try:
        name, number = reservation.split(",")
        chairs_per_person = 50 / int(number)
        print("{} will get {} chairs per person".format(name, chairs_per_person))
    except ValueError:
        print("Invalid or missing data type for number")
    except ZeroDivisionError:
        print("Can not divide by zero m8")
    finally:
        pass
