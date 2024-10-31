import calendar


class DVD:
    def __init__(self, name, _id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = _id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, _id, name, date, age_restriction):
        date, month, year = [int(x) for x in date.split('.')]
        month_name = calendar.month_name[int(month)]

        return cls(name, _id, year, month_name, age_restriction)

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction " \
               f"{self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}"
