#Modules are like Dictionaries
# myfruits = {'kiwi': "I love Kiwi's"}
# print(myfruits['kiwi'])
# def kiwi():
#     print("I love Kiwi's")
#
# blueberry = "I taste great with oatmeal!"
# Classes are like Modules
class MyFruits(object):

    def __init__(self):
        self.blueberry = "Berry's in my smoothie"


    def kiwi(self):
        print("Green is good")


# Objects are Like Imports
thing = MyFruits()
thing.kiwi()
print(thing.blueberry)













