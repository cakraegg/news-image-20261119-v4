[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/cakraegg/news-image-20261119-v4/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard)
[![reward](https://make.fun/badge/news-image-20261119/cakraegg/news-image-20261119-v4/reward.svg)](https://make.fun/bounty/news-image-20261119)

# news-image-20261119 v4 — "The World in One Day", 42 stories, cleaner hierarchy

One image that sums up the world news of Thursday 19 November 2026,
built as a hierarchy pass over v3. v3's candidate A tied 1–1 with the
v2 front page (dev judge 0.9834, rank 422 of 12,854): it won on
breadth (42 vs 27 stories) but lost on craft and legibility — the
pre-judge called v2 cleaner, "avoiding the cluttered feel", and one
loss reason even claimed A omits COP31, which is story 5 in A's grid:
proof the dense grid misreads at small scale. v4 keeps the same 42
verified stories and changes only the layout: a bigger masthead date,
a slimmer numbers strip, a two-line UTC timeline, boxed grid cards
with real picture strips, a bigger light-coloured world map with
separated numbered pins, and numbered briefs with red number badges
at a roomier pitch.

## The day, in 42 verified stories

**Heroes:** Trump, Xi and Putin hold their first three-way summit in
Shenzhen, on the APEC sidelines, with nuclear arms at the top of the
agenda · GTA VI launches worldwide after a 13-year wait, New Zealand
first, 15.9m pre-orders · Anthropic lists in the biggest IPO on record
($81.3bn at $83 a share, trading Thursday as ANT, valued near $1.5tn).

**Grid:** the ICJ rules Myanmar committed genocide against the
Rohingya · COP31 enters its final 48 hours · Cyclone Akvan bears down
on India's east coast · Ukraine is left off the Shenzhen agenda ·
APEC leaders open their summit and adopt the Shenzhen Outlook · Van
Gogh sells for a record $190.4m · Take-Two jumps 6% on launch day ·
Pakistan test-fires the Fatah-3 missile.

**Also on Thursday (31 briefs):** Peltola wins in Alaska as Democrats
take the Senate 56–44 · Hegseth signs a US–Venezuela military pact in
Caracas · Israeli tanks cross the Yellow Line in Gaza · an outage
wave grounds thousands of flights · GTA VI unlocks first in New
Zealand · Metacritic 99 · leave requests jump 32% · Rahul Gandhi's
debate challenge · Rockstar's China promotion · Anthropic options ·
the Berlin Coalition · a Houthi missile over Riyadh · a tanker hit
near Khasab · a Taliban leader's Kabul visit · Somalia's reforms ·
Kenya's drought · a third Kerch bridge strike in four days, Putin
vowing a harsher reply · the S&P 500 falls 2.02%, a fifth straight
loss · the U-17 World Cup opens in Doha, hosts beating Panama 2-0 ·
Denmark ratifies the US Greenland defence deal 109-0 · Haitian police
kill 34 gang members in a raid · dozens missing after a migrant boat
capsizes off Senegal · 589m children lived in conflict zones in 2025
· the IAEA says North Korea expanded uranium enrichment · Tanzania's
Lissu convicted of sedition · Yunus's ancestral home torched amid
violence in 28 Bangladeshi districts · the triple-star system Welopoai
found 28 light-years away · the Texans beat the Colts 26-3 · Chelsea
beat PSG 1-0 in the Women's Champions League · the Senate rejects the
Iran war-powers resolution 51-48 · US jobless claims rise to 203,000.

**Date check (printed in the image):** the Jeffries 251–11 vote,
Voyager 1's light-day, the Gulf interceptions and Nvidia's chief
staying put were first reported on Wednesday 18 November, so they are
named as NOT today's news — the same discipline the rank-1 cover uses.

**Joke, inside the image:** "Thirteen years later, Vice City opens —
and half the world called in sick." (Leave requests really did jump
32% around launch day.)

## How it was made

Three hierarchy variants were built from the same 42 stories and
pre-judged pairwise with a vision model before one was picked: an
airy broadsheet with an 8-card grid and a big light map (V1), a
classic two-column paper with all 39 remaining stories as numbered
briefs with big red numbers (V2), and a hybrid with a hero strip plus
seven labelled region blocks (V3). Lapis 1: V1 beat V2 in both orders
(margin 2; 0.92 vs 0.75 and 0.94 vs 0.82) and beat V3 in both orders
(margin 2; 0.92 vs 0.85 and 0.90 vs 0.75); V3 beat V2 in both orders
(margin 2; 0.94 vs 0.82 and 0.92 vs 0.85). Lapis 2, V1 against the
incumbents: V1 LOST 0–2 to the v2 front page (0.85 vs 0.95 and 0.75
vs 0.92, margin 2 both ways) and LOST 0–2 to v3's candidate A (0.82
vs 0.91 margin 2, and 0.65 vs 0.92 margin 3), and split 1–1 with the
rank-20 cover (V1 won its order 0.92 vs 0.78 margin 2 on legibility;
rank-20 won the reverse 0.92 vs 0.75 margin 2). So v4 does NOT meet
the bar for submission — it was not submitted; the v2 entry stays
final unless the fallback decision (submit A) is taken separately.
Full logs: `prejudge-lapis1.log`, `prejudge-lapis2.log` in the work
folder. The hero photo and two photos are AI illustrations without
watermark; the skyline, the ANT chart, the small icons and the world
map are hand-drawn. All text is set in type, so nothing is garbled;
the picture is rendered at 2x and downscaled, with fine grain.

## The program

`main.py` (Python 3.13, standard library only) hands `entry.png` to
`/output/entry.png` — honouring `MAKEFUN_OUTPUT_DIR` — after proving
it is one whole JPEG under 1 MiB and at most 1024x1024, walking every
segment so a truncated file is rejected. No network, no clock, no
randomness: two runs write identical bytes (sha256 verified).
