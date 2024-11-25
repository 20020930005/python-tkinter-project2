import tkinter as tk
from tkinter import messagebox


def generate_story():
    name = name_entry.get()
    person = person_entry.get()
    adjective = adjective_entry.get()
    birdname = birdname_entry.get()
    mistrygift = gift_entry.get()

    if not all([name, person, adjective, birdname, mistrygift]):
        messagebox.showwarning("Input Error", "Please fill in all the fields!")
        return

    story = (f"On a quiet island, a lonely lighthouse keeper named {name} "
             f"discovered a mysterious bottle washed ashore.\n"
             f"Inside was a letter from a {person}, lost at sea, "
             f"pleading for rescue and leaving coordinates.\n"
             f"Determined, Nora braved a storm in her {adjective} boat, "
             f"following the map to a deserted reef.\n"
             f"There she found not a man, but a {birdname} repeating, "
             f"“Help me!” beside a treasure chest.\n"
             f"As the bird perched on her shoulder, the chest revealed {mistrygift} "
             "and the sailor’s journal, detailing how the parrot had been his only companion.")

    messagebox.showinfo("Your Story", story)


# Create the main window
root = tk.Tk()
root.title("Madlib Game")
root.geometry("450x500")
root.configure(bg="#ffefd5")  # Pale peach background

# Add a colorful header
header = tk.Label(root, text="🌟 Welcome to the Madlib Game 🌟",
                  font=("Helvetica", 16, "bold"), bg="#ffefd5", fg="#ff4500")
header.pack(pady=10)


# Helper function to create styled labels and entry fields
def create_labeled_entry(root, label_text, bg_color, fg_color):
    label = tk.Label(root, text=label_text, font=("Helvetica", 12), bg=bg_color, fg=fg_color)
    label.pack(pady=5)
    entry = tk.Entry(root, width=40, font=("Helvetica", 10))
    entry.pack(pady=5)
    return entry


# Input fields with colorful labels
name_entry = create_labeled_entry(root, "Enter a Name:", "#ffefd5", "#000080")
person_entry = create_labeled_entry(root, "Name a Person (farmer, sailor, doctor):", "#ffefd5", "#000080")
adjective_entry = create_labeled_entry(root, "Specify an Adjective (big, small, tall):", "#ffefd5", "#000080")
birdname_entry = create_labeled_entry(root, "Name a Bird (parrot, crow, peacock):", "#ffefd5", "#000080")
gift_entry = create_labeled_entry(root, "Name a Gift (gold coin, magic watch, diamonds):", "#ffefd5", "#000080")

# Add a colorful button
generate_button = tk.Button(root, text="✨ Generate Story ✨",
                            command=generate_story,
                            font=("Helvetica", 14, "bold"),
                            bg="#4682b4", fg="#ffffff", activebackground="#5f9ea0", activeforeground="#ffffff")
generate_button.pack(pady=20)

# Add a footer for fun
footer = tk.Label(root, text="Have fun creating your unique story! 🌈",
                  font=("Helvetica", 10, "italic"), bg="#ffefd5", fg="#2e8b57")
footer.pack(pady=10)

# Run the application
root.mainloop()
