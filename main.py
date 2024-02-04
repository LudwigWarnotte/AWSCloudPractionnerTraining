import requests
import random
from colorama import Fore, Style
import bs4
import os
import keyboard


def clear_console():
    # Efface le contenu de la console
    os.system('cls')

def load_random_question():
    print("loading new question...")
    # URL de la page avec la liste des questions
    url_questions = 'https://www.freecram.net/torrent/Amazon.CLF-C02.v2023-12-04.q222.html'

    # Récupère le contenu de la page avec la liste des questions
    response_questions = requests.get(url_questions)
    html_content_questions = response_questions.content

    # Analyse le contenu HTML de la page des questions
    html = bs4.BeautifulSoup(html_content_questions, 'html.parser')

    # Trouve tous les liens des questions disponibles
    question_links = html.find_all('a', href=lambda href: href and '/question/' in href)

    # Vérifie s'il y a des liens de questions disponibles
    if question_links:
        # Sélectionne aléatoirement un lien de question
        random_question_link = random.choice(question_links)['href']

        # Construit l'URL de la question aléatoire
        random_question_url = f'https://www.freecram.net{random_question_link}'

        # Récupère le contenu de la page de la question aléatoire
        response_question = requests.get(random_question_url)
        html_content_question = response_question.content

        # Analyse le contenu HTML de la question aléatoire
        soup_question = bs4.BeautifulSoup(html_content_question, 'html.parser')

        # Trouve la question, les options, la réponse et l'explication
        question_div = soup_question.find('div', class_='qa-question')
        options_div = soup_question.find('div', class_='qa-options')
        correct_answer_div = soup_question.find('div', style='margin:10px 0px;font-weight:bold;')
        explanation_div = soup_question.find('div', class_='qa_explanation')

        # Vérifie si les éléments sont trouvés
        if all((question_div, options_div, correct_answer_div, explanation_div)):
            question = question_div.text.strip()  # Récupère la question
            options = [option.next_sibling.strip() for option in options_div.find_all('strong')]  # Récupère les options
            correct_answer = correct_answer_div.find('span').text.strip()  # Récupère la réponse correcte
            explanation = explanation_div.text.strip()  # Récupère l'explication

            # Affiche la question en gras
            clear_console()
            print(f"{Style.BRIGHT}Question : {question}{Style.RESET_ALL}")
            for index, option in enumerate(options):
                print(f"{chr(65 + index)}. {option}")

            # Demande à l'utilisateur de choisir une réponse
            user_answer = input("Choisissez une réponse (A, B, C, D) : ").upper()

            # Vérifie si la réponse est correcte et affiche l'explication
            if user_answer == correct_answer:
                print(f"{Fore.GREEN}{Style.BRIGHT}Bonne réponse!{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}{Style.BRIGHT}Mauvaise réponse. La réponse correcte est {correct_answer}{Style.RESET_ALL}")
            
            print(f"{Fore.GREEN}Explication de la réponse :{Style.RESET_ALL}")
            print(f"{explanation}")

            return True  # Retourne True si une question a été affichée avec succès

    print("Aucune question disponible.")
    return False  # Retourne False s'il n'y a pas de question à afficher

# Boucle pour charger et afficher plusieurs questions
while True:
    os.system('cls')
    print("|############################################################|")
    print("|                AWS CLOUD PRACTIONER TRAINING               |")
    print("|############################################################|")
    load_random_question()
    print("Appuyez sur la touche Espace pour passer à la question suivante, ou 'N' pour quitter.")
    
    while True:
        if keyboard.is_pressed(' '):  # Vérifie si la touche espace est enfoncée
            load_random_question()
        elif keyboard.is_pressed('N'):  # Vérifie si la touche 'N' est enfoncée
            exit()  # Remplacez cela par le code que vous voulez exécuter lorsque l'utilisateur appuie sur 'N'