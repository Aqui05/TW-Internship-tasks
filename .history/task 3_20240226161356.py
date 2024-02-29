from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Création d'une instance de ChatBot
chatbot = ChatBot("MonChatBot")

# Création d'un entraîneur pour le chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Entraînement du chatbot sur le corpus de données en anglais
trainer.train("chatterbot.corpus.english")

# Boucle pour permettre à l'utilisateur d'interagir avec le chatbot
while True:
    # Saisie de l'utilisateur
    user_input = input("Vous: ")

    # Sortir de la boucle si l'utilisateur entre "exit"
    if user_input.lower() == 'exit':
        break

    # Obtenir la réponse du chatbot
    response = chatbot.get_response(user_input)

    # Afficher la réponse du chatbot
    print("ChatBot:", response)
