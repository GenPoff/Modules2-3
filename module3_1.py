calls = 0


def count_calls():
    global calls
    calls = calls + 1
    return calls


def string_info(string):
    count_calls()
    length = len(string)
    up = string.upper()
    lo = string.lower()
    info = [length, up, lo]
    return tuple(info)




def is_contains(string, list_to_search):
    count_calls()
    for str in list_to_search:
        if string.lower() in str.lower():
            return True
        else:
            continue
    return False




print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
