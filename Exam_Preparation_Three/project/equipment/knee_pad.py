from projecttest.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    INITIAL_PROTECTION = 120
    INITIAL_PRICE = 15.0

    def __init__(self):
        super().__init__(KneePad.INITIAL_PROTECTION, KneePad.INITIAL_PRICE)

    def increase_price(self):
        self.price += self.price * 0.2
