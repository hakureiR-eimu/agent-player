---
title: Expeditions
source: https://vic3.paradoxwikis.com/Expeditions
pageid: 5267
categories: [1.13, Scripted_content, Pages_with_obsolete_template_parameters, Expand, Events, Journal]
fetched: 2026-10-27
---
This article has been verified for the current [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) (1.13) of the game.

Victoria 3
Scripted content
Decisions
•
Events
•
Journal entries
General content pages
Corn Laws
•
Domestic affairs
Expeditions
•
Ideology content
Interest group content
•
Krakatoa
Journal entry events
•
Revolution events
Production and technology content
Country content pages
American
•
Austrian
•
Balkan
•
Brazilian
British
•
Chinese
•
Colonial Indies
French
•
German
•
Greek
Japanese
•
Korean
•
Montenegrin
Philippine
•
Portuguese
•
Russian
Southern Africa
•
South America
Spanish
•
Turkish
Special content pages
Halloween
Expeditions are journal entries and events that represent one of the historical explorations undertaken by different countries in the Victorian era.

Most random monthly expedition events can only trigger once per expedition.

## Antarctic

The following journal entry and events represent expeditions to reach the South Pole.[1]

id

### Antarctic Expedition

Through the wonders of technology and the heroism of our explorers, the interior of the Antarctic Continent may finally be accessible! The race is on, and we must be the first to the Pole!
---

| Shown conditions: Has researched Sea Lane Strategies No country has reached the South Pole Not undertaking any expedition | Useable conditions: Is at peace Has 3 or more admirals |
|---|---|
| Effects: Triggers the event Expedition to Antarctica |  |

id

### Antarctic Expedition

Through the wonders of technology and the heroism of our explorers, the interior of the Antarctic Continent may finally be accessible. The race is on, and we must be first to the Pole!
---

| Visibility conditions: Only while active |  |
|---|---|
| Activated by: Event A Polar Explorer |  |
| Completion conditions: Expedition progress is 8 or more Event The South Pole has occurred | Effects when completed: Trigger event Homecoming Remove Expedition Budget Expedition Budget Country modifier 0.025% of GDP Government expenses Sets Antarctic Expedition bonus for the Grand Exhibition |
| Failure conditions: Expedition peril is 8 or more | Effects when failed: Trigger event The End Is Near Remove Expedition Budget Expedition Budget Country modifier 0.025% of GDP Government expenses |
| Every month, the following weighted random events can happen: (100) Nothing (10) +1 progress and peril (20) At the Mountains of Madness (50) Halfway Hut (10) Missed the Mark (65) The South Pole (10) Dog Meat (30) Pack Ice (50) The Great Ice Barrier (20) The Transantarctic Mountains (5) Strange Marks |  |

id

### Expedition to Antarctica

The Antarctic Continent remains almost entirely unexplored. An expedition to this vast frozen waste would be expensive and fraught with peril, but the glory of being first to the Pole would be immense.
---

Flavor text:
Murmurs and whispers soon fill the halls of the world's most prestigious science academies, as the prospect of reaching the final geographical discovery becomes much more than a fever dream.
---

| Is triggered by: Decision Antarctic Expedition |
|---|
| Trigger conditions: None |
| I know just the man for the job. Trigger the event A Polar Explorer Can the treasury bear such an expense? No effect |

id

### A Polar Explorer

We must choose a leader for the upcoming expedition to the Antarctic Continent. A few promising candidates have distinguished themselves.
---

Flavor text:
Few people are capable of rightly appreciating this heroic deed, this brilliant proof of human courage and energy. These men will sail right into the heart of the pack ice, which all previous explorers have regarded as certain death. These men are heroes — heroes in the highest sense of the word.
---

| Is triggered by: Event Expedition to Antarctica |
|---|
| Trigger conditions: Has an admiral who is not busy |
| Immediate effects: Selects up to four admirals that are Not busy Not the ruler Preferring ones with the trait explorer or flagged as a polar explorer Expedition progress and peril are set to 1 |
| [Admiral] [is an experienced polar explorer]. [Admiral] becomes the expedition leader and 'busy' Gain Expedition Budget Expedition Budget Country modifier 0.025% of GDP Government expenses Activate journal entry Antarctic Expedition |

id

### At the Mountains of Madness

The expedition spots the twin volcanic peaks of Erebus and Terror on the horizon. When they were first discovered by James Clark Ross, Erebus was observed to be in eruption. Thankfully we find the mountains at peace.
---

Flavor text:
"They rose grimly into the western sky; allowing us to distinguish various bare, bleak, blackish summits, and to catch the curious sense of phantasy which they inspired as seen in the reddish antarctic light against the provocative background of iridescent ice-dust clouds." - Lovecraft
---

| Is triggered by: Monthly pulse of journal entry Antarctic Expedition |
|---|
| Trigger conditions: Expedition progress is at least 2 This event has not triggered before |
| We should move on quickly. Expedition progress increases by 1 Collect geological samples. 50 weight: +25 weight if ruler has Explorer +100 weight if expedition leader has Explorer The expedition leader gains Studied the Polar Mountains Studied the Polar Mountains Character modifier +20 Popularity for 5 years The country gains Antarctic Research Antarctic Research Country modifier +20 Prestige for 5 years Expedition progress increases by 1 50 weight: Expedition peril increases by 1 Ascend Mount Erebus. We will be the first to reach the crater! 25 weight: +12 weight if ruler has Explorer +100 weight if expedition leader has Explorer The expedition leader gains Studied the Polar Mountains Studied the Polar Mountains Character modifier +40 Popularity for 5 years The country gains Climbed Erebus Climbed Erebus Country modifier +50 Prestige for 5 years Expedition progress increases by 1 75 weight: Expedition peril increases by 5 |

id

### Halfway Hut

