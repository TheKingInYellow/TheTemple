"""
GAME ENGINE
"""
import sys
import title
import world
from player import Player

def engine():
    intro = title.choose_title()
    raw_input(intro)
    world.load_tiles()
    player = Player()
    # room_old to make sure a new room intro is given
    room_old = None
    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.loc_x, player.loc_y)
        if room is not room_old:
            print room.intro_text()
            room_old = room
        room.alter_player(player)
        if player.is_alive() and not player.victory:
            available_actions = room.available_actions()
            # print '\tChoose from the following actions:'
            # for action in available_actions:
            #     print '\t\t', action.name[0]
            action_in = raw_input('\n\t> ').lower()
            # if action_in == help or other special actions?
            if action_in == 'exit' or action_in == 'quit':
                sys.exit("\n\tSEE YOU SPACE COWBOY...\n")

            for action in available_actions:
                # problem with user just hitting enter?
                if action_in in action.name:
                    player.do_action(action)
                    done = True
                    break
                else:
                    done = False
                    continue

            if not done:
                print "\n\tSorry, I don't know what that means..."



if __name__ == "__main__":
    engine()
