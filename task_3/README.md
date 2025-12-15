# Задание 3: Индивидуальное задание (Вариант 5)

## Описание задания

### Часть 1: Класс Train
**Создать класс Train (поезд), наследующий от Vehicle.**
- Дополнительные атрибуты:
    - number_of_cars – количество вагонов

### Часть 2: Класс Airplane
**Создать класс Airplane (самолет), наследующий от Vehicle.**
- Дополнительные атрибуты:
    - max_altitude – максимальная высота полета (в метрах)

### Часть 3: Класс TransportCompany
**Создать класс TransportCompany.**
- Атрибуты:
    - name – название компании,
    - vehicles – список транспортных средств (всех),
    - clients – список клиентов.
- Методы:
    - add_vehicle(vehicle) – добавляет транспортное средство (с валидацией),
    - list_vehicles() – возвращает список всех транспортных средств.
    - add_client(client) – добавляет клиента,
    - optimize_cargo_distribution() – распределяет грузы клиентов по транспортным средствам. С учетом следующего:
        - Грузы вип клиентов загружаются в первую очередь
        - Для загрузки нужно использовать как можно меньше транспорта

### Требования:
1. Все методы должны иметь валидацию данных
2. Наследование должно быть реализовано корректно
3. Оптимизация должна учитывать VIP статус и минимизировать количество транспорта

### Пример использования:
`python
from task_1.transport.client import Client
from task_2.transport.vehicle import Vehicle
from task_3.transport.train import Train
from task_3.transport.airplane import Airplane
from task_3.transport.transport_company import TransportCompany

# Создание компании
company = TransportCompany("Быстрая доставка")

# Добавление клиентов
client1 = Client("Иван", 5.0)
client2 = Client("Петр", 15.0, True)  # VIP
company.add_client(client1)
company.add_client(client2)

# Добавление транспорта
train = Train(30.0, 8)  # Грузоподъемность 30т, 8 вагонов
airplane = Airplane(50.0, 10000)  # Грузоподъемность 50т, высота 10000м
company.add_vehicle(train)
company.add_vehicle(airplane)

# Оптимизация распределения
results = company.optimize_cargo_distribution()
print(results)
