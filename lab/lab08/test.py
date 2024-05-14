from classes import *

standard_deck = Deck([Card('One card', 100, 100) for _ in range(5)])
test_player = Player(standard_deck, 'tester')
ta1, ta2 = TACard("ta_1", 300, 400), TACard("ta_2", 500, 600)
tutor1, tutor2 = TutorCard("t1", 200, 500), TutorCard("t2", 600, 400)
test_player.hand = [ta1, ta2, tutor1, tutor2]
breakpoint()
test_player.play(0) is ta1

