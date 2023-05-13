# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# player will play as Janus (j)
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
    # show Janus liedown (character) at right
    # show Alex liedown (character) at left
    # "You and Alex lie down together for some time, enjoying the weather and making small talk."
    
    # *sound of a bell interrupts them, signaling them to go to class.*
    scene bg tree shade (background)
    with dissolve
    play sound school bell noloop
    show Alex at left
    show Janus at right
    a "Aw man… Already?"
    a "Welp, I guess I'll see you later then. Have fun with class, I know I won't!"
    j "Thanks. Good luck!"

    # *Alex jumps up from the shade and rushes into the distance as Janus slowly gets up and begrudgingly heads to class, missing the peace and quiet of the shade already.*
    # add an animation or do the following
    # hide Alex with moveoutleft
    # hide Janus with moveoutright

    # *Transition to classroom scene*
    scene Classroom_Day
    "You mutter to yourself in between breaths as you lean your body against the desk, tired from your trek to the classroom."
    show Janus at left
    j "Haaaa… Barely made it…"
    j "Maybe I should find a place closer to class next time… Then again, that would kind of defeat the whole purpose huh?"
    j "At least class today shouldn't be too difficult… It's such a good day for taking a nap too…"
    hide Janus

    scene bg sunshine_from_window
    with dissolve
    "You bask in the gentle and warm sunlight entering through the window as the bell rings to signify the beginning of class."
    
    scene Classroom_Day
    with dissolve
    show Janus
    j "Maybe another day though… I want to actually try to be productive today."
    hide Janus (sitting)
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
    hide Himeko
    hide Mrs. Adams

    show Janus
    j "(It's such a lovely day today. I don't remember the last time the weather was this nice.)"
    j "(Still, it feels unreal that we're getting a new classmate this late in the year. I wonder how things will work out for her…)"
    hide Janus

    show Mrs.Adams at left
    show Himeko at right
    ma "… There is a seat in the back available next to the window."
    ma "anus, can you raise your hand?"

    # *The mention of his name brings Janus’ mind back to reality as he raises his hand.*

    ma "Thank you. I think that's all there is for now."
    ma "Let me know if any issues arise or if you need help. I hope things work out well for you!"
    h "Yes."
    hide Mrs. Adams with moveoutleft
    # *Himeko politely bows to the teacher before approaching her newly designated seat, sitting down quietly next to Janus and directing her gaze to front of the class, ready to receive instruction.*

    h "Hey. Class is starting. You should wake up soon."

    # *Himeko briefly whispers a few words to the boy beside her, stirring him up from his slumber.*
    show Janus at left
    j "Hmm? What's going-"
    j "Ah-"
    # *Janus quickly regains his bearings and whispers a quick gesture of thanks to his savior.*
    j "Thank you. The weather has been too pleasant recently so I couldn't help myself… Aha…"
    h "Don't mention it. I won't wake you up next time."
    j "Noted."
    
    hide Himeko
    hide Janus
    show Janus
    j "(So much for first impressions… Why did the weather have to be so nice today? Oh well. At least I’ll have plenty of time later today to appreciate it.)"



    # This ends the game.

    return
