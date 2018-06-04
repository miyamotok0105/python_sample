# Schedules a reactive process that counts the words in a text file every three seconds,
# but only prints it as a dict if it has changed

from rx import Observable
import re
import signal

def word_counter(file_name):

    file = open(file_name)

    # parse, clean, and push words in article
    article_words = Observable.from_(file) \
        .map(lambda s: Observable.from_(s.split())) \
        .merge_all() \
        .map(lambda w: re.sub(r'[^\w\s]','', w)) \
        .filter(lambda w: w != "") \
        .map(lambda w: w.lower()) \


    # count words using `group_by()`
    # tuple the word with the count
    article_word_counts = article_words \
        .group_by(lambda word: word) \
        .map(lambda grp: grp.count().map(lambda ct: (grp.key,ct))) \
        .merge_all()

    return article_word_counts

# composes the above word_counter() into a dict
def word_counter_as_dict(file_name):
    return word_counter(file_name).to_dict(lambda tuple: tuple[0], lambda tuple: tuple[1])


# Schedule to create a word count dict every three seconds an article
# But only re-print if text is edited and word counts change

article_file = "bbc_news_article.txt"

Observable.interval(3000) \
    .map(lambda index: word_counter_as_dict(article_file)) \
    .merge_all() \
    .distinct_until_changed() \
    .subscribe(lambda word_ct_dict: print(word_ct_dict))


# keep this program alive indefinitely
signal.pause()

