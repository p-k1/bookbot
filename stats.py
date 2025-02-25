def count_words(content):
    count = 0
    list = content.split()
    for word in list:
        count += 1
    return count

def count_symbols(content):
    result = {}
    for symbol in content:
        if symbol.lower() in result:
            result[symbol.lower()] += 1
        else:
            result[symbol.lower()] = 1
    return result

def dictsort(content):
    sorted = []
    for x in content:
        sorted.append({"character":x, "value": content[x]})
    sorted.sort(reverse=True, key=lambda x: x['value'])
    return sorted