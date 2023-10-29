
import os
import os.path


class Interface:

    def __init__(self):
        self.onExit = None
        self.commands = {}
        self.help = ""
        self.add_help("exit - exit from program.")
        self.add_help("help - print help strings.")
        self.add_help("cls - clear text in console.")

        self.add("help", self.info)

        def cls():
            os.system("cls")
            return ""
        self.add("cls", cls)

    def info(self):
        return self.help

    def add_help(self, text):
        self.help += text+"\n"

    def add(self, name, func):
        if not name in self.commands:
            self.commands[name] = func
        else:
            raise ValueError("Duplicate command!")

    def walk(self):
        print(self.help)
        while True:
            cmd = input("Enter Command >> ")
            if cmd == "exit":
                break
            elif cmd in self.commands:
                print(self.commands[cmd]())
            else:
                print("Command not found!")

        return self.onExit() if self.onExit is not None else ""
