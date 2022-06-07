# data parameter holds a list of dictionaries

# Dict type: {
#           'county': string,
#           'registered_voters': int
# }



def voter_sum(data) -> int:
    ...

def voter_average(data) -> float:
    ...

def voter_max(data) -> dict:
    ...

def voter_min(data) -> dict:
    ...







voting_data = [
{"county":"Arapahoe","registered_voters":422829},
{"county":"Denver", "registered_voters": 432438},
{"county":"Jefferson", "registered_voters":432338}]

# sum = 0
# for reg_voters in voting_data:
#     sum = sum + reg_voters["registered_voters"]
#     print(sum)





print(f"Total voters: {voter_sum(voting_data)}")
print(f"Average voters per county: {voter_average(voting_data)}")
max = voter_max(voting_data)
min = voter_min(voting_data)
print(f"Highest voting county: {max['county']}")
print(f"Lowest voting county: {min['county']}")