#Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

def solution(text, ending):
    return text.endswith(ending)# returns True if the string ends with the specified ending

print(solution("hello world", "world"))  # True
print(solution("foo bar baz", "qux"))  # False
print(solution("foo bar baz", "baz"))  # True