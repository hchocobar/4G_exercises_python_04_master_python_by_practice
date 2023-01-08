def sort_sequence(sequence):
    sequence_list = sequence.split(',')
    sequence_list.sort()
    return sequence_list


words = 'without,hello,bag,world'
print(sort_sequence(words))

song = "Imagine,there's,no,heaven,It's,easy,if,you,try,No,hell,below,us,Above,us,only,sky"
print(sort_sequence(song.lower()))
