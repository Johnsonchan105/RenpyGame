# The script of the game goes in this file.

# define characters
define j = Character("Janus") # player will play as Janus (j)
define h = Character("Himeko")
define a = Character("Alex")
define d = Character("David")
define s = Character("Sam")
define v = Character("Vanessa")
define g = Character("Gwen")
define ma = Character("Mrs.Adams")
define p = Character("Principal")
define vf = Character("Vanessa's Friends")
define ja = Character("Jack") 
define s_a = Character("Student A")
define s_b = Character("Student B")
define u = Character("Unknown")
define i = Character("Detective")

# images of characters
image Janus:
    "janus_normal.png"
    zoom 0.6
image Janus_Angry_Talking:
    "janus_angry_two.png"
    zoom 0.6
image Janus_Sad:
    "janus_sad.png"
    zoom 0.6
image Janus_Angry:
    "janus_angry_one.png"
    zoom 0.6
image Janus_Laugh:
    "janus_laugh.png"
    zoom 0.6
image Janus_Smirk:
    "janus_smirk.png"
    zoom 0.6
image Janus_Suprised:
    "janus_surprised.png"
    zoom 0.6
image Janus_Smile:
    "janus_smile_one.png"
    zoom 0.6
image Janus_Smile_Teeth:
    "janus_smile_three.png"
    zoom 0.6
image Janus_Smile_Closed_Eyes:
    "janus_smile_two.png"
    zoom 0.6
image Himeko:
    "himeko_normal.png"
    zoom 0.6
image Himeko_Angry:
    "himeko_angry.png"
    zoom 0.6
image Himeko_Annoyed:
    "himeko_annoyed.png"
    zoom 0.6
image Himeko_Delighted:
    "himeko_delighted.png"
    zoom 0.6
image Himeko_Laugh:
    "himeko_laugh.png"
    zoom 0.6
image Himeko_Sad:
    "himeko_sad.png"
    zoom 0.6
image Himeko_Sleepy:
    "himeko_sleepy.png"
    zoom 0.6   
image Himeko_Shocked:
    "himeko_shocked.png"
    zoom 0.6
image Himeko_Smug:
    "himeko_smug.png"
    zoom 0.6
image Himeko_Smile_Teeth:
    "himeko_smile_three.png"
    zoom 0.6
image Himeko_Smile_Closed_Eyes:
    "himeko_smile_two.png"
    zoom 0.6
image Alex:
    "alex_normal.png"
    zoom 0.6
image Alex_Angry_Talking:
    "alex_angry_two.png"
    zoom 0.6
image Alex_Angry:
    "alex_angry_one.png"
    zoom 0.6
image Alex_Laugh:
    "alex_laugh.png"
    zoom 0.6
image Alex_Sad:
    "alex_sad.png"
    zoom 0.6
image Alex_Smile_Teeth:
    "alex_smile_three.png"
    zoom 0.6
image Alex_Smile_Closed_Eyes:
    "alex_smile_two.png"
    zoom 0.6
image Alex_Smirk:
    "alex_smirk.png"
    zoom 0.6
image Alex_Suprised:
    "alex_surprised.png"
    zoom 0.6
image David:
    "david_smile_one.png"
    zoom 0.6
image David_Smile_Teeth:
    "david_smile_three.png"
    zoom 0.6
image David_Smile_Closed_Eyes:
    "david_smile_two.png"
    zoom 0.6
image David_Angry:
    "david_angry_one.png"
    zoom 0.6
image David_Laugh:
    "david_laugh.png"
    zoom 0.6
image David_Sad:
    "david_sad.png"
    zoom 0.6
image David_Smirk:
    "david_smirk.png"
    zoom 0.6
image David_Suprised:
    "david_surprised.png"
image Sam:
    "sam_normal.png"
    zoom 0.6
image Sam_Smirk:
    "sam_smirk.png"
    zoom 0.6
image Sam_Suprised:
    "sam_surprised.png"
    zoom 0.6
image Sam_Sad:
    "sam_sad.png"
    zoom 0.6
image Sam_Laugh:
    "sam_laugh.png"
    zoom 0.6
image Sam_Angry_Talking:
    "sam_angry_two.png"
    zoom 0.6
image Sam_Angry:
    "sam_angry_one.png"
    zoom 0.6
image Vanessa:
    "vanessa_normal.png"
    zoom 0.6
image Vanessa_Angry:
    "vanessa_angry.png"
    zoom 0.6
image Vanessa_Annoyed:
    "vanessa_annoyed.png"
    zoom 0.6
image Vanessa_Delighted:
    "vanessa_delighted.png"
    zoom 0.6
image Vanessa_Laugh:
    "vanessa_laugh.png"
    zoom 0.6
image Vanessa_Sad:
    "vanessa_sad.png"
    zoom 0.6
image Vanessa_Shocked:
    "vanessa_shocked.png"
    zoom 0.6
image Vanessa_Smug:
    "vanessa_smug.png"
    zoom 0.6
image Vanessa_Smile_Teeth:
    "vanessa_smile_three.png"
    zoom 0.6
image Vanessa_Smile_Closed_Eyes:
    "vanessa_smile_two.png"
    zoom 0.6
image Principal:
    "principal.png"
    zoom 0.45
image Adams:
    "adams_smile_one.png"
    zoom 0.6
image Jack:
    "jack_normal.png"
    zoom 0.6
image Jack_Angry_Talking:
    "jack_angry_two.png"
    zoom 0.6
image Jack_Sad:
    "jack_sad.png"
    zoom 0.6
image Jack_Angry:
    "jack_angry_one.png"
    zoom 0.6
image Jack_Smirk:
    "jack_smirk.png"
    zoom 0.6
image Jack_Suprised:
    "jack_surprised.png"
    zoom 0.6
image Jack_Smile:
    "jack_smile_one.png"
    zoom 0.6
image grave:
    "grave.png"
image Police:
    "police.png"
    zoom 1.5
image Detective:
    "detective_neutral.png"
    zoom 1.2

# background images
image Classroom_Day:
    "Classroom_Day.png"
image Dorm_Day:
    "Bedroom_Day.png"
image Dorm_Night:
    "Bedroom_Night_Dark.png"
image Cafeteria:
    "Cafeteria_Day.png"
image Hallway:
    "School_Hallway_Day.png"
image Street_Spring:
    "Street_Spring_Day.png"
image Rooftop:
    "Rooftop_Day.png"
image Principle_Office:
    "Principle_Office.jpeg"
    xzoom 2.4
    yzoom 1.8
image Forest_Night:
    "Forest_Night.jpeg"
    xzoom 2.4
    yzoom 1.8
image Black_Screen:
    "Black_Screen.jpeg"
    yzoom 2
image Grove:
    "grove.jpeg"
    yzoom 2
    xzoom 3
image Hospital_Day:
    "hospital_day.jpg"
    xzoom 1.5
    yzoom 1.5
image Hospital_Night:
    "hospital_night.jpg"
    xzoom 1.5
    yzoom 1.5
image Prison:
    "Prison.png"
    xzoom 1.5
    yzoom 1.5


# The game starts here.
label start:
    # *Game starts off with Janus lying down under the shade of a tree as Alex joins him.*
    jump day_one_daytime

