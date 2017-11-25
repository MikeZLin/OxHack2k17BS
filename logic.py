import numpy as np


def cell_prob(gamestate):
    board = np.asarray(gamestate['OppBoard'])
    ships = ['S0', 'S1', 'S2', 'S3', 'S4']
    ship_len = [5, 4, 3, 3, 2]
    active_len = []
    for i in range(5):
        if len(np.argwhere(board == ships[i])):
            print(ships[i], ':', ship_len[i])
        else:
            active_len.append(ship_len[i])
    mask = []
    hit_mask = []
    for i in board:
        row = []
        hit_row = []
        for j in i:
            if (j == ''):
                row.append(0)
                hit_row.append(0)
            elif ('H' in j):
                row.append(0)
                hit_row.append(1)
            else:
                row.append(1)
                hit_row.append(0)
        mask.append(row)
        hit_mask.append(hit_row)
    #mask = np.asarray(mask)
    fitscore_array = []
    for i in range(len(mask)):
        row = []
        for j in range(len(mask)):
            if board[i, j] == '':
                row.append(fit_score(mask, i, j, active_len))
        fitscore_array.append(row)


def hit_score(hit_mask, ships):
    hit_mask =


def fit_score(board, x, y, ships):
    # Horizontal
    mlen = max(ships)
    score = 0
    xmax = x + mlen
    xmin = x - mlen

    ymax = y + mlen
    ymin = y - mlen

    for i in range(x, xmax):
        try:
            if board[i, y] == 1:
                xmax = i
                break
        except:
            pass
    for i in range(x, xmin, -1):
        try:
            if board[i, y] == 1:
                xmin = i
                break
        except:
            pass

    for i in range(y, ymax):
        if board[x, i] == 1:
            ymax = i
            break
    for i in range(y, ymin, -1):
        if board[x, i] == 1:
            ymin = i
            break
    for i in ships:
        if (ymax - ymin) >= i:
            score += 1
        if (xmax - xmin) >= i:
            score += 1
    return score


testboard = {'OppBoard': [['', 'M', '', 'M', '', '', '', ''], ['', '', 'M', '', '', '', '', ''], ['', '', '', '', 'M', '', '', 'S0'], ['H', '', 'M', '', 'M', '', '', 'S0'], [
    '', '', 'M', 'S1', 'S1', 'S1', 'S1', 'S0'], ['', '', '', 'M', '', 'M', '', 'S0'], ['', 'S3', 'S3', 'S3', 'M', '', '', 'S0'], ['', '', '', 'M', '', 'M', '', '']]}
cell_prob(testboard)
