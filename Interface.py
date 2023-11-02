
import os
import os.path


class Interface:

    def __init__(self, donor=None):
        self.donor = donor
        self.onExit = None
        self.commands = {}
        self.help = "exit - exit from program.\n"


        self.add("help", self.info)
        self.add_help("print help strings.")
        self.add("cls", self.cls)
        self.add_help("clear text in console.")

    def cls(self):
        #os.system("cls")
        return "{0}".format(100*'\n')

    def info(self):
        return self.help

    def add_help(self, text):
        self.help += f"{list(self.commands.keys())[-1]} - "+text+"\n"

    def add(self, name, func=None):

        if not name in self.commands:
            if func is not None:
                self.commands[name] = func
            else:
                self.commands[name] = self.donor.__class__.__dict__[name]
        else:
            raise ValueError("Duplicate command!")

    def walk(self):
        print(self.help)
        while True:
            cmd = input("Enter Command >> ")
            if cmd == "exit":
                break
            elif cmd in self.commands:
                if self.commands[cmd].__name__ in self.__class__.__dict__:#якщо функція чужа запускаємо її з чужого об'єкту
                    print(self.commands[cmd]())
                else:
                    print(self.commands[cmd](self.donor))
            else:
                print("Command not found!")

        return self.onExit() if self.onExit is not None else ""


if __name__ == "__main__":
    ui = Interface()

    ui.walk()