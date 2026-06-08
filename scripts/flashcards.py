import tkinter as tk

def save_flashcard():
    front_content = front_text.get("1.0", tk.END).strip()
    back_content = back_text.get("1.0", tk.END).strip()
    
    with open("cards.txt", "a") as file:
        file.write(front_content + " | " + back_content + "\n")

    # Clear the textboxes
    front_text.delete("1.0", tk.END)
    back_text.delete("1.0", tk.END)

    print("Card saved to file")

def study_cards():
    cards = []

    with open("cards.txt", "r") as file:
        saved_lines = file.readlines()

    for line in saved_lines:
        parts = line.strip().split(" | ")
        card_data = {"front": parts[0], "back": parts[1]}
        cards.append(card_data)

    current_card_index = 0

    study_window = tk.Toplevel(root)
    study_window.title("Study Mode")
    study_window.geometry("400x300")

    # Display front of first card
    card_display = tk.Label(study_window, text = cards[current_card_index]["front"], font = ("Arial", 24))
    card_display.pack(pady = 50)
    is_front_side = True

    def show_card():
        side_text = cards[current_card_index]["front"] if is_front_side else cards[current_card_index]["back"]
        card_display.config(text = side_text)

    def flip_card():
        nonlocal is_front_side
        is_front_side = not is_front_side
        show_card()

    def next_card():
        nonlocal current_card_index, is_front_side
        current_card_index = (current_card_index + 1) % len(cards)
        is_front_side = True
        show_card()

    button_frame = tk.Frame(study_window)
    button_frame.pack()

    flip_card_button = tk.Button(button_frame, text = "Flip Card", command = flip_card)
    flip_card_button.pack(side = tk.LEFT, padx = 5)

    next_card_button = tk.Button(button_frame, text = "Next Card", command = next_card)
    next_card_button.pack(side = tk.LEFT, padx = 5)


    
# Initialise main window
root = tk.Tk()
root.title("Flashcard Editor")
root.geometry("400x300")

# Front of card
front_label = tk.Label(root, text = "Front of Card:")
front_text = tk.Text(root, height = 5, width = 40)

# Back of card
back_label = tk.Label(root, text = "Back of Card:")
back_text = tk.Text(root, height = 5, width = 40)

save_card_button = tk.Button(root, text = "Save Card", command = save_flashcard)
study_card_button = tk.Button(root, text = "Study Card", command = study_cards)


front_label.pack()
front_text.pack()
back_label.pack()
back_text.pack()
save_card_button.pack()
study_card_button.pack()

# Start event loop
root.mainloop()