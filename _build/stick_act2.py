# -*- coding: utf-8 -*-
"""ACT 2（第 25–38 镜）：MAYA · 22.15% · 还债赢 $995

这一幕是全片的「高地」——差额最大、结论最硬的一侧。
$1,569 利息 vs $574 投资收益 → 还债赢 $995（20 个月）。数字来自 _build/stick_numbers.py。
"""
from stick_world import B  # noqa: F401

BEATS = [
    # ---------------------------------------------------------------- 25–30 她的处境
    B(
        "Maya owes eight thousand on a card at twenty-two point one five.",
        "Maya 信用卡欠 8000，年利率 22.15%。",
        "maya_apt", ("maya",),
        "Maya sits on the edge of a stacked cardboard box in the middle of her cluttered studio, "
        "leaning forward with her elbows on her knees and a single credit card statement held "
        "open in both hands.",
        "Camera is a medium shot from the front left at hip height, angled down slightly, with "
        "stacks of boxes filling the frame behind her and the bare bulb hanging above.",
        "The bare bulb on its wire throws hard warm light straight down onto her and the paper, so "
        "the boxes behind fall into deep warm brown shadow with only their top edges catching "
        "light. The mood is cramped, exposed, and finally looking.",
        "a front-left medium shot at hip height with the stacked boxes filling the frame behind "
        "her",
        "the bare bulb on its wire above her, which swings and drags her shadow across the "
        "cardboard",
        "she lifts the statement higher with both hands and tilts it toward the bulb to read it "
        "properly",
        "pushes in slowly toward the paper in her hands, because the number on it is the whole "
        "problem",
        "she lowers the paper into her lap, sits back, and presses the heel of one hand against "
        "her forehead",
        "a medium shot from the front with the statement dropped into her lap and her hand at her "
        "forehead",
    ),
    B(
        "Her minimum payment is a hundred and sixty dollars and change.",
        "她的最低还款额是 160 美元多一点。",
        "maya_apt", ("maya",),
        "Maya crouches beside the small round table with the statement spread flat under one palm, "
        "the other hand holding a pen poised just above the paper without touching it.",
        "Camera is a high medium shot angled down from directly above the table, showing the "
        "paper, her hand, the pen, and the top of her head entering frame at the bottom.",
        "The bare bulb throws a hot pool of light onto the paper so the white sheet glows, while "
        "her auburn bob and shoulders fall into warmer shadow around it. The mood is a small "
        "number, examined closely.",
        "a high medium shot angled straight down over the small round table",
        "the loose corner of the statement, which lifts and settles on the draught from the window",
        "she brings the pen down and underlines one line on the paper, then lifts it away and "
        "holds it still",
        "pulls back slowly upward, because the number matters less than how small it looks from "
        "farther away",
        "she sets the pen down on the paper, straightens up out of the crouch, and steps back "
        "from the table",
        "a medium shot from table height of her standing back with the underlined statement lying "
        "open",
    ),
    B(
        "She's been paying that for two years. The balance has barely moved.",
        "她这样还了两年。余额几乎没动。",
        "maya_apt", ("maya",),
        "Maya stands with her back to the leaning mattress, arms hanging loose, head tipped back "
        "against the wall, staring up at the bare bulb with her mouth set in a flat line.",
        "Camera is a medium wide shot from across the room, shooting past the leaning mattress so "
        "the mattress edge cuts diagonally into the left of frame.",
        "The bare bulb is in frame above her and flares warmly, leaving the rest of the studio in "
        "deep brown shadow so only her face, hands and the mattress edge are readable. The mood is "
        "two years gone and nothing to show.",
        "a medium wide shot across the room, the leaning mattress cutting diagonally into frame "
        "on the left",
        "the bulb above her, which flickers once and makes her shadow jump on the brick wall",
        "she pushes her head off the wall, rolls her shoulders back, and lets both arms swing out "
        "to her sides",
        "tracks slowly to the right to clear the mattress, because we are moving around to see "
        "her properly",
        "she brings both hands up, counts something off on her fingers, then drops her hands and "
        "stares at the floor",
        "a medium wide shot from the right with her standing clear of the mattress, both hands "
        "dropped, head down",
    ),
    B(
        "First month interest alone comes to a hundred and forty-seven dollars.",
        "光是第一个月的利息就是 147 美元。",
        "maya_apt", ("maya",),
        "Maya sits cross-legged on the floor beside the round table with the statement on her knee "
        "and both hands held out in front of her, palms up, as if carrying something heavy in "
        "each.",
        "Camera is a medium close shot from the front at floor level, the floorboards running "
        "toward camera and her face framed from mid-chest up.",
        "Warm light from the bare bulb rakes in from the upper right and catches one cheekbone and "
        "the palms of her hands, leaving the other side of her face in warm shadow. The mood is a "
        "weight, finally measured.",
        "a floor-level medium close shot from the front with the floorboards running toward camera",
        "the paper on her knee, which slides a little as she shifts her crossed legs",
        "she tips both palms as if weighing them, lowers the left and raises the right, then holds "
        "both perfectly level",
        "rises slowly from floor level to sit at her eye height, because the realisation is "
        "lifting her head",
        "she closes both hands into fists, lets them fall onto her knees, and looks down at the "
        "statement",
        "a medium close shot at eye height with both fists resting on her knees and the statement "
        "in her lap",
    ),
    B(
        "So of her hundred and sixty, twelve dollars reach the actual debt.",
        "所以那 160 里，真正落到本金上的只有 12 块。",
        "maya_apt", ("maya",),
        "Maya leans over the round table with both hands planted flat on its surface, shoulders up "
        "around her ears, staring down at the paper with her eyebrows pulled low and tight.",
        "Camera is a medium shot from her left side at chest height, the table edge running across "
        "frame and the brick wall window behind her.",
        "Hard warm light from the bulb above falls almost straight down, putting her eye sockets "
        "in shadow and leaving a hot highlight along her forearms and the paper. The mood is "
        "cheated, quietly furious.",
        "a left-side medium shot at chest height with the table edge running across frame",
        "the bare bulb above, which sways and drags the hot highlight back and forth across the "
        "paper",
        "she presses both palms harder onto the table, pushes herself back upright, and folds her "
        "arms tight",
        "pulls back slowly to a wider shot, because the anger is bigger than the table",
        "she uncrosses her arms, slaps one hand flat down on the paper, and leaves it there with "
        "her fingers spread",
        "a left-side medium shot of her upright with one hand flat on the statement and her arms "
        "unfolded",
    ),
    B(
        "She switches. Every spare dollar at the card. No investing. No exceptions.",
        "她改了策略。每一分闲钱都砸向这张卡。不投资。不留例外。",
        "maya_apt", ("maya",),
        "Maya stands in the middle of the studio with her feet shoulder width apart, both fists "
        "clenched at her sides, chin lifted, staring straight ahead at the far wall.",
        "Camera is a medium shot from the front at chest height, framed tight enough that the "
        "boxes on either side press in from both edges of frame.",
        "Warm light from the bulb above and slightly behind her rims her shoulders and hair, while "
        "her face stays in firm half light with a bright catch in both eyes. The mood is decided, "
        "jaw set, no discussion.",
        "a front medium shot at chest height with boxes pressing in from both edges of frame",
        "the cardboard flaps of the nearest box, which lift and settle as she pushes past them",
        "she takes one hard step forward, plants her foot, and clenches both fists tighter at her "
        "sides",
        "pushes straight in toward her face, because this is the moment the decision gets made",
        "she lifts her chin higher, exhales once through her nose, and nods a single hard nod",
        "a front medium close shot of her with chin lifted, both fists clenched, warm rim on her "
        "shoulders",
    ),
    # ---------------------------------------------------------------- 31–38 结果与对照
    B(
        "Twenty months later it's gone. Fifteen hundred sixty-nine in interest.",
        "20 个月后还清。总共付了 1569 的利息。",
        "counting_table", ("maya",),
        "Maya stands at the near end of the long oak counting table with both hands resting flat "
        "on the empty tabletop in front of her, the banknote stack entirely gone, looking down at "
        "the bare wood.",
        "Camera is a medium shot from the far side of the table looking back toward her, the long "
        "empty tabletop stretching toward camera and the brass hall in shadow behind.",
        "A single warm shaft from the arched window falls across the empty wood in front of her, "
        "so the place where the stack used to be is lit and bare. The mood is finished, quiet, "
        "and slightly anticlimactic.",
        "a medium shot from the far side of the table with the long empty tabletop stretching "
        "toward camera",
        "the dust drifting through the window shaft, which settles slowly onto the bare wood",
        "she runs both hands slowly forward across the empty tabletop, then stops and holds her "
        "palms flat on the wood",
        "pulls back slowly along the table, because the emptiness only reads once we see how much "
        "table there is",
        "she straightens up, lifts both hands off the wood, and lets them hang open at her sides",
        "a medium shot from mid-table of her standing with both hands open at her sides and bare "
        "wood in front of her",
    ),
    B(
        "Now the other version. She invests instead and pays only the minimum.",
        "现在换一个版本：她拿去投资，只还最低。",
        "ledger_room", ("maya",),
        "Maya stands in the warm hall with one arm extended out to her side at shoulder height, "
        "open palm up, her head turned to look along her own outstretched arm as if following it "
        "somewhere.",
        "Camera is a medium shot from her right at chest height, the brass scale pedestal filling "
        "the background behind her and dust visible in the window light.",
        "Warm window light rakes across her from the left and separates her cleanly from the deep "
        "brown shadow of the hall, with a soft gold rim along her extended forearm. The mood is "
        "an alternative branch, being looked at.",
        "a right-side medium shot at chest height with the scale pedestal filling the background",
        "the dust motes in the window shaft, which stream past her outstretched hand",
        "she turns her palm over, brings the arm back across her body, and extends the other arm "
        "instead",
        "arcs around her to the front, because we are now comparing two directions she could take",
        "she lowers both arms, turns her whole body to face the scale, and plants her feet",
        "a front medium shot of her facing the brass scale with both arms lowered in the warm hall",
    ),
    B(
        "Twenty months in the market at a modest average: about five seventy-four.",
        "同样 20 个月放进市场，按保守平均算：大约 574。",
        "counting_table", ("maya",),
        "Maya stands beside the middle stack of banknotes with one hand resting lightly on top of "
        "it, her head tilted down, studying the height of the stack against her own hand.",
        "Camera is a medium close shot from the front at table height, the stack of notes sharp in "
        "the foreground and her face softly lit just behind it.",
        "The brass desk lamp throws a low warm rake across the tabletop so the edges of the notes "
        "glow, while her face sits in the softer fall-off of the same light. The mood is a smaller "
        "number, measured honestly.",
        "a front medium close shot at table height with the note stack sharp in the foreground",
        "the top corner of the nearest banknote, which lifts and settles in the warm draught",
        "she slides her hand down the side of the stack, measuring it with her thumb and "
        "forefinger, then stops",
        "drifts slowly upward from the stack to her face, because the comparison lives in her "
        "expression",
        "she lifts her hand off the stack, holds it a few inches above it, then lets it drop back "
        "down",
        "a medium close shot at table height with her hand resting on top of the smaller stack",
    ),
    B(
        "Interest paid: one five six nine. Market gained: five seventy-four.",
        "付出的利息 1569。市场赚到 574。",
        "counting_table", ("maya",),
        "Maya stands back from the table with both arms extended forward, one palm held high and "
        "one held low, clearly holding two different amounts apart in mid air.",
        "Camera is a level medium wide shot from the front, the long table running horizontally "
        "behind her and the brass lamp glowing at the far end.",
        "Even warm light from the lamp at the end of the table leaves both of her hands equally "
        "lit against the dark far end of the hall, so the height difference reads clearly. The "
        "mood is two numbers, held up side by side.",
        "a level medium wide shot from the front with the long table running horizontally behind "
        "her",
        "the brass lamp at the far end, whose warm glow steadies and stops flickering",
        "she raises the high palm another few inches and lowers the other, widening the gap "
        "between her hands",
        "widens out into a wider shot, because the gap between the two hands is the whole point",
        "she holds the gap still, then slowly brings both hands down together onto the tabletop",
        "a level medium wide shot of her with both hands flat on the table and the lamp glowing "
        "behind",
    ),
    B(
        "Paying it off wins by nine hundred and ninety-five dollars.",
        "还债这边赢了 995 美元。",
        "counting_table", ("maya",),
        "Maya stands at the near end of the table with both hands planted flat on the wood and her "
        "shoulders squared, chin level, looking straight out toward the camera with her mouth set "
        "in a firm line.",
        "Camera is a medium shot from the far end of the table looking straight down its length at "
        "her, the tabletop converging toward her in strong perspective.",
        "Warm light from the arched windows falls across her from the right and leaves the long "
        "table in front of her sliding into shadow, so she is the only bright thing in frame. The "
        "mood is settled, no longer arguable.",
        "a medium shot from the far end of the table looking down its length straight at her",
        "the dust in the window light, which drifts down and settles across the table between "
        "camera and her",
        "she pushes both hands down harder onto the wood, lifts her chin, and holds the pose "
        "without moving",
        "pushes in slowly down the length of the table, because the verdict is walking toward us",
        "her shoulders drop an inch as the tension leaves them, and she exhales with her mouth "
        "closed",
        "a medium shot from mid-table of her standing squared up with both hands flat on the wood",
    ),
    B(
        "And that nine ninety-five is guaranteed, immediate, and tax free.",
        "而且这 995 是确定的、立刻到手的、还不用交税。",
        "ledger_room", ("maya",),
        "Maya stands directly beneath one of the tall arched windows with both arms raised slightly "
        "out to her sides, palms turned up, head tipped back into the warm light falling on her "
        "face.",
        "Camera is a medium shot from below and in front, looking up at her against the bright "
        "arched window so the window frame curves over the top of frame.",
        "Strong warm backlight pours through the arch and wraps her whole silhouette in gold, with "
        "dust clearly drifting through the beam around her raised hands. The mood is certain, "
        "warm, unarguable.",
        "a low front medium shot looking up at her against the bright arched window",
        "the dust motes in the window shaft, which rise slowly through the light around her",
        "she turns both palms fully upward, holds them there, then closes them into fists and "
        "pulls both arms in toward her chest",
        "rises slowly until it is level with her, because we are coming up to her height as the "
        "point lands",
        "she opens both fists again, spreads her fingers wide, and lets her arms fall open at her "
        "sides",
        "a level medium shot of her backlit in the arch with both arms open and dust drifting "
        "around her",
    ),
    B(
        "At twenty-two percent there is no version where the market keeps up.",
        "在 22% 这个利率上，不存在市场能追得上的版本。",
        "maya_apt", ("maya",),
        "Maya stands in the middle of the studio with one arm swept out wide to her left, palm "
        "open, her whole body turned to follow the sweep, chin lifted and mouth open as she "
        "states it.",
        "Camera is a medium wide shot from the front right, the boxes stacked low on both sides so "
        "the sweep of her arm has clear space to travel through.",
        "The bare bulb throws hard light down from directly above her so her raised arm casts a "
        "long sweeping shadow across the cardboard and floor. The mood is emphatic, finally "
        "certain, no longer asking.",
        "a front-right medium wide shot with the low box stacks leaving clear space for her arm to "
        "sweep",
        "her own shadow on the cardboard, which sweeps across it as her arm travels",
        "she sweeps her arm across her body from right to left in one continuous movement and "
        "holds it out at the far side",
        "follows her arm across the sweep, because the gesture is the argument",
        "she drops the arm, plants both feet, and nods once with her jaw still set",
        "a front-right medium wide shot of her with both arms lowered and her feet planted in the "
        "cluttered studio",
    ),
    B(
        "Maya's answer isn't even close. Maya's answer is simple: pay it.",
        "Maya 的答案根本不接近。她的答案很简单：还掉。",
        "maya_apt", ("maya",),
        "Maya crouches down and picks up the credit card statement from the round table with both "
        "hands, holding it out in front of her at eye level and looking straight at it, perfectly "
        "steady.",
        "Camera is a medium shot from the front at eye level, the leaning mattress and the box "
        "stacks in soft focus behind her, the bare bulb burning above.",
        "Warm light from the bare bulb drops straight onto the paper in her hands so the sheet "
        "glows, and the glow bounces back up onto her chin and the underside of her jaw. The mood "
        "is done talking, doing it.",
        "a front medium shot at eye level with the leaning mattress softly blurred behind her",
        "the bare bulb above, which stops swaying and burns perfectly steady for the first time",
        "she lifts the statement higher, holds it level with her eyes, then lowers it and folds it "
        "once down the middle",
        "holds completely still and locked off, because the decision needs no camera movement",
        "she tucks the folded statement under one arm, straightens up, and turns toward the door",
        "a front medium shot of her standing straight with the folded statement tucked under her "
        "arm, turning away",
    ),
]
