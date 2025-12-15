from task_2.transport.vehicle import Vehicle

class Train(Vehicle):
    """
    Класс поезда, наследующий от Vehicle
    
    Дополнительный атрибут:
        number_of_cars (int): Количество вагонов
    """
    
    def init(self, capacity, number_of_cars):
        """
        Инициализация поезда
        
        Args:
            capacity (float): Грузоподъемность в тоннах
            number_of_cars (int): Количество вагонов
            
        Raises:
            ValueError: Если количество вагонов невалидно
        """
        # Вызываем конструктор родительского класса
        super().init(capacity)
        
        # Валидация количества вагонов
        try:
            number_of_cars = int(number_of_cars)
            if number_of_cars <= 0:
                raise ValueError("Количество вагонов должно быть положительным числом")
            self.number_of_cars = number_of_cars
        except (ValueError, TypeError):
            raise ValueError("Количество вагонов должно быть целым числом")
    
    def str(self):
        """Строковое представление поезда"""
        base_str = super().str()
        return f"🚂 Поезд {self.vehicle_id} ({self.number_of_cars} вагонов)\n   {base_str}"
    
    def repr(self):
        """Техническое строковое представление"""
        return f"Train(vehicle_id='{self.vehicle_id}', capacity={self.capacity}, number_of_cars={self.number_of_cars})"
