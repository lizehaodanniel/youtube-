# -*- coding: utf-8 -*-
"""ACT 1（第 1–22 镜）：凌晨 1:47 的厨房 —— 把观众放进处境里，再抛出「7% 这条线」。

这一幕不教任何东西，只做三件事：
    ① 让观众认出自己（1–5 镜）
    ② 让他亲手搜一次，看到两套互相矛盾的答案（6–11 镜）
    ③ 抛出分界线：答案不是立场，是一个数字（12–22 镜）
"""
from stick_world import B  # noqa: F401

BEATS = [
    # ---------------------------------------------------------------- 1–5 认出自己
    B(
        "It's 1:47 in the morning and you're still at the kitchen table.",
        "凌晨 1 点 47 分，你还坐在厨房桌前。",
        "kitchen_night", ("you",),
        "He sits alone at the warm oak table with both forearms flat on the wood, shoulders "
        "rounded forward, head bowed, eyes fixed on a phone lying face up directly in front of "
        "his hands.",
        "Camera is a low three-quarter medium shot from across the table, framing him from "
        "mid-thigh up, the pendant bulb hanging just above and behind his head.",
        "The single warm amber pendant bulb throws a tight pool of light onto the tabletop and "
        "leaves the kitchen corners in deep warm shadow, with cold blue night leaking in through "
        "the window. The mood is exhausted, private and completely still.",
        "a low three-quarter medium shot from across the table with the pendant lamp in the upper "
        "left of frame",
        "the pendant bulb above the table, which sways a few degrees as the refrigerator motor "
        "kicks on behind him",
        "he lifts his right hand off the tabletop, reaches forward and turns the phone face up, "
        "then leaves his fingertips resting on the screen without tapping it",
        "pushes in slowly and tilts slightly right, because his whole attention is narrowing down "
        "onto that one glowing rectangle",
        "his shoulders lift and drop once on a long slow breath and his left hand curls into a "
        "loose fist flat on the wood",
        "a medium close shot of his bowed face with the pale phone glow reflected in both eyes "
        "and the dark kitchen swallowing the background",
    ),
    B(
        "The laptop is closed. The phone is face up. The number hasn't moved.",
        "电脑合着。手机屏幕朝上。那个数字一动不动。",
        "kitchen_night", ("you",),
        "His two hands rest flat on the table either side of the phone, fingers spread wide and "
        "completely still, the closed laptop pushed back against the wall behind him with its "
        "lid shut.",
        "Camera is a high medium shot angled down over his shoulder from behind and slightly "
        "above, showing the whole tabletop and the top of his bowed head.",
        "Warm amber light pools on the wood between his hands while the rest of the kitchen stays "
        "in soft darkness, and the phone screen adds a cold pale rim along his knuckles. The mood "
        "is stale, waiting, and slightly hopeless.",
        "a high medium shot angled down over his shoulder from behind, the whole table in frame",
        "the cold mug beside his left hand, which trembles almost imperceptibly as the fridge "
        "vibrates through the counter",
        "he drags both hands slowly backward across the wood until only his fingertips still "
        "touch the table, then stops with his palms lifted",
        "holds completely still and locked off, because this is a moment where nothing is "
        "happening and stillness itself is the tension",
        "he lowers both palms back down flat and his thumbs begin to press hard into the "
        "tabletop edge",
        "a high medium shot of his two open hands bracketing the lit phone on the dark wood",
    ),
    B(
        "Eight thousand on a card. Four hundred and twelve in savings.",
        "信用卡欠 8000，存款 412。",
        "kitchen_night", ("you",),
        "He leans back in the wooden chair with his spine against the backrest, one hand lifted "
        "to his forehead with the fingers spread across his brow, the other hand lying open and "
        "empty on the table.",
        "Camera is a medium wide shot from the dark hallway doorway looking into the kitchen, so "
        "he is framed small and off-centre by the door frame.",
        "The warm pendant bulb is the only warm source and it falls short of the doorway, leaving "
        "the foreground frame in near darkness, while blue night light from the window rims his "
        "shoulder. The mood is small, exposed and quietly ashamed.",
        "a medium wide shot from the dark hallway doorway, he sits small and off-centre inside "
        "the bright doorway rectangle",
        "the loose window pane over the sink, which rattles once as a truck passes outside",
        "he lifts his right hand from his forehead, drags it down over his eyes and mouth, then "
        "lets it drop heavily onto the table",
        "drifts forward two slow feet into the kitchen, because we are being pulled into the room "
        "with him",
        "he pushes himself upright in the chair and both hands come down flat on the table, "
        "fingers spread, gripping nothing",
        "a medium wide shot from just inside the kitchen with him upright at the table and the "
        "dark hallway now behind the camera",
    ),
    B(
        "You made seventy thousand this year. That's the part that doesn't fit.",
        "你今年挣了 7 万。这才是说不通的地方。",
        "kitchen_night", ("you",),
        "He stands now, turned half away from the table, both hands gripping the back of the "
        "wooden chair, head tipped forward, staring at the empty chair seat as if it had said "
        "something to him.",
        "Camera is a medium shot from the side at chest height, shooting along the line of the "
        "table so the chair back cuts diagonally across the frame.",
        "Warm amber light from the pendant lamp catches one side of his face and leaves the other "
        "half in soft shadow, the window behind him a flat rectangle of cold blue. The mood is "
        "confused, defensive, and slightly angry.",
        "a side-on medium shot at chest height with the chair back cutting diagonally across "
        "frame",
        "the chair legs on the laminate floor, which scrape a short arc as he shifts his weight "
        "forward onto the balls of his feet",
        "he straightens both arms and pushes the chair back away from the table, then lets his "
        "hands stay gripping the top rail with his knuckles whitening",
        "tracks sideways with him at the same speed, keeping him centred as he leans over the "
        "chair",
        "he drops his chin to his chest, shakes his head once from left to right, then straightens "
        "up and releases the chair with both hands",
        "a side-on medium shot with him standing straight, both hands open at his sides, the chair "
        "pushed back behind him",
    ),
    B(
        "You did the math twice, then a third time, because it felt personal.",
        "你算了两遍，又算了第三遍，因为这事儿太私人了。",
        "kitchen_night", ("you",),
        "He sits on the edge of the chair again, hunched over the table with both elbows on the "
        "wood and both hands pressed flat against his temples, the phone pushed to one side and "
        "ignored now.",
        "Camera is a medium close shot from the front at eye level, framed from the chest up with "
        "the table edge running along the bottom of frame.",
        "The warm bulb hangs low and close so the light falls almost straight down his face, "
        "putting his eye sockets in soft shadow and leaving a warm highlight along his forehead "
        "and nose. The mood is tired, looping, and stuck.",
        "a front-on medium close shot at eye level framed from the chest up",
        "the phone screen on the table beside his elbow, which dims and then brightens again as "
        "the lock screen times out",
        "he drags both hands down from his temples across his cheeks and jaw, then folds his arms "
        "tightly across his chest",
        "pulls back slowly to a wider medium shot, because the thought is expanding outward rather "
        "than closing in",
        "he unfolds his arms, plants both palms flat on the table and leans forward until his "
        "shoulders are up around his ears",
        "a medium shot from the front with him hunched forward over the table, both palms flat on "
        "the wood",
    ),
    # ---------------------------------------------------------------- 6–11 搜一次，看到两套答案
    B(
        "Then you did what everyone does at 1:47. You typed it in.",
        "然后你做了所有人凌晨都会做的事：把它打了进去。",
        "kitchen_night", ("you",),
        "He hunches over the open phone with both thumbs hovering just above the glass, shoulders "
        "raised, head tipped down, the closed laptop still pushed against the wall behind him.",
        "Camera is a medium shot from behind and slightly to his left, looking over his shoulder "
        "down at the phone and the table surface beyond.",
        "The pendant lamp behind the camera throws his shadow forward across the table, and the "
        "phone throws a cold pale glow up onto his chin and the underside of his jaw. The mood is "
        "furtive, compulsive, and wide awake against his will.",
        "a medium shot from behind and slightly left, looking over his shoulder at the phone",
        "his shadow on the tabletop, which stretches and shifts as the bulb above keeps swaying",
        "he lowers both thumbs onto the glass and types a short burst of taps, then lifts his "
        "right thumb and hovers it, hesitating before the last tap",
        "leans in closer over his shoulder, because we are reading the screen with him",
        "he taps once, then immediately pulls the phone up closer to his face with both hands and "
        "goes completely still",
        "an over-the-shoulder medium close shot with the phone held up, its cold glow lighting his "
        "face from below",
    ),
    B(
        "Should I pay off debt, or invest the money first.",
        "该先还债，还是先拿去投资。",
        "kitchen_night", ("you",),
        "He holds the phone up at eye level with both hands, arms bent, reading, his eyebrows "
        "lifted high and his mouth slightly open as the words land.",
        "Camera is a medium close shot from the front and slightly below, so we look up at him "
        "holding the lit screen above his chin.",
        "The phone is now the dominant light source, throwing cold pale light straight up his face "
        "while the warm bulb behind him only rims his shoulders. The mood is caught, exposed, and "
        "suddenly very awake.",
        "a medium close shot from the front and slightly below, looking up at the lit screen under "
        "his chin",
        "the fridge hum in the background, which we read as a faint shimmer on the chrome handle "
        "behind him",
        "his eyebrows climb higher, his mouth closes, and he tilts the phone slightly as if "
        "turning the sentence over in his hands",
        "rises slowly from below to level with his eyes, because he is sitting up straighter as "
        "he reads",
        "he lowers the phone a few inches, blinks slowly once, then raises it back up and starts "
        "scrolling with his right thumb",
        "a level medium close shot of his face lit from below by the screen, both hands holding "
        "the phone under his chin",
    ),
    B(
        "Two hundred million results. Two answers. Both of them absolutely certain.",
        "两亿条结果。两个答案。两边都斩钉截铁。",
        "kitchen_night", ("you",),
        "He scrolls with his right thumb while his left hand grips the phone edge tightly, shoulders "
        "hunched high, head tipped down, his expression shifting from hope to open disbelief.",
        "Camera is a medium shot from the front at a slightly high angle, looking down the length "
        "of the table so the wood surface fills the lower third of frame.",
        "Warm amber from above fights cold blue screen light from below, splitting his face into "
        "two colour temperatures. The mood is overwhelmed and slightly ridiculous.",
        "a front medium shot at a slightly high angle looking down the length of the table",
        "the cold mug of coffee on the table, which slides a few inches as his elbow knocks it",
        "his right thumb scrolls upward in three quick flicks, then stops dead and his whole hand "
        "closes around the phone",
        "drops slowly to table level, because the weight of the search results is pressing him "
        "downward",
        "he sets the phone down flat on the wood, slides it away with the back of his fingers, "
        "and covers his face with both hands",
        "a table-level medium shot with the phone pushed aside and both of his hands over his face",
    ),
    B(
        "Half the internet says kill the debt. Every dollar. Before anything else.",
        "一半的互联网说：先把债清了。每一分钱。别的都往后排。",
        "kitchen_night", ("you",),
        "He has both hands flat on the table and is leaning right in toward the phone again, jaw "
        "set hard, one eyebrow pulled low, reading intently and nodding once against his will.",
        "Camera is a medium close shot from his right side at eye level, his profile against the "
        "dark kitchen and the window visible behind him.",
        "Warm light grazes his cheekbone and jaw while the phone throws a small cold glint into "
        "his eye. The mood is being convinced, reluctantly, by someone who sounds very sure.",
        "a right-side medium close shot at eye level with his profile against the dark kitchen",
        "the window pane over the sink, which reflects a faint flash of the phone screen as it "
        "refreshes",
        "he nods once, then catches himself, straightens his neck and stops nodding with his jaw "
        "still tight",
        "pushes in a short distance on his profile, because the argument is landing and we want "
        "to see it land",
        "he lifts one hand, jabs a single finger down onto the tabletop once, hard, then lets the "
        "hand fall open",
        "a right-side medium close profile shot with his jaw set and one finger still touching "
        "the wood",
    ),
    B(
        "The other half says the market returns ten. Never prepay a cheap loan.",
        "另一半说：市场年化 10%，低息贷款永远别提前还。",
        "kitchen_night", ("you",),
        "He has pulled back from the table and sits upright with his arms crossed tight, head "
        "tilted to one side, one eyebrow raised high in open scepticism at the phone lying in "
        "front of him.",
        "Camera is a medium shot from the front left at eye level, angled so the window and the "
        "fridge are visible in soft focus behind him.",
        "The warm bulb lights him from front-left while cold blue night fills the window behind, "
        "separating him cleanly from the background. The mood is suspicious, arms folded, not "
        "buying it.",
        "a front-left medium shot at eye level with the window and fridge softly blurred behind "
        "him",
        "the refrigerator door behind him, whose chrome handle catches a slow warm glint as the "
        "bulb sways",
        "he uncrosses his arms, reaches out with one finger and drags the phone a few inches "
        "closer, then folds his arms again",
        "drifts slowly to the right, because he is physically leaning away from what he just "
        "read",
        "he tips his head to the other side, exhales through his nose, and taps two fingers "
        "against his own upper arm",
        "a front-left medium shot of him upright with arms folded, head tilted, the phone pulled "
        "close on the table",
    ),
    B(
        "Both of those people are right. That's exactly the problem.",
        "两边都是对的。这才是问题所在。",
        "kitchen_night", ("you",),
        "He sits with both hands open and raised slightly at chest height, palms up, head tilted "
        "back a little, looking up at the ceiling with a completely lost expression.",
        "Camera is a medium shot from directly in front but positioned low near the tabletop, "
        "looking up at him so the ceiling and the hanging bulb are in frame above his head.",
        "The warm bulb hangs directly above him in frame and flares slightly, throwing his shadow "
        "down and back, while cold blue fills the edges of the room. The mood is stuck between "
        "two certainties.",
        "a low front medium shot near tabletop height looking up, the hanging bulb in frame above "
        "his head",
        "the hanging pendant bulb, which swings in a wider arc now and drags his shadow across "
        "the wall behind him",
        "he raises both palms higher, turns them over, then drops them heavily onto his thighs "
        "and slumps",
        "tilts slowly upward to include more ceiling, because he is literally looking for an "
        "answer above him",
        "his head drops forward, both hands come up to the back of his neck and he squeezes once "
        "before letting go",
        "a low front medium shot of him slumped with both hands fallen away and the bare bulb "
        "burning overhead",
    ),
    # ---------------------------------------------------------------- 12–22 抛出分界线
    B(
        "They're standing in completely different rooms when they say it.",
        "他们是在不同的房间里说这些话的。",
        "ledger_room", ("maya", "devon", "priya"),
        "Maya, Devon and Priya stand apart from one another on the long chalk number line painted "
        "across the oak floor, each of them planted at a different mark, all three facing the "
        "same direction but standing in three completely different rooms of light.",
        "Camera is a wide shot from floor level at one end of the hall, looking down the length of "
        "the chalk line so the three small figures are spread out across the frame.",
        "Warm shafts of afternoon light fall through the tall arched windows and cut the hall into "
        "three separate pools, so each figure is lit by a different beam while the gaps between "
        "them stay in warm shadow. The mood is revealing and quietly cinematic.",
        "a wide floor-level shot at one end of the hall looking down the chalk number line",
        "the dust motes inside the three window shafts, which drift slowly sideways through the "
        "warm light",
        "Priya, nearest the camera, turns her head to look along the line, then lifts one arm and "
        "points down the hall toward the far end",
        "begins a slow forward dolly along the chalk line, because we are being walked down the "
        "number line toward the decision",
        "Maya, furthest away, shifts her weight onto one foot and folds her arms, while Devon in "
        "the middle turns his head to follow whatever Priya is pointing at",
        "a wide shot from the middle of the hall with all three figures spaced along the chalk "
        "line and the scale looming behind them",
    ),
    B(
        "Here's the thing nobody puts in the title. The answer isn't a belief.",
        "没人写进标题里的那个东西是：答案不是一种立场。",
        "ledger_room", ("you",),
        "He stands alone in the warm hall facing the giant brass balance scale, both hands open at "
        "his sides, head tipped back to take in the full height of the scale in front of him.",
        "Camera is a medium wide shot from behind and to his right, so we see him small against "
        "the massive brass scale and the tall arched windows beyond.",
        "Warm amber light pours through the arched windows and catches the brass of the scale so "
        "it glows against the deep brown shadow of the hall. The mood is small human against a "
        "very large idea.",
        "a medium wide shot from behind and right, he stands small against the giant brass scale",
        "the fine brass chain on the scale, which begins a slow tremble as the mechanism settles",
        "he takes three slow steps forward toward the scale, stops, then raises his right hand "
        "and holds it out flat toward the nearest pan",
        "cranes slowly upward, because the scale is far taller than he is and we need to feel its "
        "size",
        "he lowers the hand, plants both feet shoulder width apart and squares his shoulders to "
        "the scale",
        "a medium wide shot from behind with him squared up to the towering scale, both hands "
        "open at his sides",
    ),
    B(
        "It's a number. Not the interest rate you feel. The one on paper.",
        "它是一个数字。而且不是你「感觉」的那个利率，是纸上写的那个。",
        "ledger_room", ("you",),
        "He crouches down beside the chalk number line painted on the oak floor, one hand pressed "
        "flat on the boards for balance, the other hand hovering above a chalk mark as if about "
        "to draw his own.",
        "Camera is a high medium shot angled down from above and slightly to his left, showing the "
        "chalk line running diagonally across the floorboards toward the scale base.",
        "A warm window shaft falls across the chalk line and makes the white marks glow against "
        "the dark oak, while dust drifts visibly through the beam. The mood is precise, quiet, "
        "and suddenly concrete.",
        "a high medium shot angled down from above and slightly left, the chalk line running "
        "diagonally across frame",
        "the dust in the window shaft, which drifts down through the light and settles onto the "
        "chalk marks",
        "he lowers his hovering hand and draws a short firm chalk stroke across the line, then "
        "sits back on his heels to look at it",
        "drops slowly until it is almost level with the floor, because the important thing is now "
        "on the ground and not on his face",
        "he reaches out, rubs the chalk mark once with his thumb, then stands up straight and "
        "steps back from it",
        "a low medium shot from floor level with the fresh chalk mark in the foreground and him "
        "standing straight behind it",
    ),
    B(
        "Write yours down. Not the range on the statement. The actual percentage.",
        "把你的那个写下来。不是对账单上的区间，是那个真实的百分比。",
        "home_office", ("you",),
        "He sits at the walnut desk with a pen gripped in his right hand held just above a closed "
        "spiral notebook, shoulders hunched, the glowing laptop pushed to one side and the phone "
        "lying face up beside it.",
        "Camera is a medium shot from the front right at desk height, angled across the surface so "
        "the notebook, the laptop screen edge and the phone are all visible in depth.",
        "The desk lamp throws a warm tight cone onto the notebook while the laptop adds a colder "
        "glow from the left, and the rest of the room falls away into warm brown darkness. The "
        "mood is deliberate and finally doing something.",
        "a front-right medium shot at desk height angled across the walnut surface",
        "the sticky notes along the monitor edge, which flutter once as the laptop fan spins up",
        "he brings the pen down and writes a short line in the notebook, then lifts it and holds "
        "perfectly still above the paper",
        "pushes in slowly toward the notebook, because the number on that page is the whole video",
        "he sets the pen down beside the book, turns the notebook around to face himself, and "
        "reads it back with his lips pressed together",
        "a medium close shot from desk height of the turned notebook with his hands resting either "
        "side of it",
    ),
    B(
        "Because there's a line on the number line where the advice flips over.",
        "因为在这条数轴上，有一条建议会翻转的线。",
        "ledger_room", ("you",),
        "He stands over the chalk number line with one foot planted either side of a single marked "
        "point, arms out to his sides for balance, looking down at the line running away in both "
        "directions.",
        "Camera is a high wide shot looking almost straight down at him from the ceiling height of "
        "the hall, the chalk line cutting the frame in half.",
        "Warm light from the high windows falls across the floor in broad bands, leaving alternating "
        "stripes of gold and warm shadow along the number line. The mood is a decision, drawn on "
        "the floor.",
        "a high wide shot looking almost straight down, the chalk line cutting the frame in half",
        "the dust motes drifting down through the window shafts, which thin out as the light "
        "shifts",
        "he lifts his right foot and plants it firmly back down on the same mark, then straightens "
        "his back and looks along the line to his left",
        "rotates slowly ninety degrees so the chalk line now runs vertically through frame, "
        "because the line only matters as a boundary you stand on",
        "he turns his head to look along the line to his right, then brings both arms down and "
        "looks straight ahead",
        "a high wide shot with him straddling the marked point and the chalk line running clean "
        "through frame beneath him",
    ),
    B(
        "Above it, paying the debt is a guaranteed return you can't beat.",
        "在线的上面，还债就是一笔你打不过的确定性回报。",
        "ledger_room", ("you",),
        "He stands to the left of the marked point on the chalk line with his right arm raised and "
        "his index finger pointing up at the high windows, his whole body turned toward the "
        "brighter end of the hall.",
        "Camera is a medium shot from the floor at the far end of the hall looking back toward the "
        "windows, so he is a dark shape against the bright warm glass.",
        "Strong warm backlight floods in through the arched windows and rims his entire silhouette "
        "in gold, with the brass scale catching the same light behind him. The mood is certain, "
        "warm, and unarguable.",
        "a floor-level medium shot from the far end of the hall looking back toward the bright "
        "windows",
        "the dust motes in the window light, which stream past him in one direction on a slow "
        "draught",
        "he raises his right arm higher, holds the pose, then sweeps the whole arm down and across "
        "his body to point along the floor",
        "rises slowly from the floor to stand at his height, because we are standing up with the "
        "argument",
        "he brings both hands down to his sides, steps one foot back to widen his stance and "
        "nods once",
        "a floor-level medium shot of him upright and rim-lit against the bright arched windows "
        "with the scale behind",
    ),
    B(
        "Below it, you're prepaying cheap money with money that could work.",
        "在线的下面，你是在拿本可以干活的钱，去提前还便宜的钱。",
        "ledger_room", ("you",),
        "He stands on the other side of the marked point now with both arms out in front of him, "
        "palms up, as if weighing something invisible and light in each hand.",
        "Camera is a medium shot from his left at hip height, the chalk line running under his feet "
        "and the brass scale pedestal in soft focus behind.",
        "Cooler indirect light fills this side of the hall, letting the warm gold from the windows "
        "fall only across his shoulders while his hands stay in soft neutral shadow. The mood is "
        "practical, weighing, unimpressed.",
        "a left-side medium shot at hip height with the scale pedestal softly blurred behind him",
        "the brass chain of the scale behind him, which sways once and settles as if a weight "
        "shifted",
        "he lowers his left palm a few inches and raises his right, testing the difference, then "
        "holds both still",
        "arcs slowly around him to the front, because we want to see both hands and what is in "
        "them",
        "he closes both hands into loose fists, then opens them again and lets both arms drop to "
        "his sides",
        "a front medium shot of him with both arms dropped, standing on the far side of the marked "
        "point",
    ),
    B(
        "That line sits at about seven percent. A landmark, not a law.",
        "那条线大约在 7% 的位置。是地标，不是法律。",
        "ledger_room", ("you",),
        "He crouches low and presses one hand flat against the chalk number line at a single point, "
        "the other hand braced on the boards, his head turned to look back along the line behind "
        "him.",
        "Camera is a medium close shot from the side at floor level, the chalk marks sharp in the "
        "foreground and his face in profile above them.",
        "A single narrow shaft of warm light lands exactly on the floor beside his hand, so the "
        "chalk marks there glow white while everything either side stays in warm brown shadow. "
        "The mood is a specific place, finally named.",
        "a side medium close shot at floor level with the chalk marks sharp in the foreground",
        "the chalk dust still hanging in the air above the line, which drifts down and settles",
        "he presses his hand harder onto the boards, then lifts it and holds it a few inches above "
        "the mark he just made",
        "pushes in slowly along the chalk line toward his hand, because the exact spot is the "
        "whole point",
        "he straightens up out of the crouch, keeps one hand low toward the floor and looks back "
        "over his shoulder",
        "a floor-level medium close shot with his fingertips just above the glowing chalk mark and "
        "him rising behind it",
    ),
    B(
        "Long term, before tax, an average. Not a promise. Say that out loud.",
        "长期、税前、平均值。不是承诺。这句话请大声念出来。",
        "ledger_room", ("you",),
        "He stands with both hands raised to shoulder height, palms turned outward toward the "
        "camera in an open shrug, shoulders lifted, head tilted, making a plain admission to "
        "whoever is watching.",
        "Camera is a medium shot from the front at eye level, framed so the brass scale sits "
        "directly behind his head and the arched windows are cut off at the top of frame.",
        "Flat even warm light fills the hall here with no strong shaft, so nothing is dramatised "
        "and the whole frame reads honestly and plainly. The mood is disclaiming, straight with "
        "the audience.",
        "a front medium shot at eye level with the brass scale directly behind his head",
        "the brass pans of the scale behind him, which dip slowly to one side and settle level "
        "again",
        "he raises both palms higher, turns them over so the backs face the camera, then lets "
        "them drop",
        "holds perfectly still and locked off, because an admission is stronger without camera "
        "movement",
        "he shrugs his shoulders up and down once, spreads both hands wide, and lets them fall "
        "open at his sides",
        "a front medium shot of him with both arms open at his sides and the scale level behind "
        "his head",
    ),
    B(
        "But tonight you don't need a philosophy. You need to know which side.",
        "但今晚你不需要一套哲学。你只需要知道自己在哪一边。",
        "kitchen_dawn", ("you",),
        "He stands at the kitchen table in the pale early light with both hands pressed flat on "
        "the wood, leaning forward over the phone which now lies dark and face up in front of "
        "him.",
        "Camera is a medium shot from the front through the doorway frame, the cool blue window "
        "light behind him and the warm bulb switched off above.",
        "Cold pale blue dawn light comes through the window over the sink and wraps him in a flat "
        "cool rim, while the empty warm bulb above hangs dead and dark. The mood is the end of a "
        "long night and the start of a decision.",
        "a front medium shot through the doorway frame with the cool window light behind him",
        "the sheer curtain over the sink window, which lifts and settles on a breath of morning "
        "air",
        "he straightens his arms and pushes himself back upright, then picks the phone up off the "
        "table with one hand",
        "pulls back through the doorway into the hall, because the night of thinking is over and "
        "we are leaving the room",
        "he turns the phone over in his hand, sets it down again, and rests both fists on the "
        "table",
        "a medium shot from the hallway of him standing at the table in flat blue dawn light with "
        "both fists on the wood",
    ),
    B(
        "So stop arguing. Let's run it three times and watch what happens.",
        "所以别吵了。我们把同一件事跑三遍，看看会发生什么。",
        "counting_table", ("maya", "devon", "priya"),
        "Maya, Devon and Priya stand along the far side of the long oak counting table, each behind "
        "one of the three stacks of banknotes, all three resting their hands on the table edge and "
        "looking down at their own stack.",
        "Camera is a medium wide shot from the near end of the table looking down its length, the "
        "three stacks receding into the warm dark far end of the hall.",
        "The brass desk lamp at the near end throws a low warm rake of light along the tabletop, "
        "catching the edges of the notes and leaving all three faces in half light. The mood is "
        "three experiments about to start.",
        "a medium wide shot from the near end of the table looking down its length toward the "
        "dark far end",
        "the brass lamp shade at the near end, which warms and flickers once as the bulb settles",
        "Maya lifts both hands off the table and places them flat on top of her own stack, then "
        "looks straight down at it",
        "tracks slowly forward down the length of the table, because we are being walked into the "
        "experiment",
        "Devon and Priya each rest one hand on their own stack beside her, all three now looking "
        "down together",
        "a medium wide shot from the middle of the table with all three figures behind their "
        "stacks and the lamp behind camera",
    ),
    B(
        "Same eight thousand. Same five hundred a month. Same twenty-four hours.",
        "同样的 8000，同样的每月 500，同样的 24 小时。",
        "counting_table", ("maya", "devon", "priya"),
        "All three figures stand in a row facing the camera with their hands resting flat on the "
        "table, three identical stacks of notes in front of them, nobody moving yet.",
        "Camera is a level medium wide shot from the front, all three of them evenly spaced across "
        "the frame with the table edge running straight along the bottom.",
        "Even warm light from both sides of the table leaves all three faces equally lit with no "
        "hero, so the only visible difference between them is the clothing. The mood is control "
        "variables, held still.",
        "a level medium wide shot from the front with all three evenly spaced across frame",
        "the corner of the nearest banknote stack, which lifts slightly on a draught from the "
        "window",
        "all three lift their right hands off the table at the same moment and hold them out, "
        "palms down, above their own stacks",
        "drifts slowly from left to right across the row, because we need to register that all "
        "three are identical",
        "all three hands come back down flat onto their stacks at once and stay there, completely "
        "still",
        "a level medium wide shot of all three standing with hands flat on identical stacks under "
        "even warm light",
    ),
    B(
        "The only thing that changes is the number on the contract.",
        "唯一会变的，是合同上那个数字。",
        "counting_table", ("maya", "devon", "priya"),
        "Maya stands at the left end of the table closest to the brass lamp, one hand resting on "
        "her stack, the other held out open toward the lamp as if showing something written "
        "there.",
        "Camera is a medium shot from the far end of the table looking back toward the brass lamp, "
        "so Maya is brightly lit at the near end and Devon and Priya fall away into warm shadow "
        "behind her.",
        "The brass lamp throws a hard warm pool of light onto Maya and her stack while the other "
        "two stacks and faces sink into deep warm shadow down the table. The mood is one variable, "
        "isolated under a lamp.",
        "a medium shot from the far end of the table looking back toward the glowing brass lamp",
        "the warm cone of light from the lamp, which widens as the filament brightens and holds",
        "Maya turns her open hand over so the palm faces up, holds it under the lamp, then closes "
        "it into a fist",
        "pushes in slowly toward the lamp end of the table, isolating Maya from the other two",
        "she lowers the fist onto the tabletop with a soft thud and rests her other hand on top "
        "of it",
        "a medium shot from mid-table with Maya brightly lit at the lamp end and the other two "
        "figures in shadow",
    ),
]
