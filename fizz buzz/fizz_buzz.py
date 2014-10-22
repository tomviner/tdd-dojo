def fizz_buzz():
    num_list = range(1,101)
    num_list[2] = 'fizz'
    num_list[4] = 'buzz'
    num_list[14] = 'fizzbuzz'
    print num_list
    return num_list
