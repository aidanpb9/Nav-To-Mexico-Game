from Modules.utils import clear
from Modules.utils import slow_print
from Modules.utils import text_buffer


class Story:

    @staticmethod
    def intro():
        clear()
        slow_print("You wake up to your phone playing a voicemail.")
        slow_print(f"It is your mother's voice: \"Don't be late!\"")
        slow_print("\"What is she talking about?\", I think")
        slow_print("Press enter to continue")
        text_buffer()


    @staticmethod
    def intro2():
        clear()
        slow_print("\"Ah I remember now...")
        slow_print("My parents are waiting for me at a resort in Mexico!")
        slow_print("I need to pack my bag, book a plane ticket, and head for the airport!\"")
        text_buffer()
        slow_print("GOALS: pack bag, book ticket, get in the car")
        text_buffer()

    @staticmethod
    def attic_discovery():
        clear()
        slow_print("\"The pc needs a password. I'll call dad to find out what the password is.\"")
        text_buffer()
        slow_print("As you step away from the pc, you notice an out of place painting leaning against the wall.")
        text_buffer()
        slow_print("You move the painting to reveal a tunnel to the attic. Let's explore!")
        text_buffer()
        slow_print("You crawl through the hole. There must be a light around here somewhere...")
        text_buffer()
        slow_print("\"Got it! I can see.\" ")
        text_buffer()



