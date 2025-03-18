from Modules.Modules_Rooms import Rooms
from Modules.Modules_Story import Story



def main():
    #a dict with events that have happened in the story
    story_sequence = {
        "examined_bedroom": False,
        "has_bedroom_key": False,
        "packed_bag": False
    }

    #start in bedroom
    room = Rooms(story_sequence)
    current_room = room.current_room

    #start the story with intro
    story = Story()
    story.intro()
    while True:
        room.get_current_room(current_room)

        action = room.action_options()
        if action == 1:
            current_room = room.leave_room(current_room)

        elif action == 2:
            room.examine_room(current_room)

        elif action == 3:
            room.map()

        else:
            print("Invalid Entry")

if __name__ == "__main__":
    main()