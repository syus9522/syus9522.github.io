start = '''
You are an 18 year old girl, living in New York City. You see many posters
about pollution affecting the area you live. You have often been criticized
for the way you act socially. Do you want to help the cause or not? By helping
the cause, it will help your image ;).
'''


print(start)


print("Type yes if you would like to help the cause. Type no if you would not like to help the cause.")
user_input = input()
while (user_input != "yes"):
    print("Boo! No one likes you anymore. Try again.")
    print("Type yes if you would like to help the cause. Type no if you would not like to help the cause.")
    user_input = input() # finished the story writing what happens
if user_input == "yes":
    print("Yay! We are glad you will participate!") # finished the story by writing what happens


print('''Now that you are about to participate, you decide to play a game that tests your recycling skills. Your first question is 'You see garbage on the street.
What do you do? Do you either ignore it or throw it in the trash?' What will you say?''')

user_input = input()
while (user_input != "I throw it in the trash" and user_input != "I ignore it"):
    print("Boo! No one likes you anymore. Try again.")
    print("Do you either ignore it or throw it in the trash?' What will you say?")
    user_input = input()
if user_input == "I throw it in the trash" :
    print("You just won one point! Congrats!")
if user_input == "I ignore it" :
    print("You are a terrible person. You lose one point.")


print('''You have made it to level two on the game you are playing. The second question is 'You are cleaning up after a party. You had soda cans and you don't know
where to put the plastic soda rings. Where do you eventually put them?' What do you do? Do you throw it away or recycle it?''')

user_input = input()
while (user_input != "I throw it away." and user_input != ""):
    print("Boo! No one likes you anymore. Try again.")
    print("")
    user_input = input()
if user_input == "" :
    print("")
if user_input == "" :
    print("")

user_input = input()
if user_input== "":
  print("Dude, woah. Why are you so mean?! You lose one point.")

elif user_input == "I recycle it":
  print("You are showing your caring side. Keep it up! You gain one point.")

print('''You have made it to the final level of the game. The final question is 'You are in a deserted area. You see that trash is everywhere. Do you organize the trash by what can be recycled or
do you fall asleep on the trash?' You feel this is a tough question. You don't know what to say. You ask your friend for help. What does your friend say?''')
user_input = input()
if user_input== "I organize the trash.":
  print("You won the game! Congrats!!! We respect you!")

elif user_input == "I sleep on it":
  print("You lost the game! You know nothing about the effects of pollution and not recycling. Do your research next time.")
