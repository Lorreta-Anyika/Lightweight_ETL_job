""" Write a script that will gracefully bypass any string related data in a List
"""

de_list = [
          "8", 
           8,  
           "Republic of Ireland", 
           "Federal Republic of Nigeria", 
           "Federal Republic of Germany", 
           "Federal Republic of Somalia"
           ]

for item in de_list:
    if type(item) == str:
        pass
    else:
        print(f"{item} is not a string. {type(item)} not permitted.")