import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def mainPart(sent):

    input_sent = sent
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(input_sent)
    filtered_sentence2 = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence2.append(w)

    filtered_sentence2 = " ".join(filtered_sentence2)

    words = nltk.word_tokenize(filtered_sentence2.lower())
    nltk.pos_tag(words)
    grammar = "NP: {<VB.*>?<RB>?<PRP.*>?<IN>?<CD>?<DT>?<JJ.*>*<NN.*>+}"
    parser = nltk.RegexpParser(grammar)
    t = parser.parse(nltk.pos_tag(words))
    a = [s for s in t.subtrees() if (s.label().startswith('N') or s.label() == 'CD')]
    c = []
    num = []
    key = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "today", "tomorrow",
               "yesterday", "reminder", "remind", "th", "pm", "am"]
    for i in range(len(a)):

        count = 0
        phrase = ""

        for j in range(len(a[i])):

            if a[i][j][0].lower() in key:
                phrase = phrase
            else:
                phrase = phrase + str(a[i][j][0]) + " "
                count = count + 1

        c.append(phrase)
        num.append(count)

    if (c == [] or max(num) <= 1):
        return "Did'nt got any pattern!"
    else:
        maxi = max(num)
        for i in range(len(num)):
            if (num[i] == maxi):
                return c[i].rstrip()
