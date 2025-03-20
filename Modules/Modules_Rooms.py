from Modules.utils import text_buffer, slow_print
from Modules.utils import clear
from Modules.Modules_Story import Story

class Rooms:

    def __init__(self, story_sequence):
        self.story_sequence = story_sequence


    @staticmethod
    def action_options() -> int:
        user_action = int(input("1-leave room     2-examine room     3-map     4-save game\n"))
        return user_action


    def get_current_room(self):
        clear()
        slow_print(f"You are in the {self.story_sequence["current_room"]}.")


    def get_adj_rooms(self):
        adjacent_rooms = {
            "bedroom": ["living_room"],
            "living_room": ["bedroom", "kitchen", "entrance_room", "upstairs_room"],
            "kitchen": ["living_room", "garage"],
            "garage": ["kitchen"],
            "upstairs_room": ["living_room", "attic"],
            "attic": ["upstairs_room"],
            "entrance_room": ["living_room"]
        }
        return adjacent_rooms.get(self.story_sequence["current_room"], [])


    def leave_room(self) -> str:
        if self.story_sequence["has_bedroom_key"]:
            if not self.story_sequence["unlocked_bedroom"]:
                clear()
                slow_print("You used the bedroom key to unlock the door!")
                text_buffer()
                self.story_sequence["unlocked_bedroom"] = True
            adjacent_rooms = self.get_adj_rooms()
            clear()
            room_select = input(f"What room? {adjacent_rooms}").strip()
            self.story_sequence["current_room"] = room_select
        else:
            clear()
            slow_print("Seems the bedroom door is locked.")
            slow_print("I'll look around for a key...")
            text_buffer()
        return self.story_sequence["current_room"]


    def examine_room(self):
        examine_room = f"examine_{self.story_sequence["current_room"]}"
        call_examine = getattr(self, examine_room)
        call_examine()


    def examine_bedroom(self):
        clear()

        if not self.story_sequence["examined_bedroom"]:
            Story.intro2()
            self.story_sequence["examined_bedroom"] = True

        if not self.story_sequence["packed_bag"]:
            clear()
            slow_print("There is a window, a suitcase, and a dresser.")
            slow_print("What would you like to examine?")
            user_action = int(input("1-window\t2-suitcase\t 3-dresser\t4-stop examining\n"))

            while user_action !=4:
                if user_action == 1:
                    clear()
                    slow_print("A nice day outside, I should pack my suitcase for Mexico!")
                    text_buffer()

                elif user_action == 2:
                    clear()
                    pack_case_input = input("Will you pack your suitcase? y/n ")
                    if pack_case_input == 'y':
                        clear()
                        slow_print("Suitcase all packed!")
                        text_buffer()
                        self.story_sequence["packed_bag"] = True
                        return self.examine_bedroom()
                    else:
                        clear()
                        slow_print("You did not pack your suitcase.")
                        text_buffer()   #check this change

                elif user_action == 3:
                    self.examine_bedroom_dresser()

                elif user_action == 4:
                    break
                clear()
                slow_print("What would you like to examine?")
                user_action = int(input("1-window\t2-suitcase\t 3-dresser\t4-stop examining\n"))

        else:
            clear()
            slow_print("There is a window and a dresser.")
            slow_print("What would you like to examine?")
            user_action = int(input("1-window\t 2-dresser\t3-stop examining\n"))

            while user_action != 3:
                if user_action == 1:
                    clear()
                    slow_print("It's a lovely day outside!")
                    text_buffer()

                elif user_action == 2:
                    self.examine_bedroom_dresser()

                elif user_action == 3:
                    break
                clear()
                slow_print("What would you like to examine?")
                user_action = int(input("1-window\t 2-dresser\t 3-stop examining\n"))


    def examine_bedroom_dresser(self):
        clear()
        if self.story_sequence["has_bedroom_key"]:
            slow_print("You check the dresser, but don't find anything.")
            text_buffer()
        else:
            slow_print("There seems to be a key hidden in the sock drawer!")
            takes_key = input("Will you take it? y/n ")

            if takes_key == 'y':
                clear()
                self.story_sequence["has_bedroom_key"] = True
                slow_print("Acquired the bedroom key.")
                text_buffer()
            else:
                clear()
                slow_print("You did not grab the key.")
                text_buffer()


    @staticmethod
    def examine_living_room():
        clear()
        slow_print("There is a couch and a tv in the living room.")
        slow_print("What would you like to examine?")
        user_action = int(input("1-couch     2-tv     3-stop examining\n"))

        while user_action != 3:
            if user_action == 1:
                clear()
                slow_print("The couch is quite comfortable.")
                text_buffer()
            elif user_action == 2:
                clear()
                slow_print("The tv isn't working right now.")
                text_buffer()
            elif user_action == 3:
                break
            clear()
            slow_print("What would you like to examine?")
            user_action = int(input("1-couch     2-tv     3-stop examining\n"))



    @staticmethod
    def examine_kitchen():
        clear()
        slow_print("Examining kitchen")
        text_buffer()

    @staticmethod
    def examine_garage():
        clear()
        slow_print("Examining garage")
        text_buffer()


    def examine_entrance_room(self):
        if self.story_sequence["has_car_keys"]:
            clear()
            slow_print("The hall is well decorated.")
            text_buffer()
        else:
            clear()
            slow_print("There is a table with some keys on it.")
            take_keys_input = input("Will you take the keys? y/n ")

            if take_keys_input == 'y':
                clear()
                self.story_sequence["has_car_keys"] = True
                slow_print("Acquired car keys.")
                text_buffer()
            else:
                clear()
                slow_print("You did not take the keys")
                text_buffer()

    @staticmethod
    def examine_upstairs_room():
        clear()
        slow_print("Examining upstairs room")
        text_buffer()

    @staticmethod
    def examine_attic():
        clear()
        slow_print("Examining attic")
        text_buffer()

    @staticmethod
    def map():
        clear()
        slow_print("Here is a map of the house:\n")
        print("             entrance")
        print("                 |    ")
        print("bedroom-----living room-----kitchen-----garage")
        print("                 |    ")
        print("             upstairs-----attic")
        text_buffer()