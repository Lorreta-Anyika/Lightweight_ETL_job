de_list = ["8", 8,  "Republic of Ireland", "Federal Republic of Nigeria", "Federal Republic of Germany", "Federal Republic of Somalia"]
# Write a Script that checks the data type of elements in a List, filter out the ones with
#  string and has Republic at the beginning and Nigeria at the end

for each_item in de_list:
    print(f"{each_item} has a datatype of {type(each_item).__name__}")
    if type(each_item) == str:
        word_list = each_item.split()
        starter_word = word_list[0]
        ending_word = word_list[-1]
        #print(f"find below useful words: {starter_word}, {ending_word}", end="\n\n")
        if starter_word =="Republic" and ending_word == "Nigeria":
            print(f"Only {each_item} passed the quality checks!")
        else:
            print("None of the items in the list passed the checks")


        