label day_one_daytime:
    # *Game starts off with Janus lying down under the shade of a tree as Alex joins him.*
    scene Street_Spring
    with dissolve
    show Janus at right
    show Alex_Smile_Teeth at left
    a "Hey Jane! Whatcha doing all the way out here for? It's always a pain in the ass to find you ya know?"
    show Janus_Smile at right
    j "Ah, sorry about that. Homeroom was a bit noisy today and the weather outside looked really pleasant so I couldn’t help myself."
    j "Also, please stop calling me Jane. People are gonna get misunderstandings."
    a "Sorry, no can do. Blame yourself for keeping that mop of hair atop your head."
    a "Things almost as long as Himeko's hair for Christ's sake!"
    a "Anyhow, summer break is coming in 5 days! You excited?"
    j "Yea, to get away from you" 
    a "Awww you dont mean that, you love me <3"
    j "Whatever you say to delude yourself"
    hide Janus
    hide Alex

    # *a scene of introducing Himeko*
    scene Rooftop
    with dissolve
    show Himeko
    "Himeko is a girl who recently came from overseas, and is popular in part due to her long, straight, silky black hair."
    hide Himeko

    # *back to the conversation*
    scene Street_Spring
    with dissolve
    show Janus_Smile at right
    show Alex_Smile_Teeth at left
    j "Haha… I guess I can't argue with you there… Speaking of, she's transferring into our classes today isn't she?"
    a "That's right! I heard that her parents are super rich, but that's besides that point."
    j "Anyways, did something happen? It's not too often you come seek me out like this."
    a "Haha… You know… It gets a little stifling when talk goes around so it's nice taking a page from your book every once in a while."
    j "I'll take that as a compliment from the oh-so-popular Prince Charming."
    a "Hey! It's tough being this attractive you know? Sometimes I wish I didn't have so many eyes on me, like you."
    j "Heh. I mean, it gets kinda boring and lonely at times, but at least it's relatively peaceful."
    a "Man… What I wouldn't do for some peace sometimes."
    j "Agreed."
    "sound of a bell interrupts them, signaling them to go to class."
    a "Aw man… Already?"
    a "Welp, I guess I'll see you later then. Have fun with class, I know I won't!"
    j "Thanks. Good luck!"

    # *Transition to classroom scene*
    scene Classroom_Day
    "You mutter to yourself in between breaths as you lean your body against the desk, tired from your trek to the classroom."
    show Janus at left
    j "Haaaa… Barely made it…"
    j "Maybe I should find a place closer to class next time… Then again, that would kind of defeat the whole purpose huh?"
    j "At least class today shouldn't be too difficult… It's such a good day for taking a nap too…"
    j "Maybe another day though… I want to actually try to be productive today."
    hide Janus 
    show Adams
    ma "Alrighty, quiet down class."
    ma "I'm sure you've heard the news but we have a new student transferring into our class today."
    ma "Make sure you treat her nicely ok?"
    hide Adams
    show Himeko_Smile_Closed_Eyes at left with moveinleft
    "As if on cue, Himeko enters the classroom, her luscious black hair being blown back from the light autumn wind."
    "The entire class stares at her in awe as she faces the class and starts to introduce herself."
    h "My English isn't the best. Nor are my conversational skills."
    h "I hope we have a pleasant time together."
    "The entire class remains silent, partly due to the strangeness of her introduction."
    show Adams at right
    ma "Well class, be sure to be nice to Miss Himeko ok?"
    ma "She's new here and will greatly appreciate any help she can get."
    h "Thank you teacher."
    ma "Well then, here's your…"
    hide Himeko_Smile_Closed_Eyes
    hide Adams

    show Janus
    j "(It's such a lovely day today. I don't remember the last time the weather was this nice.)"
    j "(Still, it feels unreal that we're getting a new classmate this late in the year. I wonder how things will work out for her…)"
    hide Janus

    show Adams at left
    show Himeko at right
    ma "… There is a seat in the back available next to the window."
    ma "Janus, can you raise your hand?"

    "The mention of his name brings Janus’ mind back to reality as he raises his hand."

    ma "Thank you. I think that's all there is for now."
    ma "Let me know if any issues arise or if you need help. I hope things work out well for you!"
    h "Yes."
    hide Adams with moveoutleft 
    "Himeko politely bows to the teacher before approaching her newly designated seat, sitting down quietly next to Janus and directing her gaze to front of the class."

    h "Hey. Class is starting. You should wake up soon."

    # *Himeko briefly whispers a few words to the boy beside her, stirring him up from his slumber.*
    show Janus at left
    j "Hmm? What's going-"
    j "Ah-"
    hide Janus
    show Janus_Smile at left
    "Janus quickly regains his bearings and whispers a quick gesture of thanks to his savior."
    hide Himeko
    show Himeko_Smug at right
    j "Thank you. The weather has been too pleasant recently so I couldn't help myself… Aha…"
    h "Don't mention it. I won't wake you up next time."
    j "Noted."
    
    hide Himeko_Smug
    j "(So much for first impressions… Why did the weather have to be so nice today? Oh well. At least I’ll have plenty of time later today to appreciate it.)"
    hide Janus_Smile

    "After class"

    s_a "Maan, I'm beat…"
    s_b "I feel you. Why did we have to stay indoors today when the weather is so nice?"

    show Janus at left

    "Janus silently chuckle to himself, glad knowing that he isn't the sole person carrying that sentiment."

    j "(Hmmm… I'll be able to finish my work pretty quickly today so I'll have some free time on my hands. Maybe I should check up on Alex some time today if he's not busy?)"

    "It was then that you noticed an influx of students headed towards your direction, your confusion quickly going away when you realized Himeko was sitting next to you."
    
    show Himeko at right
    j "(Ahh, she's probably going to get grilled today. After all, she's been quite the hot topic these past couple days.)"
    j "(Well, I'm sure she'll be able to handle it. She seems really composed and mature.)"
    
    "The students congregate around Himeko's desk, eager to ask her questions like “How does your daily hair routine look like?” or “Are you currently seeing someone?” before a loud voice silences them."
    
    show Vanessa_Angry at center
    v "Hey! One at a time! You'll overwhelm the poor girl."

    scene Rooftop
    with dissolve
    show Vanessa
    "The girl whose voice is able to control the unruly class is Vanessa, a very popular student with plenty of admirers. She also has a crush on Alex."
    hide Vanessa

    scene Classroom_Day
    show Vanessa at left
    show Himeko at right
    h "Thank you."
    "Himeko lets out a brief sigh of relief before thanking her savior, then proceeding to answer her classmates' questions in a more civilized manner."
    hide Vanessa
    hide Himeko

    show Janus
    j "(Speaking of, it's almost lunch time isn't it? I should probably start heading off…)"
    hide Janus

    scene Hallway
    with dissolve
    show Janus
    "You head off towards the cafeteria, sparing a glance back at his classmates' antics and quietly giggling to yourself."
    hide Janus

    scene Cafeteria

    show Janus
    "Your stomach growling as you put on a hairnet."
    j "(It really sucks working here sometimes. Sometimes I wish I could just eat already, but someone's got to pay the bills.)"

    "Janus finishes donning his work attire just as students start pouring into the cafeteria, beginning a long day of serving food to them."

    "A while later..."

    "Janus is still immersed in his work when he suddenly hears a familiar voice call out to him."
    
    show Alex_Smile_Teeth at left
    a "Hey Jane!"

    "Janus silently palms his forehead before forcing a smile and looking at his friend."
    
    j "Hello Alex. What may I get you today?"
    
    hide Alex_Smile_Teeth

    show Alex at left

    a "Dude, you don’t have to be so formal you know? I’m your friend."

    j "Yes, but this is my job after all. Besides, I thought I told you not to call me that."

    a "Sorry bro, couldn't help myself. Can I get a meatball sub though? I’m pretty damn hungry and am in the mood for one."

    j "Sure. One second."

    "As Janus prepares a sub for his friend, he is suddenly interrupted by Alex"

    hide Alex
    show Alex_Sad at left

    a "Uhhh… Actually, hold that thought. I see David and his cronies. I better get going-"

    j "Ahhh, gotcha. Later then?"

    a "Sounds good, see you soon-"

    "Alex quickly evacuates himself from the cafeteria just as a group of imposing figures enter, the lively atmosphere visibly dampening upon their arrival."

    hide Alex_Sad with fade

    show Janus at right with moveinright
    show David_Smirk at center
    show Sam_Smirk at left

    "The head of the group approaches Janus, towering over him as he grumbles something under his breath."

    d "Seen your friend around?"

    j "Sorry, he just left. May I interest you in something on our menu instead?"

    d "Forget it. Nothing on this menu tastes good anyway. Also, when are you gonna get a damn haircut? That mop of yours ain’t doing you any good."

    "Janus bites his lip as he maintains his composure, the instigator luckily losing interest quickly as he turns around and directs his group."

    d "Come on, let’s get going."

    hide Sam_Smirk

    show Sam_Sad at left

    s "Are you sure David? We’re pretty tired and hungry-"

    hide David_Smirk

    show David_Angry 

    d "Shut it. I don’t need to remind you of your position do I?"

    s "S-sorry. Apologies. Didn’t mean to."

    d "Good. We’re off then."

    "The group promptly leaves the cafeteria, the resulting atmosphere becoming quite awkward before its former liveliness picks up again."
    
    hide David_Angry
    hide Sam_Sad

    "Janus releases a breath he was holding before muttering to himself."

    j "(What a group. Thinking they can get away with anything just because their leader is rich. Makes me wonder how they even ended up like that in the first place.)"

    "Janus calms down a bit before resuming his duties, thinking to himself all the while."

    j "(I should check up on Alex after my shift. Seems like something happened, and whenever David’s involved, it’s not a good sign. Hopefully the weather will still be nice by then.)"

    "The rest of lunch goes by without a hitch as the students enjoy themselves in the cafeteria."

    hide Janus

    scene Rooftop
    "Janus makes his way to the school rooftop, only to see Alex crouched by the corner."
    show Janus at right
    show Alex_Sad at left
    "Janus rushes over to his friend only to see various bruises on him, clearly a sign of a scuffle."
    hide Janus
    show Janus_Suprised at center with moveinright

    j "Alex! Are you ok? What happened?"

    a "Ugh… Don’t shake me like that Jane. I’m still sore all over."

    j "Oh-"

    j "Sorry. Just what the hell happened to you?"

    hide Janus_Suprised
    show Janus

    "Janus starts tending to his friend’s wounds as Alex starts recounting today’s events."

    a "It’s a bit of a long story, but basically, you know Vanessa? That one popular girl? Well we’ve actually known each other for a while, and she tried asking me out today."
    a "Unfortunately, David had her eye on her, and, well, you can probably figure out the rest. Also, why the hell do you have all these medical supplies on you-"

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

    scene Dorm_Night

    show Janus at center

    "Janus makes it to his room as he gets ready for bed, lying down and thinking about today’s events."

    j "(If only something could be done about it, huh? Haa… If only miracles came true more often)."

    "Janus then falls into a deep slumber as he thinks of the upcoming day."
    scene Black_Screen with fade
    hide Janus with fade
    "....."
    "....."
    menu:
        "day2":
            jump day_two_daytime

