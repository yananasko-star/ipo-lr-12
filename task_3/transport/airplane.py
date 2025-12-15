from task_2.transport.vehicle import Vehicle

class Airplane(Vehicle):
    """
    Класс самолета, наследующий от Vehicle
    
    Дополнительный атрибут:
        max_altitude (float): Максимальная высота полета в метрах
    """
    
    def init(self, capacity, max_altitude):
        """
        Инициализация самолета
        
        Args:
            capacity (float): Грузоподъемность в тоннах
            max_altitude (float): Максимальная высота полета в метрах
            
        Raises:
            ValueError: Если высота невалидна
        """
        # Вызываем конструктор родительского класса
        super().init(capacity)
        
        # Валидация высоты полета
        try:
            max_altitude = float(max_altitude)
            if max_altitude <= 0:
                raise ValueError("Высота полета должна быть положительным числом")
            self.max_altitude = max_altitude
        except (ValueError, TypeError):
            raise ValueError("Высота полета должна быть числом")
    
    def str(self):
        """Строковое представление самолета"""
        base_str = super().str()
        return f"✈️ Самолет {self.vehicle_id} (макс. высота: {self.max_altitude:,}м)\n   {base_str}"
    
    def repr(self):
        """Техническое строковое представление"""
        return f"Airplane(vehicle_id='{self.vehicle_id}', capacity={self.capacity}, max_altitude={self.max_altitude})"
