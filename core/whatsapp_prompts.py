from datetime import datetime
import random

greetings_morning = [
    "Bonjour Vanoushka",
    "Coucou Vanoushka",
    "Salut Vanoushka",
    "Hello Vanoushka",
    "Bonne matinée Vanoushka"
]

greetings_evening = [
    "Bonsoir Vanoushka",
    "Bonne soirée Vanoushka",
    "Salut ce soir Vanoushka",
    "Hey Vanoushka",
    "J’espère que ta soirée se passe bien Vanoushka"
]

questions_about_nael = [
    "Comment Naël se porte aujourd’hui ?",
    "Est-ce que Naël mange bien en ce moment ?",
    "Comment se passe son sommeil ces derniers temps ?",
    "As-tu eu un moment calme avec lui aujourd’hui ?",
    "Est-ce qu’il rigole beaucoup en ce moment ?",
    "Il découvre de nouvelles choses ces jours-ci ?",
    "Comment il se réveille en ce moment ?",
    "Tu as remarqué quelque chose de nouveau chez lui ?",
    "Est-ce qu’il a vu son pédiatre récemment ?",
    "As-tu besoin de quelque chose pour Naël ?",
    "Est-ce que tout va bien côté santé avec lui ?"
]

def generate_prompt(period: str) -> str:
    date = datetime.now().strftime("%A %d %B %Y")
    greeting = random.choice(greetings_morning) if period == "matin" else random.choice(greetings_evening)
    question = random.choice(questions_about_nael)

    prompt = (
        f"Nous sommes le {date}. Rédige un message court, bienveillant et naturel d’un père à la mère de son enfant. "
        f"Le message doit commencer par : {greeting}. Il doit poser une seule question sincère sur leur enfant Naël, comme : « {question} ». "
        f"Le ton doit rester simple, respectueux, humain, sans être froid ni distant. "
        f"Ne fais aucune supposition sur ce que le père sait. Ne dis jamais qu’il a vu Naël ou qu’il connaît ce qu’il a fait. "
        f"Ne parle jamais d’amour ou de sentiments amoureux envers la mère. "
        f"Garde le message naturel, comme un vrai SMS rapide et attentionné."
    )

    return prompt
