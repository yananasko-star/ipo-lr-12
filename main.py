
main.py - Задание 4
Главное меню системы транспортной логистики
"""

def main():
    print("=" * 50)
    print("СИСТЕМА ТРАНСПОРТНОЙ ЛОГИСТИКИ")
    print("=" * 50)
    
    try:
        # Импортируем все классы
        from task_1.transport.client import Client
        from task_2.transport.vehicle import Vehicle
        from task_3.transport.train import Train
        from task_3.transport.airplane import Airplane
        from task_3.transport.transport_company import TransportCompany
        
        print("Тестовый пример работы системы:")
        print("-" * 30)
        
        # 1. Создаем компанию
        company = TransportCompany("Экспресс-Доставка")
        print(f"✓ Создана компания: {company.name}")
        
        # 2. Добавляем клиентов
        client1 = Client("Иван Иванов", 5.0)
        client2 = Client("Петр Петров", 12.0, True)  # VIP
        client3 = Client("Анна Сидорова", 8.0)
        
        for client in [client1, client2, client3]:
            company.add_client(client)
            vip = " (VIP)" if client.is_vip else ""
            print(f"✓ Добавлен клиент: {client.name}{vip}, груз: {client.cargo_weight}т")
        
        # 3. Добавляем транспорт
        truck = Vehicle(15.0)
        train = Train(30.0, 10)
        plane = Airplane(50.0, 10000)
        
        for transport in [truck, train, plane]:
            company.add_vehicle(transport)
            print(f"✓ Добавлен транспорт: {transport}")
        
        print("\n" + "=" * 50)
        print("ОПТИМИЗАЦИЯ РАСПРЕДЕЛЕНИЯ ГРУЗОВ")
        print("=" * 50)
        
        # 4. Оптимизируем распределение
        result = company.optimize_cargo_distribution()
        
        print("\nРезультаты:")
        print(f"Использовано транспорта: {result.get('Использовано транспорта', 0)}")
        
        if result.get('Распределено'):
            print("\nРаспределенные грузы:")
            for item in result['Распределено']:
                print(f"  ✓ {item}")
        
        if result.get('Не распределено'):
            print("\nНе распределено:")
            for item in result['Не распределено']:
                print(f"  ✗ {item}")
        
        print("\n" + "=" * 50)
        print("ПРОГРАММА УСПЕШНО ВЫПОЛНЕНА!")
        print("=" * 50)
        
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        print("Проверьте, что все задания выполнены правильно.")

if name == "main":
    main()
