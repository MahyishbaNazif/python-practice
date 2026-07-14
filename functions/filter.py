marks = [66,77,44,33,55,11]
def failing(score):
    return score < 60
result = filter(failing,marks)
print("Failing scores:", list(result))