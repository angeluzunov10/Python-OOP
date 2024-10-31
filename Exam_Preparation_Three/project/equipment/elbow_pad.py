from projecttest.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    INITIAL_PROTECTION = 90
    INITIAL_PRICE = 25.0

    def __init__(self):
        super().__init__(ElbowPad.INITIAL_PROTECTION, ElbowPad.INITIAL_PRICE)

    def increase_price(self):
        self.price += self.price * 0.1
