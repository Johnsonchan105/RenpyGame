# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# player will play as Jenus (j)
define j = Character("You")
define h = Character("Himeko")
define a = Character("Alex")
define d = Character("David")
define s = Character("Sam")
define v = Character("Vanessa")
define g - Character("Gwen")
define ma = Character("Mrs. Adams")

# The game starts here.

label start:
    # *Game starts off with Janus lying down under the shade of a tree as Alex joins him.*
    scene bg tree shade (background)
    with dissolve
    show Janus at right
    show Alex at left
    a "Hey Jane! Whatcha doing all the way out here for? It's always a pain in the ass to find you ya know?"
    j "Ah, sorry about that. Homeroom was a bit noisy today and the weather outside looked really pleasant so I couldn’t help myself."
    j "Also, please stop calling me Jane. People are gonna get misunderstandings."
    a "Sorry, no can do. Blame yourself for keeping that mop of hair atop your head."
    a "Things almost as long as Hime's hair for Christ's sake!"
    hide Janus
    hide Alex

    # *a scene of introducing Himeko*
    scene bg somebg (background when introducing someone)
    with dissolve
    show Himeko
    "Hime is a girl who recently came from overseas, and is popular in part due to her long, straight, silky black hair."

    # *back to the conversation*
    scene bg tree shade (background)
    with dissolve
    show Janus at right
    show Alex at left
    j "Haha… I guess I can't argue with you there… Speaking of, she's transferring into our classes today isn't she?"
    a "That's right! I heard that her parents are super rich, but that's besides that point."
    j "Anyways, did something happen? It's not too often you come seek me out like this."
    # *Brief monologue discussing how Alex is quite popular whereas Janus is quite the opposite.*
    a "Haha… You know… It gets a little stifling when talk goes around so it's nice taking a page from your book every once in a while."
    j "I'll take that as a compliment from the oh-so-popular Prince Charming."
    a "Hey! It's tough being this attractive you know? Sometimes I wish I didn't have so many eyes on me, like you."
    j "Heh. I mean, it gets kinda boring and lonely at times, but at least it's relatively peaceful."
    a "Man… What I wouldn't do for some peace sometimes."
    j "Agreed."
    hide Janus
    hide Alex

    # *The two lie down together for some time, enjoying the weather and making small talk*
    # maybe add an animation for this scene? Otherwise just use what below this comment
    # scene bg tree shade (background)
    # with dissolve
    # show Jenus liedown (character) at right
    # show Alex liedown (character) at left
    # "You and Alex lie down together for some time, enjoying the weather and making small talk."
    
    # *sound of a bell interrupts them, signaling them to go to class.*
    scene bg tree shade (background)
    with dissolve
    play sound school bell noloop
    show Alex at left
    show Jenus at right
    a "Aw man… Already?"
    a "Welp, I guess I'll see you later then. Have fun with class, I know I won't!"
    j "Thanks. Good luck!"

    # *Alex jumps up from the shade and rushes into the distance as Janus slowly gets up and begrudgingly heads to class, missing the peace and quiet of the shade already.*
    # add an animation or do the following
    # hide Alex with moveoutleft
    # hide Jenus with moveoutright

    # *Transition to classroom scene*
    scene Classroom_Day
    "You mutter to yourself in between breaths as you lean your body against the desk, tired from your trek to the classroom."
    show Jenus at left
    j "Haaaa… Barely made it…"
    j "Maybe I should find a place closer to class next time… Then again, that would kind of defeat the whole purpose huh?"
    j "At least class today shouldn't be too difficult… It's such a good day for taking a nap too…"
    hide Jenus

    scene bg sunshine_from_window
    with dissolve
    "You bask in the gentle and warm sunlight entering through the window as the bell rings to signify the beginning of class."
    
    scene Classroom_Day
    with dissolve
    show Jenus
    j "Maybe another day though… I want to actually try to be productive today."
    hide Jenus (sitting)
    show Mrs. Adams
    ma "Alrighty, quiet down class."
    ma "I'm sure you've heard the news but we have a new student transferring into our class today."
    ma "Make sure you treat her nicely ok?"
    hide Mrs. Adams
    show Himeko with moveinleft at left
    "As if on cue, a Japanese beauty enters the classroom, her luscious black hair being blown back from the light autumn wind."
    "The entire class stares at her in awe as she faces the class and starts to introduce herself."
    h "My English isn't the best. Nor are my conversational skills."
    h "I hope we have a pleasant time together."
    "The entire class remains silent, partly due to the strangeness of her introduction."
    # want to add an image of ellipsis to show the class is silent
    show Mrs. Adams at right
    ma "Well class, be sure to be nice to Miss Himeko ok?"
    ma "She's new here and will greatly appreciate any help she can get."
    h "Thank you teacher."
    ma "Well then, here's your…"

    

    # This ends the game.

    return
