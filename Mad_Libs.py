#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time


# In[ ]:


"""The Mad Libs game based on Jimmy Fallon and Benedict Cumberbatch - Detective Skit"""

#All the questions that will be asked
while True:
    prompt = input("Start game? (y/n)")
    if prompt == 'y':
        # get the names of the two people that will be playing
        person_1 = input("Enter the name of first person: ")
        person_2 = input("Enter the name of second person: ")
        
        # questions start from here . 19 questions in total
        # all based on the actual questions from Jimmy Fallon
        male_name = input("Male name: ").lower()
        favourite_teacher = input("Favourite teacher: ").lower()
        exclamation = input("Exclamation statement e.g 'Gosh darn': ").lower()
        number = (input("Number: "))
        plural_object = input("Plural object e.g 'eggs': ").lower()
        store_name = input("Store name: ").lower()
        body_part = input("Body part: ").lower()
        silly_word = input("Silly word: ").lower()
        holiday_name = input("Name of holiday: ").lower()
        movie_title = input("Name of movie: ").lower()
        verb = input("Verb ending in 'ing': ").lower()
        distance = input("Amount of distance e.g 15km: ").lower()
        country = input("Name any country: ").lower()
        animal = input("Any animal: ").lower()
        movie_quote = input("Movie quote/line: ").lower()
        body_part2 = input("Body part: ").lower()
        children_song = input("Any children's song: ").lower()
        adjective = input("Adjective: ").lower()
        
        print("----------------------------------------------------------------------")
        time.sleep(2)
        print(f"{person_1}: Hello... I'm detective {male_name.title()}. You are?\n")
        time.sleep(3)
        print(f"{person_2}: {favourite_teacher.title()}\n")
        time.sleep(2)
        print(f"{person_1}: You are here today under suspicion of 2nd degree robbery\n")
        time.sleep(4)
        print(f"{person_2}: {exclamation.title()}!\n")
        time.sleep(2)
        print(f"{person_1}: That's right. {number} {plural_object} were stolen from {store_name.title()}\n")
        time.sleep(6)
        print(f"{person_1}: The crime scene has your {body_part} written all over it!\n")
        time.sleep(6)
        print(f"{person_2}: That is {silly_word}!\n")
        time.sleep(2)
        print(f"{person_1}: Where were on you on the night of {holiday_name.title()}?\n")
        time.sleep(4)
        print(f"{person_2}: We were watching {movie_title.upper()}\n")
        time.sleep(3)
        print(f"{person_1}: Then why is there security camera footage that shows you {verb}, just {distance} away from the crime scene?\n")
        time.sleep(7)
        print(f"{person_1}: Alright, I'm through with playing games. Where you from?\n")
        time.sleep(4)
        print(f"{person_2}: {country.title()}.\n")
        time.sleep(2)
        print(f"{person_1}: Just as I suspected. You know, one of the best parts about being a detective is that I get to "
              f"lock up criminals like you, and go home to my children and my pet {animal},"
              f" and say... {movie_quote.title()}\n")
        time.sleep(14)
        print(f"{person_2}: Fine, I did it. But I only did it because I needed the money... to buy myself {body_part2} implants\n")
        time.sleep(8)
        print(f"{person_1}: I knew it! I knew it all along! Every time I solve a crime I like to sing my favourite song... "
              f"{children_song.title()}\n")
        time.sleep(7)
        print(f"{person_2}: You have a {adjective} voice! I love you!\n")
        time.sleep(5)





