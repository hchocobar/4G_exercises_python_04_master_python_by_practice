def remove_duplicate_words(text):
    all_words = text.split(' ')  # Genera lista
    words = set(all_words)  # Elimina duplicados generando un conjunto
    sort_words = list(words) # Convierte el conjunto en lista para poder ordenarlo
    sort_words.sort()  # Ordena la lista
    return sort_words

song = "Imagine there's no heaven It's easy if you try No hell below us Above us, only sky Imagine all the people Livin' for today Ah Imagine there's no countries It isn't hard to do Nothing to kill or die for And no religion, too Imagine all the people Livin' life in peace You"
print(remove_duplicate_words(song.lower()))
