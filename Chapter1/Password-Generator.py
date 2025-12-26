# modules and global variables
from abc import ABC, abstractmethod
import string
import random



# create password generator abstract class
class PasswordGeneratorAbstract(ABC):

    @abstractmethod
    def generate_password(self,length = 8):
        pass


# create numeric password generator
class NumericPasswordGenerator(PasswordGeneratorAbstract):
    letters = string.digits
    def generate_password(self,length = 8):
        return "".join(str(random.choice(self.letters)) for _ in range(length))

# create letters password generator
class LettersPasswordGenerator(PasswordGeneratorAbstract):
    letters = string.ascii_letters

    def generate_password(self,length = 8):
        return "".join(str(random.choice(self.letters)) for _ in range(length))

# create mixed password generator
class MixedPasswordGenerator(PasswordGeneratorAbstract):
    letters = string.ascii_letters + string.digits
    def generate_password(self, length=8):
        return "".join(str(random.choice(self.letters)) for _ in range(length))


# first_list = ['a','b','c','d','e','f']
# second_list = [1,2,3,4,5,6]
# print(first_list + second_list)


# run the application
generator = MixedPasswordGenerator()
print(generator.generate_password())