label day_two_daytime:
    scene Dorm_Day
    show Janus_Suprised with zoomin
    "Janus jolts awake, drenched in sweat and his entire nervous system ablaze as he tries to calm his breathing and nerves."

    j "(Haa… Haa… It was just a nightmare. It’s been a while since I’ve dreamt, especially one that bad.)"

    "Later that day..."

    scene Hallway
    show Janus at right
    "The school was abuzz as Janus arrived on campus, students moving to and fro as commotion filled the halls."
    show Alex_Laugh at left
    a "Yo Jane! Good to see you’re doing alright! Pretty sure the commotion’s getting to you, huh?"

    j "Yeah… Good to see you’re still alive Alex! Did something happen? It’s way too noisy…"

    a "Oh yeah, I forget you’re pretty busy all the time so you must’ve not heard. Anyways, I don’t know the full details, but apparently David’s not here so his dad’s been pretty frantic."
    a "The school seems to be pretty happy though, with The Dark Lord all gone and stuff for now."

    j "Ohhh, so that's what happened… No wonder why I’ve been seeing so many smiles lately."

    a "This calls for a celebration!"

    j "But we have class soon-"
 
    a "DOESN’T MATTER, THE DARK LORD HAS BEEN DEFEATED!!!"

    "Alex gently shoves his friend towards the rooftop, away from the crowd."

    scene Rooftop
    show Janus_Smile at right
    show Alex_Laugh at left

    "Alex hands Janus a warm and delicious smelling package, shortly after Janus’ stomach growls."

    j "Alex…"

    a "Consider this a thanks for yesterday. Besides, I figured you needed it."

    j "Thanks for the meal, I’ll make sure to return the favor."

    a "It’s on the house. Better eat quick though, classes should be starting soon."

    j "I told you…"

    "Janus happily wolfs down the meal his friend bought for him, making small talk between bites before heading back to their respective homerooms."

    scene Classroom_Day

    show Janus_Smile at right
    show Himeko_Smile_Closed_Eyes at left

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

    "The students get ready to leave homeroom before Mrs. Adams stops them."

    ma "Janus? Himeko? Can you please go to the principal’s office? You’ve been requested there."

    "Janus and Himeko exchange confused glances as they nod their heads and start walking towards the principal's office"

    scene Principle_Office

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

    v "Oh hey, it's Alex’s friend. How’s it going?"

    j "Oh hey Vanessa. It’s going alright. What may I get for you today?"

    v "Always so formal aren’t you? Anyways, I’d like a strawberry parfait, while my friends here would like…"

    "Janus gets their food ready as they sit down, Janus overhearing some gossip as he gets their food ready."
    hide Vanessa
    show Vanessa_Smug at left
    vf "So, are you actually interested in him, Vanessa"

    v "I mean, a little I guess? His family’s quite rich though."

    vf "WOW. You sure are heartless sometimes aren’t you? I never would have suspected it."
    hide Vanessa_Smug
    show Vanessa at left
    "The group quiets down as Janus gives them their orders, before leaving with a polite smile."
    hide Vanessa
    show Vanessa_Smug at left
    vf "Aren’t you worried about his friend? They say he’s cursed. People around him go missing like his parents, you know?"

    v "And you believe that? I may be many things but I’m not superstitious you know… Besides, he’s a pretty easy guy to fool. Man barely has a life outside his work and studies."

    "The group chuckles at Vanessa’s words, unaware that Janus is listening in from a distance as he pretends to preoccupy himself."

    vf "If you’re after money why not David? He’s rich."

    v "Yeah but he’s kind of a jerk. Even I have my limits you know…"

    "A long night at the cafe ensues, filled with laughter and an increasingly frustrated Janus."

    scene Dorm_Night
    show Janus at center

    j " Finally… Home…"

    "Janus plops onto the bed, nearly knocking out had it not been for the events that transpired in the cafeteria."

    j "(I hope Alex can see through her facade tomorrow… Then again, he’s not the brightest bulb there is…)"

    "Janus audibly groans in frustration before deciding to call it a day, burying himself under the covers and hoping things turn out well."
    
    scene Black_Screen with fade
    hide Janus with fade
    "....."
    "....."
    menu:
        "day 3":
            jump weekend

