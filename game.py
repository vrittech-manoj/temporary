wap to make a game in which a random number should be generated from 0 to 100, where a 
user can input their guess number untill match exact number.
and score should be number of thime he guessed .(more guessed number bad in performance, less guessed number more tilented)

start

random_number = generate_random_number using rand function in python

guessed_time = 1
while True:
    user_input_guessed_number = take user input number 

    if user_input_guessed_number equal to random_number:
        print(" congrats you guessed successfully with try",  guessed_time)
        break

    elif user_input_guessed_number > random_number:
        print(" just above than your input ")
    else:
        print(" just less than your input ")
        
    guessed_time = guessed_time + 1

end