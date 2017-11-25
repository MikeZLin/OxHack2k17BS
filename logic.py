import numpy as np


def cell_prob(gamestate):
    board = np.asarray(gamestate['OppBoard'])
    ships = ['S0', 'S1', 'S2', 'S3', 'S4']
    ship_len = [4, 3, 2, 2, 1]
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
                row.append(1)
                hit_row.append(0)
            elif ('H' in j):
                row.append(1)
                hit_row.append(1)
            else:
                row.append(0)
                hit_row.append(0)
        mask.append(row)
        hit_mask.append(hit_row)
    # mask = np.asarray(mask)
    fitscore_array = []
    for i in range(len(mask)):
        row = []
        for j in range(len(mask)):
            if mask[i][j] == 1:
                row.append(fit_score(mask, i, j, active_len))
            else:
                row.append(0)
        fitscore_array.append(row)
    # print(np.asarray(mask))
    fitscore_array = fitscore_array + hit_mask_func(hit_mask, mask, active_len)
    new_mask = np.subtract(mask, hit_mask)
    score = np.multiply(new_mask, fitscore_array)
    maxsc = np.amax(score)
    idi = -1
    idj = -1
    for i in range(len(score)):
        for j in range(len(score[0])):
            if score[i][j] == maxsc:
                idi = i
                idj = j
                break
        if idi != -1:
            break

    print(score)
    return [idj, idi]


def hit_mask_func(hit_mask, mask, ships):
    weight = 40
    scorechart = np.zeros([8, 8])
    for i in range(len(hit_mask)):
        for j in range(len(scorechart[i])):
            if hit_mask[i][j] == 1:
                scorechart += hit_score(mask, i, j, ships)

    scorechart = np.multiply(scorechart, weight)
    return scorechart


def hit_score(board, y, x, ships):
    mlen = max(ships)
    score = np.zeros([8, 8])
    xmax = min(7, x + mlen)
    xmin = max(0, x - mlen)

    ymax = min(7, y + mlen)
    ymin = max(0, y - mlen)

    for i in range(x, xmax + 1):
        try:
            if board[y][i] == -1:
                xmax = i - 1
                break
        except:
            xmax = i - 1
    for i in range(x, xmin - 1, -1):
        try:
            if board[y][i] == -1:
                xmin = i + 1
                break
        except:
            xmin = i + 1

    for i in range(y, ymax + 1):
        try:
            if board[i][x] == -1:
                ymax = i - 1
                break
        except:
            ymax = i - 1
    for i in range(y, ymin - 1, -1):
        try:
            if board[i][x] == -1:
                ymin = i + 1
                break
        except:
            ymin = i + 1
    for length in ships:
        for i in range(max(ymin, y - (length)), min(ymax, y + (length)) + 1):
            score[i][x] += 1
        for j in range(max(xmin, x - (length)), min(xmax, x + (length)) + 1):
            score[y][j] += 1
    score = list(score)
    return score


def fit_score(board, y, x, ships):
    # Horizontal
    mlen = max(ships) + 1
    score = 0
    xmax = min(7, x + mlen)
    xmin = max(0, x - mlen)

    ymax = min(7, y + mlen)
    ymin = max(0, y - mlen)

    for i in range(x, xmax + 1):
        try:
            if board[y][i] == 0:
                xmax = i - 1
                break
        except:
            xmax = i - 1
    for i in range(x, xmin - 1, -1):
        try:
            if board[y][i] == 0:
                xmin = i + 1
                break
        except:
            xmin = i + 1

    for i in range(y, ymax + 1):
        try:
            if board[i][x] == 0:
                ymax = i - 1
                break
        except:
            ymax = i - 1
    for i in range(y, ymin - 1, -1):
        try:
            if board[i][x] == 0:
                ymin = i + 1
                break
        except:
            ymin = i + 1
    for i in ships:
        xscore = max(0, min(xmax, x + i) - max(xmin, x - i) - i + 1)
        yscore = max(0, min(ymax, y + i) - max(ymin, y - i) - i + 1)
        score += xscore + yscore
    return score


# testboard = {'OppBoard': [['', 'M', '', 'M', '', '', '', ''], ['', '', 'M', '', '', '', '', ''], ['', '', '', '', 'M', '', '', 'S0'], ['H', 'H', '', '', 'M', '', '', 'S0'], [
#    '', '', 'M', 'S1', 'S1', 'S1', 'S1', 'S0'], ['', '', '', 'M', '', 'M', '', 'S0'], ['', 'S3', 'S3', 'S3', 'M', '', '', 'S0'], ['', '', '', 'M', '', 'M', '', '']]}

# testboard = {'OppBoard': [['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], [
#    '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '']]}
# print(cell_prob(testboard))