label weekend:
    scene Dorm_Day
    show Janus at center

    "Saturday"

    "Janus wakes up in the afternoon, groggily texting his friend good luck with his date before heading back to bed."

    j "(Is it just me or am I more tired recently? Why am I so exhausted and sore? Ugh, my head hurts… I’ll have to make sure to restock on medication some time this week…)"

    "Janus continues lying in bed as he receives a message back a while later, Alex apparently having been stood up."

    j "(That’s odd… I thought for sure she’d be there… Maybe something happened?)"

    "(I’m glad nothing bad happened to Alex, but I can’t help but worry about Vanessa, and possibly David. Maybe I’ll see them in class in a few days? Anyways, I have got to rest up, my head and body are killing me...)"
    
    scene Dorm_Night
    show Janus at center

    "Strange, I feel so tired anyways. Well might as well go to bed"

    scene Black_Screen with fade
    hide Janus with fade
    "....."
    "....."
    menu:
        "day 4":
            jump day4

label day4:
    "Sunday"

    "Janus wakes up late in the afternoon, head splitting from pain as he tries to recall information."

    j "(There’s no way I slept an entire day. I’m sure I got up at some point, but I can’t remember… Ugh, can this damn headache stop?)"

    "Janus relaxingly makes himself dinner, spending the remainder of his weekend catching up on work and hobbies before preparing for another grueling week of school."

    "..."
    scene Black_Screen with fade
    hide Janus with fade
    "....."
    "....."
    menu:
        "day 5":
            jump day_five_daytime

label day_five_daytime:
    scene Hallway
    show Janus_Smile at right

    "The entire school is in murmurs, nowhere near the excitement present on Friday as Janus confusingly makes his way to Alex, soon finding him."

    show Alex_Smile_Teeth at left

    j "Alex!"

    a "Jane!"

    "They smile and shake each other's hands, catching up with one another before addressing the issue at hand."

    j "Hey, do you know why everyone looks so… gloomy?"

    hide Alex_Smile_Teeth
    show Alex_Suprised at left

    a "Seriously…? Did you not check your emails?"    

    j "I’ve sorta been out of it this weekend… Haha…"

    a "What am I gonna do with you…"

    "Alex quickly explains to Janus how no one has seen David, and that authorities have gotten involved."

    a "Apparently, they’re bringing students in for questioning too… Jane… I’m scared… What if they suspect me of something?"
    j "You’ll be fine Alex, I can vouch for your innocence."

    a "Thanks Jane… Still nerve-wracking, you know? First the principal and now this…"

    j "I get you…"

    "Janus sees his friend off with more words of encouragement as he prepares for homeroom."

    scene Classroom_Day
    show Janus at right
    show Adams at center
    ma  " As of today, classes will be canceled for the foreseeable future due to the ongoing investigation. Today’s class is for the purpose of informing you of future policies and plans, as well as…"

    "Mr. Adams informs of how things will be running much to the joy (and dismay) of the students, before ending class early so students could head to their dorms. However, before Janus could leave, he hears a voice call out for him."
    hide Adams
    show Himeko at left

    h "Janus."

    j "Hm? What’s up Himeko?"

    h "My dorm. Follow me. I need help. I’ll explain later, just follow me."

    "The girl takes his hand and drags him with her, seemingly unfazed by the glances they receive as Janus quietly succumbs to his fate, too tired to put up much of a fight."

    scene Dorm_Day
    show Janus_Smile at right
    show Himeko at left

    j "So Himeko, what’s the issue you needed help with?"

    "The two awkwardly sit opposing one another before Himeko decides to speak."

    h "Was it you?"

    j "Excuse me?"

    h "The disappearances."

    j "Umm… What?"

    h "I’m asking if you’re the reason why David and Vanessa are missing."

    j "Umm… No? Hold up, I’m very confused right now-"

    h "You don’t seem to be lying, but I could’ve sworn I saw you in the forest."

    j "In the forest? Why would I be in the forest?"

    h "I told myself that too, and believed my eyes were playing tricks on me, until I saw you there again. That couldn’t have been a coincidence, no?"

    j "I’ve never gone into the forest before though?"

    h "Let’s go together then. I want to see if my eyes are telling the truth."

    h "Also, no is not an option. I’ll confront law enforcement if you don’t comply."

    j "You can be really scary at times, you know that-?"

    "Himeko’s lips curve slightly upwards as her gaze pierces Janus."

    h "Why thank you."

    j "That’s not a compliment you know… Also, why not report this to law enforcement in the first place?"

    "Himeko’s lips give way to a small smile upon hearing this."

    h "You’re an interesting guy. I want to trust you and get to know more about you."

    j "Why thanks, I would’ve been really happy hearing that in a different situation…"

    scene Forest_Night

    show Janus_Smile at center
    show Himeko_Smile_Closed_Eyes at right

    j "Remind me why I’m the one walking first again?"

    h "Safety reasons."

    j "Do you know where we’re going? My head is aching…"

    h "Yes. Don’t worry. We’ll be there soon."

    "The two venture deeper into the forest, Janus’ headache getting worse as Himeko eggs him in the right direction."

    j "Are you sure we’re there yet? Feels like we’re heading in circles."

    h "I am sure. We’re close."

    "The two press onwards, eventually encountering an obscure grove that seems to have met little human interaction."

    h "This is the place."

    scene Grove

    "Janus slowly makes his way in, the sight he sees making his heart drop and blood run cold: one crude gravestone adorned with dried blood."
    show grave at center
    show Janus_Suprised at right

    "The next thing he sees is darkness."

    scene Black_Screen
    "....."
    "....."
    show Janus_Suprised at center
    j "(Am I in a dream again? What’s going on? And why does this bloody headache get worse every damn time?)"

    "Janus’ headache intensifies as flashbacks of distant memories resurface. Of his dying mother, of his missing dad, and now the forest."

    j "(Just what is going on… Someone… Help me… It hurts and I’m scared…)"

    u "Don’t worry Jane, I’ll keep us safe…"

    j "Huh…? Who are you? Why do you know my name?"

    u "Remember, Jane… You know who I am… After all, I’ve always been with you…"

    "Janus’ head threatens to split open as more memories start to pour in. Fragmented images of his parents, of David, of Vanessa, and countless other events."

    u "Remember who always watches you from the shadows… Who makes your dreams come true… Who keeps you safe and happy…"

    u "I’m Jack… And I’m also you…"

    scene Grove
    show Jack_Smirk at left
    show Janus_Suprised at right

    "Janus bolts awake, sweat pouring out of him like crazy as he hyperventilates, noticing a body next to him."

    ja "It’s already too late Jane… She tried to stop us… We had no choice…"

    j "No… This can’t be…"

    "Himeko’s eyes are wide open, blood flowing from the corners of her lips as she struggles to breathe."

    j "HIMEKO!!!"

    "Janus rushes over to her, quickly opening his bag for medical supplies and trying to staunch the bleeding."

    ja "What are you doing Jane…? Saving her would ruin the both of us… Do you know how hard I’ve worked for us?"

    "He ignores the voice in his head as tears run down his face, every part of his body burning as he desperately tries to save his new classmate."

    ja "Everything I’ve done was for the both of us! Who got rid of David when no one could? It was me! I made all your wishes come true! No one else but me!"

    j "Stop… I don’t want your help! YOU KILLED THEM!"

    ja "Jack: Isn’t that what you wanted as well? For them to stop, just like dad?"

    j "No… No… No… Not like this… This can’t be happening… Get out of my head… GET OUT!"

    "Janus' hands don’t stop moving as he hurriedly applies first aid to his classmate, the paleness of her skin accelerating with each passing second."

    ja "Silly Jane, I’m a part of you as much as you are me… Why do you try to save her still? You’ll only bring about the end of both of us you know?"

    j "I don’t care! I’d happily let that happen if it’d keep others safe! I don’t want to live a life that I can’t be proud of!"

    "Himeko’s pulse barely felt as Jane rushes to finish his first aid."

    ja "Stop! Do you want to throw away everything we’ve worked for? Everything we’ve lived for? If it weren’t for me, we would’ve never had the strength to change our future for the better!"
    ja "I was born from you! Born to make your unrealized desires reality! And now you want to oppose me? I wouldn’t have even existed if you had the strength and courage to fight for yourself!"

    j "I, I-"

    ja "If you let her live, your life as you know it will end. I’m sorry for hurting her, but we had no choice! Trust me Jane, you need me. Without me, you would’ve never been able to escape that hellhole years ago. "
    ja "Without me, dad would’ve killed you as well! I’m a part of you Jane, the only one you can truly trust, the only who can truly make you safe and happy." 
    ja "So stop Jane, for your sake, for both our sakes, so that everything we’ve ever worked for isn’t thrown away."

    jump choices
