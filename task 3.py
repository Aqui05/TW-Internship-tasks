import tkinter as tk
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Création d'une instance de ChatBot
chatbot = ChatBot("MonChatBot")

# Création d'un entraîneur pour le chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Entraînement du chatbot sur le corpus de données en anglais
trainer.train("chatterbot.corpus.english")

# Fonction pour gérer l'interaction avec le chatbot
def send_message():
    user_input = user_entry.get()
    
    # Sortir de l'application si l'utilisateur entre "exit"
    if user_input.lower() == 'exit':
        root.destroy()
        return
    
    # Obtenir la réponse du chatbot
    response = chatbot.get_response(user_input)
    
    # Afficher la réponse du chatbot
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, "Vous: " + user_input + "\n")
    chat_history.insert(tk.END, "ChatBot: " + str(response) + "\n\n")
    chat_history.config(state=tk.DISABLED)
    
    # Effacer l'entrée utilisateur
    user_entry.delete(0, tk.END)

# Création de la fenêtre principale
root = tk.Tk()
root.title("ChatBot Interface")

# Zone de texte pour afficher l'historique du chat
chat_history = tk.Text(root, height=15, width=50, state=tk.DISABLED)
chat_history.pack(padx=10, pady=10)

# Zone d'entrée pour que l'utilisateur puisse saisir du texte
user_entry = tk.Entry(root, width=50)
user_entry.pack(padx=10, pady=10)

# Bouton pour envoyer le message
send_button = tk.Button(root, text="Envoyer", command=send_message)
send_button.pack(pady=10)

# Exécution de la boucle principale
root.mainloop()
