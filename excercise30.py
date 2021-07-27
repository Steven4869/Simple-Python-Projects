class string():
    def __init__(self):
        self.string = ""

    def get(self):
        self.string = input("Enter string: ")

    def put(self):
        print("String is:")
        print(self.string)


obj = string()
obj.get()
obj.put()