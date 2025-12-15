class TransportCompany:
    def init(self, name):
        self.name = name
        self.vehicles = []
        self.clients = []
    
    def add_vehicle(self, vehicle):
        from task_2.transport.vehicle import Vehicle
        if not isinstance(vehicle, Vehicle):
            raise TypeError("Должен быть транспорт")
        self.vehicles.append(vehicle)
        return True
    
    def add_client(self, client):
        from task_1.transport.client import Client
        if not isinstance(client, Client):
            raise TypeError("Должен быть клиент")
        self.clients.append(client)
        return True
    
    def list_vehicles(self):
        return [str(v) for v in self.vehicles]
    
    def optimize_cargo_distribution(self):
        if not self.clients or not self.vehicles:
            return "Нет данных для оптимизации"
        
        # Сортируем: VIP сначала
        sorted_clients = sorted(self.clients, key=lambda x: not x.is_vip)
        
        # Сортируем транспорт по вместимости
        sorted_vehicles = sorted(self.vehicles, key=lambda x: x.capacity, reverse=True)
        
        results = []
        not_distributed = []
        
        for client in sorted_clients:
            loaded = False
            for vehicle in sorted_vehicles:
                try:
                    vehicle.load_cargo(client)
                    results.append(f"{client.name} → {vehicle.vehicle_id}")
                    loaded = True
                    break
                except:
                    continue
            
            if not loaded:
                not_distributed.append(client.name)
        
        # Считаем использованный транспорт
        used = len([v for v in sorted_vehicles if v.current_load > 0])
        
        return {
            "Распределено": results,
            "Не распределено": not_distributed,
            "Использовано транспорта": used
        }
    
    def str(self):
        return f"Компания: {self.name}, Транспорт: {len(self.vehicles)}, Клиенты: {len(self.clients)}"
