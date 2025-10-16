class OnlineSalesRegisterCollector:
    def __init__(self) -> None:
        self.__name_items: list[str] = []
        self.__number_items: int = 0
        self.__item_price: dict[str, float] = {"чипсы": 50, "кола": 100, "печенье": 45, "молоко": 55, "кефир": 70}
        self.__tax_rate: dict[str, int | float | str] = {"чипсы": 20, "кола": 20, "печенье": 20, "молоко": 10, "кефир": 10}

    # 1. Геттеры
    @property
    def name_items(self) -> list[str]:
        return self.__name_items

    @property
    def number_items(self) -> int:
        return self.__number_items

    # 2. Добавить товар
    def add_item_to_cheque(self, name: str) -> None:
        if not isinstance(name, str) or not (1 <= len(name) <= 40):
            raise ValueError(
                "Нельзя добавить товар, если в его названии нет символов или их больше 40"
            )
        if name not in self.__item_price:
            raise NameError("Позиция отсутствует в товарном справочнике")
        self.__name_items.append(name)
        self.__number_items += 1

    # 3. Удалить товар
    def delete_item_from_check(self, name: str) -> None:
        if name not in self.__name_items:
            raise NameError("Позиция отсутствует в чеке")
        self.__name_items.remove(name)
        self.__number_items -= 1

    # 4. Сумма по чеку (скидка 10% при >10 позициях)
    def check_amount(self) -> float:
        amount = sum(self.__item_price[n] for n in self.__name_items)
        if len(self.__name_items) > 10:
            amount *= 0.9
        return amount

    # 5. НДС 20%
    def twenty_percent_tax_calculation(self) -> float:
        base = sum(
            self.__item_price[n]
            for n in self.__name_items
            if self.__tax_rate.get(n) in (20, 0.2, "20%")
        )
        if len(self.__name_items) > 10:
            base *= 0.9
        return base * 0.2

    # 6. НДС 10%
    def ten_percent_tax_calculation(self) -> float:
        base = sum(
            self.__item_price[n]
            for n in self.__name_items
            if self.__tax_rate.get(n) in (10, 0.1, "10%")
        )
        if len(self.__name_items) > 10:
            base *= 0.9
        return base * 0.1

    # 7. Общая сумма налогов
    def total_tax(self) -> float:
        return self.ten_percent_tax_calculation() + self.twenty_percent_tax_calculation()

    # 8. Вернуть телефон покупателя
    @staticmethod
    def get_telephone_number(telephone_number: int) -> str:
        if not isinstance(telephone_number, int):
            raise ValueError("Необходимо ввести цифры")
        digits = str(telephone_number)
        if len(digits) != 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        return f"+7{digits}"
