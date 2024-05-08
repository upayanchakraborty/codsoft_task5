import random
quizset = [
    {
        "question": "Which of the following operating systems is primarily based on a Graphical User Interface (GUI)?",
        "options": ["A. Android", "B. Windows", "C. Linux", "D. MacOS"],
        "answer": "A"
    },
    {
        "question": "What is the name of the operating system of Microsoft?",
        "options": ["A. Beta", "B. BharOS", "C. Linux", "D. Windows"],
        "answer": "D"
    },
    {
        "question": "In MS Word _______ is used to copy the format of the text.",
        "options": ["A. Font Dialogue box", "B. Format Painter", "C. Fill Color", "D. Copy"],
        "answer": "B"
    },
    {
        "question": "What does the acronym SQL stand for?",
        "options": ["A. Structured Query Language", "B. Simple Query Language", "C. Standard Query Language", "D. Sequential Query Language"],
        "answer": "A"
    },
    {
        "question": "Which programming language is often used for data analysis and scientific computing?",
        "options": ["A. JavaScript", "B. Java", "C. Python", "D. C++"],
        "answer": "C"
    },
    {
        "question": "What does API stand for in the context of web development?",
        "options": ["A. Application Programming Interface", "B. Advanced Programming Interface", "C. Automated Program Interaction", "D. All of the above"],
        "answer": "A"
    },
    {
        "question": "In Python, which keyword is used to define a function?",
        "options": ["A. define", "B. func", "C. def", "D. function"],
        "answer": "C"
    },
    {
        "question": "What is the output of the following code: `print(3 * 'Hello ')`?",
        "options": ["A. Hello Hello Hello Hello", "B. 9", "C. Hello Hello Hello", "D. Syntax Error"],
        "answer": "C"
    },
    {
        "question": "Python was developed by whom?",
        "options": ["A. Wick van Rossum", "B. Charles Babbage", "C. Guido van Rossum", "D. Rasmus Lerdorf"],
        "answer": "C"
    },
    {
        "question": "Which data type in Python is used to represent a sequence of characters?",
        "options": ["A. int", "B. float", "C. str", "D. list"],
        "answer": "C"
    },
    {
        "question": "What is the primary purpose of version control systems like Git?",
        "options": ["A. To write code", "B. To run code", "C. To manage and track changes in code", "D. To execute code"],
        "answer": "C"
    },
    {
        "question": "What is the main advantage of object-oriented programming (OOP)?",
        "options": ["A. Simplicity", "B. Reusability", "C. Procedural nature", "D. No need for functions"],
        "answer": "B"
    },
    {
        "question": "What is the HTTP status code for a successful response?",
        "options": ["A. 200 OK", "B. 404 Not Found", "C. 500 Internal Server Error", "D. 302 Found"],
        "answer": "A"
    },
    {
        "question": "In Python, which library is commonly used for data visualization?",
        "options": ["A. NumPy", "B. Pandas", "C. Matplotlib", "D. TensorFlow"],
        "answer": "C"
    },
    {
        "question": "What is the purpose of a constructor method in object-oriented programming?",
        "options": ["A. To create objects", "B. To destroy objects", "C. To update objects", "D. To copy objects"],
        "answer": "A"
    },
    {
        "question": "Which of the following is not a valid Python data type?",
        "options": ["A. int", "B. double", "C. list", "D. tuple"],
        "answer": "B"
    },
    {
        "question": "What is the result of the following Python code: `3 + '3'`?",
        "options": ["A. 6", "B. '33'", "C. TypeError", "D. '6'"],
        "answer": "C"
    },
    {
        "question": "Which programming language is often used for developing mobile applications?",
        "options": ["A. Java", "B. Python", "C. C#", "D. PHP"],
        "answer": "A"
    },
    {
        "question": "What is the purpose of the `if` statement in programming?",
        "options": ["A. To perform a loop", "B. To declare a function", "C. To make decisions based on conditions", "D. To define a class"],
        "answer": "C"
    }
]
def ask(ques):
    print(ques["question"])
    for option in ques["options"]:
        print(option)
    user_answer = input("Enter your answer (A,B,C,D): ").upper()
    if user_answer in ('A', 'B', 'C', 'D'):
        if user_answer == ques["answer"]:
            return True
        else:
            return False
    else:
        print("Invalid input. Please enter A, B, C, or D.")
if __name__=="__main__":
    score=0
    random.shuffle(quizset)
    for i in range(1,6):
        print(f'Question {i} of 5')
        if ask(quizset[i]):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {quizset[i]['answer']}.\n")

    print(f"You scored {score}/5.")
