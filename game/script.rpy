# The script of the game goes in this file.

# Deklaruje jednotlivý postavy co vystupujou
# Neni nutný pro každej kus dialogu deklarovat postavu
# Možnosti viz wiki

# Objekt/proměnnou postavy je možný pojmenovat libovolnym způsobem,
# pokud název obsahuje jen čísla (nesmí začínat číslem), ASCII písmena
# a podtržítka

define n = Character("Neiro", what_slow_cps=30, image="neiro")
# what_slow_cps nastavuje, že se text vypisuje znak po znaku
define h = Character("Horus", what_slow_cps=20, image="horus")
# image má nastavit rodinu obrázků, ale ještě nevim jak to funguje
define a = Character("Alma", what_slow_cps=60, image="alma")
define e = Character("???", what_slow_cps=40)

# obrázky je možný organizovat do rodin/grup. Z jedný rodiny může
# bejt aktivní pouze jeden obrázek, vyvolání dalšího yeetne ten
# předchozí

# cesta k obrázku je relativní k `images/`
# narozdíl od zvuků je potřeba obrázky takhle registrovat
# jako objekty/proměnný
image poope back = "back.png"
image poope welcome = "welcome.png"
image poope worry_eyes = "worry_eyes.png"
image poope dead_neiro = "dead_neiro"
image poope korubon = "korubon.png"
image poope build = "neiro-build.png"

# "scény" jsem dal do jedný rodiny, zatim má každá postava jen
# jeden obrázek, takže neni třeba vytvářet grupu
image horus = "horus.png"
image neiro = "neiro.png"
image alma = "alma.png"

# Tady začíná samotná hra.
# Hry v renpy jsou tvořený sekvencí příkazů,
# který se obdobně jako v jinejch programovacích jazycích
# spouštěj odshora dolů jeden po jednom, pokud něco nezmění
# běh programu

