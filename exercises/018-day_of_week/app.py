#Complete the function to return the number of day of the week for k'th day of year. 
def day_of_week(k):
    # -1 porque los días comienzan en 0 sunday
    # + 4 porque ese año comenzó en jueves que es el subíndice 4
    day = ((k - 1 + 4) % 7)
    return day



#Invoke function day_of_week with an interger between 0 and 6 (number for days of week)
print(day_of_week(1))
print(day_of_week(2))
print(day_of_week(7))
print(day_of_week(14))