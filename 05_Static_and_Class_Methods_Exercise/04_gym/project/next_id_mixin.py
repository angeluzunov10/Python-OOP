class NextIdMixin:
    id = -1         # Not needed, only to avoid warnings

    @classmethod
    def get_next_id(cls):
        return cls.id

    @classmethod
    def increment_id(cls):
        cls.id += 1
