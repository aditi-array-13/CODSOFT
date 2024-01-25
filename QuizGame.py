# CodSoft
# Task 5
# Quiz Game

import tkinter as tk
from tkinter import messagebox


class QuizGame:
    def __init__(self, main):
        self.submit_button = None
        self.choice_radios = None
        self.choices_var = None
        self.question_label = None
        self.root = main
        self.root.title("Quiz Game")
        self.root.geometry("400x300")

        self.questions = [
            {
                'question': 'What is the capital of France?',
                'choices': ['Berlin', 'Madrid', 'Paris', 'Rome'],
                'correct_answer': 'Paris'
            },
            {
                'question': 'Which planet is known as the Red Planet?',
                'choices': ['Mars', 'Venus', 'Jupiter', 'Mercury'],
                'correct_answer': 'Mars'
            },
            {
                'question': 'What is the largest mammal in the world?',
                'choices': ['Elephant', 'Blue Whale', 'Giraffe', 'Hippopotamus'],
                'correct_answer': 'Blue Whale'
            },
            # Add more questions as needed
        ]

        self.score = 0
        self.current_question_index = 0

        self.create_widgets()

    def create_widgets(self):
        self.question_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.question_label.pack(pady=10)

        self.choices_var = tk.StringVar()
        self.choices_var.set("")

        self.choice_radios = []
        for i in range(4):
            choice_radio = tk.Radiobutton(self.root, text="", variable=self.choices_var, value=i + 1)
            choice_radio.pack(anchor="w")
            self.choice_radios.append(choice_radio)

        self.submit_button = tk.Button(self.root, text="Submit Answer", command=self.evaluate_user_answer)
        self.submit_button.pack(pady=10)

        self.display_next_question()

    def display_next_question(self):
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.question_label.config(text=f"Question {self.current_question_index + 1}: {question_data['question']}")

            for i, choice in enumerate(question_data['choices']):
                self.choice_radios[i].config(text=choice)

    def evaluate_user_answer(self):
        if self.current_question_index < len(self.questions):  # Check if there are more questions
            user_answer = self.choices_var.get()
            correct_answer = str(self.questions[self.current_question_index]['correct_answer'])

            if user_answer == correct_answer:
                messagebox.showinfo("Correct!", "Well done! Your answer is correct.")
                self.score += 1

            self.current_question_index += 1  # Move to the next question
            self.display_next_question()
        else:
            self.display_final_results()

    def display_final_results(self):
        final_message = f"Your final score is: {self.score}/{len(self.questions)}\n"
        if self.score == len(self.questions):
            final_message += "Congratulations! You got all questions right."
        elif self.score >= len(self.questions) // 2:
            final_message += "Good job! You did well."
        else:
            final_message += "Keep practicing. You can do better!"

        messagebox.showinfo("Quiz Completed", final_message)
        self.play_again()

    def play_again(self):
        answer = messagebox.askyesno("Play Again", "Do you want to play again?")
        if answer:
            self.reset_game()
            self.display_next_question()
        else:
            self.root.destroy()

    def reset_game(self):
        self.score = 0
        self.current_question_index = 0


# Main program
if __name__ == "__main__":
    root = tk.Tk()
    quiz_game = QuizGame(root)
    root.mainloop()
