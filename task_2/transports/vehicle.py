import random
import string

class Vehicle:
    """
    Базовый класс для транспортных средств
    
    Атрибуты:
        vehicle_id (str): Уникальный идентификатор
        capacity (float): Грузоподъемность в тоннах
        current_load (float): Текущая загрузка
        clients_list (list): Список загруженных клиентов
    """
    
    def init(self, capacity):
        """
        Инициализация транспортного средства
        
        Args:
            capacity (float): Грузоподъемность в тоннах
            
        Raises:
            ValueError: Если capacity невалидна
        """
        # Валидация грузоподъемности
        try:
            capacity = float(capacity)
            if capacity <= 0:
                raise ValueError("Грузоподъемность должна быть положительным числом")
            self.capacity = capacity
        except (ValueError, TypeError):
            raise ValueError("Грузоподъемность должна быть числом")
        
        # Генерация случайного ID (формат: VH-XXXXXX, где X - буква/цифра)
        random_id = ''.join(random.choices(
            string.ascii_uppercase + string.digits, 
            k=6
        ))
        self.vehicle_id = f"VH-{random_id}"
        
        self.current_load = 0.0
        self.clients_list = []
    
    def load_cargo(self, client):
        """
        Загрузка груза клиента
        
        Args:
            client: Объект клиента (должен быть экземпляром Client)
            
        Raises:
            TypeError: Если client не является объектом Client
            ValueError: Если превышена грузоподъемность
            
        Returns:
            bool: True если груз успешно загружен
        """
        # Импортируем Client здесь, чтобы избежать циклического импорта
        try:
            from task_1.transport.client import Client
        except ImportError:
            raise ImportError("Не удалось импортировать класс Client. Убедитесь, что task_1 существует.")
        
        # Валидация типа клиента
        if not isinstance(client, Client):
            raise TypeError(f"Объект должен быть экземпляром класса Client, получен {type(client).name}")
        
        # Проверка перегрузки
        new_load = self.current_load + client.cargo_weight
        if new_load > self.capacity:
            raise ValueError(
                f"Превышена грузоподъемность! "
                f"Текущая загрузка: {self.current_load:.1f}т, "
                f"добавить: {client.cargo_weight:.1f}т, "
                f"максимум: {self.capacity:.1f}т"
            )
        
        # Загрузка груза
        self.current_load = new_load
        self.clients_list.append(client)
        
        return True
    
    def get_available_capacity(self):
        """
        Возвращает оставшуюся грузоподъемность
        
        Returns:
            float: Доступная грузоподъемность
        """
        return self.capacity - self.current_load
    
    def str(self):
        """Строковое представление транспортного средства"""
        return (
            f"Транспорт {self.vehicle_id}: "
            f"грузоподъемность {self.capacity:.1f}т, "
            f"текущая загрузка {self.current_load:.1f}т, "
            f"свободно {self.get_available_capacity():.1f}т"
        )
    
    def repr(self):
        """Техническое строковое представление"""
        return f"Vehicle(vehicle_id='{self.vehicle_id}', capacity={self.capacity})"
