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
    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.loc_x, player.loc_y)
        print room.intro_text()
        room.alter_player(player)
        if player.is_alive() and not player.victory:
            available_actions = room.available_actions()
            print '\tChoose from the following actions:'
            for action in available_actions:
                print '\t\t', action.name
            action_in = raw_input('\n\t> ').lower()
            # if action_in == help or other special actions?
            if action_in == 'exit' or action_in == 'quit':
                sys.exit("\n\tSEE YOU SPACE COWBOY...\n")
            for action in available_actions:
                if action_in == action.name.lower():
                    player.do_action(action)
                    break
            else:
                print "\n\tSorry, I don't know what that means."

if __name__ == "__main__":
    engine()
