class Tag:
    def __init__(self, id, name):
        self.name = name
        self.id = id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Tag ID: {self.id}, {self.name}"
