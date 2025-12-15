class Client:
    """
    Класс для представления клиента транспортной компании
    
    Атрибуты:
        name (str): Имя клиента
        cargo_weight (float): Вес груза в тоннах
        is_vip (bool): VIP статус клиента
    """
    
    def init(self, name, cargo_weight, is_vip=False):
        """
        Инициализация клиента с валидацией данных
        
        Args:
            name (str): Имя клиента
            cargo_weight (float): Вес груза
            is_vip (bool, optional): VIP статус. По умолчанию False.
            
        Raises:
            ValueError: Если данные невалидны
        """
        # Валидация имени
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Имя клиента должно быть непустой строкой")
        self.name = name.strip()
        
        # Валидация веса груза
        try:
            cargo_weight = float(cargo_weight)
            if cargo_weight <= 0:
                raise ValueError("Вес груза должен быть положительным числом")
            self.cargo_weight = cargo_weight
        except (ValueError, TypeError):
            raise ValueError("Вес груза должен быть числом")
        
        # Валидация VIP статуса
        if not isinstance(is_vip, bool):
            raise ValueError("VIP статус должен быть True или False")
        self.is_vip = is_vip
    
    def str(self):
        """Строковое представление клиента"""
        vip_status = "VIP" if self.is_vip else "обычный"
        return f"Клиент: {self.name}, Груз: {self.cargo_weight}т, Статус: {vip_status}"
    
    def repr(self):
        """Техническое строковое представление"""
        return f"Client(name='{self.name}', cargo_weight={self.cargo_weight}, is_vip={self.is_vip})"
