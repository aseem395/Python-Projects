questions = [
    [
        "Who was the first president of India?", "Ram Nath Kovind", "Rajendra Prasad", "Sarvepalli Radhakrishnan", "Droupadi Murmu", 3
        ],

    [
        "Who was the first prime minister of India?", "Ram Nath Kovind", "Narendra Modi", "Sarvepalli Radhakrishnan", "Jawaharlal Nehru", 4
        ],

    [
        "Total number of states in India", "25", "29", "30", "28", 2
        ],

    [
        "Total number of UTs in India", "5", "9", "3", "7", 2
        ],

    [
        "Which is the largest planet in our solar system?", "Earth", "Jupiter", "Saturn", "Neptune", 2
        ],
    
    [
        "What is the capital city of Australia?", "Sydney", "Melbourne", "Canberra", "Perth", 3
        ],

    [
        "What is the smallest prime number?", "1", "2", "3", "0", 2
        ],

    [
        "Who is known as the ‘Missile Man of India’?", "Vikram Sarabhai", "Homi Bhabha", "APJ Abdul Kalam", "Rakesh Sharma", 3
        ],
    
    [
        "What is the national flower of India?", "Rose", "Marigold", "Lotus", "Sunflower", 3
        ],

    [
        "Which day is celebrated as World Environment Day?", "5th June", "22nd April", "16th September", "14th November", 1
        ],

    [
        "Which is the longest river in the world?", "Amazon", "Ganges", "Nile", "Yangtze", 3
        ],

    [
        "What is the currency of Japan?", "Yuan", "Ganges", "Won", "Ringgit", 3
        ],

    [
        "Who invented the telephone?", "Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "Guglielmo Marconi", 1
        ],

    [
        "What is the chemical symbol for water?", "O2", "CO2", "H2O", "NaCl", 3
        ],

    [
        "Which organ in the human body is responsible for pumping blood?", "Lungs", "Liver", "Heart", "Kidney", 3
        ],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]

for i in range(0,len(questions)):
    question = questions[i]
    print(f"Question for Rs. {levels[i]} is: ")
    print(f"{question[0]}")
    print("Choose the correct option(1-4): ")
    print(f"1. {question[1]}                   2. {question[2]}")
    print(f"3. {question[3]}                   4. {question[4]}")
    
    ans = int(input())
    
    if ans == question[-1]:
        print(f"Correct answer, you have won Rs. {levels[i]}")
        if i == len(levels):
            print(f"You have won the game, you get Rs. {levels[i]}")
    
    else:
        print("Sorry, wrong answer")
        if i == 4:
            print(f"You get Rs. {levels[i]}")
        elif i == 9:
            print(f"You get Rs. {levels[i]}")
        else:
            break