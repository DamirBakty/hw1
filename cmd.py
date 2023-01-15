from dataclasses import dataclass
import os


@dataclass()
class Terminal:
    current_path: str = os.path.abspath(os.sep)

    def ls(self):
        for n, directory in enumerate(os.scandir(self.current_path)):
            print(directory.name, end=" ")
            if n % 5 == 4:
                print()

    def cd(self, name):
        if name == '..':
            self.current_path = os.path.dirname(self.current_path)
            return
        path = os.path.join(self.current_path, name)
        if not os.path.exists(path):
            return "No such file or directory"
        if not os.path.isdir(path):
            return f"{name}: is Not a directory"
        self.current_path = os.path.join(self.current_path, name)
        return

terminal = Terminal()

while True:
    message = input(f'{terminal.current_path}: ').split()
    try:
        if len(message) == 1:
            command = message[0]
            if command == 'ls':
                terminal.ls()
                print()
            else:
                print("Command not found")
        if len(message) == 2:
            command = message[0]
            name = message[1]
            terminal.cd(name=name)
    except:
        print("Command not found")