menu choices:
    "Stop the First Aid":
        jump Himeko_dies
    "Continue the First Aid":
        jump Himeko_lives

label Himeko_dies:
    scene Grove
    show Jack_Smirk at center
    ja "That’s it Jane. Let me handle it, as I’ve always have. I’ll make this world a better place for the both of us. Go and take a long nap…"
    show Janus_Angry at left
    j "No... No I won't let you make decisions anymore, I will decide what to do from now on."
    ja "What is done is done. Do as you will, but dont come crying to me when things go wrong"
    hide Jack with fade
    jump choice1

menu choice1:
    "Hide the body":
        jump hide_evidence
    "Run back home":
        jump dorm_arrest
label hide_evidence:
    scene Grove
    show Jack_Smirk at center

    ja "So you couldn't live with the consequence of our actions and you come running back to me. No matter. I'll do as I always has, for the both of us."

    "Jack stuffs several heavy stones into Himeko's pockets and deposits her body into the nearby pond."

    ja "There we go. Nice and clean! Now run along back home Janus and always remember: I am always by your side."

    scene Dorm_Night with fade
    show Janus_Angry at center

    "Memories of Himeko’s screams, blood, and the cold, dark groves start piercing his head. "

    "Janus jumps in front of his mirror. He notices his hair is caked with sweat and dirt, his shoes also stained with mud."

    j "This can’t be – I was just in the woods. How is it 3 AM right now?"

    "Memories of David and Himeko come flashing back. The final look of fear on their faces ... "

    j "He killed Them. Jack killed Them... No..."

    j "I killed Them"

    "Janus couldn't sleep as he laid wide awake in bed, curled up and shivering as he recalled repeatde the events of the night. Why is this all happening?"

    jump Himeko_dies_day_three

label dorm_arrest:
    scene Dorm_Night with fade
    show Janus_Angry at center

    "Memories of Himeko’s screams, blood, and the cold, dark groves start piercing his head. "

    "Janus jumps in front of his mirror. He notices his hair is caked with sweat and dirt, his shoes also stained with mud. His arms and legs feel sore, yet he doesn’t remember doing much physical activity..."

    j "This can’t be – I was just in the woods with Himeko. How is it 3 AM right now?"

    "Memories of David and Himeko come flashing back. The final look of fear on David’s face ... "

    j "He killed Them. Jack killed Them... No..."

    j "I killed Them"

    "Janus couldn't sleep as he laid wide awake in bed, curled up and shivering as he recalled repeatde the events of the night. Why is this all happening?"

    "Suddenly, the loud speaker blared from outside Janus's dorm door"

    "STUDENT JANUS. EXIT YOUR DORM WITH YOUR HANDS UP..."

    "Janus exits his dorm and was led to jail to await his trial."

    jump jail_ending

label Himeko_lives:
    scene Grove
    show Janus at left
    show Himeko_Sleepy at center
    show Jack_Angry at right
    ja "So that’s your choice... Foolish and arrogant until the very end... At least that’s the first time you didn’t run away."
    hide Jack_Angry with fade
    "Some color returns to Himeko. Her breathing is now audible."
    j "I have to get her to the nurse, quickly."

    "Janus carries Himeko to the end of the forest. One of the teachers is probably doing their patrols. They’ll find Himeko and get her care.."

    jump Himeko_lives_day_three

    scene Black_Screen with fade

label Himeko_dies_day_three:
    scene Black_Screen
    "School Announcement “Due to the disappearance of students, there is now a curfew. All students must be in their dorm rooms by nighttime. An official detective has been called and is expected to arrive by tomorrow."
    "Every student will be sharply questioned regarding the disappearances.”"
    scene Rooftop
    show Alex_Suprised at left
    show Janus_Sad at right
    a "Janus! There you are! Did you hear the news? Himeko is now missing too."

    j "I know – I mean yeah…their disappearances must be linked together."

    a "Yeah just be careful at night! Any one of us could be next."

    hide Alex_Suprised
    show Alex at left

    j "And what about you? I haven’t heard from you these past few nights. Hanging out with your new girlfriend?"

    a "Yeah I’ve been – wait a minute are you jealous?"

    j "It feels like you’ve forgotten about me since Vanessa confessed to you!"

    a "Hey I’m allowed to have a relationship aren’t I? But I suppose now is not the time to be sneaking out to see her. She said she heard a rumor."

    a "Apparently David’s parents are furious. They can’t accept the fact their little demon is gone. The school is going to find a scapegoat to detain."

    "Janus feels the color leaving his face."

    j "What do you mean?"

    a "Yeah, Vanessa heard it from her parents. I think it’s kind of dramatic, but his parents hired a detective, the one that’s coming tomorrow." 
    a "The detective has to detain someone, his parents won’t accept the fact that there’s no evidence."

    j "Alex, what if one of us gets detained?"

    a "We’ll be fine, we have nothing to hid–"

    j "Alex! You were with Vanessa, but I don’t have an alibi, they’re just going to detain me."

    a "Jane, c’mon, it’ll be fin-"

    j "No Alex! You don’t understand. You have wealthy parents. Most of this school has wealthy parents. They won’t get detained. But I’m an easy target. David hated me and..."

    a "Janus! I’ll tell the detective we’ve been hanging out together. Okay? Then they’d have no reason to suspect you."

    j "Promise?"

    a "I promise."
    hide Alex
    "If I can just make it out unscathed for two more days. I can go home. Winter break starts this weekend. If I can get away for two more days. I can leave this place."
    "I WON'T get arrested."

    jump Himeko_dies_night_three

