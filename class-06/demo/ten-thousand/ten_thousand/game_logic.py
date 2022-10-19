class GameLogic:
    pass

    @staticmethod
    def roll_dice(dice):
        import random
        # dice_list = [1, 2, 3, 4, 5, 6]
        # return_tuple = tuple(random.choice(dice_list))
        number_list = []
        for num in range(dice):
            roll = random.randint(1, 6)
            number_list.append(roll)
        number_list = tuple(number_list)
        return number_list


if __name__ == '__main__':
    print('ran directly as a module')
    # to execute run: python -m ten_thousand.game_logic
    # Executing without the -m "can" have a different import structure in certain aspects when doing multiple imports
    # from different folders
