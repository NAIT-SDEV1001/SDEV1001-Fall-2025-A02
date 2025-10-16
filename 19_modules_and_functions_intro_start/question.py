import copy

teams = ["edmonton", "calgary"]
# question asked about shallow and deep copies
# you can ignore if you'd like but something to
# note:)
def test(teams_test):
    new_list = copy.deepcopy(teams_test)
    # you could also do this
    # new_list = [*teams_test]
    new_list.append('new york')
    return new_list
print("this should be three")
print(test(teams))

# the orignal list as a whol
print(teams)