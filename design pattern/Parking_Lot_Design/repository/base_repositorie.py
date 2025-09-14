class BaseRepository:
    def __init__(self):
        self.storage = {}

    def add(self, obj):
        self.storage[obj.id] = obj
        return obj

    def get_by_id(self, obj_id):
        return self.storage.get(obj_id)

    def get_all(self):
        return list(self.storage.values())

    def remove(self, obj_id):
        if obj_id in self.storage:
            del self.storage[obj_id]
            return True
        return False
