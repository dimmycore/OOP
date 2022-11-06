# программа которая позволит составить список гостей мероприятия.
# в класс «клиент» добавим метод, который будет возвращать информацию об имени, фамилии и городе клиента.
# затем создаём список, в который будут добавлены все клиенты, и выведем его в консоль.


class Client:
    def __init__(self, fist_name, second_name, city):
        self.first_name = fist_name
        self.second_name = second_name
        self.city = city

    def __str__(self):
        return f'{self.first_name} {self.second_name}. {self.city}.'

    def get_guest(self):
        return f'{self.first_name} {self.second_name},г. {self.city}'

client_1 = Client('Иван','Петров','Москва')
client_2 = Client('Владимир','Зайцев','Кострома')
client_3 = Client('Олеся','Янина','Новосибирск')

guest_list = [client_1, client_2, client_3]

for guest in guest_list:
    print(guest.get_guest())
