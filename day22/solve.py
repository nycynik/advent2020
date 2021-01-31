import copy

# with hash instead of array


def get_data():

    data_file = open("data.txt")
    # data_file = open("test.txt")

    player = None
    players = []
    cards = {}
    for idx, val in enumerate(data_file):
        if player == None:
            # find the player
            if val is not "":
                # player = int(val.strip().split(' ')[1][:-1])
                player = (val.strip())[:-1]
                players.append(player)
                cards[player] = []
                continue
        else:
            if val.strip() == '':
                player = None
                continue
            else:
                # add cards
                cards[player].append(int(val))

    data_file.close()

    print(f"added {len(players)} players.\n")

    return (players, cards)


def check_data(data):
    players = data[0]
    cards = data[1]

    players_in_game = copy.deepcopy(players)

    winner = None
    game_round = 1
    while winner == None:
        print(f'\n-- Round {game_round} --')

        # main game
        for p in players_in_game:
            print(f"{p}'s deck: {cards[p]}")

        best_card = -1
        round_winner = None
        winnin_stack = []
        for p in players_in_game:
            card_played = cards[p].pop(0)
            if card_played > best_card:
                best_card = card_played
                round_winner = p
            winnin_stack.append(card_played)
            print(f"{p} plays {card_played}")

        print(f"{round_winner} wins the round!")
        winnin_stack.sort(reverse=True)
        cards[round_winner].extend(winnin_stack)

        game_round += 1

        for p in players_in_game:
            if len(cards[p]) == 0:
                winner = 1
                break

        # if game_round > 30:
        #     break

    # determine winner
    winner = None
    print('\n== Post-game results ==')
    for p in players_in_game:
        print(f'{p}\'s deck: {cards[p]}')
        if len(cards[p]) > 0:
            winner = p

    # calculate score
    mux = len(cards[winner])
    score = 0
    for c in cards[winner]:
        score += c * mux
        mux -= 1

    print(f'\nWinner is {winner} with a score of {score}')

    return p


def main():
    data = get_data()
    check_data(data)


main()
