# Расширенный редактор (по умолчанию)
def generate():
    return []

def check(reply, clue):
    return reply.strip() == clue.strip()


# Расширенный редактор (Будут отображаться верные/неверные ответы)
def generate():
    return []

def check(reply, clue):
    if reply.strip() == clue.strip():
        return True
    # return False, f"You answer was: {reply}. Correct answer was: {clue}"
    return False, f"\nОжидаемый ответ: \n{clue}\nВаш ответ: \n{reply}"