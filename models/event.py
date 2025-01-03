class Event:
    def __init__(self, name, date, city, country, description):
        self.name = name
        self.date = date
        self.city = city
        self.country = country
        self.description = description

    def to_dict(self):
        return {
            'name': self.name,
            'date': self.date,
            'city': self.city,
            'country': self.country,
            'description': self.description
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)