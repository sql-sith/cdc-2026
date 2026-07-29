def find_landing_spot(grid: list[list[int]]):
    scores = [] # 2d-array of (safe?, score)
    for i, line in enumerate(grid):
        scores.append([])
        for j, space in enumerate(line):
            if space != 0:
                scores[i].append((False, 0))
                continue
            score = 0
            if i > 0:
                score += grid[i-1][j]
            if j > 0:
                score += grid[i][j-1]
            if i+1 < len(grid):
                score += grid[i+1][j]
            if j+1 < len(grid[i]):
                score += grid[i][j+1]
            scores[i].append((True, score))
    best = None
    for i, line in enumerate(scores):
        for j, space in enumerate(line):
            if not space[0]:
                continue
            if best is None:
                best = [i,j]
                continue
            if scores[best[0]][best[1]] > space:
                best = [i,j]
    return best

if __name__ == '__main__':
    test_cases = [
        ([[1, 0], [2, 0]],),
        ([[9, 0, 3], [7, 0, 4], [8, 0, 5]],),
        ([[1, 2, 1], [0, 0, 2], [3, 0, 0]],),
        ([[9, 6, 0, 8], [7, 1, 1, 0], [3, 0, 3, 9], [8, 6, 0, 9]],)
    ]
    results = [[0, 1], [1, 1], [2, 2], [2, 1]]
    for case, result in zip(test_cases, results):
        a = find_landing_spot(*case)
        print(a)
        print(result, 'success' if result==a else 'fail')