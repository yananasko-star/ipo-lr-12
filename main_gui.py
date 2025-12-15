dpg.delete_item(dpg.get_item_parent("type_input"))
                except Exception as e:
                    print(f"Ошибка: {e}")
            
            dpg.add_button(label="Сохранить", callback=save)
    
    def distribute(self):
        if not self.clients or not self.vehicles:
            dpg.set_value("results_text", "Нет данных для распределения")
            return
        
        result = self.company.optimize_cargo_distribution()
        if isinstance(result, dict):
            text = "Распределено:\n"
            for item in result.get("Распределено", []):
                text += f"✓ {item}\n"
            for item in result.get("Не распределено", []):
                text += f"✗ {item}\n"
            dpg.set_value("results_text", text)
        else:
            dpg.set_value("results_text", str(result))
    
    def update_display(self):
        # Клиенты
        clients_text = ""
        for client in self.clients:
            vip = " (VIP)" if client.is_vip else ""
            clients_text += f"{client.name}: {client.cargo_weight}т{vip}\n"
        dpg.set_value("clients_text", clients_text)
        
        # Транспорт
        vehicles_text = ""
        for vehicle in self.vehicles:
            vehicles_text += f"{vehicle}\n"
        dpg.set_value("vehicles_text", vehicles_text)
    
    def export(self):
        # Простой экспорт
        with open("результаты.txt", "w", encoding="utf-8") as f:
            f.write("Результаты распределения:\n")
            for client in self.clients:
                f.write(f"Клиент: {client.name}\n")
        print("Экспорт завершен")

if name == "main":
    gui = SimpleGUI()
    gui.run()
