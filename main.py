from game.game import Game

if __name__ == '__main__':
    game = Game(disks=8)
    print('**************** INITIAL STATE *****************')
    game.print_game()
    print('**************** INITIAL STATE *****************')

    disks = game.get_disks
    origin_stack = game.get_origin_stack
    spare_stack = game.get_spare_stack
    target_stack = game.get_target_stack

    game.play_game(disks, origin_stack, spare_stack, target_stack)
