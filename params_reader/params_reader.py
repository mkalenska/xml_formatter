def read_params_from_input():
    params = {}
    print("Enter 1 if you want to use tab as indent char (default False)")
    params['use_tab'] = True if input() == 1 else False
    print("Enter number of indent chars (default 4)")
    params['indent'] = input()
    print("Enter 1 to keep line breaks (default True)")
    params['keep_line_breaks'] = True if input() == 1 else False
    print("Enter number of blank lines to keep (default 2)")
    params['keep_blank_lines'] = input()
    print("Enter 1 if you want to wrap text (default True)")
    params['wrap_text'] = True if input() == 1 else False
    print("Enter file name to save")
    name = input()

    f = open(name, "w")
    f.write("\n".join(str(x) + '-' + str(params[x]) for x in params.keys()))
    f.write("\n")

    return params


def read_params_from_file(name):
    params = {}
    f = open(name, "r")
    lines = f.readlines()
    for line in lines:
        line_arr = line[:-1].split('-')
        value = line_arr[1]
        if value == 'True':
            value = True
        elif value == 'False':
            value = False
        elif value.isdigit():
            value = int(value)
        params[line_arr[0]] = value

    return params