# -*- coding: utf-8 -*-
"""ACT 4（第 63–88 镜）：陷阱 → 顺序 → 收尾

63–72 真正吃掉人的不是利率，是最低还款（$8,000 @ 22.15%，只还 2% → 112 年 / $83,071 利息）
73–80 顺序：先拿雇主配比 → 7% 以上的全杀 → 以下的拆开 → 同时建应急金
81–88 回到 1:52 的厨房：结论不是视频给的，是算术给的
"""
from stick_world import B  # noqa: F401

BEATS = [
    # ---------------------------------------------------------------- 63–72 陷阱
    B(
        "But here's what actually eats people, and it isn't the rate.",
        "但真正吃掉人的不是利率，是别的东西。",
        "trap_room", ("you",),
        "He stands just inside the dark circular chamber with both hands lowered at his sides, "
        "head tipped back, staring up at the giant wooden wheel built from oversized credit-card "
        "rectangles that fills the whole far wall.",
        "Camera is a medium wide shot from behind and slightly below, so he is a small dark shape "
        "in the foreground and the enormous wheel looms over him.",
        "A single cold overhead work lamp throws a hard cone of light onto the top of the wheel "
        "while everything below stays in cold near-darkness, and the wet stone walls catch faint "
        "blue reflections. The mood is small, cold, and cornered.",
        "a medium wide shot from behind and slightly below with the enormous wheel looming above",
        "the steady drip from the leaking bucket, which falls onto the stone floor and splashes",
        "he lifts one hand and presses it flat against the nearest oversized card on the wheel, "
        "then pushes it a few inches",
        "cranes slowly upward to take in the full height of the wheel, because its size is the "
        "point",
        "he takes his hand off the card, steps back two paces, and lowers his head",
        "a medium wide shot from behind of him standing back with his head down and the wheel "
        "above",
    ),
    B(
        "It's the minimum payment. Two percent of the balance, every month.",
        "它是最低还款额。余额的 2%，每个月。",
        "trap_room", ("you",),
        "He crouches beside the dented metal bucket with one hand held out under the steady leak, "
        "watching the water fall into his palm and spill straight through his fingers.",
        "Camera is a medium close shot from the front at floor level, the wet reflective stone "
        "running toward camera and the bucket cutting into the left of frame.",
        "The cold work lamp throws a hard narrow beam onto the falling water and his cupped hand, "
        "while the rest of the chamber stays in blue near-black. The mood is watching something "
        "leave faster than it arrives.",
        "a floor-level medium close shot from the front with the wet stone running toward camera",
        "the water leaking from the bucket, which falls in a steady rhythm into his open palm",
        "he closes his hand into a fist to hold the water, holds it, then opens it again and "
        "watches it empty",
        "pushes in slowly on his open hand under the leak, because the leak is the whole idea",
        "he pulls his hand out from under the drip, stands up, and wipes it once down his "
        "sweatpants",
        "a floor-level medium shot of him standing straight with the bucket still leaking beside "
        "him",
    ),
    B(
        "Eight thousand at twenty-two percent. Paying the minimum takes a century.",
        "8000 块，22% 的利率。只还最低，需要一个世纪。",
        "trap_room", ("you",),
        "He stands inside the giant wooden wheel with both hands braced flat against two of the "
        "oversized card panels, shoulders low, testing the weight of it before he pushes.",
        "Camera is a medium shot from the front, positioned outside the wheel and looking in "
        "through the gap between two card panels at him.",
        "Cold light from the single work lamp above rakes down into the wheel and catches his "
        "forearms and one cheekbone, leaving the rest of him in hard cold shadow. The mood is "
        "trapped inside the thing he is pushing.",
        "a medium shot from outside the wheel looking in through the gap between two card panels",
        "the whole wheel above him, which creaks and rotates a few slow degrees under his hands",
        "he plants his feet and pushes both hands forward hard, walking two steps as the wheel "
        "turns, then stops dead",
        "rotates slowly with the turning wheel, because the machine is what is moving and not him",
        "he lets both hands slide off the panels, straightens up, and stands still inside the "
        "wheel",
        "a medium shot from outside the wheel of him standing still inside it with both hands "
        "lowered",
    ),
    B(
        "One hundred and twelve years. Eighty-three thousand dollars of interest.",
        "112 年。83,071 美元的利息。",
        "trap_room", ("you",),
        "He sits on the wet stone floor with his back against the inside curve of the wheel, both "
        "forearms resting on his raised knees and his hands hanging loose between them, head "
        "bowed forward.",
        "Camera is a wide shot from across the chamber at floor level, the wheel curving around "
        "him and the leaking bucket in the foreground throwing a long cold reflection.",
        "The cold work lamp sits directly above the wheel so the light falls in a hard ring around "
        "him, and the puddle on the stone throws that cold light back up onto his jaw. The mood "
        "is a number too big to argue with.",
        "a floor-level wide shot from across the chamber with the bucket in the cold foreground",
        "the spreading puddle on the stone, which widens slowly as the bucket keeps dripping",
        "he lifts his head, looks straight across the chamber, then drops his chin back toward his "
        "chest",
        "pushes in slowly across the wet floor toward him, because the number is what we are "
        "walking into",
        "his shoulders rise and fall once on a slow breath and both hands curl into loose fists "
        "between his knees",
        "a floor-level medium shot of him sitting against the wheel with both fists between his "
        "knees",
    ),
    B(
        "For an eight thousand dollar purchase. Read that again, slowly.",
        "为了一笔 8000 块的消费。把这句话再读一遍，慢慢读。",
        "grocery", ("you",),
        "He stands in the supermarket aisle with a red shopping cart in front of him, both hands "
        "resting loose on the handlebar, his head turned to look along the tall shelf stacked with "
        "colourful cereal boxes and canned goods.",
        "Camera is a medium shot from the side at chest height, the aisle receding into blurred "
        "depth behind him and the green price tag strip running along the shelf edge in the "
        "foreground.",
        "Flat fluorescent ceiling light fills the aisle evenly and reflects off the glossy white "
        "linoleum, throwing a pale cold sheen up onto his face and hands. The mood is completely "
        "ordinary, and that is exactly the problem.",
        "a side medium shot at chest height with the supermarket aisle receding into blurred depth",
        "the overhead fluorescent strip, which hums and flickers once before settling steady",
        "he turns the cart slowly into the aisle, walks three paces alongside the shelf, and stops "
        "with both hands still resting on the handlebar",
        "tracks sideways with him along the shelf, because we are walking the aisle with him",
        "he lifts one hand off the handlebar, runs two fingers along the green price tag strip, "
        "then lets the hand drop back onto the cart",
        "a side medium shot of him stopped in the aisle with both hands on the cart and the tall "
        "shelves behind",
    ),
    B(
        "The minimum payment is not a plan. It's a subscription to the balance.",
        "最低还款额不是还款计划，是一份「余额订阅」。",
        "trap_room", ("you",),
        "He stands with one hand gripping the rim of the leaking bucket and the other hand raised "
        "slightly out to his side, palm down, as if pressing something back down where it belongs.",
        "Camera is a medium shot from his left at hip height, the wet stone wall closing in behind "
        "him and the wheel edge cutting into the right of frame.",
        "Cold overhead light falls in a single hard column onto the bucket and his hand, while the "
        "walls behind him stay in near-black blue with only a wet sheen. The mood is naming the "
        "thing correctly for the first time.",
        "a left-side medium shot at hip height with the wet stone wall closing in behind him",
        "the water in the bucket, which sloshes once as he grips the rim and steadies it",
        "he lifts the bucket an inch off the floor, holds it level, then sets it back down hard",
        "drops slowly to the level of the bucket, because the bucket is what we are talking about",
        "he straightens up, wipes his palm down his sweatshirt, and looks along the chamber toward "
        "the way out",
        "a left-side medium shot of him standing straight and looking toward the chamber exit",
    ),
    B(
        "So before you argue about seven percent, do this one thing first.",
        "所以在争论 7% 之前，先把这一件事做了。",
        "home_office", ("you",),
        "He sits at the walnut desk with both hands on the glowing laptop, shoulders square, one "
        "finger already reaching out toward the screen, his whole attention on one spot.",
        "Camera is a medium shot from over his left shoulder, looking down across the desk at the "
        "laptop screen and his reaching hand.",
        "The desk lamp throws a warm cone onto the desk surface while the laptop throws a colder "
        "glow up onto his hands and chin, and the room behind is warm dark. The mood is one "
        "specific action, about to be taken.",
        "a medium shot from over his left shoulder looking down at the laptop screen",
        "the laptop fan, which we read as the sticky note on the monitor edge lifting once",
        "he brings his finger down onto the screen, taps once, then pulls his hand back into his "
        "lap",
        "pushes in slowly toward the screen, because the thing he just tapped is the whole task",
        "he straightens his back, rests both hands flat on the desk either side of the laptop, and "
        "sits still",
        "a medium shot from over his shoulder of him sitting back with both hands flat on the desk",
    ),
    B(
        "Find the autopay amount. Whatever it is, raise it above the minimum.",
        "找到自动还款那个金额。不管现在是多少，把它抬到最低额之上。",
        "home_office", ("you",),
        "He leans in over the desk with one hand gripping the desk edge and the other holding a "
        "pen above the spiral notebook, head down close to the page, reading what he has just "
        "written.",
        "Camera is a high medium shot angled down from above and to his right, the notebook page "
        "filling the lower half of frame and the lamp cone visible at the edge.",
        "Warm lamp light pools tightly on the notebook page so the paper glows, while his face "
        "stays in the softer warm shadow just above it. The mood is a small edit with a very large "
        "consequence.",
        "a high medium shot angled down from above and right with the notebook page filling the "
        "lower frame",
        "the sticky notes on the monitor, which flutter as the laptop fan spins up again",
        "he strikes through one line in the notebook with the pen, then writes a new figure beside "
        "it",
        "pushes in slowly toward the new figure on the page, because that number is the whole "
        "move",
        "he lifts the pen away, caps it with one hand, and sets it down on the desk beside the "
        "notebook",
        "a high medium shot of the notebook with the new figure written and the pen laid beside it",
    ),
    B(
        "Even fifty dollars more bends the entire curve in your favour.",
        "哪怕每月多 50 块，整条曲线都会被掰向你这边。",
        "ledger_room", ("you",),
        "He crouches on the oak floor beside the chalk number line with both hands flat on the "
        "boards, tracing the line forward with one finger as it bends away toward the windows.",
        "Camera is a medium shot from the side at floor level, the chalk line running across frame "
        "and the giant brass scale pedestal rising in the background.",
        "Warm shafts from the arched windows cross the floor and light the chalk line in bright "
        "segments, so the bend in it reads clearly against the dark oak. The mood is a small "
        "change in angle, visible over a long distance.",
        "a side medium shot at floor level with the chalk line running across frame",
        "the dust motes in the window shafts, which drift down across the chalk line",
        "he traces the line with one finger from left to right, then stops and taps one point "
        "twice",
        "tracks slowly along the chalk line in the direction he is tracing",
        "he sits back on his heels, keeps one hand flat on the floor, and looks along the line "
        "toward the windows",
        "a floor-level medium shot of him crouched at the end of the chalk line with the scale "
        "behind",
    ),
    B(
        "That one move beats every clever strategy in this video.",
        "这一步，比这条视频里所有聪明的策略都强。",
        "home_office", ("you",),
        "He leans back in the desk chair with his arms folded and one eyebrow raised, looking at "
        "the glowing laptop with an expression of mild surprise at how simple it turned out to be.",
        "Camera is a medium wide shot from the front at chest height, the whole desk in frame with "
        "the dark bookshelf and the warm lamp behind him.",
        "Warm lamp light fills the right of frame and cold screen light the left, and the two meet "
        "across his chest so he sits exactly between them. The mood is that was it, that was the "
        "whole thing.",
        "a front medium wide shot at chest height with the whole desk in frame",
        "the lamp shade beside him, which glows a little warmer as the bulb settles",
        "he unfolds his arms, plants both hands on the desk, and pushes the chair back a few "
        "inches",
        "pulls back slowly to include more of the dark room, because the video is ending and the "
        "room is still there",
        "he rests both hands flat on the desktop, looks down at them, and gives one slow nod",
        "a medium wide shot of him sitting back in the chair with both hands flat on the desk",
    ),
    # ---------------------------------------------------------------- 73–80 顺序
    B(
        "Then, and only then, run the actual order of operations.",
        "然后，也只有到那时，才去跑真正的操作顺序。",
        "counting_table", ("you",),
        "He stands at the near end of the long oak table with both hands resting flat on the wood, "
        "looking down the length of the table toward the three stacks at the far end.",
        "Camera is a medium wide shot from behind and above his shoulder, the table receding away "
        "from camera into the warm dark far end of the hall.",
        "Warm light from the brass lamp rakes along the tabletop and falls off gradually, so the "
        "near end is bright and the far end where the stacks sit is deep warm shadow. The mood is "
        "a sequence, laid out in order.",
        "a medium wide shot from behind and above his shoulder with the table receding away",
        "the warm rake of lamp light along the table, which steadies and stops shifting",
        "he lifts his right hand off the table and holds it out flat over the first position along "
        "the table",
        "tracks slowly forward down the table behind him, following the direction he is pointing",
        "he moves the hand along to a second position, then a third, stopping at each one",
        "a medium wide shot from mid-table with him reaching out along the three positions",
    ),
    B(
        "One. The employer match. That's an instant fifty percent return.",
        "第一，雇主的配比。那是一笔立刻到手的 50%。",
        "cubicle", ("you",),
        "He sits in the office chair at the grey laminate desk with both arms raised out to his "
        "sides at shoulder height, palms up and open, his head tipped back and his mouth open "
        "mid-sentence.",
        "Camera is a medium shot from the front at chest height, the beige fabric partitions "
        "closing in either side of him and the dual monitor arm visible above him.",
        "Flat cool fluorescent light from the office ceiling fills the cubicle evenly and leaves a "
        "faint cold sheen on the laminate desk, while the monitor behind him throws a soft warm "
        "edge onto his shoulders. The mood is free money, sitting right there at work.",
        "a front medium shot at chest height with the beige cubicle partitions closing in either "
        "side",
        "the sticky note stuck to the monitor bezel, which lifts and settles as the air "
        "conditioning kicks on",
        "he closes both hands into fists, pulls both arms in toward his chest, then opens his "
        "palms wide again",
        "rises slowly to his eye level, because this is the one step that stands above the rest",
        "he lowers both arms, plants both hands flat on the desk, and pushes the chair back a few "
        "inches",
        "a medium shot of him sitting square to the desk with both hands flat on the laminate and "
        "the partitions behind",
    ),
    B(
        "No debt short of twenty-five percent beats free money. Take the match.",
        "除了 25% 以上的债，没有哪种债能打得过白给的钱。先把配比拿满。",
        "ledger_room", ("you",),
        "He stands beside the giant brass balance scale with one hand resting flat in the nearer "
        "pan and the other hand held out to his side, comparing the two without looking down.",
        "Camera is a medium shot from the side at chest height, the scale beam crossing the frame "
        "and the chalk number line visible on the floor behind him.",
        "Warm window light catches the brass of the pan and throws a gold glow up onto his jaw, "
        "while the far pan stays in cool shadow. The mood is one side of the scale, overwhelmingly "
        "heavier.",
        "a side medium shot at chest height with the scale beam crossing frame",
        "the nearer brass pan, which sinks slowly under the weight of his hand and holds there",
        "he pushes down on the pan with his flat hand, holds the pressure, then lifts it away "
        "entirely",
        "tilts down slowly to follow the pan as it drops, because the drop is the argument",
        "he steps back from the scale, folds both arms, and watches the beam settle at an angle",
        "a side medium shot of him standing back with arms folded and the scale tipped in his "
        "favour",
    ),
    B(
        "In twenty twenty-six you can defer twenty-four thousand five hundred yourself.",
        "2026 年，你自己可以递延的上限是 24,500。",
        "home_office", ("you",),
        "He sits at the walnut desk with the spiral notebook open in front of him and a pen held "
        "steady in his right hand, his left hand holding the page flat, head down and focused.",
        "Camera is a medium close shot from the front at desk height, the notebook page filling "
        "the lower half of frame and the glowing laptop edge visible behind.",
        "Warm lamp light falls in a tight cone onto the open page while the laptop adds a cold "
        "edge from behind, and the bookshelf disappears into warm darkness. The mood is a limit, "
        "written down and checked.",
        "a front medium close shot at desk height with the open notebook filling the lower frame",
        "the laptop screen behind the notebook, which dims once and brightens again",
        "he writes a figure on the page, lifts the pen, then underlines it with a single slow "
        "stroke",
        "pushes in slowly toward the underlined figure, because that ceiling is the number that "
        "matters",
        "he sets the pen down, closes the notebook halfway, and rests both hands on the cover",
        "a medium close shot from desk height of the half-closed notebook with both his hands "
        "resting on it",
    ),
    B(
        "Two. Anything above seven percent. Kill it like it is on fire.",
        "第二，7% 以上的，像灭火一样把它干掉。",
        "ledger_room", ("you",),
        "He stands on the chalk number line with one arm swept out low and hard across his body, "
        "palm down and chopping, his whole weight shifted onto his front foot.",
        "Camera is a medium shot from the front left at chest height, the chalk line running under "
        "his feet and the brass scale in soft focus behind.",
        "Warm window light rakes across him from the right and catches the chopping forearm, while "
        "the hall behind falls into deep warm shadow. The mood is urgent, flat, no negotiation.",
        "a front-left medium shot at chest height with the chalk line under his feet",
        "the chalk dust rising from the line, which lifts where his foot scuffs the boards",
        "he chops his arm down once, holds it at the bottom of the arc, then brings it back up "
        "and chops again",
        "pushes in slowly with each chop, because the urgency is in the repetition",
        "he stops mid-air, straightens up, and lets the arm fall to his side with his jaw still "
        "set",
        "a front-left medium shot of him standing straight with one arm dropped and his jaw set",
    ),
    B(
        "Three. Below seven, split it between the debt and the index.",
        "第三，7% 以下的，在还债和指数基金之间拆开。",
        "counting_table", ("you",),
        "He stands at the middle of the long oak table with one hand resting on top of one stack "
        "of notes and the other hand resting on a second stack, looking down at both hands.",
        "Camera is a medium shot from the far end of the table at tabletop height, the two stacks "
        "separated in frame with the warm dark hall beyond him.",
        "The brass lamp throws a low even rake that lights both stacks equally, and his face sits "
        "in the soft warm fall-off between them. The mood is both at once, deliberately.",
        "a medium shot from the far end of the table at tabletop height with both stacks in frame",
        "the two banknote stacks, whose corners lift together on the same draught",
        "he lifts his right hand off the first stack and moves it halfway toward the second, then "
        "stops",
        "drifts slowly from one stack to the other, because the money is going both ways at once",
        "he settles both hands flat, one on each stack, holds them there, and looks up",
        "a medium shot from mid-table of him with one hand on each stack and his head lifting",
    ),
    B(
        "Four. Build the emergency fund while you do, or the card refills.",
        "第四，同时把应急金建起来，否则那张卡会自己长回来。",
        "kitchen_night", ("you",),
        "He stands at the kitchen counter beside the sink with one hand resting on the laminate "
        "and the other raised slightly, palm up, looking down at the counter as if setting "
        "something aside there.",
        "Camera is a medium shot from the front at chest height, the window with the dark blue "
        "night filling the background behind him and the warm bulb above out of frame.",
        "Warm light from the pendant lamp falls softly from behind camera onto the counter and his "
        "hands, while the window behind him stays flat cold blue. The mood is putting something "
        "aside, on purpose.",
        "a front medium shot at chest height with the cold blue window filling the background",
        "the curtain over the sink window, which lifts and settles against the night air",
        "he sets his raised hand down flat on the counter, then slides it a few inches away from "
        "the other hand",
        "drops slowly to counter height, because what matters is happening on the surface",
        "he straightens up, keeps both hands on the counter, and looks down at the gap between "
        "them",
        "a medium shot at counter height of him with both hands apart on the counter and the dark "
        "window behind",
    ),
    B(
        "That's the whole system. It fits on the back of an index card.",
        "这就是整套系统。它小到能写在一张索引卡的背面。",
        "porch", ("you",),
        "He stands on the wooden porch at the top of the steps with both hands held out in front "
        "of him at chest height, framing an invisible rectangle in the air between them.",
        "Camera is a medium shot from the front at chest height, the mailbox and the potted fern "
        "at the bottom of the steps and the open front door blurred behind him.",
        "Low golden-hour light rakes across the porch boards and catches his hands and one side of "
        "his face, while the doorway behind him falls into warm shadow. The mood is small, "
        "complete, and portable.",
        "a front medium shot at chest height on the porch with the mailbox and fern below",
        "the potted fern beside the steps, whose fronds turn slowly in the evening air",
        "he brings both hands closer together, shrinking the rectangle he is framing, then holds "
        "them still",
        "pushes in slowly toward the small gap between his hands, because the whole system is that "
        "small",
        "he lowers both hands to his sides, straightens his back, and looks out past the mailbox",
        "a front medium shot of him standing on the porch with both hands lowered in golden light",
    ),
    # ---------------------------------------------------------------- 81–88 收尾
    B(
        "It's 1:52 now. You wrote your rate down. Twenty-two point one five.",
        "现在是 1:52。你把利率写下来了。22.15。",
        "kitchen_night", ("you",),
        "He sits at the oak table with the spiral notebook open in front of him and the pen laid "
        "across the page, one hand resting flat beside the book, looking down at what he wrote.",
        "Camera is a medium close shot from the front at table height, the notebook open in the "
        "foreground and his face just above it in warm light.",
        "The pendant bulb throws warm light straight down onto the open page so the paper glows, "
        "and the same light rims the top of his head and shoulders. The mood is five minutes "
        "later, something has changed.",
        "a front medium close shot at table height with the open notebook in the foreground",
        "the pendant bulb above, which has stopped swaying and now burns perfectly still",
        "he lifts his hand off the table, picks up the pen, and sets it back down on the page",
        "pulls back slowly from the page to his face, because the number is read and now we watch "
        "him",
        "he sits back in the chair, folds his arms, and looks across the dark kitchen",
        "a medium shot from table height of him sitting back with arms folded in the warm kitchen",
    ),
    B(
        "Above the line. So you already know what tomorrow looks like.",
        "在线的上面。所以你已經知道明天长什么样了。",
        "ledger_room", ("you",),
        "He stands on the chalk number line with one foot clearly forward of the marked point, "
        "both hands open at his sides, facing down the length of the hall toward the windows.",
        "Camera is a medium wide shot from floor level at the far end of the hall, the chalk line "
        "running toward camera and him standing on it in the middle distance.",
        "Warm shafts from the arched windows light the far end of the hall brightly and leave him "
        "in warm half light, with dust drifting through the beams between camera and him. The "
        "mood is a position, taken and settled.",
        "a floor-level medium wide shot from the far end with the chalk line running toward camera",
        "the dust in the window shafts, which drifts steadily across the frame toward camera",
        "he shifts his weight forward onto the front foot and holds it there without moving",
        "pushes in slowly along the chalk line toward him, because we are walking up to where he "
        "stands",
        "he brings both hands together in front of him, folds them, and looks straight ahead down "
        "the hall",
        "a floor-level medium shot of him standing on the marked side of the line with folded "
        "hands",
    ),
    B(
        "Not because a video told you. Because the arithmetic did.",
        "不是因为一个视频这么说。是因为算术这么说。",
        "ledger_room", ("you",),
        "He stands directly beneath the giant brass balance scale with both hands resting on the "
        "stone pedestal, head tipped back to look up at the beam high above him.",
        "Camera is a low medium wide shot from the floor looking up, the massive brass column "
        "rising through frame with him small at its base.",
        "Warm light from the windows catches only the top of the scale and leaves the base in deep "
        "warm shadow, so he is lit mostly by the soft glow bouncing off the brass. The mood is "
        "impersonal, and that is the comfort.",
        "a low medium wide shot from the floor looking up at the scale with him small at its base",
        "the fine brass chain of the scale, which hangs perfectly still for the first time",
        "he lifts both hands off the pedestal, turns his palms upward, and lets them fall back to "
        "his sides",
        "tilts slowly upward to follow the column of the scale to the top of frame",
        "he lowers his chin, steps back from the pedestal, and stands with both arms at his sides",
        "a low medium wide shot of him standing back from the scale base with the column rising "
        "above",
    ),
    B(
        "And the arithmetic has never once cared how you feel about debt.",
        "而算术从来没有在乎过你对这笔债是什么感受。",
        "ledger_room", ("you",),
        "He walks slowly away from the scale along the chalk number line with his hands in his "
        "sweatshirt pockets, shoulders level, head down, not looking back at the scale behind him.",
        "Camera is a medium wide shot from the side at hip height, tracking position, the empty "
        "rows of wooden chairs crossing the middle distance.",
        "Warm window shafts fall across the floor in wide bands and he passes through each one in "
        "turn, brightening and dimming as he goes. The mood is moving on, unimpressed and "
        "unhurried.",
        "a side medium wide shot at hip height with the empty chair rows in the middle distance",
        "the dust in each window shaft, which swirls once as he walks through it",
        "he walks four steady paces along the line, then slows and comes to a stop",
        "tracks with him along the line, never overtaking, keeping him centred in frame",
        "he turns his head slightly to look back over one shoulder, then turns forward again and "
        "keeps still",
        "a side medium wide shot of him stopped mid-hall with the empty chairs and the chalk line",
    ),
    B(
        "Maya's twenty months will end. Yours will end too, eventually.",
        "Maya 的那 20 个月会结束。你的也会，早晚的事。",
        "counting_table", ("maya",),
        "Maya stands at the near end of the long oak table with both hands flat on the bare wood "
        "where her stack used to be, her head level, looking straight out along the table.",
        "Camera is a medium shot from the far end of the table at tabletop height, the long empty "
        "tabletop stretching toward her and the brass lamp glowing behind camera.",
        "Warm light from the lamp behind camera rakes along the table and lands on her hands and "
        "the bare wood, while the far end of the hall stays in deep shadow. The mood is an end, "
        "already visible from here.",
        "a medium shot from the far end at tabletop height with the empty table stretching toward "
        "her",
        "the dust drifting through the window shaft, which settles onto the bare wood in front of "
        "her",
        "she lifts both hands slowly off the wood, then lays them back down flat and still",
        "pushes in slowly toward her along the empty table, because the finish line is at her end",
        "she straightens her back, drops her hands to her sides, and gives one small nod",
        "a medium shot from mid-table of her standing straight with bare wood in front of her",
    ),
    B(
        "The quiet part is that nobody will be there when it does.",
        "安静的那部分是：那一天到来时，不会有人在旁边。",
        "sidewalk", ("you",),
        "He walks along the grey city sidewalk with both hands pushed into his sweatshirt pockets, "
        "his shoulders level and his head down, passing the bus stop shelter and the red fire "
        "hydrant.",
        "Camera is a medium wide shot from the side at chest height, the cracked concrete paving "
        "running toward camera and the brick storefronts with rolled-down grates behind him.",
        "Flat pale morning light with thin mist fills the street and separates him cleanly from "
        "the blurred brick storefronts, throwing almost no shadow at all. The mood is quiet, "
        "unaccompanied, and completely fine with that.",
        "a side medium wide shot at chest height tracking along the cracked concrete paving",
        "the thin morning mist, which drifts slowly across the pavement between camera and him",
        "he walks five steady paces along the sidewalk, passes the red fire hydrant, and slows to "
        "a stop beside the bus shelter",
        "tracks with him at chest height without overtaking, keeping him centred as he walks",
        "he turns his head to look at the empty scratched plastic bench inside the shelter, then "
        "turns forward again",
        "a side medium wide shot of him stopped at the bus shelter with the mist drifting past",
    ),
    B(
        "No notification. No party. Just a zero where a number used to be.",
        "没有通知。没有庆祝。只是本该有数字的地方变成了一个零。",
        "kitchen_dawn", ("you",),
        "He sits at the table with one hand resting flat on the open notebook, the other hand "
        "hanging loosely at his side, his head turned toward the window and his expression "
        "completely level.",
        "Camera is a medium close shot from the front right at eye level, the window filling the "
        "background and the notebook edge running along the bottom of frame.",
        "Flat cold dawn light fills the window behind him and rims his shoulder and hair, while "
        "his face stays in soft neutral light with no warm source at all. The mood is "
        "unsentimental, exactly as expected.",
        "a front-right medium close shot at eye level with the bright window behind him",
        "the curtain at the window, which hangs completely still in the flat morning light",
        "he lifts his hand off the notebook, holds it a few inches above the page, then lays it "
        "back down",
        "holds perfectly still and locked off, because nothing happens here and that is the point",
        "he turns his head back to the notebook, looks down at it, and lets his hand rest flat on "
        "the page",
        "a medium close shot of him looking down at the notebook with one hand flat on the page",
    ),
    B(
        "And that is the version of this that actually lasts.",
        "而这一版，才是真正留得下来的那个。",
        "porch", ("you",),
        "He stands at the bottom of the porch steps beside the mailbox with both hands loose at his "
        "sides, looking down the street into the low golden light, his shoulders down and level.",
        "Camera is a medium wide shot from the side and slightly behind, the porch boards running "
        "toward camera, the doormat and the chipped white railing framing him.",
        "The sun sits almost on the horizon so the whole street is flooded in deep amber, throwing "
        "his shadow long back across the porch boards toward the door. The mood is finished, "
        "quiet, and durable.",
        "a side medium wide shot from slightly behind with the porch boards running toward camera",
        "his long shadow on the porch boards, which stretches further as the last light drops",
        "he takes one slow step down onto the path, stops, then straightens and keeps both hands "
        "loose at his sides",
        "pulls back slowly and rises, because we are leaving him standing there",
        "he turns his head once to look back at the house, then turns forward again and stands "
        "still",
        "a medium wide shot from the porch of him standing at the bottom of the steps in deep "
        "amber light",
    ),
]
