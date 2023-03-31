def ritm(poem:list) -> bool:
    vowels = ("а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я")
    return len(set(map(lambda x: len(list(filter(lambda i: i in vowels, x))), poem))) == 1


poem = input().lower().split(' ')
print(["Пам парам", "Парам пам-пам"][ritm(poem)])