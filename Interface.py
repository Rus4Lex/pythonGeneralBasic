
import os
import os.path


class Interface:

    def __init__(self, donor=None):
        self.donor = donor
        self.onExit = None
        self.commands = {}
        self.help = ""
        self.add_help("exit - exit from program.")
        self.add_help("help - print help strings.")
        self.add_help("cls - clear text in console.")

        self.add("help", self.info)
        self.add("cls", self.cls)

    def cls(self):
        os.system("cls")
        return ""

    def info(self):
        return self.help

    def add_help(self, text):
        self.help += text+"\n"

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