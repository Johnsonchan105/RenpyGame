# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Janus")
define h = Character("Himeko")
define a = Character("Alex")
define d = Character("David")
define s = Character("Sam")
define v = Character("Vanessa")
define g - Character("Gwen")
define mra = Character("Mr. Adams")

# The game starts here.

label start:
    # *Game starts off with Janus lying down under the shade of a tree as Alex joins him.*
    # scene bg tree shade (background)
    # with dissolve
    # show Janus (character) at right
    # show Alex (character) at left
    a "Hey Jane! Whatcha doing all the way out here for? It's always a pain in the ass to find you ya know?"
    j "Ah, sorry about that. Homeroom was a bit noisy today and the weather outside looked really pleasant so I couldn’t help myself."
    j "Also, please stop calling me Jane. People are gonna get misunderstandings."
    a "Sorry, no can do. Blame yourself for keeping that mop of hair atop your head."
    a "Things almost as long as Hime's hair for Christ's sake!"
    # hide Janus (character)
    # hide Alex (character)

    # *a scene of introducing Himeko*
    # scene bg somebg (background when introducing someone)
    # with dissolve
    # show Himeko (character)
    "Hime is a girl who recently came from overseas, and is popular in part due to her long, straight, silky black hair."

    # *back to the conversation*
    # scene bg tree shade (background)
    # with dissolve
    # show Janus nervous (character with different emotion) at right
    # show Alex (character) at left
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
    # hide Janus nervous (character)
    # hide Alex (character)

    # *The two lie down together for some time, enjoying the weather and making small talk until the sound of a bell interrupts them, signaling them to go to class.*
    # scene bg tree shade (background)
    # with dissolve
    # show Jenus liedown
    # show Alex liedown
    



    # This ends the game.

    return
