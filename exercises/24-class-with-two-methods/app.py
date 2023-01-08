class MyClass:
    def __init__(self):
        self.cadena = ''


    def get_string(self):
        self.cadena = input('')

    
    def print_string(self):
        print(self.cadena.capitalize())


str_obj = MyClass()
str_obj.get_string()
str_obj.print_string()