from abc import ABC, abstractmethod


class IStorage(ABC):
    @abstractmethod
    def list_blogs(self):
        pass

    @abstractmethod
    def add_blog(self, title, content):
        pass

    @abstractmethod
    def update_blog(self, id, title, content):
        pass

    @abstractmethod
    def delete_blog(self, id):
        pass