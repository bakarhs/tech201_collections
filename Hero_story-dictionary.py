story1 = {
    "start": "We start this story, meeting Viktor. Viktor just made his way out from university and is now working the company he always dreamed of working for. It was all that he could have ever imagined, good pay, great benefits and he can finally leave his little home in the family in the suburbs. What you don’t know though is that Viktor was actually the main breadwinner of the family but now that he is gone his parents will struggle, it’s not like they’re getting any younger, but he doesn’t care its time he lives his own life. ",
    "middle": "It’s been a while since Viktor has been at the company now and the harsh reality of not everyone being as they may seem has finally kicked in. Viktor is different now and he will do anything to get 1 up on any of his colleagues, after being burnt by someone people he saw as a friend he decided to adapt. This was survival of the fittest and he was going to do anything to get to the top, he became a wolf in sheep’s clothing, ready to strike at the most optimal time.",
    "end": "Although, Viktor had everything he could ever dream of; Money! Power! Fame! he had lost everything that really meant anything. The sacrifices he had made to get to the position he was currently in came back to haunt him. After many sleepless nights, he can only remember those he betrayed and it ate away at him again and again for the as if he would never know peace again. As a young man he was so kind and filled with love for his family and friends but along his path to the top he became corrupted climbing this corporate ladder, the same ladder he thought would solve all his problems, but really and truly it just turned him into a shell of whom he used to be. He had worn so many masks up to this point that he no longer knew who is Viktor. The world was not so kind to him, most of us go through the same story, when you don’t have “it” you want “it” but when you get “it” you no longer want “it”. This is the greed of humanity, a greed we can never escape.",
}

print(story1)
print(type(story1))
print(story1.keys())
print(story1.values())

print(story1.get("start"))
print(story1.get("middle"))
print(story1.get("end"))

story1.update({"Villain": "Viktor", })
