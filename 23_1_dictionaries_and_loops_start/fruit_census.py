fav_fruit_voters = {
    "daniel": "apple",
    "jessica": "apple",
    "michael": "banana",
    "john": "banana",
    "jessie": "apple",
    "jim": "orange",
    "jenny": "apple",
    "jason": "orange",
    "joseph": "banana",
    "james": "orange",
    "mary": "apple",
    "melody": "banana",
}

voting_results = {
    "banana": 0,
    "apple": 0,
    "orange": 0
}

# I want to do a few things here.
# see the list the list of voters
# I know the keys of the fav_fruit_voters will be the voters
print('our favourite fruit voters')
for voter in fav_fruit_voters.keys():
    print(F"- {voter}")

# I want to tally up the results
    # we're going to do this using the value of the vote.
# the votes cast above are essentially the values of
# the list fav_fruit_voters.
print("tallying votes")
for vote in fav_fruit_voters.values():
    # just for debugging (remove later)
    # print(vote)
    # we're going to use that vote value as a key to the
    # object of voting results and also increase the amount by
    # one.
    voting_results[vote] = voting_results[vote] + 1
    # above we're using the string of the vote value to access
    # the value in the voting results
    # debugging purposes
    # print(voting_results[vote])

# debugging purposes
# print("you can see below that the voting results have been modified")
# print(voting_results)

# we're going to use sorted which will print out the results
# in order.
print("The amount of votes are as follows")
for fruit, number_of_votes in sorted(voting_results.items()):
    print(F"{fruit} has {number_of_votes} votes")

# the above is going to do this alphabetically.

# optional
# print("The amount of votes ascending")
# for fruit, number_of_votes in sorted(voting_results.items(),
#                                      key=lambda item: item[1]):# optional
#     print(F"{fruit} has {number_of_votes} votes")