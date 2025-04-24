questions = [
    ["What is the capital of France?", "Berlin", "Madrid", "Paris", "Rome", 3],
    [
        "Which planet is known as the Red Planet?",
        "Earth",
        "Mars",
        "Jupiter",
        "Venus",
        2,
    ],
    [
        "Who wrote 'Romeo and Juliet'?",
        "Charles Dickens",
        "William Shakespeare",
        "Mark Twain",
        "Jane Austen",
        2,
    ],
    [
        "What is the largest ocean on Earth?",
        "Atlantic Ocean",
        "Indian Ocean",
        "Arctic Ocean",
        "Pacific Ocean",
        4,
    ],
    [
        "Who painted the Mona Lisa?",
        "Vincent van Gogh",
        "Pablo Picasso",
        "Leonardo da Vinci",
        "Claude Monet",
        3,
    ],
    ["What is the smallest prime number?", "0", "1", "2", "3", 2],
    [
        "Which country is known as the Land of the Rising Sun?",
        "China",
        "Japan",
        "Thailand",
        "India",
        2,
    ],
    ["What is the chemical symbol for gold?", "Au", "Ag", "Pb", "Fe", 0],
    [
        "Who is known as the Father of Computers?",
        "Albert Einstein",
        "Isaac Newton",
        "Charles Babbage",
        "Nikola Tesla",
        3,
    ],
    [
        "What is the hardest natural substance on Earth?",
        "Gold",
        "Iron",
        "Diamond",
        "Silver",
        3,
    ],
]

prizes = [
    10000,
    50000,
    100000,
    500000,
    1000000,
    5000000,
    10000000,
    50000000,
    100000000,
    1000000000,
]


def main():
    print(
        "We will go through few GK questions. To answer, enter the correct option as [a, b, c, d] or if you want to quit enter q.\n"
    )

    prize = 0
    i = 0

    for question_data in questions:
        correct_answer_index = question_data[5]
        print(
            f"{question_data[0]}",
            f"a. {question_data[1]}",
            f"b. {question_data[2]}",
            f"c. {question_data[3]}",
            f"d. {question_data[4]}",
            sep="\n",
        )

        answer = input("\nEnter the correct option: ")
        while answer not in ["a", "b", "c", "d", "q"]:
            print("\nPlease provide option between 'a','b','c','d' and 'q'.")
            answer = input("\nEnter the correct option: ")

        match answer:
            case "a":
                answer = 1
            case "b":
                answer = 2
            case "c":
                answer = 3
            case "d":
                answer = 4

        if answer == "q":
            print("Quitting the competition.")
            break
        elif answer == correct_answer_index:
            prize += prizes[i]
            i += 1
            print(f"\nCongratulations!! You have won {prize}\n")
        else:
            print(
                f"\nYou loose! The correct answer is {question_data[correct_answer_index]}.\n"
            )


if __name__ == "__main__":
    main()
