# This is a sample Code Challenge
# Learn more: https://stepik.org/lesson/9172

def generate():
    return []

def check(reply, clue):
    if reply.strip() == clue.strip():
        return True
    return False, f"Ваш ответ: {reply}. Ожидаемый ответ: Не найден"
    # return False, f"Ваш ответ: {reply}. Ожидаемый ответ: {clue}"

# def solve(dataset):
#     a, b = dataset.split()
#     return str(int(a) + int(b))


""" Taken on my course 1989434 """
