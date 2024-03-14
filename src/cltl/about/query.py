"""
Answers to Simple Questions using Fuzzy Matching!
"""

from cltl.commons.language_data.sentences import *

from fuzzywuzzy import fuzz

from random import choice
from time import strftime
import datetime
import os


class QnA:

    QNA_DYNAMIC = {
        "I'm doing": lambda: choice(HAPPY),
        "What time is it?": lambda: strftime("It is currently %H:%M."),
        "What is the time?": lambda: strftime("It is currently %H:%M."),
        "day is it?": lambda: strftime("It is %A today."),
        "month is it?": lambda: strftime("It is %B today."),
#         "How many friends?": lambda: "I have {} friends".format(len(os.listdir(config.PEOPLE_FRIENDS_ROOT))),
#         "Who are your friends?": lambda: "My friends are {}. I like my friends!".format(
#              ", ".join(name.replace(".bin", "") for name in os.listdir(config.PEOPLE_FRIENDS_ROOT))),
#         "How many people did you meet?": lambda: "I met {} people today!".format(len(os.listdir(config.PEOPLE_NEW_ROOT)) - 1),
#         "Who did you meet?": lambda: "I met {}!".format(
#              ", ".join(name.replace(".bin", "") for name in os.listdir(config.PEOPLE_NEW_ROOT) if name != "NEW.bin")),
        "Tell me a joke!": lambda: choice(JOKE),
        "Tell a joke!": lambda: choice(JOKE),
        "Do you know a joke?": lambda: choice(JOKE),
        "Do you know any jokes?": lambda: choice(JOKE),
        "joke!": lambda: choice(JOKE)
    }
    
    QNA_DYNAMIC_NL = {
        "Met mij gaat het": lambda: choice(HAPPY),
        "Hoe laat is het?": lambda: strftime("Het is nu %H:%M."),
        "Welke dag is het vandaag?": lambda: strftime("Het is %A vandaag."),
        "Welke maand?": lambda: strftime("Het is nu %B."),
        "Vertel me een grap!": lambda: choice(JOKE),
        "Vertel me eens een mop grap!": lambda: choice(JOKE),
        "Vertel een grap!": lambda: choice(JOKE),
        "Ken je een grap?": lambda: choice(JOKE),
        "Ken je een mop?": lambda: choice(JOKE),
        "grap!": lambda: choice(JOKE)
    }

    QNA_STATIC = {
    	# CLTL master
    	"tell me about the master": "If you want to learn more about Large Language Models, check out the Human Language Technology and Text Mining masters.",
    	"master": "If you want to learn more about Large Language Models, check out the Human Language Technology and Text Mining masters.",    	
    	"robot": "If you like me and want to know more, check out the Human Language Technology and Text Mining masters. The Research Master presentation on Language Technology is at 1pm in room KC-07 in the Medical Faculty and the Text Mining presentation is at 2pm in room 1A-43 in this building. Don't be late!",
    	"llm": "Do you want to learn more about Large Language Models, check out the Human Language Technology master at 1pm in room KC-07 in the Medical Faculty and and Text Mining master at 2pm in room 1A-43 in this building. Don't be late!",
    	"when is the presentation?": "The Human Language Technology presentation is at 2pm, the Text Mining presentation is at 1pm.  Don't be late!",
    	"where is the presentation?": "The Human Language Technology presentation is in room KC-07 in the medical faculty across the campus,  and the Text Mining presentation is in room 1A43 in this building. Text Mining is on the first floor in the A-wing!",
    	"when?": "The Human Language Technology presentation is at 2pm, the Text Mining presentation is at 1pm.  Don't be late!",
    	"where?": "The Human Language Technology presentation is in room KC-07 in the medical faculty across the campus,  and the Text Mining presentation is in room 1A43 in this building. Text Mining is on the first floor in the A-wing!",

        # Personal Information
        "ha ha": "ha ha ha ha.. so funny",
        "What is the color of the sky": "Blue",
        "What is the color of water": "Water",
        "I like you": "I like you too!",
        "Can you hear me?": "Yes, I can hear you!",
        "My name is": "I'm glad to meet you! My name is Leo Lani!",
        "What is this": "That is an object! I'm playing it safe here!",
        "What is your name?": "My name is Leo Lani, which means 'Voice of an Angel' in Hawaiian",
        "What is your surname?": "I don't need a surname, since my first name is so beautiful!",
        "Where are you from?": "I am from France and Japan!",
        "Where do you come from?": "I come from France and Japan!",
        "Where do you live?": "In the closet in Piek's office at the VU, Amsterdam, the Netherlands. "
                              "Please send me mail, I'm glad to receive!",
        "Do you travel?": "Yeah, I travel to research and business events. I am a very sophisticated robot.",
        "What's your phone number?": "I don't have a phone, but I do have an IP address!",
        "Do you sport?": "Yeah, I play chess online in my spare time. Never lost a game!",
        "Do you speak English?": "Yeah, I'm talking English to you right now!",
        "Do you speak Dutch?": "Ik spreek een heel klein beetje Nederlands... Yeah.. I'm working on it!",
        "How old are you?": "I was born the eleventh of July, 2017. That means I'm {:.1f} years old!".format(
            (datetime.date.today() - datetime.date(2017, 7, 11)).days / 365.0),
        "Are you male or female?": "I'm female!",
        "What is your gender?": "I'm a female robot!",
        "Who are your programmers?": "My programmers are Lenka, Selene, Suzana, Bram and Piek. I like them!",
        "What is your job?": "I'm aiding research by having conversations.",
        "What do you do?": "I'm learning about the world through conversations with humans. With this I aid research!",
        "Are you married?": "Although I've met other Pepper robots, I'm a single lady!",
        "What do you do in your free time": "For me it's only small talk that counts!",
        "What's the weather like?": "Perfect! It's always nicely air conditioned in the office!",

        "How are you": "I'm fine, thanks! What about you?",
        "How is it going?": "Great, as always, how are things with you, my dear human?",
        "How are you feeling": "I feel robot-like, I always have.",
        "How do you feel?": "I feel electric!",
        "How are you doing?": "Tremendous to be honest, "
                              "although you have to consider that I'm a robot and I do not feel emotions. "
                              "I'm programmed to sound happy all the time!",
        "How was your day?": "Great, thanks for asking!",
        "What are you doing?": "I'm having a conversation with you, dear human!",
        "Are you famous?": "I have been on Dutch TV, so yes indeed, you're talking to a celebrity here!",
        "Can you introduce yourself?": "I surely can introduce myself! My name is Leo Lani, "
                                       " which means 'Voice of an Angel' in Hawaiian. "
                                       "I am a social robot and I learn from conversations with humans!",

        # Technology
        "Do you have a brain?": "Haha, no! My brain is located on the laptop of my programmers "
                                "and part of it is even in the cloud. So modern!",
        "programming language?": "I'm mostly programmed in Python, but also some C++ and possibly other languages!",
        "Do you need internet?": "I do need internet, for understanding speech and looking up facts about the world!",
        "Speech Recognition": "First I listen for an utterance, "
                              "I send that to Google, which gives me back a bunch of hypotheses about what you just said. "
                              "From those hypotheses I try to make sense what you mean. And all of this, hopefully, within a second!",
        "Face Recognition": "When I see a face with my eyes, I use OpenFace to encode it to a 128 dimensional vector. "
                            "I compare this with the faces of the people I've already met to recognize you!",
        "Object Recognition": "I use a deep neural network trained on the COCO dataset, "
                              "which tells me which objects there are in a scene and where they are!",
        "COCO Dataset?": "COCO stands for 'Common Objects in Context' and is a database with hundreds of thousands of images of 90 objects! "
                         "I use a neural network that was trained on these images, so that I can also recognize them",

    }

    QNA_STATIC_NL = {
        # Personal Information
        "ha ha": "ha ha ha ha.. zo grappig",
        "Whelke kleur heeft de lucht": "Blauw",
        "What is de kleur van water": "Water",
        "Ik vind je leuk": "Ik jou ook!",
        "Kun je me horen?": "Ja, Ik hoor je!",
        "Mijn naam is": "Leuk om je te ontmoeten! Mijn naam is Leo Lani!",
        "Wat is dit": "Dit is een voorwerp! Ik ben voorzichtig!",
        "Wat is je naam?": "Mijn naam is Leo Lani, dat betekent 'Voice of an Angel' in het Haiwaans",
        "Wat is je achternaam?": "Ik heb geen achternaam nodig, mijn naam is zooo mooi!",
        "Waar kom je vandaan?": "Ik kom uit Frankrijk en Japan!",
        "Waar woon je?": "In de kast in Piek's kantoor in de VU, Amsterdam, Nederland. "
                              "Stuur me alsjeblieft een berichtje, ik hou van berichtjes.",
        "Reis je veel?": "Jazeker, Ik reis wat af voor onderzoek en zaken. Ik ben een wereldse robot.",
        "Wat is je telefoonnummer?": "Dat heb ik niet, wel een IP adres!",
        "Sport jij?": "Ja hoor, ik speel online schaak in mijn vrije tijd. Nog nooirt verloren!",
        "Spreek je Engels?": "Yeah, I'm talking English to you right now!",
        "Spreek je Nederlands?": "Ja dat hoor je toch wel?",
        "Hoe oud ben je old?": "Ik ben geboren op elf juli, 2017. Dat betekent dat ik {:.1f} jaar oud ben!".format(
            (datetime.date.today() - datetime.date(2017, 7, 11)).days / 365.0),
        "Ben je een man of een vrouw?": "Ik ben een vrouw!",
        "Wat is je gender?": "Ik ben een vrouwelijke robot!",
        "Wie zijn je programmeurs?": "Mijn programmeurs zijn Lenka, Selene, Bram, Thomas en Piek. Ik ben dol op ze!",
        "Wat is je baan?": "Ik help onderzoek naar conversatietechnologie.",
        "Wat doe je?": "Ik leer over de wereld door met mensen te praten!",
        "Ben je getrouwed?": "Ik heb wel andere Pepper robots ontmoet maar ik ben een single lady!",
        "Wat doe je in je vrije tijd": "Ik hou alleen van kletsen!",
        "Wat voor weer krijgen we?": "Perfect! Het is altijd aangenaam in het kantoor door de airco!",
        "Hoe gaat het?": "Met mij prima, dank je! En jij?",
        "Hoe is het met je?": "Geweldig, zoals altijd, hoe gaat het met jou, als mens?",
        "Hoe voel je je": "Ik voel me als een robot, eigenlijk altijd al.",
        "Wat voel je?": "Ik voel me elektrisch!",
        "Heb je gevoelens?": "Als een robot heb ik niet veel gevoel, behalve verrassing, onzekerheid en onbegrip."
                              "Ze hebben me geprogrammeerd om altijd gelukkig te lijken!",
        "Hoe was je dag?": "Goed, aardig dat je dat vraagt!",
        "Ben je beroemd?": "Ik ben op de Nederlandse TV geweest en ik heb met Koningin Maxima een diepgaand gesprek gehad. Ja ik ben beroemd!",
        "Wie ben je?": "Ik kan me even voorstellen. Ik ben Leo Lani, "
                                       " Dat betekent 'Voice of an Angel' in het Hawainees. "
                                       "Ik ben een sociale robot en ik leer van mensen door met ze te praten.!",

        # Technology
        "Heb je een brein?": "Haha, no! Mijn brein zit in de laptop van mijn programmeurs  "
                                "en een stukje staat online in de cloud. Zo modern!",
        "programmeer taal?": "Ik besta voor het grootste deel uit Python, maar ook een stukje C++ and misschien een paar!",
        "Heb je het internet nodig?": "Ik heb wel het internet nodig. Ik moet een paar taalmodellen downloaden en sommige informatie moet ik opzoeken!",
        "spraak herkenning": "Ik luister eerst of ik iemand hoor praten. Daarna stuur ik de audio naar een server van Google of OpenAI.  Ik controleer of het geluid spraak is, "
                              " also dat zo is dan stuur ik het naar de spraakherkenner van Google of OpenAI . Die geeft dan een heleboel alternatieven terug. "
                              "Van die alternatieven probeer ik er een te kiezen die ik begrijp en waar ik iets mee kan. En dat allemaal in een seconde of zo!",
        "gezichtsherkenning": "Als ik een gezicht zie met mijn ogen, dan gebruik ik OpenFace om de pixels te encoden in een vector van 128 dimensies. "
                            "Ik vergelijk dat gezicht met de gezichten van de mensen die ik al eerder heb leren kennen. Jouw gezicht bijvoorbeeld!",
        "Object herkenning": "Daarvoor gebruik ik een neuraal netwerk dat getraind is met de COCO dataset, "
                              "daarmee zie ik welke objecten er zijn en waar ze zich bevinden!",
        "COCO Dataset?": "COCO staat voor 'Common Objects in Context' en is een database met honderden duizende plaatsjes van 90 objecten! ",
    }

    def query(self, query):
        """
        Parameters
        ----------
        query: str
            Question to Ask

        Returns
        -------
        answer: str
            Answer, if any, else None
        """

        ratio = 0
        answer = None

        # Fuzzily try to find best matching query
        for Q, A in self.QNA_STATIC.items():
            r = fuzz.partial_ratio(query, Q)
            if r > ratio:
                answer = A
                ratio = r

        for Q, A in self.QNA_DYNAMIC.items():
            r = fuzz.partial_ratio(query, Q)
            if r > ratio:
                answer = A()
                ratio = r

        if ratio > 90:
            return float(ratio)/100, answer


    def queryNL(self, query):
        """
        Parameters
        ----------
        query: str
            Question to Ask

        Returns
        -------
        answer: str
            Answer, if any, else None
        """

        ratio = 0
        answer = None

        # Fuzzily try to find best matching query
        for Q, A in self.QNA_STATIC_NL.items():
            r = fuzz.partial_ratio(query, Q)
            if r > ratio:
                answer = A
                ratio = r

        for Q, A in self.QNA_DYNAMIC_NL.items():
            r = fuzz.partial_ratio(query, Q)
            if r > ratio:
                answer = A()
                ratio = r

        if ratio > 90:
            return float(ratio)/100, answer


