"""
    - 1. sort list of number 
    - 2. sort list of word
    - 3. sort string
    - 4. list with none comparable mix-type cannot be sorted
    - 5. revert: sort(list_of_number, reverse=True) => revert list
    - 6. sort with key => key=function
"""


# 1. sort array of number
def sp1():
    arr_of_number = [1, 2, 3, 4, 2345, 1234, 12, 3412, 341, 234134,
                     12, 34, 1234, 123, 4123, 4, 1234, 1234, 123, 4123, 41, 234]
    sorted_arr_of_number = sorted(arr_of_number)
    print(sorted_arr_of_number)


# 2. sort list
def sp2():
    string = "Nguyễn Hữu Hiếu"

    arr_of_word = string.split(" ")
    sorted_arr_of_word = sorted(arr_of_word)
    print(sorted_arr_of_word)

# 3. sort string


def sp3():
    string = "Nguyen Vawn A"
    sorted_string = sorted(string)
    print(sorted_string)

# 5. reverse


def sp5():
    arr_of_number = [1, 2, 3, 4, 2345, 1234, 12, 3412, 341, 234134,
                     12, 34, 1234, 123, 4123, 4, 1234, 1234, 123, 4123, 41, 234]
    sorted_arr_of_number = sorted(arr_of_number, reverse=True)
    print(sorted_arr_of_number)


# 6. sorted with key=function
def sp6():
    string = "The resulting order is a"
    words = string.split(' ')
    set_of_word = {*words}
    sorted_words = sorted(set_of_word)  # chữ hoa sẽ xếp trước chữ thường
    print(sorted_words)
    sorted_words = sorted(set_of_word, key=str.lower)
    print(sorted_words)
    sorted_words = sorted(set_of_word, key=str.upper)
    print(sorted_words)
    sorted_words = sorted(set_of_word, key=len)  # độ dài các kí tự
    print(sorted_words)


if __name__ == "__main__":
    sp6()
