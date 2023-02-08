does_he = False
phrases = {1: 'Fuzzy Duck', 
           -1: 'Ducky Fuzz'}
phrase_id = 1
for step in range(1, 101):
    if does_he:
        player_id = 10 - step % 10
    else:
        player_id = step % 10 or 10

    if step % 15 == 0:
        msg = 'Does he?'
        does_he = not does_he
    else:
        msg = phrases[phrase_id]
        phrase_id *= -1

    print('%s\t%s\t%s' % (step, player_id, msg))