# renpy organizuje programy pod návěští/labely,
# mezi kterejma jde skákat.
#
# Můžeš mít například univerzální label pro gameover.
# Nebo label pro každou kapitolu, speciální situace atd.
# pro jméno labelu platí stejný pravidla jako pro ostatní
# identifikátory, viz řádky 7-9
label start:
    # nastaví scénu
    # pokud nejsou přiložený další nastavení, viz odkaz v README.md,
    # tak to akorát zobrazí příslušnej obrázek na pozadí.
    # back (tj. images/back.png) je definovanej automaticky
    # byl jsem línej to měnit
    scene back
    # přehrává audio na kanálu hudby, kanálů je víc. Jenom na kanálu
    # `audio` může hrát víc zvuků najednou, další kanály jsou
    # `sound` pro zvukový efekty a `voice` pro dabing
    play music "audio/night.mp3"
    # zobrazí obrázek korubonu
    show poope korubon
    # textová replika, jen tři tečky aby to nepřekáželo
    "..."
    # hraje udejchanou ženskou jako sound efekt
    play sound "audio/panting.wav"

    # zobrazý obrázek `worry_eyes` na středu obrazovky,
    # další před-definovaný pozice existujou, viz mozek a wiki
    show poope worry_eyes at center

    # replika bez postavy která by jí řikala
    "this is my fault. i did this to her. and now she's back."

    # odebere obrázek ze scény, korubon jsme dávat pryč nemuseli,
    # protože korubon a worry_eyes jsou v jedný grupě, takže
    # došlo k automatickýmu nahrazení
    hide poope worry_eyes

    # Nella (se jménem nastavenym na ???) nadává
    e "come back!!! neiro, come back you bitch!!!"

    # zobrazí repliku Neiro a její obrázek po levý straně
    # schová ho potom co domluví.
    show neiro at left
    n "shit, shit, shit"
    hide neiro

    e "i'll fucking kill you!!!"

    show neiro at left
    n "i need to... i need to run..."

    n "she'll wake someone up with her screams... i have to hurry"
    hide neiro

    e "i swear i'll kill you!"

    # pokud člověk chce aby hráli dva zvuky po sobě, tak
    # je potřeba použít tuhle syntaxi, jinak příkaz play
    # zastaví předchozí hrající audioklip
    #
    # popř. je možné použít queue, ale to už je zbytečně extra
    # povolený formáty: wav, mp3, ogg, opus
    #
    # pokud možno, tak opus je nejefektivnější z těhlech formátů
    play sound ["audio/doorslam.wav", "audio/footsteps-running.wav"]

    "*door slam and running footsteps*"

    show neiro at left
    n "shit, it's cold out here."
    n "where should i even go now? i ruined everything..."
    n "definitely far away from here."

    "*you see an orphanage behind yourself*"

    # menu, zprostředkovává výběr možností,
    # obsah menu musí být odsazený o jednu úroveň dál
    # (pozor na mezery vs. tabulátory, musí to být konzistentní jinak to
    # hodí chybu, která se otravně hledá)
    #
    # menu by mělo začínat dialogem, který mu předchází
    menu:
        n "but which way do I go?"

        # jednotlivé možnosti jsou textové řetězce ukončené dvojtečkou
        # o další úroveň odsazený je obsah skriptu, který se má spustit
        # pokud hráč zvolí danou možnost
        "to the right, towards the center of korubon":
            n "no, someone would recognize me from the orphanage and bring me back..."
            n "it's a matter of time until i'd be face to face with her again"
            n "let's go left instead."

        # pro volby který mají větší vliv na plinutí příběhu
        # je vhodné skákat na další návěští spíš než to mastit
        # do bloku sem
        "to the left, towards...?":
            n "alright, let's go left"

    n "i've never been there... i think it leads out of korubon, for sure, but where to?"
    n "doesn't matter now."

    play sound "audio/running.mp3"
    "*running*"

    n "i've been running until i couldnt... then i continued to walk... it's been at least an hour."
    n "how come not a single car passed me by?"

    n "i'm so angry at myself... i messed everything up... i ruined my life but also her life... shit, i don't even deserve to live anymore!"

    n "i-"

    play sound "audio/truck.wav"
    "*truck engine in the distance*"

    n "oh, a car's coming this way. finally... i can leave my miserable life behind."

    # tady zneužíváme kanál `audio`, abychom mohli zároveň přehrávat
    # audio záznam jak motoru náklaďáku tak troubení
    play audio "audio/honk.wav"
    "*makes a step into the road, truck honking*"

    menu:
        n "should i let the truck hit me?"

        # v tomto bloce je první případ kdy může Neiro exnout,
        # pokud hráč zvolí špatnou možnost, skočíme na label start
        # tudíž na začátek
        "yes":
            hide neiro
            play sound "audio/crash.wav"
            show poope dead_neiro at center
            "game over, start again?"
            hide poope dead_neiro
            jump start

        # pokud zvolí správně, tak skočíme na návěští první kapitoly
        "no":
            n "fuck, fuck, what am i doing?!"
            play sound "audio/crash.wav"
            ""
            "GAME OVER..."
            jump chapter_1

    # pokud label končí nebo obsahuje příkaz `return`
    # tak `return` ukončuje běh skriptu daného návěští
    # a předává kontrolu vyšší instanci
    #
    # např. pokud by v chapter_1 byl return, vrátil by se
    # program sem k tomuto komentáři
    #
    # label start by měl mít return vždycky prej
    return

# label pro první kapitolu
# tady už by to mělo bejt docela jasný,
# hehe
label chapter_1:
    # prázdné řádky jsou programu jedno
    # programátoři je používají pro přehlednost.
    # je lepší dát související příkazy spolu a oddělit
    # je od ostatních prázdným řádkem
    #
    # co znamená "související" je subjektivní,
    # v renpy se nabízí spolu oddělovat repliky jednotlivých postav
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

    # konec programu
    "To be continued..."
