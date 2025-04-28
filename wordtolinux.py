class HumanToLinuxCommand:
    def __init__(self):
        self.commands = {
            "open": "xdg-open",
            "exit": "exit",
            "shutdown": "sudo shutdown -h now",
            "reboot": "sudo reboot",
            "sleep": "sleep",
            "ls": "ls -l",
            "mkdir": "mkdir",
            "rm": "rm",
            "cp": "cp",
            "mv": "mv",
            "cd": "cd"
        }

    def translate(self, human_input):
        words = human_input.split()
        command = ""
        for word in words:
            if word in self.commands:
                command += self.commands[word] + " "
            else:
                command += word + " "
        return command.strip()

def main():
    translator = HumanToLinuxCommand()
    while True:
        user_input = input("Enter a human language command (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        print(translator.translate(user_input))

if __name__ == "__main__":
    main()