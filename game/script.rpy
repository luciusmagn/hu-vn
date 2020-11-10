# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Neiro", what_slow_cps=30, image="neiro")
define h = Character("Horus", what_slow_cps=20, image="horus")
define a = Character("Alma", what_slow_cps=60, image="alma")
define e = Character("???", what_slow_cps=40)

image poope back = "back.png"
image poope welcome = "welcome.png"
image poope worry_eyes = "worry_eyes.png"
image poope dead_neiro = "dead_neiro"
image poope korubon = "korubon.png"
image poope build = "neiro-build.png"
image horus = "horus.png"
image neiro = "neiro.png"
image alma = "alma.png"

# The game starts here.


label start:

    scene back
    play music "audio/night.mp3"
    show poope korubon
    "..."
    play sound "audio/panting.wav"

    show poope worry_eyes at center

    "this is my fault. i did this to her. and now she's back."

    hide poope worry_eyes

    e "come back!!! neiro, come back you bitch!!!"

    show neiro at left
    n "shit, shit, shit"
    hide neiro

    e "i'll fucking kill you!!!"

    show neiro at left
    n "i need to... i need to run..."

    n "she'll wake someone up with her screams... i have to hurry"
    hide neiro

    e "i swear i'll kill you!"

    play sound ["audio/doorslam.wav", "audio/footsteps-running.wav"]

    "*door slam and running footsteps*"

    show neiro at left
    n "shit, it's cold out here."
    n "where should i even go now? i ruined everything..."
    n "definitely far away from here."

    "*you see an orphanage behind yourself*"

    menu:
        n "but which way do I go?"

        "to the right, towards the center of korubon":
            n "no, someone would recognize me from the orphanage and bring me back..."
            n "it's a matter of time until i'd be face to face with her again"
            n "let's go left instead."

        "to the left, towards...?":
            n "alright, let's go left"

    n "i've never been there... i think it leads out of korubon, for sure, but where to?"
    n "doesn't matter now."

    play sound ["audio/running.mp3"]
    "*running*"

    n "i've been running until i couldnt... then i continued to walk... it's been at least an hour."
    n "how come not a single car passed me by?"

    n "i'm so angry at myself... i messed everything up... i ruined my life but also her life... shit, i don't even deserve to live anymore!"

    n "i-"

    play sound "audio/truck.wav"
    "*truck engine in the distance*"

    n "oh, a car's coming this way. finally... i can leave my miserable life behind."

    play audio "audio/honk.wav"
    "*makes a step into the road, truck honking*"

    menu:
        n "should i let the truck hit me?"

        "yes":
            hide neiro
            play sound "audio/crash.wav"
            show poope dead_neiro at center
            "game over, start again?"
            hide poope dead_neiro
            jump start

        "no":
            n "fuck, fuck, what am i doing?!"
            play sound "audio/crash.wav"
            ""
            "GAME OVER..."
            jump chapter_1

    return

label chapter_1:
    hide neiro
    play sound "audio/glitch.wav"
    show poope welcome
    "..."
    show poope build

    "Neiro Shimohira"
    "AGE: 20"
    "BIRTHDAY: 1.12"
    "HEIGHT: 155cm"
    "HAIR COLOUR: DARK BROWN"
    "EYE COLOUR: BLUE"
    "STRENGTH: OBSERVING, FAST LEARNING, CLIMBING TREES"
    "WEAKNESSES: SOCIAL SITUATIONS, BAD LIFE CHOICES, RUNNING AWAY FROM PROBLEMS"
    "CLOTHING: BLACK COAT, BLACK BOOTS, WHITE SHIRT, BLACK PANTS. BLUE BEANIE"
    hide poope build

    # chapter one
    "june, year x\nlocation unknown\n6:30pm"

    play sound "audio/streetsound.wav"
    show neiro at left
    n "*she stands on the sidewalk, her right eye and half of face are bandaged, people walking by and talking*"

    n "where the hell am i? what is this place?"
    n "this isn't korubon?"
    hide neiro

    show horus at right
    h "nope, this is the city"
    hide horus

    show neiro at left
    n "who are you?"
    hide neiro

    show horus at right
    h "i'm a lightbulb enthusiast from the future"
    hide horus

    show neiro at left
    n "future?"
    hide neiro

    show horus at right
    h "yes, we aren't supposed to meet yet"
    hide horus

    show neiro at left
    n "what?"
    hide neiro

    show horus at right
    h "this is just a way to cuck alma so she gets interested."
    hide horus

    show alma at center
    a "fuck you"
    hide alma

    show horus at right
    h "it's like what they did with the danganronpa demo"
    hide horus

    show neiro at left
    n "what is a dakartonpa?"
    hide neiro

    "To be continued..."
