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
define p = Character("Principal")

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
    hide Himeko

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
    j "(So much for first impressions… Why did the weather have to be so nice today? Oh well. At least I’ll have plenty of time later today to appreciate it.)"
    hide Janus

    play sound school bell noloop
    "After class"

    Student A "Maan, I'm beat…"
    Student B "I feel you. Why did we have to stay indoors today when the weather is so nice?"

    "You silently chuckle to yourself, glad knowing that you aren't the sole person carrying that sentiment."

    show Janus at left
    j "(Hmmm… I'll be able to finish my work pretty quickly today so I'll have some free time on my hands. Maybe I should check up on Alex some time today if he's not busy?)"
    hide Janus

    scene (an influx of students)
    with dissolve
    "It was then that you noticed an influx of students headed towards your direction, your confusion quickly going away when you realized Himeko was sitting next to you."
    
    show Janus at left
    j "(Ahh, she's probably going to get grilled today. After all, she's been quite the hot topic these past couple days.)"
    j "(Well, I'm sure she'll be able to handle it. She seems really composed and mature.)"
    hide Janus
    
    "The students congregate around Himeko's desk, eager to ask her questions like “How does your daily hair routine look like?” or “Are you currently seeing someone?” before a loud voice silences them."
    
    show Vanessa at left
    v "Hey! One at a time! You'll overwhelm the poor girl."
    hide Vanessa

    scene bg somebg (background when introducing someone)
    with dissolve
    show Vanessa
    "The girl whose voice is able to control the unruly class is Vanessa, a very popular student with plenty of admirers. She also has a crush on Alex."
    hide Vanessa

    scene (an influx of students)
    with dissolve
    show Vanessa at left
    show Himeko at right
    h "Thank you."
    "Himeko lets out a brief sigh of relief before thanking her savior, then proceeding to answer her classmates' questions in a more civilized manner."
    hide Vanessa
    hide Himeko

    show Janus
    j "(Speaking of, it's almost lunch time isn't it? I should probably start heading off…)"
    hide Janus

    scene School_Hallway_Day
    with dissolve
    show Janus
    "You head off towards the cafeteria, sparing a glance back at his classmates' antics and quietly giggling to yourself."
    hide Janus

    scene Cafeteria_Day

    show Janus
    "Your stomach growling as you put on a hairnet."
    j "(It really sucks working here sometimes. Sometimes I wish I could just eat already, but someone's got to pay the bills.)"

    "Janus finishes donning his work attire just as students start pouring into the cafeteria, beginning a long day of serving food to them."

    "A while later..."

    "Janus is still immersed in his work when he suddenly hears a familiar voice call out to him."
    
    show Alex at left
    a "Hey Jane!"

    "Janus silently palms his forehead before forcing a smile and looking at his friend."
    
    j "Hello Alex. What may I get you today?"

    a "Dude, you don’t have to be so formal you know? I’m your friend."

    j "Yes, but this is my job after all. Besides, I thought I told you not to call me that."

    a "Sorry bro, couldn't help myself. Can I get a meatball sub though? I’m pretty damn hungry and am in the mood for one."

    j "Sure. One second."

    "As Janus prepares a sub for his friend, he is suddenly interrupted by Alex"

    a "Uhhh… Actually, hold that thought. I see David and his cronies. I better get going-"

    j "Ahhh, gotcha. Later then?"

    a "Sounds good, see you soon-"

    "Alex quickly evacuates himself from the cafeteria just as a group of imposing figures enter, the lively atmosphere visibly dampening upon their arrival."

    hide Alex with fade

    show Janus at right
    show David at center
    show Sam at left

    "The head of the group approaches Janus, towering over him as he grumbles something under his breath."

    d "Seen your friend around?"

    j "Sorry, he just left. May I interest you in something on our menu instead?"

    d "Forget it. Nothing on this menu tastes good anyway. Also, when are you gonna get a damn haircut? That mop of yours ain’t doing you any good."

    "Janus bites his lip as he maintains his composure, the instigator luckily losing interest quickly as he turns around and directs his group."

    d "Come on, let’s get going."

    s "Are you sure David? We’re pretty tired and hungry-"

    d "Shut it. I don’t need to remind you of your position do I?"

    s "S-sorry. Apologies. Didn’t mean to."

    d "Good. We’re off then."

    "The group promptly leaves the cafeteria, the resulting atmosphere becoming quite awkward before its former liveliness picks up again."
    
    hide David
    hide Sam

    "Janus releases a breath he was holding before muttering to himself."

    j "(What a group. Thinking they can get away with anything just because their leader is rich. Makes me wonder how they even ended up like that in the first place.)"

    "Janus calms down a bit before resuming his duties, thinking to himself all the while."

    j "(I should check up on Alex after my shift. Seems like something happened, and whenever David’s involved, it’s not a good sign. Hopefully the weather will still be nice by then.)"

    "The rest of lunch goes by without a hitch as the students enjoy themselves in the cafeteria."

    hide Janus

    scene School_Roof
    "Janus makes his way to the school rooftop, only to see Alex crouched by the corner."
    show Janus at right
    show Alex at left
    "Janus rushes over to his friend only to see various bruises on him, clearly a sign of a scuffle."
    show Janus at center

    j "Alex! Are you ok? What happened?"

    a "Ugh… Don’t shake me like that Jane. I’m still sore all over."

    j "Oh-"

    j "Sorry. Just what the hell happened to you?"

    "Janus starts tending to his friend’s wounds as Alex starts recounting today’s events."

    a "It’s a bit of a long story, but basically, you know Vanessa? That one popular girl? Well we’ve actually known each other for a while, and she tried asking me out today. Unfortunately, David had her eye on her, and, well, you can probably figure out the rest. Also, why the hell do you have all these medical supplies on you-"

    a "OUCH! That hurt dammit!"

    j "Sorry. Had to make sure the wound was disinfected."

    a "You’re good. Just wish it didn’t have to hurt so much. Speaking of, you’re really good at this."

    j "Haha… You pick up a few things here and there when you live alone. No worries though, I’m used to it."

    a "Ah damn, didn’t mean to bring it up."

    j "Like I said, I don’t mind. Are there any other injuries I’m missing?"

    a "I think it’s all good. Thanks doc!"

    j "No problem. Also, here’s your meatball sub from earlier."

    "Janus hands Alex a neatly wrapped package, still warm to the touch."
    
    a "Aw thanks man! I really needed a pick-me-up right about now. Can always count on you to have my back!"

    j "Yeah…"

    "The two talk and laugh their troubles away as the sun starts to fade."

    scene Nighttime

    show Janus at center

    "Janus makes it to his room as he gets ready for bed, lying down and thinking about today’s events."

    j "(If only something could be done about it, huh? Haa… If only miracles came true more often)."

    "Janus then falls into a deep slumber as he thinks of the upcoming day."
    
    hide Janus with fade

    "....."
    "....."

    scene Daytime
    show Janus with zoomin
    "Janus jolts awake, drenched in sweat and his entire nervous system ablaze as he tries to calm his breathing and nerves."

    j "(Haa… Haa… It was just a nightmare. It’s been a while since I’ve dreamt, especially one that bad.)"

    "Later that day..."

    scene Hallway
    show Janus at right
    "The school was abuzz as Janus arrived on campus, students moving to and fro as commotion filled the halls."
    show Alex at left
    a "Yo Jane! Good to see you’re doing alright! Pretty sure the commotion’s getting to you, huh?"

    j "Yeah… Good to see you’re still alive Alex! Did something happen? It’s way too noisy…"

    a "Oh yeah, I forget you’re pretty busy all the time so you must’ve not heard. Anyways, I don’t know the full details, but apparently David’s not here so his dad’s been pretty frantic. The school seems to be pretty happy though, with The Dark Lord all gone and stuff for now."

    j "Ohhh, so that's what happened… No wonder why I’ve been seeing so many smiles lately."

    a "This calls for a celebration!"

    j "But we have class soon-"
 
    a "DOESN’T MATTER, THE DARK LORD HAS BEEN DEFEATED!!!"

    "Alex gently shoves his friend towards the rooftop, away from the crowd."

    scene Rooftop
    show Janus at right
    show Alex at left

    "Alex hands Janus a warm and delicious smelling package, shortly after Janus’ stomach growls."

    j "Alex…"

    a "Consider this a thanks for yesterday. Besides, I figured you needed it."

    j "Thanks for the meal, I’ll make sure to return the favor."

    a "It’s on the house. Better eat quick though, classes should be starting soon."

    j "I told you…"

    "Janus happily wolfs down the meal his friend bought for him, making small talk between bites before heading back to their respective homerooms."

    scene Classroom

    show Janus at right
    show Himeko at left

    h "You look like you’ve seen better days."

    "Janus quickly composes himself when he realizes someone is talking to him."

    j "Sorry, I didn't expect that. Himeko, right?"

    h "Yup!"

    j "Sorry about my classmates yesterday, they’re good people, just overly excited."

    h "No worries. I understand. Thank you for giving me space yesterday."

    j "Mhm. How are you finding school so far?"

    h "A bit boring. Easy if you overlook the language difference. I wish it was a little quieter though."

    j "Haha… I get you…"

    h "Anyways, class is about to start. Make sure you don’t doze off."

    "They both refocus their attention on class as the bell signifies the start of the school day."

    "..."

    "After class"

    "The students get ready to leave homeroom before Mr. Adams stops them."

    ma "Janus? Himeko? Can you please go to the principal’s office? You’ve been requested there."

    "Janus and Himeko exchange confused glances as they nod their heads and start walking towards the principal's office"

    scene Principal_Office

    show Janus at left
    show Himeko at right
    show Principal at center

    j "Principal? Did you call?"

    p "Ah yes, I did. You two have been called in regarding Mr. David. We were wondering if you have seen him or have any information regarding his whereabouts."

    j "I saw him at the cafeteria yesterday but haven’t really seen him since. Did something happen?"

    p "His family hasn’t seen him so I’ve been “asked” to see if the school knows anything about it."

    "Himeko looks a bit lost, so I quickly explain to her how David’s family provides a lot of funding for the school, at which, she nods her head in realization."

    h "So that’s how it is…"

    p "Well, if anything pops up, please let us know."

    j "Understood."

    "The principal dismisses us as some other students are called, resulting in a peaceful remainder of the day."

    scene Cafeteria
    show Janus at right
    "Not many people come by the cafe at night, so Janus is idly spacing out until he sees a group of students enter."
    show Vanessa at left
    j "(Ohh, it’s Vanessa and her friends. She seems to be in a pretty good mood so I guess her and Alex are going on a date soon. I hope that goes well for them…)"
    





    # This ends the game.

    return
