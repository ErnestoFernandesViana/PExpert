def create_strings_from_characters(frequencies, string1, string2):
    string1_dict  = {x:string1.count(x) for x in string1}
    string2_dict = {x:string2.count(x) for x in string2}
    result_by_letter = []
    for x in frequencies:
        if frequencies.get(x) >= (string1_dict.get(x, 0) + string2_dict.get(x, 0)):
            result_by_letter.append(2)
        elif (frequencies.get(x) >= string1_dict.get(x, 0)) or (frequencies.get(x) >= string2_dict.get(x, 0)):
            result_by_letter.append(1)
        elif (frequencies.get(x) < string1_dict.get(x, 0)) and (frequencies.get(x) < string2_dict.get(x, 0)):
            result_by_letter.append(0)
    return min(result_by_letter)


frequencies = {"h": 2, "e": 1, "l": 1, "r": 4, "a": 3, "o": 2, "d": 1, "w": 1}
string1 = "hello"
string2 = "world"

f = {"a": 3, "b": 1, "c": 3, "d": 2, "e": 1}
s1 = "aaabbbc"
s2 = "bbccde"
print(create_strings_from_characters(f, s1, s2))
print(create_strings_from_characters( frequencies, string1, string2))
