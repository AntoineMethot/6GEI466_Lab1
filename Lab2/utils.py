import re
from flask import abort

def validate_content(s: str) -> str:
    s = (s or "").strip()
    if not (1 <= len(s) <= 50):
        abort(400, "Invalid length")
    if not re.fullmatch(r"[A-Za-zÀ-ÖØ-öø-ÿ '\-]+", s):
        abort(400, "Invalid characters")
    return s

def validate_date(s: str) -> str:
    s = (s or "").strip()
    if not re.fullmatch(r"\d{2}/\d{2}/\d{4}", s):
        abort(400, "Invalid date format")
    return s

def get_zodiac_sign(date_str: str) -> str:
    # Dummy implementation for zodiac sign based on date
    month, day = map(int, date_str.split('/'))
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    return "N/A"

HOROSCOPES = {
    "Aries": {
        "text": """
        💼 Travail / études
        De nouvelles idées émergent et ta motivation est en hausse. C’est un bon moment pour prendre des initiatives, proposer quelque chose ou te démarquer. Assure-toi simplement de bien communiquer pour éviter les malentendus.

        ❤️ Relations
        Sur le plan relationnel, l’authenticité est clé. Exprime ce que tu ressens, mais sans brusquer les autres. Les échanges honnêtes peuvent renforcer les liens existants ou clarifier une situation floue.

        💪 Énergie & bien-être
        Ton dynamisme est présent, mais pense à canaliser ton énergie. Le sport ou une activité physique t’aidera à évacuer le stress et à garder l’équilibre.

        ✨ Conseil du moment
        Fonce, mais avec intention. Choisis tes combats et fais confiance à ton instinct… tout en gardant un œil sur les détails.
        """,
        "image": "ARIES.png"
    },
    "Taurus": {
        "text": """
        💼 Travail / études
        Tu es en phase de stabilisation et de consolidation. C’est un moment propice à l’organisation, à la planification et à la mise en œuvre de projets. Sois patient et méthodique.

        ❤️ Relations
        Les relations sont plus stables. L’authenticité est importante, mais aussi le respect des limites personnelles. Le partage d’expériences peut renforcer les liens.

        💪 Énergie & bien-être
        Ton énergie est plus stable, mais reste attentif à ton équilibre. Prends soin de toi, surtout si tu es en train de faire face à des situations stressantes.

        ✨ Conseil du moment
        Sois patient et méthodique. La stabilité est ton allié.
        """,
        "image": "TAURUS.png"
    },
    "Gemini": {
        "text": """
        💼 Travail / études
        Tu es en phase de changement et d’adaptation. C’est un moment propice à l’apprentissage, à la communication et à l’échange d’idées. Sois ouvert à de nouvelles perspectives et n’hésite pas à explorer des solutions créatives.

        ❤️ Relations
        Les relations sont plus dynamiques. L’authenticité est importante, mais aussi la capacité à communiquer efficacement. Les échanges peuvent être enrichissants, surtout si tu es ouvert aux différents points de vue.

        💪 Énergie & bien-être
        Ton énergie est élevée, mais reste attentif à ton équilibre mental. Le sport ou une activité physique t’aidera à canaliser ton énergie et à garder un esprit clair.

        ✨ Conseil du moment
        Sois curieux et ouvert. L’apprentissage et l’échange sont tes alliés.
        """,
        "image": "GEMINI.png"
    },
    "Cancer": {
        "text": """
        💼 Travail / études
        Tu es en phase de réflexion et d’introspection. C’est un moment propice à la planification, à la prise de recul et à l’analyse des situations. Sois attentif à tes émotions et n’hésite pas à demander de l’aide si nécessaire.

        ❤️ Relations
        Les relations sont plus sensibles. L’authenticité est importante, mais aussi la capacité à écouter et à comprendre les autres. Le partage d’émotions peut renforcer les liens.

        💪 Énergie & bien-être
        Ton énergie est fluctuante, mais reste attentif à ton équilibre émotionnel. Prends soin de toi, surtout si tu es en train de faire face à des situations stressantes.

        ✨ Conseil du moment
        Sois attentif à tes émotions. La réflexion et l’introspection sont tes alliées.
        """,
        "image": "CANCER.png"
    },
    "Leo": {
        "text": """
        💼 Travail / études       
        Tu es en phase de confiance en toi et d’expression. C’est un moment propice à prendre des initiatives, à te démarquer et à faire valoir tes compétences. Sois ouvert à l’attention que tu reçois, mais reste humble.

        ❤️ Relations
        Les relations sont plus chaleureuses. L’authenticité est importante, mais aussi la capacité à exprimer tes sentiments. Le partage d’expériences peut renforcer les liens.

        💪 Énergie & bien-être
        Ton énergie est élevée, mais reste attentif à ton équilibre. Le sport ou une activité physique t’aidera à canaliser ton énergie et à garder un esprit clair.

        ✨ Conseil du moment
        Sois confiant et authentique. Ton énergie positive peut inspirer les autres.
        """,
        "image": "LEO.png"
    },
    "Virgo": {
        "text": """
        💼 Travail / études
        Tu es en phase de perfectionnement et d’organisation. C’est un moment propice à l’analyse, à la planification et à l’optimisation des processus. Sois attentif aux détails et n’hésite pas à améliorer tes méthodes.

        ❤️ Relations
        Les relations sont plus structurées. L’authenticité est importante, mais aussi la capacité à communiquer clairement. Le partage d’expériences peut renforcer les liens.

        💪 Énergie & bien-être
        Ton énergie est plus stable, mais reste attentif à ton équilibre. Prends soin de toi, surtout si tu es en train de faire face à des situations stressantes.

        ✨ Conseil du moment
        Sois attentif aux détails. La perfection et l’organisation sont tes alliés.
        """,
        "image": "VIRGO.png"
    },
    "Libra": {
        "text": """
        💼 Travail / études
        Tu es en phase d’équilibre et de diplomatie. C’est un moment propice à la collaboration, à l’harmonie et à la prise de décision. Sois ouvert aux différents points de vue et n’hésite pas à chercher un terrain d’entente.

        ❤️ Relations
        Les relations sont plus harmonieuses. L’authenticité est importante, mais aussi la capacité à écouter et à comprendre les autres. Le partage d’expériences peut renforcer les liens.

        💪 Énergie & bien-être
        Ton énergie est plus stable, mais reste attentif à ton équilibre. Prends soin de toi, surtout si tu es en train de faire face à des situations stressantes.

        ✨ Conseil du moment
        Sois diplomate et ouvert. L’équilibre et l’harmonie sont tes alliés.
        """,
        "image": "LIBRA.png"
    },
    "Scorpio": {
        "text": """
        💼 Travail / études
        Tu es en phase de transformation et de profondeur. C’est un moment propice à l’analyse, à la recherche et à la prise de décisions importantes. Sois attentif à tes instincts et n’hésite pas à creuser les sujets en profondeur.

        ❤️ Relations
        Les relations sont plus intenses. L’authenticité est importante, mais aussi la capacité à exprimer tes sentiments. Le partage d’émotions peut renforcer les liens.

        💪 Énergie & bien-être
        Ton énergie est fluctuante, mais reste attentif à ton équilibre émotionnel. Prends soin de toi, surtout si tu es en train de faire face à des situations stressantes.

        ✨ Conseil du moment
        Sois attentif à tes instincts. La profondeur et la transformation sont tes alliées.
        """,
        "image": "SCORPIO.png"
    },
    "Sagittarius": {
        "text": """
        💼 Travail / études
        Tu es en phase d’expansion et d’aventure. C’est un moment propice à l’exploration, à l’apprentissage et à la prise de risques calculés. Sois ouvert aux nouvelles opportunités et n’hésite pas à sortir de ta zone de confort.

        ❤️ Relations
        Les relations sont plus dynamiques. L’authenticité est importante, mais aussi la capacité à communiquer efficacement. Les échanges peuvent être enrichissants, surtout si tu es ouvert aux différents points de vue.

        💪 Énergie & bien-être
        Ton énergie est élevée, mais reste attentif à ton équilibre mental. Le sport ou une activité physique t’aidera à canaliser ton énergie et à garder un esprit clair.

        ✨ Conseil du moment
        Sois aventureux et curieux. L’expansion et l’apprentissage sont tes alliés.
        """,
        "image": "SAGITTARIUS.png"
    },
    "Capricorn": {
        "text": """
        💼 Travail / études
        Tu es en phase de discipline et de responsabilité. C’est un moment propice à la planification, à la mise en œuvre de projets et à la prise de décisions importantes. Sois attentif à tes objectifs et n’hésite pas à travailler dur pour les atteindre.

        ❤️ Relations
        Les relations sont plus sérieuses. L’authenticité est importante, mais aussi la capacité à communiquer clairement. Le partage d’expériences peut renforcer les liens.

        💪 Énergie & bien-être
        Ton énergie est plus stable, mais reste attentif à ton équilibre. Prends soin de toi, surtout si tu es en train de faire face à des situations stressantes.

        ✨ Conseil du moment
        Sois discipliné et responsable. La persévérance est ta meilleure alliée.
        """,
        "image": "CAPRICORN.png"
    },
    "Aquarius": {
        "text": """
        💼 Travail / études
        Tu es en phase d’innovation et de créativité. C’est un moment propice à l’exploration de nouvelles idées, à la collaboration et à la prise de risques calculés. Sois ouvert aux nouvelles perspectives et n’hésite pas à sortir des sentiers battus.

        ❤️ Relations
        Les relations sont plus originales. L’authenticité est importante, mais aussi la capacité à communiquer efficacement. Les échanges peuvent être enrichissants, surtout si tu es ouvert aux différents points de vue.

        💪 Énergie & bien-être
        Ton énergie est élevée, mais reste attentif à ton équilibre mental. Le sport ou une activité physique t’aidera à canaliser ton énergie et à garder un esprit clair.

        ✨ Conseil du moment
        Sois innovant et créatif. L’originalité et la collaboration sont tes alliées.
        """,
        "image": "AQUARIUS.png"
    },
    "Pisces": {
        "text": """
        💼 Travail / études
        Tu es en phase d’intuition et de sensibilité. C’est un moment propice à la réflexion, à la créativité et à l’écoute de tes instincts. Sois attentif à tes émotions et n’hésite pas à exprimer tes idées de manière artistique ou originale.

        ❤️ Relations
        Les relations sont plus empathiques. L’authenticité est importante, mais aussi la capacité à écouter et à comprendre les autres. Le partage d’émotions peut renforcer les liens.

        💪 Énergie & bien-être
        Ton énergie est fluctuante, mais reste attentif à ton équilibre émotionnel. Prends soin de toi, surtout si tu es en train de faire face à des situations stressantes.

        ✨ Conseil du moment
        Sois attentif à ton intuition. La sensibilité et la créativité sont tes alliées.
        """,
        "image": "PISCES.png"
    }
}