![Event trigger.png](https://central.paradoxwikis.com/images/3/35/Event_trigger.png) **The below description is one of several available for this event.**

The expedition disembarks upon the frozen shore of the Antarctic continent. At a relatively accessible location, a crewman suggests constructing a durable hut where we could rest and leave supplies for the return journey, and perhaps even for future explorers.
---

Flavor text:
"The temperature of the hut is low, of course, but in every other respect we are absolutely comfortable. There is an unlimited quantity of biscuit, and our discovery at Pram Point means an unlimited supply of seal meat. An empty kerosene tin and some firebricks have been made into an excellent little stove, which has been connected to the old stove-pipe. Already we can regard it as a temporary home." - Scott
---

| Is triggered by: Monthly pulse of journal entry Antarctic Expedition |
|---|
| Trigger conditions: Expedition progress equals 1 This event has not triggered for this expedition |
| Enabled if: No country has built a halfway hut This hut shall stand the test of time. Builds a halfway hut for any country to use Expedition peril increase by 1 Enabled if: No country has built a halfway hut The hut need only last until our return. Expedition progress increases by 1 Enabled if: Some country has built a halfway hut We should rest and resupply before moving on. Expedition progress increases by 1 Expedition peril increases by 1 |

id

### Missed the Mark

The expedition has realized that they have overshot on their route towards the next supply depot.
---

Flavor text:
"As we continued our way through the merciless white, snow cairns had become more and more scarce. Or that we thought. God help us, we can't keep up this pulling, that is certain. Amongst ourselves we are unending cheerful, but what each man feels in his heart I can only guess." - Scott
---

| Is triggered by: Monthly pulse of journal entry Antarctic Expedition |
|---|
| Trigger conditions: Expedition progress is greater than 3 This event has not triggered before |
| We need those supplies. Turn back. 75 weight: +40 weight if ruler has Explorer +150 weight if expedition leader has Explorer Expedition progress decreases by 1 25 weight: Expedition peril increases by 3 Push on, we can do without the supplies. 25 weight: +12 weight if ruler has Explorer +50 weight if expedition leader has Explorer Expedition progress increases by 1 75 weight: Expedition peril increases by 5 |

id

### The End Is Near

The expedition is doomed. Utterly exhausted, frostbitten, and out of supplies, all that is left to do is await the cold embrace of death.
---

Flavor text:
"Every day we have been ready to start for our depot 11 miles away, but outside the door of the tent it remains a scene of whirling drift. I do not think we can hope for any better things now. We shall stick it out to the end, but we are getting weaker, of course, and the end cannot be far. It seems a pity but I do not think I can write more. For God's sake look after our people." - Scott
---

| Is triggered by: Either: Failure of journal entry Antarctic Expedition Abandon ship. choice for the event Icebound (50 weight) |
|---|
| Trigger conditions: None |
| I am just going outside and may be some time. The expedition leader is killed Remove all effects linked to expedition events. |

id

### The South Pole

![Event trigger.png](https://central.paradoxwikis.com/images/3/35/Event_trigger.png) **The below description is one of several available for this event.**

The expedition has reached its destination: the South Pole! [Expedition Leader] proudly erects a tent bearing the [Country adjective] flag, and the crew drink a celebratory mug of cocoa.
---

Flavor text:
The Pole. Unsullied, immaculate. The air glistened as if the snow possessed a light of its own; under our frozen feet must have laid a secret sun.
"It's here." And we took measures, we registered every possible anomaly, "it's here, move the beacon," and then it was here, right before my eyes, and then it was there, closer to the sleds, but it was here. It was finally here, and its reflected pallor illuminated our tired faces. "Gentlemen, now we can rest."
---

| Is triggered by: Monthly pulse of journal entry Antarctic Expedition |
|---|
| Trigger conditions: Expedition progress is at least 6 Is not the first country to reach the south pole |
| Option conditions Enabled if: No other country has already reached the south pole Success! But now the hard journey north begins... Expedition progress increases by 1 Disable future expeditions Enabled if: Another country has already reached the south pole Damnation! And now the hard journey north begins... Expedition progress increases by 1 |

id

### Dog Meat

Supplies are running low for the Antarctic explorers. The crew debates the merits of killing some of the sled dogs, and dividing the meat between the men and the remaining dogs to increase their odds of survival.
---

Flavor text:
"One cannot calmly contemplate the murder of animals which possess such intelligence and individuality, which have frequently such endearing qualities, and which very possibly one has learnt to regard as friends and companions."
"We have agreed to shrink from nothing to achieve our goal! And besides if we do not do this, the dogs will surely die from malnutrition or exhaustion regardless." - Scott
---

| Is triggered by: Monthly pulse of journal entry Antarctic Expedition |
|---|
| Trigger conditions: Expedition progress is at least 3 This event has not triggered before |
| It is the practical thing to do. The expedition leader gains Ate the Dogs Ate the Dogs Character modifier −30 Popularity for 5 years Expedition progress increases by 1 We will not stoop to such barbarism! You pet the dogs and continue the journey. Expedition progress increases by 1 Expedition peril increases by 3 |

id

### Homecoming

![Event trigger.png](https://central.paradoxwikis.com/images/3/35/Event_trigger.png) **The below description is one of several available for this event.**

The crew of the Antarctic expedition have finally returned home. As the first men ever to reach the South Pole, they are lauded as [Country adjective] heroes.
---

Flavor text:
"Glory. Victory. Cheers and parades. Absurd sums of money. Kind words. The repetition of the hero's shadow over one's own name. The crew. That precious group of indomitable bastards. Home. Days. Nights. How much I had missed the days and the nights, their calculated succession. The boredom of the routine. Waking up on my bed. Hot chocolate. Coffee. Tea. My favorite tartlets. How much I had missed the noise from this street."
---

| Is triggered by: Completion of journal entry Antarctic Expedition |
|---|
| Trigger conditions: None |
| Option conditions Enabled if: Is not the first to reach the south pole We will succeed next time. The expedition leader: Gains trait Explorer Is flagged as a polar explorer Gains Successful Polar Explorer Successful Polar Explorer Character modifier +70 Popularity permanently The country gains Pole Expedition Returned Pole Expedition Returned Country modifier +50 Prestige for 5 years Enabled if: Is the first to reach the south pole They are a credit to their nation. The expedition leader: Gains trait Explorer Is flagged as a polar explorer Gains Successful Polar Explorer Successful Polar Explorer Character modifier +35 Popularity The country gains First to the Pole First to the Pole Country modifier +100 Prestige for 5 years |

id

### Pack Ice

Broken pieces of sea ice start to cover the surface of the water as the expedition approaches its destination. The ship's hull tries to make its way through the cold mass by ramming and crushing, but the ice becomes stronger as they advance.
---

Flavor text:
"It wouldn't be sound to confess that such a peril intrigued me, but the imminent arrival of our final goal, announced by the increasing sea ice that surrounded us, could not but terrify and fascinate me at the same time. The snow cover that extended over it had prevented the sea from reflecting our silhouettes or our ship's — there was nothing else to see: it was just us, and the pole."
---

| Is triggered by: Monthly pulse of journal entry Antarctic Expedition |
|---|
| Trigger conditions: Expedition progress is at most 1 This event has not triggered for this expedition |
| Option conditions Always enabled: Onwards! 50 weight: Trigger the event Icebound in 30 days. Expedition peril increases by 1 50 weight: +25 weight if ruler has Explorer +100 weight if expedition leader has Explorer Expedition progress increases by 1 Enabled if: The expedition leader either: Is flagged as a polar explorer Has the Explorer trait AND any of: Mountain Commander, Expert Naval Commander, or Tactful We have to trust [Expedition Leader]'s expertise. Expedition progress increases by 1 |

id

### Icebound

![Event trigger.png](https://central.paradoxwikis.com/images/3/35/Event_trigger.png) **The below description is one of several available for this event.**

A series of pressure waves struck the expedition's ship, causing the ice around it to separate into large pieces. A moment of victory is quickly followed by two floes being pinched on her starboard side, one at her bow and one at her stern. The crew gathers as they make a plan to free her.
---

Flavor text:
"The cold had reached us. The planks of antique oaks were now shyly hidden behind snow-laden layers of white, and the whole ship would have seemed deserted if it wasn't for the tremulous lights that we had managed to keep lit. The ice was engulfing us, and with its natural grace started to stab our precious shelter."
---

| Is triggered by: Choice Onwards! of the event Pack Ice (50 weight) |
|---|
| Trigger conditions: None |
| Option conditions Always enabled: We'll blast through the ice! The ship becomes icebound 20 weight: +10 weight if ruler has Explorer +40 weight if expedition leader has Explorer Expedition progress increases by 1 80 weight: Trigger this event again in 30 days. Enabled if: The ship is icebound Abandon ship. 50 weight: +25 weight if ruler has Explorer +50 weight if expedition leader has Explorer Trigger the event Whaling Station in 30 days. 50 weight: Trigger the event The End Is Near in 30 days. |

id

### Whaling Station

[Expedition Leader] has successfully led the expeditionary crew to a whaling station on South Georgia, braving the journey from Elephant Island in an uncovered lifeboat with meager supplies. Tales of [Expedition Leader]'s heroism resound throughout the nation despite the failure of the expedition.
---

Flavor text:
"During our last night camping under the ruthless white, our cook had asked me if it had been a tough decision, "going back," he had said, "after making it so far, wasn't it hard?". No, I wanted to say. No, it wasn't.
What joy could the pole bring to a man, trapped between the sea and the mountain ranges, a starving silhouette of fog and cold? If the dry air had blown slightly stronger, we would all had dispelled, like diaphanous flakes of snow."
---

| Is triggered by: Choice Abandon ship. of the event Icebound (50 weight) |
|---|
| Trigger conditions: None |
| Three cheers for [Expedition Leader]! The expedition leader Gains trait Explorer Is flagged as a polar explorer Gains Polar Savior Polar Savior Character modifier +25 Popularity for 5 years Remove all effects linked to expedition events. |

id

### The Great Ice Barrier

As the expedition's ship turns to the side, the crew witnesses in awe a high, perpendicular face of ice; their only entrance to the continent.
---

Flavor text:
"And there it stood. If it had a face, I know it'd be laughing at us. That ridiculous cracking sound — the ice breaking. And there it goes, there, a block falls into the sea. Threatening. Fatal. It's in the direction of our ship. This moment had haunted our minds since when we left the last harbor. Sailing had been difficult, but going into that uncharted continent would be like descending into the depths of a frozen hell."
---

| Is triggered by: Monthly pulse of journal entry Antarctic Expedition |
|---|
| Trigger conditions: Expedition progress is less than 2 This event has not triggered before |
| We must climb it! 75 weight: +40 weight if ruler has Explorer +150 weight if expedition leader has Explorer Expedition progress increases by 1 25 weight: Expedition peril increases by 1 We should make a detour around the fissures. Send a notice that the Antarctic Expedition is ongoing |

id

### The Transantarctic Mountains

The expedition has advanced through eternal days of snow marching until finding the impenetrable sight of the Transantarctic Mountains. A new challenge awaits, as their routes have been scarcely documented.
---

Flavor text:
"The ever-grey sky had left us in a state of cruel anesthesia, incapable of discerning the line that separated snow from atmosphere, snow from footprints, snow from us. A sharper grey was laid before us, and in its numbness resided a familiar comfort.
The wall of stone was covered in white, and it took us most of the day to understand that it was no vertical sky, no heaven falling upon us, the final chant, the doomed trumpets, a mirage. Those were mountains."
---

| Is triggered by: Monthly pulse of journal entry Antarctic Expedition |
|---|
| Trigger conditions: Expedition progress is at least 3 This event has not triggered within the last 2.5 years |
| We'll find a new route. 33 weight: +15 weight if ruler has Explorer +33 weight if expedition leader has Explorer Expedition progress increases by 2 33 weight: +15 weight if ruler has Explorer +33 weight if expedition leader has Explorer Expedition progress increases by 1 33 weight: Expedition peril increases by 1 We'll be taking a known approach. Send a notice that the Antarctic Expedition is ongoing |

id

### Strange Marks

During the expedition's advances through the snow a strange rock with unknown marks has been discovered, partly buried under their feet.
---

Flavor text:
"A light-colored rock was dug up this very morning. Its smooth texture and perfect curvature was only interrupted by a pattern of unfamiliar marks, all appearing in a sequence that none of our men could dare to decipher. When positioned between one's eye and the sun, its tone varies, seemingly depending on the time of the day; now white, now yellow, at dusk — green."
---

| Is triggered by: Monthly pulse of journal entry Antarctic Expedition |
|---|
| Trigger conditions: Expedition progress is at least 3 This event has not triggered for this expedition |
| Stop and study it. Takes the rock (provides points for the Grand Exhibition ) 33 weight: +15 weight if ruler has Explorer +33 weight if expedition leader has Explorer Expedition progress increase by 2 33 weight: Send a notice that the Antarctic Expedition is ongoing 33 weight: Expedition peril increase by 1 Ignore it. Expedition progress increases by 1 |

## American West

|  | Please help improve this article or section by [expanding it](https://vic3.paradoxwikis.com/index.php?title=Expeditions&action=edit) with: American West events. |
|---|---|

This expedition has three paths and so can be completed up to three times.[2]

id

### Map the American Western Frontier

Launch an expedition to map out the unknown regions an geography of the North American Western Frontier.
---

| Shown conditions: Has researched Colonization At least one of the following has not been completed: The Buenaventura River The Oregon Trail The Great Salt Lake Not undertaking any expedition | Useable conditions: Is at peace Has an interest in the Pacific Coast region Has researched Quinine Has 3 or more commanders |
|---|---|
| Effects: Triggers event Expedition to Map the Western Frontier |  |

id

### Western Frontier Expedition

An expedition to map out the unknown regions and geography of the North American Western Frontier.
---

| Visibility conditions: Only while active |  |
|---|---|
| Activated by: Event Expedition to Map the Western Frontier |  |
| Completion conditions: Expedition progress is 8 or more | Effects when completed: Randomly triggers an untriggered event: Buenaventura River Oregon Trail The Great Salt Lake Remove Expedition Budget Expedition Budget Country modifier 0.025% of GDP Government expenses Sets Western Frontier Expedition bonus for the Grand Exhibition |
| Failure conditions: Expedition peril is 8 or more | Effects when failed: Trigger event Failed Expedition Remove Expedition Budget Expedition Budget Country modifier 0.025% of GDP Government expenses |
| Every month, the following weighted random events can happen: (80) Nothing (20) +1 progress and peril (20) Swollen River (20) Bear Sighted (10) Wildlife Photography (20) Mountain Sighted (20) Snow on the Ground (20) Undiscovered Plant Species (20) A Circular Expedition (30) A Stop on the Way (15) The Miracle of Life (30) An Explorer's Life for Me (20) A New Quest (20) When the Earth Opened Its Mouth (30) Cabin Fever (5) Bad News (5) [Leader's Vice] Supplies Run Low |  |

## Congo River

The following journal entry and events represent expeditions to map the Congo River.[3]

id

### Congo River Expedition

The heart of the African continent remains a mystery for many. We shall launch an expedition to plot the course of the Congo River.
---

| Shown conditions: Has researched Colonization No country has mapped the course of the Congo River Not undertaking any expedition | Useable conditions: Is at peace Has an interest in the Congo region Has researched Quinine Has 3 or more commanders |
|---|---|
| Effects: Triggers event The Congo River Expedition |  |

id

### Congo River Expedition

The heart of the African continent remains a mystery for many. We shall launch an expedition to plot the course of the Congo River.
---

| Visibility conditions: Only while active |  |
|---|---|
| Activated by: Event The Expedition Arrives |  |
| Completion conditions: Expedition progress is 8 or more | Effects when completed: Trigger event Successful Expedition Remove Expedition Budget Expedition Budget Country modifier 0.025% of GDP Government expenses Remove Expedition Extra Expenses Expedition Extra Expenses Country modifier 0.025% of GDP Government expenses Sets Congo River Expedition bonus for the Grand Exhibition |
| Failure conditions: Either: Expedition peril is 8 or more Cancelled expedition | Effects when failed: Trigger event Failed Expedition Remove Expedition Budget Expedition Budget Country modifier 0.025% of GDP Government expenses Remove Expedition Extra Expenses Expedition Extra Expenses Country modifier 0.025% of GDP Government expenses |
| Every month, the following weighted random events can happen: (70) Nothing (30) +1 progress and peril (30) Boat Repairs (40) The White Fog (30) Crocodiles! (40) Rear Column (30) Trading Enclave (40) Into the Jungle (80) The Seven Cataracts (30) A Generous Present (20) Local Guides (20) Expedition Member Drowns (10) Expedition Beset by Malaria (10) Dysentery in the Expedition (20) Attack on the River (20) Grave of the Fallen (50) Dr. [Old Expedition Leader], I Presume (15) An Unexpected Guest (10) Bad News (15) Among Us (20) An Insolvent Business (10) [Leader's Vice] Supplies Run Low (30) An Unexpected Group |  |

## Niger River

The following journal entry and events represent expeditions to map the Niger River.[4]

id

### Niger River Expedition

Launch an expedition to plot the Niger River.
---

| Shown conditions: Has researched Colonization No country has plotted the Niger River Not undertaking any expedition | Useable conditions: Is at peace Has an interest in the Niger region Has researched Quinine Has 3 or more commanders |
|---|---|
| Effects: Triggers event Expedition to Plot the Niger River |  |

id

### Congo River Expedition

An expedition shall be launched to plot the course of the Niger River.
---

| Visibility conditions: Only while active |  |
|---|---|
| Activated by: Event The Expedition Embarks |  |
| Completion conditions: Expedition progress is 8 or more | Effects when completed: Trigger event Successful Expedition Remove Expedition Budget Expedition Budget Country modifier 0.025% of GDP Government expenses Remove Expedition Extra Expenses Expedition Extra Expenses Country modifier 0.025% of GDP Government expenses Sets Niger River Expedition bonus for the Grand Exhibition |
| Failure conditions: Either: Expedition peril is 8 or more Cancelled expedition | Effects when failed: Trigger event Failed Expedition Remove Expedition Budget Expedition Budget Country modifier 0.025% of GDP Government expenses Remove Expedition Extra Expenses Expedition Extra Expenses Country modifier 0.025% of GDP Government expenses |
| Every month, the following weighted random events can happen: (70) Nothing (30) +1 progress and peril (20) Local Guides (20) Expedition Member Drowns (10) Expedition Beset by Malaria (10) Dysentery in the Expedition (20) Attack on the River (15) Expedition Film (20) Hippopotamus Sighted (20) Grave of the Fallen (15) Kidnapped (2) Death of a Leader (40) Dr. [Old Expedition Leader], I Presume (20) An Unexpected Guest (10) Bad News (15) Among Us (20) An Insolvent Business (10) [Leader's Vice] Supplies Run Low (20) An Unexpected Group |  |

## Nile River

The following journal entry and events represent expeditions to find the source of the Nile River.[5]

id

### Nile River Expedition

The center of the African continent holds the secret to the source of the Nile.
---

| Shown conditions: Has researched Colonization No country has found the source of the Nile Not undertaking any expedition | Useable conditions: Is at peace Has an interest in the Zanj region Has researched Quinine Has 3 or more commanders |
|---|---|
| Effects: Triggers the event The Nile Expedition |  |

id

### Nile River Expedition

The center of the African continent holds the secret to the source of the Nile.
---

| Visibility conditions: Only while active |  |
|---|---|
| Activated by: Event The Expedition Arrives |  |
| Completion conditions: Expedition progress is 8 or more | Effects when completed: Trigger event Successful Expedition Remove Expedition Budget Expedition Budget Country modifier 0.025% of GDP Government expenses Remove Expedition Extra Expenses Expedition Extra Expenses Country modifier 0.025% of GDP Government expenses Sets Niger River Expedition bonus for the Grand Exhibition |
| Failure conditions: Either: Expedition peril is 8 or more Cancelled expedition | Effects when failed: Trigger event Failed Expedition Remove Expedition Budget Expedition Budget Country modifier 0.025% of GDP Government expenses Remove Expedition Extra Expenses Expedition Extra Expenses Country modifier 0.025% of GDP Government expenses |
| Every month, the following weighted random events can happen: (70) Nothing (30) +1 progress and peril (15) Expedition Beset by Malaria (2) Death of a Leader (15) Dysentery in the Expedition (20) Local Guides (20) Rhinoceros Sighted (10) Local Tax (20) Lost Mule (10) A Beetle in Hand is Worth Two in the Ear (10) [Leader's Vice] Supplies Run Low (15) Geographical Study (15) An Unexpected Guest (5) Bad News (20) Among Us (10) An Insolvent Business (20) Grave of the Fallen (20) An Unexpected Group |  |

## Africa expedition events

|  | Please help improve this article or section by [expanding it](https://vic3.paradoxwikis.com/index.php?title=Expeditions&action=edit). |
|---|---|

## Tibet

The following journal entry and events represent the British "expedition" to Tibet.[6]

id

### Expedition to Tibet

| Shown conditions: Is not Tibet Tibet is unrecognized Is recognized Has researched Colonization No country has completed this expedition Not undertaking any expedition | Useable conditions: Is at peace Tibet is not a subject of a recognized country Does not have Tibet Fiasco Tibet Fiasco Country modifier −10% Authority Is a great power Has an interest in the Himalayas region Has researched Quinine Has 3 or more commanders Has researched Civilizing Mission |
|---|---|
| Effects: Triggers the event To Tibet! |  |

id

### Expedition to Tibet

In our great game against our rivals, one realm stands above the rest in its potential value and threat: Tibet. We find ourselves driven to protect our flank and deny our enemy's ambitions by securing our interests in this Himalayan land.
---

| Visibility conditions: Only while active |  |
|---|---|
| Activated by: Either: Great Game objective subgoal Event The Expedition Sets Forth |  |
| Completion conditions: Either: Expedition progress is 6 or more and received event The Convention of [Lhasa] Tibet is a direct subject of this country | Effects when completed: Remove Expedition Budget Expedition Budget Country modifier 0.025% of GDP Government expenses If playing with the Great Game objective and is Great Britain or Russia , Gain 10 points in the Great Game |
| Failure conditions: Any of: Another country has completed this expedition Tibet does not exist or is at war with this country The expedition leader has died or been dismissed Tibet or its overlord refused subjugation | Effects when failed: Gain Tibet Fiasco Tibet Fiasco Country modifier −10% Authority for 5 years Remove Expedition Budget Expedition Budget Country modifier 0.025% of GDP Government expenses |
| Times out after 5 years with the following effects: Gain Tibet Fiasco Tibet Fiasco Country modifier −10% Authority for 5 years Remove Expedition Budget Expedition Budget Country modifier 0.025% of GDP Government expenses |  |
| Every month, the following weighted random events can happen: (66) Nothing (10) Cross-Border Yak-cident (10) The Great Mountain Survey (10) Leeches! (10) Building an Expeditionary Force (10) A Fierce Face (10) Into the Himalayas (10) Himalayan Blizzard (10) Gyantse Dzong (10) Unsanctioned Pillaging (10) Issuing the Ultimatum |  |

id

### To Tibet!

We have decided to venture into Tibet and secure these lands for our own interests. We will have to survey a route into the Himalayan region, then make a show of strength, and then force the Tibetans to the negotiating table.
---

Flavor text:
"It's simple, really." Cigar smoke lingered as the man gestured at the map on the wall with a smouldering stoagie. He jabbed at a cemtral
[sic]
spot. "
That
is our weak point. If anyone else holds that point, they have a dagger to our throats. We need to secure, uh..." He paused as he tried to peer through the haze of tobacco, "Tibet! We must secure Tibet to save ourselves."
---

| Is triggered by: Decision Expedition to Tibet |
|---|
| Trigger conditions: None |
| I know just the man for the job. Trigger event Choosing a Leader |

id

### Choosing a Leader

A group of strong candidates have expressed their interest in leading the expedition. However, this is not a decision we should make lightly.
---

Flavor text:
The first to arrive was a well-dressed, fresh-faced, almost young gentleman whose keenness to impress was only matched by his willingness to oblige. His smile, as wide as one can imagine, was fashionably put together: "If I may...," he politely said, presenting his credentials.
---

| Is triggered by: Event To Tibet! |
|---|
| Trigger conditions: Has a commander who is not busy |
| Immediate effects: Selects up to three commanders that are Not busy Not the ruler Preferring ones with the trait explorer Expedition progress and peril are set to 1 |
| [Commander] [Name] [Commander] becomes the expedition leader and 'busy' Trigger event The Expedition Sets Forth in 30 days |

id

### The Expedition Sets Forth

With [Leader] in charge, our expedition to Tibet is ready to commence.
Since he is in charge, if he dies the expedition will end in failure.
---

Flavor text:
[Leader] scowled as he went through the reports. If every rumor about a vital mountain pass was true, the Himalayas were riddled with more holes than Swiss cheese. There was nothing to do but go out and figure out which one was real.
---

| Is triggered by: Event Choosing a Leader |
|---|
| Trigger conditions: None |
| Onwards, to Tibet! Activate journal entry Expedition to Tibet Gain Expedition Budget Expedition Budget Country modifier 0.025% of GDP Government expenses |

id

### Cross-Border Yak-cident

A group of local yak herders crossed the border, and only realized their mistake when a Tibetan patrol intercepted them and herded them back. The herders have complained of rough treatment, prompting [Leader] to declare this an acton of wanton aggression that must be answered in kind.
---

Flavor text:
"It's the principle of the matter, nevermind the details! An international border was violated, and appropriate measures must be taken to address this insult to diplomacy and our sovereignty! I could have a regiment of men marching over there
right now
if you just gave me the word."
---

| Is triggered by: Monthly pulse of journal entry Expedition to Tibet |
|---|
| Trigger conditions: Expedition progress is less than 4 No interest group has Hostility Resisted Hostility Resisted Interest Group modifier +2 Approval or Resisted Being Hostile Resisted Being Hostile Interest Group modifier +2 Approval |
| We must be prepared for bold action. Every interest group with Jingoist or a Jingoist leader: Gains Hostility Resisted Hostility Resisted Interest Group modifier +2 Approval for 5 years If no interest group besides the Armed Forces is Jingoist, A random interest group besides the Rural Folk or Armed Forces: Gains Hostility Resisted Hostility Resisted Interest Group modifier +2 Approval for 5 years Leader gains Jingoist Expedition progress increases by 1 This talk of aggression is ludicrous! Every interest group with Isolationist or a Pacifist leader: Gains Resisted Being Hostile Resisted Being Hostile Interest Group modifier +2 Approval for 5 years |

id

### The Great Mountain Survey

Surveyors have begun studying the mountains and passes that surround Tibet. Diving into uncharted terrain and climbing unexplored mountains is hazardous work, but [Leader] wishes to get involved all the same.
---

Flavor text:
"Have you seen that peak? We
must
climb it!"
"But why"
"Because... it's
there
!"
---

| Is triggered by: Monthly pulse of journal entry Expedition to Tibet |
|---|
| Trigger conditions: Expedition progress is less than 4 No country character has encountered Mt. Everest |
| Immediate effects: Expedition leader encounters Mt. Everest |
| Option conditions Always enabled: We cannot risk [Leader], send someone else. Generates a general with the trait Engineer Enabled if: Is Great Britain or East India Date is before 1870.1.1 and no country has used this option before Andrew Scott Waugh is eminently qualified for the job. Andrew Scott Waugh becomes a general Enabled if: Is Great Britain or East India Date is after 1892.1.1 and no country has used this option before No peak is too formidable for Charles Granville Bruce! Charles Granville Bruce becomes a general Always enabled: [Leader] is our man on the spot and should take charge here. 1 weight: [Leader] dies and expedition fails 1 weight: +1 weight if ruler has Explorer +2 weight if expedition leader has Explorer [Leader] gains Surveyor and Famed Mountaineer Famed Mountaineer Character modifier +10 Popularity permanently Expedition progress increases by 1 For all options, except the last: [Leader] gains Sidelined Mountaineer Sidelined Mountaineer Character modifier −10 Popularity for 5 years Expedition progress increases by 1 |

id

### Leeches!

The foothills of the Himalayas are filled with treacherous flora and fauna. One promising route into the Tibetan Plateau involves delving into a region full of unsavory wildlife. If the route is to be used, [Leader] will have to inspect it himself.
---

Flavor text:
"Nope."
"Nope. Nope nope nope."
The scout looked at the swamp water one last time. A giggle escaped his lips. "Hahahahahaaa,
nope!
"
This was going to be someone else's problem, not his.
---

| Is triggered by: Monthly pulse of journal entry Expedition to Tibet |
|---|
| Trigger conditions: Expedition progress is less than 4 |
| [Leader] can do it and must do it. 1 weight: [Leader] dies and expedition fails 1 weight: +0.5 weight if ruler has Explorer +2 weight if expedition leader has Explorer [Leader] gains the trait Sickly Expedition progress increases by 1 2 weight: +1 weight if ruler has Explorer +4 weight if expedition leader has Explorer Expedition progress increases by 1 Perhaps resting among the mountain air would be better. [Leader] randomly: Loses one of Sickly, Beetle Eared, Opium Addict, Cocaine Addict, or Alcoholic Or replaces Wounded with Scarred [Leader] gains Well-Rested Leader Well-Rested Leader Character modifier +50% Character health for 5 years |

id

### Building an Expeditionary Force

With an adequate knowledge of the land ahead, [Leader] has declared that he is ready to assemble the troops and proceed ahead into the Tibetan Plateau.
---

Flavor text:
It shouldn't have been this difficult. It was a job, just like any other, but somehow... somehow just getting the right men for the job was proving more difficult than anyone expected. There were plenty of regulars on hand, of course, but why not use the cream of the crop? Should any artillery come along? What about horses? Officers?
After much dithering, he finally picked out his favorite pewter models and placed them on the table. He'd get to figuring out the expedition's problems later that evening.
---

| Is triggered by: Monthly pulse of journal entry Expedition to Tibet |
|---|
| Trigger conditions: Expedition progress is less than 4 No country character has built an expeditionary force |
| Immediate effects: Expedition leader builds an expeditionary force |
| Option conditions Always enabled: The expedition must not, cannot, lack for men. [Leader] gains Leader of Men Leader of Men Character modifier +20 Command limit permanently Expedition progress increases by 1 Always enabled: Only the hardiest soldiers can face what's to come. [Leader] gains Best of the Best Best of the Best Character modifier −10% Morale loss permanently Expedition progress increases by 1 Enabled if: [Leader] is an admiral We need an unorthodox approach here. [Leader] gains Marine Commander Marine Commander Character modifier +25% Weekly experience gain for navies −5% Morale loss permanently Expedition progress increases by 1 |

id

### A Fierce Face

Our expedition has come across an animal den while traversing a treacherous mountain pass. Investigation revealed that it is inhabited by a rare animal - the Pallas's Cat.
---

Flavor text:
When he lowered the lantern to peer into the den's depths, baleful golden eyes stared back at him. Their round pupils and the markings surrounding them gave off a peculiar sort of humanity, like an mustachioed man with furrowed brows. The cat was judging him, thought the expeditionary, and it was dug in as adeptly as any soldier in their trench.
He shifted the light's angle, and three smaller sets of eyes glared back. A mother in her den, guarding three kittens that were just old enough to hiss at the light. The botanical gardens would pay handsomely for them, but would that make up for the fingers it would cost?
---

| Is triggered by: Monthly pulse of journal entry Expedition to Tibet |
|---|
| Trigger conditions: Expedition progress is less than 4 No owned state has A Fluffy Zoo Exhibit A Fluffy Zoo Exhibit State modifier +25% Migration attraction No country character has Luxurious Pelt Luxurious Pelt Character modifier +25 Popularity +20% Character health |
| Immediate effects: Expedition leader builds an expeditionary force |
| Option conditions Always enabled: Capture them, and have them shipped to [Capital City]. 25% chance: If [Leader] has Wounded, [Leader] dies and expedition fails Otherwise, [Leader] gains Wounded Capital gains A Fluffy Zoo Exhibit A Fluffy Zoo Exhibit State modifier +25% Migration attraction for 5 years Expedition progress increases by 1 Enabled if: [Leader] has Cruel A magnificent pelt, ready to be claimed! 33% chance: If [Leader] has Wounded, [Leader] dies and expedition fails Otherwise, [Leader] gains Wounded [Leader] gains Luxurious Pelt Luxurious Pelt Character modifier +25 Popularity +20% Character health for 5 years Expedition progress increases by 1 Always enabled: Make our notes, but let them be. Expedition progress increases by 1 |

id

### Into the Himalayas

With maps prepared and men ready, [Leader] can venture into Tibet at last.
---

Flavor text:
"We are here to neither find glory nor gold." The officer paced slowly down the line of assembled here. "Not for ourselves, at least. No one will remember us."
He thrust a finger towards the vast mountains in the distance. "Now
that
will be remembered. Do we want to stand here, on this forgotten tuft of grass, or stand tall
there
, atop rocks that will last beyond all memory?"
---

| Is triggered by: Monthly pulse of journal entry Expedition to Tibet |
|---|
| Trigger conditions: Expedition progress is 4 or more The expedition is not delayed This event has not occurred this expedition |
| Immediate effects: The expedition enters Tibet |
| To the roof of the world! If Tibet is a subject, Tibet's overlord receives event [Expedition Country] Interference in Tibet in 1 day Otherwise, Tibet receives event The [Expedition Country] are Coming! in 1 day Expedition progress increases by 1 Tibet receives event Blocking the [Expedition Country] Force? in 14 days |

id

### [Expedition Country] Interference in Tibet

Our envoy in Lhasa has passed along reports that a [Expedition Country] force, led by [Leader], has violated Tibet's borders and is making its way towards the capital.
---

Flavor text:
The ambassador's calm voice was betrayed by his sweaty brow. "I assure you," he dictated to the messenger, nervously drumming the table with his fingers, "that everything is absolutely under control in Tibet."
He paused, marshalling his next words with the care of a master tactician. "However, it would behoove the government to respond quickly to this action by whatever means it sees fit, in the most timely fashion possible."
He let out a deep breath. Now it was
their
turn to figure out this mess.
---

| Is triggered by: Event Into the Himalayas |
|---|
| Trigger conditions: None |
| This disturbance is a mere trifle. No action is needed to save Tibet. Gain +5 relations with [Expedition Country] Tibet gains +5 liberty desire Tibet receives event The [Expedition Country] are Coming! in 1 day Issue a protest to [Expedition Country]'s embassy. Lose −15 relations with [Expedition Country] Tibet receives event The [Expedition Country] are Coming! in 1 day This is unacceptable! Send reinforcements to Lhasa and tell them they have our support. Lose −30 relations with [Expedition Country] Gain Himalayan Affairs Himalayan Affairs Country modifier −5% Authority for 5 years Create an incident with [Expedition Country] for 2 infamy Tibet : Loses −5 liberty desire Gains Overlord Military Support Overlord Military Support Country modifier −25% Military goods cost for 2.5 years Receives event The [Expedition Country] are Coming! in 1 day |

id

### The [Expedition Country] are Coming!

Reports are coming in of a [Expedition Country] force that has crossed the border and is making its way to the capital. This is a blatant violation of our sovereignty, but resisting [Expedition Country] may be too much for us to handle ourselves.
---

Flavor text:
"No, we didn't dare shoot at them!" stammered the guard. "You weren't there! You didn't see how many men were coming! You didn't see their guns! There were only a dozen of us—we had to fall back!"
---

| Is triggered by: Either: Event Into the Himalayas Event [Expedition Country] Interference in Tibet |
|---|
| Trigger conditions: None |
| Option conditions Always enabled: We must look the other way for now. Lose −15 relations with [Expedition Country] Enabled if: Is independent or an autonomous subject Regardless of their strength, we must resist now! Start a diplomatic play against [Expedition Country] with the wargoal War Reparations |

id

### Blocking the [Expedition Country] Force?

The [Expedition Country] incursion continues to advance towards our capital. To buy time, we could instruct patrols to set up simple roadblocks along the most obvious routes of the [Expedition Country] force.
This may lead to incidents with [Expedition Country].
---

Flavor text:
It was a simple proposal, on the face of it. If the enemy were to be stopped, they had to meet some actual resistance. But... could we afford a direct confrontation? That was the question that haunted the minds of every minister and general dealing with the problem.
---

| Is triggered by: Event Into the Himalayas |
|---|
| Trigger conditions: None |
| We cannot risk a fight. Let them proceed. Every interest group with Jingoist or a Jingoist, Brave, or general leader: Gains Government Cowardice Government Cowardice Interest Group modifier −2 Approval for 5 years A random state gains Expedition Disturbs the People Expedition Disturbs the People State modifier −2 Standard of living +25% Effects of turmoil for 5 years A roadblock can't hurt. Delay them at the next opportunity. Every interest group with Jingoist or a Jingoist, Brave, or general leader: Gains Government Bravery Government Bravery Interest Group modifier +2 Approval for 5 years [Expedition Country] receives event The [Leader] Expedition is Blocked in 1 day |

id

### The [Leader] Expedition is Blocked

A Tibetan patrol has set up a roadblock along the route of [Leader]'s expedition. Any delay in the expedition's progress could be disastrous for the project.
---

Flavor text:
[Leader] scowled at the sight before him. The mass of Tibetan soldiers standing across the road ahead of him looked formidable, but he knew what weapons he had brought with the expedition. Getting through the roadblock wasn't the problem—the problem was the price of doing it.
---

| Is triggered by: Event Blocking the [Expedition Country] Force? |
|---|
| Trigger conditions: None |
| Make as big a bag as possible! Forwards! Create an incident with Tibet for 15 infamy 33% chance [Leader] gains Cruel If Tibet is a subject, Tibet's overlord receives event [Expedition Country] Clash in Tibet in 1 day Expedition progress increases by 1 This would be a slaughter—pull back. The expedition is delayed for 3 months |

id

### [Expedition Country] Clash in Tibet

Reports have come in of a bloody clash between the [Expedition Country] expedition and local Tibetan forces. Our duty to Tibet behooves us to relieve it, but some ministers have expressed discomfort at the idea of strengthening the government in [Lhasa] at all.
---

Flavor text:
"What happened in that pass is a disgrace, a tragedy!"
"It's a grievous insult to them and to us!"
"So then, gentlemen, what is our next step? Shall we assist them directly? March to the frontier? Supply arms?"
The awkward silence that followed was interrupted only by a dry cough.
---

| Is triggered by: Event The [Leader] Expedition is Blocked |
|---|
| Trigger conditions: None |
| We cannot give any material aid. Tibet gains +5 liberty desire We shall support the Tibetan military. Tibet : Loses −5 liberty desire Gains Overlord Military Support Overlord Military Support Country modifier −25% Military goods cost for 2.5 years Gain Himalayan Expenses Himalayan Expenses Country modifier 0.025% of GDP Government expenses for 2.5 years |

id

### Himalayan Blizzard

[Leader]'s expedition has been held up by vicious and unexpected weather along one of the more treacherous paths on the way to [Lhasa]. Delays could be costly, but forging through the weather could be costlier still.
---

Flavor text:
The frozen wind was blowing under [Leader]'s boots and around his toes. The frost was biting the ground below. It was well below zero, and yet he could hear a soldier cry out. He assumed it was about the snow, but he could barely see beyond the tip of his nose and couldn't tell where the soldier was, much less what was happening around them.
---

| Is triggered by: Monthly pulse of journal entry Expedition to Tibet |
|---|
| Trigger conditions: Expedition progress is 4 or more The expedition is not delayed |
| We must brave the snow and push on! 3 weight: +1 weight if ruler has Explorer +2 weight if expedition leader has Explorer Expedition progress increases by 1 1 weight: [Leader] dies and expedition fails We must brave the snow and push on! The expedition is delayed for 3 months |

id

### Gyantse Dzong

A vast fortified monastery thrusts out of the Tibetan stone ahead — Gyantse Dzong, granite guardian of the Tsangpo Valley and one of the key approaches to Lhasa. There can be no safe route to the capital as long as this fortress is not held by the expedition's soldiers.
---

Flavor text:
The impregnable fortress towered over the surrounding landscape. The nearby villages were specks of dust compared to the stone giant that loomed overhead. The venerable walls and ancient halls echoed with centuries of struggle, of pride, of countless prayers and battles and intrigues. It stood as a persistent testament to the wills of generations of leaders.
A barrage of [Leader]'s guns could end it in a day.
---

| Is triggered by: Monthly pulse of journal entry Expedition to Tibet |
|---|
| Trigger conditions: Expedition progress is 4 or more The expedition is not delayed This event has not occurred this expedition |
| We must brave the snow and push on! Lose −15 relations with Tibet and Tibet's overlord Expedition progress increases by 1 We must brave the snow and push on! 1 weight: +1 weight if ruler has Explorer +4 weight if expedition leader has Explorer Expedition progress increases by 1 1 weight: The expedition is delayed for 3 months |

id

### Unsanctioned Pillaging

As [Leader]'s soldiers approach Tibet, some soldiers have gotten unruly. Reports have come in of gangs of our men going into houses and monasteries, taking whatever they fancy.
---

Flavor text:
"I assure you, sir, this is completely within acceptable bounds. We were opposed, after all, and it's to be expected that actions would be taken afterwards. Although, of course, the reports from that one monastery must be exaggerated."
---

| Is triggered by: Monthly pulse of journal entry Expedition to Tibet |
|---|
| Trigger conditions: Expedition progress is 4 or more The expedition is not delayed This event has not occurred within 2.5 years |
| So? That's just how armies are. Lose −10 relations with Tibet Tibet's capital gains 10 devastation Expedition progress increases by 1 Discipline the soldiers and offer an apology to local officials. Gain +10 relations with Tibet Gain Tibetan Restitution Tibetan Restitution Country modifier 0.015% of GDP Government expenses for 2.5 years 1 weight: +1 weight if ruler has Explorer +4 weight if expedition leader has Explorer Expedition progress increases by 1 1 weight: No progress |

id

### Issuing the Ultimatum

With our expedition near [Lhasa], it's time we deal with the thorny issue of diplomatic channels. We need to speak to whoever has ultimate authority over these lands.
---

Flavor text:
He found the officer slumped over a table, screaming into his hands.
"You talk to one official, and he passes you on to the next. Then you talk to
that
fellow, and
he
says you've got the wrong man, and points you to a third person. Then that fellow— that fellow says you have it all wrong, and the
first
fellow is the one with all the authority."
"Oh, where does it end? Who's in charge? Am
I
even in charge?"
---

| Is triggered by: Monthly pulse of journal entry Expedition to Tibet |
|---|
| Trigger conditions: Expedition progress is 6 or more The expedition is not delayed This event has not occurred this expedition |
| Option conditions Always enabled: Issue our demands to Tibet, of course. Tibet receives event The [Expedition Country] Ultimatum (Tibet) in 1 day Enabled if: Tibet is a subject Speak directly with [Tibet's Overlord]. Tibet 's overlord receives event The [Expedition Country] Ultimatum (Overlord) in 1 day |

id

### The [Expedition Country] Ultimatum (Tibet)

The [Expedition Country] expedition has, despite our best efforts, reached our capital. Their costly demands are straightforward: submit to their authority.
---

Flavor text:
"It's quite simple, really," grinned the [Expedition Country] envoy. "You already know the scorpion. Why not turn to us instead? Cut off relations with other foreign powers and let us handle the rest."
---

| Is triggered by: Event Issuing the Ultimatum |
|---|
| Trigger conditions: None |
| We will submit to [Expedition Country]. Tibet 's overlord receives event The Convention of [Lhasa] (Overlord) in 1 day [Expedition Country] receives event The Convention of [Lhasa] (Expedition) in 1 day Tibet becomes a protectorate of [Expedition Country] Your show of force means nothing! Leave here now, emptyhanded! Lose −40 relations with [Expedition Country] [Expedition Country] fails the expedition |

id

### The [Expedition Country] Ultimatum (Overlord)

The [Expedition Country] expedition into Tibet has undercut our authority in the region, and now they demand we formally cede control to them. This is a grievous insult, but dare we stand against them now?
---

Flavor text:
"It's quite simple, really," grinned the [Expedition Country] envoy. "You have been the scorpion, but now it's time for us to wield the stinger. Let us manage this parcel of Himalayan rock, and we can leave you be and let this matter finally come to an end."
---

| Is triggered by: Event Issuing the Ultimatum |
|---|
| Trigger conditions: None |
| Option conditions Always enabled: We will submit to [Expedition Country]'s demands. [Expedition Country] receives event The Convention of [Lhasa] (Expedition) in 3 day Tibet becomes a protectorate of [Expedition Country] Enabled if: [Expedition Country] is AI, and this country is not Your show of force means nothing! Leave here now, emptyhanded! Create an incident with [Expedition Country] for 10 infamy [Expedition Country] fails the expedition |

id

### The Convention of [Lhasa] (Overlord)

The [Expedition Country] expedition has directly approached Tibetan officials and forced them to acknolwedge
[sic]
[Expedition Country] suzerainty. They are now subjects of [Expedition Country].
---

Flavor text:
"It's quite simple, really," grinned the [Expedition Country] envoy. "We had a simple discussion with the people who mattered, and now they are ours. They knew the scorpion, and now it's time to know us." He chuckled, waving the [Ex Tibetan Overlord] officials away.
---

| Is triggered by: Event The [Expedition Country] Ultimatum (Tibet) |
|---|
| Trigger conditions: None |
| Tibetan land will always be ours! Gain claims on every state owned by Tibet [Expedition Country] must return Tibet now. Create a diplomatic play against Tibet with the wargoal Transfer Subject |

id

### The Convention of [Lhasa] (Expedition)

[Leader]'s expedition to Tibet has been a resounding success, and this strategic region is now under our thumb. [Leader] is already being feted in [Capital City], and he has a bright future ahead of him.
---

Flavor text:
"It's simple, really." Cigar smoke lingered as the man gestured at the map on the wall with a smouldering stoagie. "
That
was our weak point. It was of vital necessity that we pour whatever men and gold was needed to secure, uh..." He paused as he tried to peer through the haze of tobacco, "Tibet! We had to secure Tibet to save ourselves."
He turned back to the other men in the club. "Now! Who's ready for some billiards?"
---

| Is triggered by: Either: Event The [Expedition Country] Ultimatum (Tibet) Event The [Expedition Country] Ultimatum (Overlord) |
|---|
| Trigger conditions: None |
| Three cheers for [Leader]! [Leader]: Commander rank increases by 1 Gains Master of the Himalayas Master of the Himalayas Character modifier +20 Popularity permanently Completes journal entry Expedition to Tibet |

## References

1. ↑ For script details, see /Victoria 3/game/common/decisions/antarctica_expedition_decision.txt, /Victoria 3/game/common/journal_entries/00_antarctica.txt, and /Victoria 3/game/events/expedition_events/antarctic_expedition_events.txt
2. ↑ For script details, see /Victoria 3/game/common/decisions/west_america_expidition_decision.txt, /Victoria 3/game/common/journal_entries/00_west_america.txt, and /Victoria 3/game/events/expedition_events/west_america_expedition_events.txt
3. ↑ For script details, see /Victoria 3/game/common/decisions/congo_expedition_decision.txt, /Victoria 3/game/common/journal_entries/00_congo.txt, and /Victoria 3/game/events/expedition_events/congo_river_expedition_events.txt
4. ↑ For script details, see /Victoria 3/game/common/decisions/niger_river_expedition_decision.txt, /Victoria 3/game/common/journal_entries/00_niger_river.txt, and /Victoria 3/game/events/expedition_events/niger_river_expedition_events.txt
5. ↑ For script details, see /Victoria 3/game/common/decisions/central_africa_expedition_decision.txt, /Victoria 3/game/common/journal_entries/00_central_africa.txt, and /Victoria 3/game/events/expedition_events/central_africa_expedition_events.txt
6. ↑ For script details, see /Victoria 3/game/common/decisions/tibet_expedition_decision.txt, /Victoria 3/game/common/journal_entries/03_tibetan_expedition.txt, and /Victoria 3/game/events/tibetan_expedition.txt
