from collections import Counter

def getSpamEmails(subjects, spam_words):
    result = []

    spam_words = set(word.lower() for word in spam_words)

    for subject in subjects:
        subject_words = subject.lower().split()
        word_count = Counter(subject_words)

        spam_count = 0
        for word in word_count:
            if spam_count == 2:
                break
            if word in spam_words:
                spam_count += min(2, word_count[word])

        result.append("spam" if spam_count >= 2 else "not_spam")

    return result


print(getSpamEmails(["Let it go"], ["free", "millions"]))