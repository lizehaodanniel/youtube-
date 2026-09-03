# -*- coding: utf-8 -*-
"""ACT 3（第 39–62 镜）：DEVON 与 PRIYA —— 同一道题的另外两个答案。

DEVON  7.14% → 17 个月 / $432 利息 / 对照投资 $408 → 只差 $24（打平，答案由睡眠决定）
PRIYA  3.50% → 17 个月 / $205 利息 / 对照投资 $408 → 投资赢 $204
数字来自 _build/stick_numbers.py，改输入重跑即可复核。
"""
from stick_world import B  # noqa: F401

BEATS = [
    # ================================================================ DEVON 39–50
    B(
        "Devon owes the same eight thousand. His rate is seven point one four.",
        "Devon 欠同样的 8000。他的利率是 7.14%。",
        "devon_driveway", ("devon",),
        "Devon leans against the open driver door of the ten-year-old silver sedan with one elbow "
        "propped on the roof and one hand resting on the door frame, looking down the driveway "
        "toward the street.",
        "Camera is a medium shot from the front right at chest height, the car body cutting "
        "diagonally across the left of frame and the open garage filling the background.",
        "Low golden-hour sunlight rakes in from the far end of the driveway and catches the "
        "chipped front bumper and one side of his face, while the garage interior stays in deep "
        "warm shadow behind him. The mood is relaxed, ordinary, and slightly careless.",
        "a front-right medium shot at chest height with the car cutting diagonally across frame",
        "the coiled garden hose on its hook inside the garage, which drips once onto the concrete",
        "he pushes off the car roof with his elbow, straightens up, and walks two slow steps out "
        "into the driveway",
        "tracks sideways with him along the car, keeping the sedan in frame as he moves",
        "he stops in the open light, turns to face the car, and rests both hands on his hips",
        "a medium shot from the side with him standing in the golden light with both hands on his "
        "hips and the car beside him",
    ),
    B(
        "A used car loan he took because the dealer made it feel easy.",
        "一笔二手车贷款，他办下来只是因为车商让他觉得太容易了。",
        "devon_driveway", ("devon",),
        "Devon stands in the open garage doorway with one hand resting flat on the folded tarp "
        "stacked on the shelf, his head turned to look back out at the car behind him.",
        "Camera is a medium shot from inside the garage looking out, so the pegboard of hand tools "
        "frames one side of shot and the bright driveway fills the doorway behind him.",
        "Warm daylight floods in through the doorway behind him and rims his whole silhouette, "
        "while the tools on the pegboard catch small hard glints in the dim garage. The mood is "
        "looking back at a decision that cost nothing to make.",
        "a medium shot from inside the garage looking out through the bright doorway",
        "the hand tools hanging on the pegboard, which tremble once as the garage door shifts",
        "he lifts his hand off the tarp, turns fully around, and walks out into the bright "
        "driveway",
        "follows him out of the garage into the daylight, because we are stepping back into the "
        "moment he signed",
        "he stops in the sunlight, squints against it, and shades his eyes with one hand",
        "a medium shot from the garage of him standing in the bright driveway with one hand "
        "shading his eyes",
    ),
    B(
        "Run it the same way. He throws everything at the loan.",
        "同样的方式再跑一遍。他把所有钱都砸向这笔贷款。",
        "counting_table", ("devon",),
        "Devon stands at the middle of the long oak table with both hands planted flat on the "
        "wood, leaning forward over his banknote stack with his shoulders squared and his head "
        "down.",
        "Camera is a medium shot from the far end of the table at tabletop height, the stack "
        "between his hands in the foreground and the brass lamp glowing behind him.",
        "Warm light from the lamp behind him throws his shadow forward along the tabletop and "
        "leaves his face in half light, with the note edges catching a warm rake. The mood is "
        "committed, methodical, no drama.",
        "a medium shot from the far end of the table at tabletop height with the lamp behind him",
        "his own shadow on the tabletop, which stretches forward as the lamp brightens",
        "he pushes both hands down flat, drags them slowly inward across the wood, and stops with "
        "them close together",
        "pushes in slowly toward his hands on the table, because the money leaving is the action",
        "he straightens his back, lifts both hands off the wood, and folds his arms",
        "a medium shot from mid-table of him standing back with arms folded and the stack in front "
        "of him",
    ),
    B(
        "Seventeen months later. Four hundred and thirty-two dollars of interest.",
        "17 个月后。总共付了 432 的利息。",
        "counting_table", ("devon",),
        "Devon stands beside a much smaller stack of banknotes than Maya's, one hand resting on "
        "top of it, looking down at it with his head tilted and one eyebrow raised.",
        "Camera is a medium close shot from the front at table height, the small stack sharp in "
        "the foreground and his face just behind it in softer light.",
        "The brass lamp throws a low warm rake across the table so the short stack casts a long "
        "thin shadow, and his face sits in the warm fall-off beyond it. The mood is a number small "
        "enough to be surprising.",
        "a front medium close shot at table height with the short stack sharp in the foreground",
        "the long thin shadow of the short stack, which stretches as the lamp shifts",
        "he slides his hand down the side of the stack to measure it, then holds his thumb and "
        "forefinger apart",
        "drifts up from the stack to his face, because the surprise is on his face and not in the "
        "money",
        "he drops his hand back onto the stack, tilts his head the other way, and exhales",
        "a medium close shot at table height with his hand flat on the short stack and his head "
        "tilted",
    ),
    B(
        "Now he invests instead and pays the schedule like normal.",
        "现在换他拿去投资，然后按正常节奏还。",
        "ledger_room", ("devon",),
        "Devon walks slowly along the chalk number line in the warm hall with his hands in his "
        "hoodie pocket, head down, following the line with his eyes as he goes.",
        "Camera is a medium wide shot from the side at hip height, tracking position, the chalk "
        "line running across the bottom of frame and the arched windows beyond.",
        "Warm shafts cut across the hall and he walks through each one in turn, so his figure "
        "brightens and dims as he crosses the floor. The mood is an alternative path, walked "
        "calmly.",
        "a side medium wide shot at hip height with the chalk line running along the bottom of "
        "frame",
        "the dust motes inside each window shaft, which swirl as he walks through them",
        "he stops mid-stride, lifts one foot and plants it down again on the same chalk mark, then "
        "keeps his hands in his pockets",
        "tracks with him at hip height as he continues along the line, never overtaking him",
        "he comes to a stop, turns his whole body to face the windows, and rocks back on his "
        "heels",
        "a side medium wide shot of him stopped on the chalk line with the bright windows beyond",
    ),
    B(
        "Seventeen months, same modest market: about four hundred and eight.",
        "同样 17 个月，同样保守的市场：大约 408。",
        "counting_table", ("devon",),
        "Devon crouches beside the table with his eyes level with the top of the second stack, one "
        "hand braced on the table edge, comparing the height of the two stacks from the side.",
        "Camera is a medium shot from the side at the height of the tabletop, so both stacks are "
        "seen in profile and their difference in height is readable.",
        "Warm raking light from the lamp reveals the edges of every note in both stacks, and his "
        "face catches only the last of that light at the right of frame. The mood is two things "
        "almost the same size.",
        "a side medium shot at tabletop height with both stacks readable in profile",
        "the brass lamp glow behind him, which steadies and stops moving",
        "he lifts one hand and holds it flat, palm down, level with the top of the taller stack, "
        "then lowers it slowly",
        "slides slowly sideways along the table, because we are sighting along the two heights",
        "he stands back up out of the crouch, rests both hands on the table edge, and looks "
        "between the two stacks",
        "a side medium shot at table height with him standing back and both stacks in profile",
    ),
    B(
        "Four thirty-two versus four oh eight. The gap is twenty-four dollars.",
        "432 对 408。差额只有 24 块。",
        "counting_table", ("devon",),
        "Devon holds both hands out in front of him at chest height, palms up and almost level, "
        "with only a narrow gap between them, looking down at his own two hands.",
        "Camera is a medium close shot from the front at eye level, his two hands centred in frame "
        "and his face visible just above them.",
        "Warm light from the lamp falls evenly across both palms so the narrow gap between his "
        "hands is the clearest thing in the shot. The mood is almost nothing, measured precisely.",
        "a front medium close shot at eye level with both his hands centred in frame",
        "the banknote corner on the table beside him, which lifts and settles in the draught",
        "he wobbles both hands slightly as if testing a balance, then holds them perfectly still "
        "again",
        "pushes in slowly toward the gap between his hands, because the gap is the entire point",
        "he lets both hands drop a few inches, spreads his fingers, and shrugs his shoulders up",
        "a medium close shot of him with both hands dropped and his shoulders lifted in a shrug",
    ),
    B(
        "Twenty-four dollars across a year and a half. One tank of gas.",
        "一年半下来 24 块。一箱油钱。",
        "devon_driveway", ("devon",),
        "Devon stands beside the silver sedan with one hand resting on the fuel flap, the other "
        "held out loosely to his side with the fingers spread, looking down at the ground and "
        "laughing quietly.",
        "Camera is a medium shot from the front left at chest height, the car side panel filling "
        "the right half of frame and the golden light raking across the driveway.",
        "Low warm sun catches the curve of the car panel and one side of his face, while the "
        "garage shadow creeps out across the concrete toward him. The mood is genuinely amused by "
        "how small it is.",
        "a front-left medium shot at chest height with the car panel filling the right of frame",
        "the oil stains on the concrete, which catch a low warm sheen as the sun drops",
        "he pats the fuel flap twice with his open hand, then lets that arm swing down to his side",
        "drifts slowly round to the front of him, because the joke only lands on his face",
        "he shakes his head, still smiling, and tucks both hands into his hoodie pocket",
        "a front medium shot of him smiling with both hands pocketed and the golden car behind him",
    ),
    B(
        "So the honest answer for Devon is: it genuinely does not matter.",
        "所以 Devon 的诚实答案是：这事儿真的无所谓。",
        "ledger_room", ("devon",),
        "Devon stands in the centre of the warm hall with both arms out to his sides and both "
        "palms turned up, shoulders lifted high, head tilted to one side in a full open shrug.",
        "Camera is a level medium shot from the front, the brass scale balanced and level directly "
        "behind his head and the arched windows cut off at the top of frame.",
        "Flat even warm light fills the hall with no dramatic shaft, so the shrug reads plainly "
        "and nothing is dressed up. The mood is honest, unbothered, and slightly funny.",
        "a level front medium shot with the brass scale held level behind his head",
        "the brass scale behind him, which tips a few degrees to one side and settles back level",
        "he lifts both palms higher, holds the shrug, then drops his arms and lets them swing",
        "holds still and locked off, because a shrug needs no camera move to land",
        "his shoulders come down slowly, he rocks forward onto the balls of his feet, and nods "
        "once to himself",
        "a level front medium shot of him standing easy with the scale balanced behind his head",
    ),
    B(
        "Which means he should decide on something other than arithmetic.",
        "这意味着他该用算术以外的东西来做决定。",
        "devon_driveway", ("devon",),
        "Devon sits on the low concrete step at the edge of the driveway with his forearms resting "
        "on his knees and his hands hanging loose between them, staring out at the street.",
        "Camera is a medium wide shot from the side and slightly behind, the garden hose and the "
        "garage wall framing one edge and the long driveway stretching away in front of him.",
        "The sun has dropped lower so the light is now deep amber and raking flat across the "
        "asphalt, putting him in warm half light with a long shadow behind. The mood is thinking "
        "about something that cannot be calculated.",
        "a side medium wide shot from slightly behind with the long driveway stretching away",
        "the potted fern by the garage wall, whose leaves stir once in the evening air",
        "he lifts his head, looks along the driveway, then lowers his chin onto his hands",
        "rises slowly to stand behind him, because the thought is lifting us up with it",
        "he straightens his back, plants both feet on the step, and rests his hands flat on his "
        "knees",
        "a medium wide shot from behind of him sitting upright on the step in deep amber light",
    ),
    B(
        "Sleep. If the number wakes you up, kill it. That's a real return.",
        "睡眠。如果这个数字让你半夜醒来，就干掉它。那也是一笔真实的回报。",
        "bathroom", ("devon",),
        "Devon stands at the white pedestal sink with both hands gripping the cold porcelain edge "
        "on either side of the basin, his shoulders raised high and his head hanging forward so "
        "his face is turned toward the fogged mirror above the sink.",
        "Camera is a medium shot from the front through the narrow bathroom doorway, the fogged "
        "rectangular mirror and the chrome-framed sink filling the frame with the pale green tiles "
        "visible either side.",
        "Flat cold daylight comes in through the frosted window and fills the small room without "
        "a single warm source, leaving his face pale and his eye sockets faintly shadowed. The "
        "mood is 3 a.m., wide awake, and out of arguments.",
        "a front medium shot through the bathroom doorway with the fogged mirror filling frame",
        "the thin stream of water from the tap, which runs steadily into the basin and swirls at "
        "the plug",
        "he grips the basin edge harder, pushes himself back upright, and turns his head to look "
        "straight at himself in the mirror",
        "pushes in slowly toward the mirror, because the point is that he is looking straight at "
        "himself",
        "he lifts one hand, wipes a clear streak across the fogged glass, then lowers it back down "
        "onto the basin edge",
        "a medium close shot of his face inside the wiped streak of mirror with the pale green "
        "tiles behind him",
    ),
    B(
        "Devon's answer is a shrug, and the shrug is entirely correct.",
        "Devon 的答案是一个耸肩，而这个耸肩完全正确。",
        "devon_driveway", ("devon",),
        "Devon stands at the end of the driveway with his back to camera, both hands in his hoodie "
        "pocket, shoulders lifted in a last shrug, looking out toward the street where the light "
        "is going.",
        "Camera is a medium wide shot from behind and slightly above, the whole driveway and the "
        "garage framing him small against the fading golden street.",
        "The sun is almost down so the light is warm and low and long, throwing his shadow all the "
        "way back toward the garage behind him. The mood is settled, unbothered, and done.",
        "a medium wide shot from behind and slightly above with the whole driveway in frame",
        "his long shadow on the asphalt, which stretches further as the last light drops",
        "he lifts both shoulders one final time, holds the shrug for a beat, then lets them fall "
        "slowly and stands easy with his weight settled on both feet",
        "pulls back slowly and rises, because we are leaving him to it",
        "he turns halfway back toward camera, nods once, then turns away again and starts walking",
        "a medium wide shot from behind of him walking down the driveway in the last golden light",
    ),
    # ================================================================ PRIYA 51–62
    B(
        "Priya owes the same eight thousand at three point five percent.",
        "Priya 欠着同样的 8000，年利率 3.5%。",
        "priya_studio", ("priya",),
        "Priya sits at the pale birch desk with her hands folded on the closed laptop, sitting "
        "bolt upright, the corkboard with the credit-union calendar visible over her shoulder.",
        "Camera is a medium shot from the front right at desk height, the potted plants on the "
        "floating shelf filling the left of frame and the wide window behind her.",
        "Soft even daylight comes through the sheer curtains and fills the whole room without hard "
        "shadow, so her cream blouse and the birch desk read almost the same warm tone. The mood "
        "is calm, tidy, and unhurried.",
        "a front-right medium shot at desk height with the potted plants filling the left of frame",
        "the leaves of the nearest potted plant, which turn slowly in the draught from the window",
        "she lifts both hands off the laptop, turns them palm up on the desk, and looks down at "
        "them",
        "pushes in slowly toward her hands on the birch desk, because the rate is the only "
        "difference",
        "she folds her hands together again, sits back, and turns her head to look at the "
        "corkboard",
        "a medium shot from desk height of her sitting back with hands folded and the corkboard "
        "beyond",
    ),
    B(
        "An old loan from a credit union that simply liked her.",
        "一笔信用社的老贷款，他们当时只是喜欢她这个人。",
        "priya_studio", ("priya",),
        "Priya stands in front of the corkboard with one hand raised toward the pinned "
        "credit-union calendar, the other hand resting at her side, her head tilted as she reads "
        "it.",
        "Camera is a medium shot from her left at chest height, the corkboard filling the "
        "background and the window light coming in from the right of frame.",
        "Flat soft daylight wraps her from the right and leaves the corkboard in gentle warm "
        "shadow, with a pale green cast bouncing back off the plant leaves. The mood is a good "
        "deal, quietly appreciated.",
        "a left-side medium shot at chest height with the corkboard filling the background",
        "the corner of the pinned calendar, which lifts and settles in the draught",
        "she reaches up and straightens the calendar with one finger, then steps back to look at "
        "it square",
        "pulls back slowly to include more of the corkboard, because the whole relationship is on "
        "that board",
        "she lowers her hand, turns away from the board, and walks back toward the desk",
        "a medium shot from behind her as she walks back to the desk with the corkboard behind",
    ),
    B(
        "She can clear it in seventeen months for two hundred and five.",
        "她可以在 17 个月内清掉，利息总共 205。",
        "counting_table", ("priya",),
        "Priya stands at the far end of the long oak table with one hand resting on a noticeably "
        "small stack of banknotes, the other hand flat on the table, looking along the table "
        "toward the lamp.",
        "Camera is a medium shot from the near end of the table at tabletop height, the small "
        "stack in the middle distance and the warm dark hall behind her.",
        "Warm raking light from the lamp at the near end catches the top edge of the small stack "
        "and falls off before it reaches her, leaving her face in gentle half light. The mood is "
        "a small cost, easily paid.",
        "a medium shot from the near end of the table at tabletop height with the small stack in "
        "the middle distance",
        "the dust drifting through the window shaft, which settles across the table between us and "
        "her",
        "she slides the small stack a few inches forward across the wood, then leaves her hand "
        "resting on it",
        "drifts slowly forward down the table toward her, closing the distance between us",
        "she lifts her hand off the stack, straightens up, and folds both arms loosely",
        "a medium shot from mid-table of her standing at the far end with arms folded and the "
        "small stack beside her",
    ),
    B(
        "Or she can invest and let three and a half percent sit there.",
        "或者她可以拿去投资，让那 3.5% 就这么待着。",
        "ledger_room", ("priya",),
        "Priya stands beside the giant brass balance scale with one hand resting lightly on the "
        "edge of the nearest pan, her head turned to look along the beam of the scale.",
        "Camera is a medium wide shot from the floor at the base of the stone pedestal looking "
        "up, so the scale beam crosses the top of frame above her.",
        "Warm window light catches the brass beam and the pan rim and throws a soft gold glow down "
        "onto her face, while the hall behind stays in deep brown shadow. The mood is patient, "
        "letting something sit.",
        "a floor-level medium wide shot from the base of the pedestal looking up at the beam",
        "the fine brass chain on the pan, which sways a little and then hangs still",
        "she pushes the pan gently with one hand, watches it rock, then takes her hand away and "
        "steps back",
        "rises slowly from the floor to stand at her height, following the pan she just rocked",
        "she folds both arms, plants her feet, and watches the pan until it stops moving",
        "a medium wide shot from the front of her standing before the scale with arms folded and "
        "the pan stilling",
    ),
    B(
        "Seventeen months invested at the same average: four hundred and eight.",
        "同样 17 个月投进去，按同样的平均：408。",
        "counting_table", ("priya",),
        "Priya stands beside the taller of the two stacks with both hands resting on the oak "
        "tabletop either side of it, looking straight down at the notes from directly above.",
        "Camera is a medium close shot from the front at table height, the taller stack centred in "
        "frame and her face just above it in warm half light.",
        "The brass lamp throws a warm rake that lights every visible note edge in the tall stack, "
        "and the glow bounces warmly up onto her chin. The mood is a bigger number, quietly "
        "earned.",
        "a front medium close shot at table height with the tall stack centred in frame",
        "the warm glow of the brass lamp, which steadies and brightens slightly",
        "she slides both hands inward along the wood until they bracket the stack, then holds "
        "them perfectly still for a moment",
        "rises slowly from the stack to her face, because the verdict shows up there first",
        "she lifts both hands off the table, straightens her back, and lets her arms fall open",
        "a medium close shot of her standing straight with the tall stack in front of her and "
        "hands open",
    ),
    B(
        "Two hundred and five against four hundred and eight dollars.",
        "205 对 408。",
        "counting_table", ("priya",),
        "Priya holds her left hand out flat and low and her right hand out flat and much higher, "
        "both palms up, looking from one to the other with her head level.",
        "Camera is a level medium shot from the front, both of her hands clearly separated in "
        "frame with the dark far end of the hall behind her.",
        "Even warm light from the arched windows leaves both palms equally lit so the height "
        "difference between them is unmistakable. The mood is a clear margin, stated without "
        "drama.",
        "a level front medium shot with both hands clearly separated against the dark hall",
        "the dust in the window shaft, which drifts slowly down between her two hands",
        "she raises the higher hand another couple of inches, holds it, then brings both hands "
        "down together",
        "widens out slightly, because we need to see her whole body take the comparison in",
        "she lowers both hands to the tabletop, rests them flat on the wood, and looks down",
        "a level medium shot of her with both hands flat on the wood and the tall stack beside "
        "her",
    ),
    B(
        "Investing wins by two hundred and four. Not life changing, but real.",
        "投资这边赢了 204。不算改变人生，但确实是真的。",
        "priya_studio", ("priya",),
        "Priya sits back in her desk chair with her arms folded loosely and one eyebrow raised, "
        "looking at the closed laptop with a dry, unimpressed expression.",
        "Camera is a medium shot from the front at eye level, the birch desk edge along the bottom "
        "of frame and the plants on the shelf softly blurred behind her.",
        "Soft even daylight fills the room and leaves no hard shadow anywhere, so the whole frame "
        "reads flat, calm and matter-of-fact. The mood is a real edge, refused the chance to be "
        "exciting.",
        "a front medium shot at eye level with the birch desk edge along the bottom of frame",
        "the sheer curtain at the window, which lifts and settles on a slow breath of air",
        "she unfolds her arms, rests both hands flat on the desk, and tips her head to one side",
        "drifts slowly closer, because we are leaning in to hear the honest part",
        "she gives a small single nod, presses her lips together, and spreads both hands open on "
        "the desk",
        "a front medium shot of her with both hands open on the desk and a small nod given",
    ),
    B(
        "And something else is happening that the spreadsheet never shows.",
        "还有一件事情正在发生，是表格永远看不见的。",
        "priya_studio", ("priya",),
        "Priya stands at the wide window with one hand resting on the sill and the other raised to "
        "the sheer curtain, holding it aside so the flat daylight comes straight into the room.",
        "Camera is a medium shot from behind and to her right, looking out past her through the "
        "window with the plants visible along the bottom of frame.",
        "Flat pale daylight floods in through the held curtain and wraps the whole room in an even "
        "cool-warm wash, with the plant leaves throwing soft green shadows on the rug. The mood is "
        "something underneath, being pointed at.",
        "a medium shot from behind and right looking out past her through the window",
        "the sheer curtain she is holding, which billows inward on the draught and settles",
        "she lifts the curtain higher with one hand and holds it there, then turns her head to "
        "look over her shoulder",
        "arcs slowly around her to the front, because we need to see what she is looking at",
        "she lets the curtain fall back, turns fully into the room, and folds both arms",
        "a front medium shot of her standing at the window with arms folded and daylight behind",
    ),
    B(
        "Her rate sits below inflation. She is being paid to borrow.",
        "她的利率低于通胀。等于有人付钱让她借钱。",
        "ledger_room", ("priya",),
        "Priya stands on the chalk number line with one hand held out low and flat, palm down, "
        "just above the floor, and the other hand raised high above her head, showing two very "
        "different heights.",
        "Camera is a medium shot from the front at hip height, the giant brass scale pedestal "
        "rising behind her and the arched windows bright beyond.",
        "Warm shafts fall across her from the left and light the raised hand strongly while the "
        "low hand stays in warm floor shadow, so the two hands read in completely different light. "
        "The mood is an invisible advantage, made visible.",
        "a front medium shot at hip height with the scale pedestal rising behind her",
        "the dust motes in the window shafts, which rise past her raised hand",
        "she lowers the high hand slowly down her side until it is level with the low one, then "
        "raises it back up again just as slowly",
        "tilts slowly upward to follow the raised hand, because the gap is vertical",
        "she brings both hands down to her sides, squares her shoulders, and looks straight ahead",
        "a front medium shot of her standing square with both arms lowered and the scale behind",
    ),
    B(
        "Priya's answer is: invest it, and don't feel heroic about it.",
        "Priya 的答案是：投出去，但别觉得自己多伟大。",
        "priya_studio", ("priya",),
        "Priya sits at the birch desk with both hands flat on the closed laptop, shoulders level, "
        "giving a single small shake of her head with her mouth pressed into a flat unimpressed "
        "line.",
        "Camera is a medium close shot from the front at eye level, the corkboard and the plant "
        "shelf softly blurred in the background.",
        "Even soft daylight lights her face flatly from both sides with no drama at all, matching "
        "the refusal to make this feel like a victory. The mood is correct and completely "
        "unsentimental.",
        "a front medium close shot at eye level with the corkboard blurred behind her",
        "the leaves on the floating shelf, which stir once and settle in the still room",
        "she shakes her head once from side to side, lifts both hands off the laptop, and turns "
        "them palm up flat on the desk",
        "holds perfectly still, because refusing the drama is the whole statement",
        "she lowers her hands back onto the laptop, sits up straight, and gives one small nod",
        "a medium close shot of her upright with both hands flat on the closed laptop",
    ),
    B(
        "Three people ask the same question. Three completely different correct answers.",
        "三个人问了同一个问题。得到三个完全不同的正确答案。",
        "counting_table", ("maya", "devon", "priya"),
        "Maya, Devon and Priya stand along the far side of the long oak table together, each with "
        "one hand resting on their own stack of notes, all three facing the same direction down "
        "the length of the table.",
        "Camera is a level medium wide shot from the near end of the table looking down its full "
        "length, the three stacks diminishing into the warm dark far end.",
        "The brass lamp throws one long rake of warm light down the table that touches all three "
        "of them equally, while everything past the table sinks into deep warm shadow. The mood is "
        "three right answers, side by side.",
        "a level medium wide shot from the near end looking down the full length of the table",
        "the three banknote stacks, whose corners all lift together on the same draught",
        "all three lift their free hands at the same moment and place them flat on top of their "
        "own stacks",
        "tracks slowly forward down the table toward all three, because the comparison only lands "
        "at the end",
        "all three drop their hands to their sides together and stand straight, nobody looking at "
        "anyone else",
        "a level medium wide shot from mid-table of all three standing straight behind their three "
        "stacks",
    ),
    B(
        "Which is exactly why the internet keeps screaming past itself.",
        "这就是为什么互联网会一直互相吼过去。",
        "ledger_room", ("maya", "devon", "priya"),
        "Maya, Devon and Priya stand on the chalk number line at three separate marks, each facing "
        "a different direction, none of them looking at the other two.",
        "Camera is a high wide shot looking down from the ceiling height of the hall, the chalk "
        "line cutting the frame diagonally and the three figures spread along it.",
        "Three separate warm shafts from the arched windows isolate each figure in their own pool "
        "of gold, with deep warm brown shadow filling the spaces between them. The mood is three "
        "rooms, three people, one argument.",
        "a high wide shot from ceiling height with the chalk line cutting diagonally across frame",
        "the three separate shafts of dust, each one drifting in its own direction",
        "Maya folds her arms and turns her back slightly, Devon shoves both hands into his hoodie "
        "pocket, and Priya turns to face the windows",
        "pulls back slowly and higher, because the disagreement is only visible from far above",
        "all three plant their feet and hold their positions, three separate figures in three "
        "separate beams of light",
        "a high wide shot of all three isolated in their own window shafts along the chalk line",
    ),
]
