import Modules.utils
from Modules.Modules_Rooms import Rooms
from Modules.Modules_Story import Story
from Modules.utils import text_buffer
from Modules.utils import slow_print


def main():
    story_sequence = {
        "current_room": "bedroom",
        "examined_bedroom": False,
        "has_bedroom_key": False,
        "unlocked_bedroom": False,
        "packed_bag": False,
        "has_car_keys": False
    }

    story = Story()

    start_game_input = input("Do you have an existing game? y/n ")
    if start_game_input == 'y':
        new_data = Modules.utils.load_game()
        if new_data:
            story_sequence = new_data
            slow_print("Game Loaded!")
            text_buffer()
        else:
            slow_print("No game found. Starting new game...Press Enter")
            text_buffer()
            story.intro()
    elif start_game_input == 'n':
        story.intro()

    room = Rooms(story_sequence)

    while True:
        room.get_current_room()

        action = room.action_options()
        if action == 1:
            story_sequence["current_room"] = room.leave_room()

        elif action == 2:
            room.examine_room()

        elif action == 3:
            room.map()

        elif action == 4:
            Modules.utils.save_game(story_sequence)
            text_buffer()

        else:
            print("Invalid Entry")
            text_buffer()

if __name__ == "__main__":
    main()