label Himeko_lives_day_three:
    scene Black_Screen

    "School Announcement “Last night Himeko was found near the end of the woods injured. Due to Himeko’s injuries and David’s disappearance, there is now a curfew. All students are advised to stay indoors and MUST be in their dorm rooms by nighttime." 
    "An official detective has been called and is expected to arrive by tomorrow. Every student will be sharply questioned regarding the disappearance of David and Himeko’s recent attack."

    scene Rooftop
    show Alex_Suprised at left
    show Janus_Sad at right

    a "Janus! There you are! Did you hear the news? Himeko is in the hospital. She was bleeding a lot when she was found. It sounds like she was attacked last night."

    j "Does she remember what happened to her?"

    "Janus could feel the pounding of his heart against his chest. He felt short of breath."

    "Please, Himeko, please don’t remember anything, Janus prays."

    a "Vanessa visited her earlier. She didn’t really say much."

    j "I’ll visit her too! I need to see how she’s doing..."

    a "Just be careful at night Jane. Any one of us could be next."

    j "And what about you? I haven’t heard from you these past few nights. Hanging out with your new girlfriend?"

    hide Alex_Suprised
    show Alex at left

    a "Yeah I’ve been– wait a minute are you jealous?"

    j "It feels like you’ve forgotten about me since Vanessa confessed to you!"

    a "Hey I’m allowed to have a relationship aren’t I? But I suppose now is not the time to be sneaking out to see her. She said she heard a rumor."

    a "Apparently David’s parents are furious. They can’t accept the fact their little demon is gone. The school is going to find a scapegoat to detain."

    "Janus feels the color leaving his face."

    j "What do you mean?"

    a "Yeah, Vanessa heard it from her parents. I think it’s kind of dramatic, but his parents hired a detective, the one that’s coming tomorrow." 
    a "The detective has to detain someone, his parents won’t accept the fact that there’s no evidence right now."

    j "Alex, what if one of us gets detained?"

    a "We’ll be fine, we have nothing to hid–"

    j "Alex! You’ve been with Vanessa, but I don’t have an alibi, they’re just going to detain me."

    a "Jane, c’mon, it’ll be fin-"

    j "No Alex! You don’t understand. You have wealthy parents. Most of this school has wealthy parents. They won’t get detained. But I’m an easy target. David hated me..."

    a "Janus! I’ll tell the detective we’ve been hanging out together. Okay? Then they’d have no reason to suspect you."

    j "Promise?"

    a "I promise."
    
    hide Alex

    hide Janus_Sad
    show Janus_Angry

    "If I can just make it out unscathed for two more days. I can go home. Winter break starts this weekend. If I can get away for two more days. I can leave this place."
    "I WON'T get arrested."

    jump Himeko_visit

label Himeko_dies_night_three:
    scene Dorm_Night
    show Janus_Sad at center
    "Janus paces back and forth in his room."

    j "I’m going to jail. They’re going to find out Jack, no I, killed them."

    j "But Alex will defend me, it’ll be alright."

    "Janus looks at the woods outside his window. Their bodies are there out there." 
    
    j "I have to find it before the detective does."

    "Janus covers himself in black and sneaks out of his window."

    scene Black_Screen with fade

    jump day_four

label Himeko_visit:
    scene Hospital_Day
    show Janus at left
    show Himeko_Sad at right
    "Himeko lays in a hospital bed. Her hair is tangled, her face and lips are pale from the lost of blood."

    h "Who’s... who’s there?"

    j "Hey Himeko! It’s Janus."

    j "I just wanted to check on you, after I heard about your injuries."

    h "Janus..."

    hide Himeko_Sad 
    show Himeko_Shocked at right

    "A look of confusion, then fear falls on Himeko’s face."

    "‘She must remember something,’ Janus thinks. ‘She’s instinctively scared of me’."

    "Himeko sees the look of fear reflected on Janus’s face and composes herself."

    hide Himeko_Shocked
    show Himeko at right

    h "Janus! Ah, thank you for visiting me. I’ve been having visitors all day. It’s been nice, people here are so caring."

    "A sharp pain goes through Janus’s brain."

    show Jack_Angry at center
    ja "That smile is fake, Janus. She knows you know. She’s playing dumb. You have to eliminate her too! She’s going to rat you out the moment she can!"
    
    j "Ah stop it! Go away!"

    h "What…?"

    j "Ah sorry, I just get these headaches sometimes."

    hide Jack with fade

    "Janus tries to have a friendly conversation with Himeko, but can’t help but feel underlying tension between them."

    "No, If she remembered that I was the one who sent her here, she’d be screaming bloody murder. She doesn’t remember." 
    "But even though she might not remember, she knows I’m suspicious. Who knows if or when she’ll get her memory back."

    "Janus awkwardly bids farewell to Himeko and returns to his dorm"

    jump Himeko_lives_night_three

label Himeko_lives_night_three:
    scene Dorm_Night
    show Janus_Sad at center
    "Janus tries to sleep that night, tossing and turning."

    j "She’s going to out me out eventually... and then I’ll be locked up for the rest of my life."

    j "No, I should just be happy she’s safe and recovering."

    j "Ahh... Maybe I should just sleep this off."

    "..."

    scene Hospital_Night

    show Janus_Suprised at left
    show Himeko_Sleepy at right

    "Janus regains consciousness, realizing he’s no longer in his room – he’s in the nurse’s room with Himeko, his hands held a pillow over her face."

    "Himeko looks so harmless, the moonlight shining on her face."

    j "She’s harmless now, but she’ll be trouble once she recovers."

    jump hospital_menu

menu hospital_menu: 
    "Maybe she truly forgot. I should let her recover.":
        jump good_hospital
    "I can’t take any chances. She has to go":
        jump bad_hospital

label good_hospital:
    scene Hospital_Night
    show Janus at left
    show Himeko_Sleepy at right
    "Janus leaves the nurse’s room and sneaks back into his own room. The worry that Himeko will remember consumes him."
    hide Janus with fade
    jump day_four_good

