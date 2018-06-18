from snipslms.entities.entity import Entity


class Album(object):
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_dict(cls, a_dict):
        album = cls(
            name=a_dict['name']
        )

        return album


Entity.register(Album)
