def title_case(title, minor_words=''):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    for i in range(1, len(title)):
        if title[i].lower() in minor_words:
            title[i] = title[i].lower()
        else:
            title[i] = title[i].capitalize()
    return ' '.join(title)