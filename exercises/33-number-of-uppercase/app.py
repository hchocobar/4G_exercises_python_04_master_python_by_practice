def count_upper_lower(text):
    my_dict = {"upper_case": 0, "lower_case": 0}
    for char in text:
        if char.isupper():
            my_dict["upper_case"] += 1
        elif char.islower():
            my_dict["lower_case"] += 1
        else:
            pass
    return my_dict


song = "Imagine there's no heaven It's easy if you try No hell below us Above us, only sky"
print(count_upper_lower(song))
