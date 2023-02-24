def oxford_comma(items):
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return items[0] + ' and ' + items[1]
    last_word = items.pop()
    return ', '.join(items) + ", and " + last_word 