label bad_hospital:
    scene Hospital_Night

    show Janus at left
    show Himeko_Sleepy at right
    "Janus feels Jack take over his body and he puts the pillow over her face..."
    hide Janus with fade
    show Jack_Angry with fade
    "Small fragments of consciousness pass him - the sound of Himeko choking, her wide eyes in shock - before his memory blackens out."
    hide Himeko_Sleepy with fade
    jump day_four

label day_four:
    scene Dorm_Day
    show Janus_Sad at left
    "Janus is huddled in a corner as he stares at his trembling fingertips, overcome with grief and guilt as his eyes and lungs burn from the anguish he is feeling."
    show Jack_Smirk at right
    ja "Excellent Janus..."
    ja "With this we have secured our livelihood and future..."
    j "No..."
    ja "There's no use in crying over spilt milk. What's important is that we are safe."
    j "I... I don't want to be safe if this is what I need to do..."
    ja "Are you stupid? Why not work towards a better outcome for yourself? David is gone and we're safe, so what's the problem?"
    j "I know..."

    jump choice
menu choice:
    "I just can't accept this outcome...":
        jump pre_jail_scene
    "It just all hurts so much...":
        jump take_over

label take_over:
    scene Dorm_Day
    hide Janus with fade
    show Jack_Smirk at center
    ja "That's right Janus... Just leave everything to me... I'll make sure the world is a better place for the both of us..."
    ja "Why don't you take a long nap and let me take care of it all..."
   
    scene Black_Screen with fade

    "The End"
    return

label day_four_good:
    scene Dorm_Day
    show Janus_Angry at right
    show Jack_Smirk at left
    ja "Are you an idiot? You just jeopardized both our futures! Why couldn't you just get rid of her?"
    j "Shut it, Jack. I've already decided. There's already too much blood on our hands. I refuse to dirty them anymore."
    ja "You...!"
    ja "I hope your decision was the right one. You're not the only one at risk here."
    j "I know, but I don't care. I refuse to live with all this guilt. I can't undo the things that've happened, but I want to try to make things right."
    ja "You and your stupid sense of justice... You better pray that it all pays out for you in the end."
    j "That doesn't matter. What matters is that I try."
    ja "Whatever you say... I'll make sure to clean up after you like always."
    "Jack stops talking, leaving Janus alone with his thoughts, thoughts of worry but also pride in knowing that Himeko is alive."
    ja "They’re looking for someone to blame, remember?."

    j "It’ll probably be me anyway..."

    "Then, Janus feels a jolting headache. He starts breaking out into sweat."

    ja "Are you stupid? FRAME someone. Deflect. I worked too hard to be locked up."

    j "Stop! I don't need your help! I had to clean up your mess!"

    ja "Everything I’ve done is to keep us safe! You should be grateful. Now all you have to do is not get thrown in jail.."

    j "It’s all because of you!"

    ja "I SAVED YOU! Now you just need to find someone else to blame. It’s only a temporary solution. They won't be there forever."

    "Student Janus, come to the principal's office immediately."

    ja "Well lets see how you get out of this one."
    
    j "I'll do it without your help"

    scene Principle_Office
    show Janus_Sad at left
    show Detective at center 
    show Principal at right

    i "Hello Mr. Janus. I am Detective Thomas. As you have probably heard by now, some of your classmates have recently disappeared."

    i "This is just a formal investigation. I am not accusing anyone of anything, I am just gathering information about what has been going on recently." 

    i "Please help me figure out what happened to your classmates and be as accurate and detailed as possible. I want to know what you were doing the night before yesterday?"

    "‘This is not just an investigation,’ Janus thinks. ‘He’s going to detain someone by the end of the night.’" 

    jump investigate_menu

menu investigate_menu:
    "Lie to the detective":
        jump lie
    "Tell the truth":
        jump truth

label lie:
    scene Principle_Office
    show Janus at left
    show Detective at center
    show Principal at right
    j "I was with Alex that night. He’s my best friend."

    i "I see. And have you noticed any tensions between Himeko and David and your other classmates?"

    j "Yeah.    Sam is one of David’s cronies–I mean friends. They didn’t look too happy with each other the last time I saw them."

    "The detective writes in his notepad."

    "It was a long interview, with Janus telling little white lies here and there. What looked like Sam’s annoyance was exaggerated into a possible cause of David’s disappearance."

    i "Thank you for taking the time out of the day for this interview. I understand that you may have concerns about the recent events and I assure you I will find the culprit."

    j "Thank you detective."

    p "Janus you are now dismissed."

    jump day_four_night

label truth:
    scene Principle_Office
    show Janus_Sad at left
    show Detective at center 
    show Principal at right
    "Janus tells the detective the truth. About his alter ego, about what happened to Himeko and David."

    "Janus feels a migraine splitting his head once more."

    ja "How can you be so foolish! You’ve thrown away all our hard work. All the work I’ve done to keep us safe."

    j "I can’t keep living like this. I just can’t live with this guilt. I’m not going to let you hurt more people."

    i "Janus, you are under arrest for causing the disappearence and assulting fellow students."

    i "You have the right to remain silent. Anything you say can and will be used against you in a court of law. You have the right to an attorney. If you cannot afford a lawyer, one will be provided for you."

    jump jail_ending

label day_four_night:
    scene Dorm_Night
    show Janus_Sad at left

    j "That was stressful, but I got out of it fine."

    show Jack_Smile at right

    ja "This is temporary, we must silence others in order to protect us."

    j "No. Lets rest, we need rest in order to make it through to the break."

    "Knocks comes from the door"

    hide Jack_Smile with fade
    
    "Janus walks to the door and opens it, revealing Alex standing in the doorway."
    
    show Alex at right

    a "Hey Jane, you doing alright? You don't look so good."

    j "Yea... yea. It's been a long day man."

    a "Yea I hear ya, did you get called in to be questioned today?"

    j "I did, what about you?"

    a "I also got questioned today and MAN was it stressful."

    j "It sure was, say, do you know where Sam is gonna be tomorrow?"

    a "Uhhh I think he's going to be in the forest with Gwen tomorrow, why?"

    j "Nothing... just wondering"

    a "Well okay, I better be going, Vanessa just texted."

    j "Sounds good! I'll see you tmrw."

    a "Wait! Before I go, how is Himeko, you visited her right?"

    "A tinge of guilt sprang through Janus"

    j "Yea... she's alright, although last I heard she doesn't remember anything of the night."

    a "I'm glad shes better now. I really hope they caught whoever that attacked her."

    "The feeling of guilt increased within Janus"

    j "I hope they do too."

    a "Alright man, I really gotta run. I'll see ya tomorrow! Keep yourself safe."

    j "Will do. See ya.+"

    hide Alex with fade

    show Jack_Suprised at right

    ja "Janus, it our perfect chance!"

    j "I don't know if I want to..."

    ja "CHOOSE OR PERISH"

    jump day_4_choice

menu day_4_choice:
    "Refuse":
        jump day_5_jail
    "Take action":
        jump take_action

label take_action:
    scene Dorm_Night
    show Janus_Angry at left
    show Jack_Smirk at right

    j "ALRIGHT ALRIGHT I GET IT. Fine. Lets do it."

    ja "Finally you're taking steps to protect yourself. Now I don't have the be the one to step in."

    j "What should I do???"

    ja "Murder someone you simpleton! How DENSE are you?"

    j "But who..."

    jump murder_H

