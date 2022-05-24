class Lives:
    def __init__(self):
        self.lives = 4
        self.jumper = ""

    def life_value(self, lives):
        match lives:
            case 4:
                self.jumper = " _____\n/_____\ \n\     / \n \   / \n   O \n  /|\ \n  / \ \n \n^^^^^^^^"
            case 3:
                self.jumper = "/_____\ \n\     / \n \   / \n   O \n  /|\ \n  / \ \n \n^^^^^^^^"
            case 2:
                self.jumper = "\     / \n \   / \n   O \n  /|\ \n  / \ \n \n^^^^^^^^"
            case 1:
                self.jumper = " \   / \n   O \n  /|\ \n  / \ \n \n^^^^^^^^"
            case 0:
                self.jumper = "   X \n  /|\ \n  / \ \n \n^^^^^^^^"

