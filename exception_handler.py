"""Write a script that will intentionally break
 if any string related data is in a List 
"""

de_list = [
           8, 
           "8",  
           "Republic of Ireland", 
           "Federal Republic of Nigeria", 
           "Federal Republic of Germany", 
           "Federal Republic of Somalia"
           ]

for item in de_list:
    if type(item) == str:
        raise TypeError(f"Wrong data type. {type(item)} not allowed!")
    else:
        print(item)
    