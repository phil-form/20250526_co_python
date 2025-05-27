from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    
class StartMenuButton(Command):
    def execute(self):
        print("Open start memu")
        
        
class PreviousButton(Command):
    def execute(self):
        print("Go to previous page")