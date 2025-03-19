from Modules.utils import clear
from Modules.utils import slow_print
from Modules.utils import text_buffer

class Story:

    @staticmethod
    def intro():
        clear()
        slow_print("You wake up to your phone playing a voicemail.")
        slow_print(f"It is your mother's voice: \"Don't be late!\"")
        slow_print("What is she talking about?")
        slow_print("Press enter to continue", end="")
        text_buffer()
        clear()


    @staticmethod
    def intro2():
        clear()
        slow_print("Ah I remember now...")
        slow_print("My parents are waiting for me at a resort in Mexico!")
        slow_print("I need to pack my bag, book a plane ticket, and head for the airport!")
        text_buffer()
        slow_print("GOALS: pack bag, book ticket, get in the car")
        text_buffer()
        clear()



