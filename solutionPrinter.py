
def solution_println(string, result):
    start_string = "\033[33m|---"
    stop_string = "---|\033[0m"

    if type(result) != str:
        str_len = len(string+str(result))+3
    else:
        str_len = len(string + result) + 2
    placeholder = "-" * str_len

    result = f"""
    {start_string}{placeholder}{stop_string}
    {start_string}\033[0m {string} {str(result)} \033[33m{stop_string}
    {start_string}{placeholder}{stop_string}
    """
    print(result)