menu murder_H:
    "Himeko":
        jump H_murder
    "Sam":
        jump S_murder
    "Vanessa":
        jump V_murder
    "Alex":
        jump A_murder
    "Gwen":
        jump G_murder
    "No one":
        jump No_murder
menu murder:
    "Sam":
        jump S_murder
    "Vanessa":
        jump V_murder
    "Alex":
        jump A_murder
    "Gwen":
        jump G_murder
    "No one":
        jump No_murder
label No_murder:
    scene Dorm_Night
    show Janus_Angry_Talking at left
    show Jack_Suprised at right

    j "No, I'm not going to do it. You've done enough already."

    ja "Don't you get it? Its the perfect-"

    j "No means no, now leave."

    ja "Fine, if you don't do anything, I will."

    j "What??? NO!"

    jump fight

label A_murder:
    scene Dorm_Night
    show Janus at left
    show Jack_Smile at right

    ja "Alex is the right choice. He knows us too wel. He needs to go."

    hide Janus
    show Janus_Angry_Talking at left

    j "WHAT? NO??? WHAT ARE YOU SAYING?"

    ja "You know I'm right."

    j "You know what, this has gone too far. I'm going to turn myself in."

    hide Jack_Smile
    show Jack_Angry_Talking

    ja "Fine, I'll do it myself."

    j "NO!"

    jump fight

label V_murder:
    scene Dorm_Night
    show Janus at left
    show Jack_Smirk at right

    ja "Vanessa is the right choice. Remember how she said she was only with Alex for his money? She needs to go."

    j "But Alex loves..."

    ja "Do you want to see your friend suffer??? One way or another its not going to end well."
    
    hide Janus
    show Janus_Sad at left

    j "..."

    j "I'm sorry Alex."

    scene Black_Screen with fade

    "..."
    jump arrest

label S_murder:
    scene Dorm_Night
    show Janus_Angry at left
    show Jack_Smirk at right

    ja "Sam is the right choice. He bullied you alongsides David, do not let him go free for what he did to you."

    j "...."

    j "Fine."

    scene Black_Screen with fade

    "..."
    jump arrest

label arrest:
    scene Dorm_Day
    show Janus at left

    "Janus woke up to the sound of banging on his dorm door."

    hide Janus
    show Janus_Suprised at left

    "STUDENT JANUS. YOU ARE UNDER ARREST FOR THE SUSPISION OF ASSULT AND HOMICIDE. EXIT YOUR DORM WITH YOUR HANDS UP."

    "Janus exits his dorm and was led to jail to await for his trial"

    jump jail_ending



label G_murder:
    scene Dorm_Night
    show Janus_Sad at left
    show Jack_Smirk at right

    ja "Gwen is the right choice. Since Sam is going with her to the forest tomorrow, this is the perfect opportunity to frame him."

    j "...."

    j "Fine."

    scene Black_Screen with fade

    "..."

    jump day_5_ending

label H_murder:
    scene Dorm_Night
    show Janus at left
    show Jack_Smirk at right

    ja "Himeko is the right choice, who knows what she'll tell."

    "Hands shaking, Janus recalls the sensations that night in the forest as Himeko gasped for air."

    hide Janus
    show Janus_Angry_Talking at left

    j "No."

    ja "What?"

    j "I won't do it, I'm going to turn myself in tomorrow. This can't go on, I can't hurt anyone else."

    hide Jack_Smirk
    show Jack_Angry_Talking

    ja "Fine, I'll do it myself."

    j "NO."

    jump fight

menu fight:
    "Resist Jack":
        jump day_5_jail
    "Let go":
        jump take_over

label day_5_jail:
    scene Dorm_Night
    show Janus_Angry at left
    show Jack_Suprised at right

    j "No I'm not gonna do anything, you've already done enough damage. I'm turning myself in."
    
    ja "You idiot, deal with this yourself then."

    hide Jack with fade

    j "Sigh, lets head to sleep."

    scene Black_Screen with fade
    hide Janus with fade
    "..."

    jump truth

label day_5_ending:
    scene Hallway
    show Janus_Sad at left
    "There are a lot of hushed whispers during the day. Janus walks around, trying to hear the gossip."
    
    show Vanessa_Shocked at right

    vf "They locked up Sam! Apparently the detective thought he was the most suspicious."

    v "Sam huh? I’d always thought it would be Janus. Who knows what he’s thinking with that creepy demeanor of his."

    hide Vanessa_Shocked with fade

    "Janus starts breaking into sweat."

    j "Sam is locked up because of me..."

    "Janus and Alex meet up to say their goodbyes before winter break."
    
    show Alex_Smile_Closed_Eyes at right

    j "I’ll miss you man. Thank you for being my one true friend here."

    a "Jane, you don’t always have to be so formal with me. It’s not like I’ll never see you again. Unless you also get taken out by the killer. "

    "A pang of guilt shocks Janus."

    a "Ah... bad timing. Sorry."

    j "No, you’re all good."

    jump safe_end

label safe_end:
    scene Dorm_Night

    show Janus_Sad at left

    j "I can’t believe it, I got away. I get to go away from this place, but Sam’s still there."

    show Jack_Smirk at right

    ja "See, aren’t you glad? I got rid of the school bully, got his crony locked up in jail."

    j "No, this isn’t right...I...we hurt innocent people."

    ja "And It’s your right! The school would have never done anything to David had we not taken action."

    j "I never asked for your help! Things would have been better off without you."

    ja "You did ask for my help! I’ve been with you all along, eliminating people, framing Sam."

    j "There could have been another way!"

    ja "Really? Remember all those times you tried to report David? All the times the teachers wouldn’t risk their jobs to get David in trouble?" 
    ja "If the school won’t seek justice, it’s only right that we do."

    j "It doesn't change the fact that we hurt them."

    ja "It was all for you and only you. Now just sit tight and get out."

    "Janus clutched at his head, and falling onto the floor."

    scene Black_Screen with fade

    "The end"
    return

label pre_jail_scene:
    scene Dorm_Day
    show Jack_Suprised at right
    show Janus_Angry at left
    j "I'm tired of being trampled over. To be forced to be witness. That's why I'm going to make things right."
    j "I'm turning myself in. You can't stop me Jack. I've made up my mind."
    ja "You! You would trample over everything we've been through just to satisfy your stupid sense of justice!?"
    j "Yes. I refuse to live a life in which I can't even be proud of myself. Goodbye Jack."
    ja "....."
    ja "If that's what you've decided, I can't change our fate."
    ja "I still think you're too stupid, simple, and naive."
    hide Jack with fade
    jump truth

label jail_ending:
    scene Prison
    show Janus_Sad at center

    j "When did things go so wrong? I just wanted to live a normal life..."
    
    "The presence of Jack lingers in the edge of Janus's conciousness, threatening to take over any second."

    j "I won't let you. Not again, not ever for as long as I live."

    show Jack at right

    ja "Remember that I am you, and you are me. We will always be together for as long as we live."

    "Jack's presence fades, but Janus knows with certainty that he will be back."

    hide Jack

    scene Black_Screen with fade

    "The End"
    return
