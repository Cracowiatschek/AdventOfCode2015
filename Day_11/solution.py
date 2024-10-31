from solutionPrinter import solution_println as sp


sample = "abcdefgh"
data = "hxbxwxba"


def check_constraint(password):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    iter_check = [alphabet[i]+alphabet[i+1]+alphabet[i+2] for i in range(len(alphabet)-2)]
    pairs = [i+i for i in alphabet]
    # pairs_constraint = []
    letters = ['i', 'o', 'l']

    iter_cnt = sum([1 for i in iter_check if i in password])
    pairs_cnt = sum([1 for i in pairs if i in password])
    illegal_letters = sum([1 for i in letters if i in password])

    if illegal_letters == 0 and pairs_cnt >= 2 and iter_cnt >= 1:
        return True
    else:
        return False


def password_generator(actual_pass):
    actual_pass = list(actual_pass)
    last_char = len(actual_pass) - 1

    while last_char >= 0:
        if actual_pass[last_char] == 'z':
            actual_pass[last_char] = 'a'
            last_char -= 1
        else:
            actual_pass[last_char] = chr(ord(actual_pass[last_char]) + 1)
            break
    else:
        actual_pass.insert(0, 'a')

    return ''.join(actual_pass)

def search_new_password(old_password):
    correct_password = False
    password = old_password
    while not correct_password:
        new_password = password_generator(password)
        password = new_password
        check_pass = check_constraint(new_password)
        if check_pass:
            correct_password = True
    return password

new_password = search_new_password(data)

sp("New password Santa is: ", new_password)
sp("Again new password Santa is: ", search_new_password(new_password))

