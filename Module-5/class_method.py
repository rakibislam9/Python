# class phone:

#     price = 19500

#     color = 'blue'

#     brand = 'Apple'


#     def call(self):
#         print('calling one person')

    
# myPhone = phone()

# myPhone.call()


class phone:

    price = 19500

    color = 'blue'

    brand = 'Apple'


    def call(self):
        print('calling one person')


    def send_message(self, message):
        print('sending message to one person')
    
myPhone = phone()

myPhone.call()

print(myPhone.send_message("Hello World"))