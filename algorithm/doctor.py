#!/usr/bin/env python3
import random


hedges       = ("Please tell me more.",
                "Many of my patients tell me the same thing.",
                "Please continue.")

qualifiers   = ("Why do you say that ",
                "You seem to think that ",
                "Can you explain whay ")

replacements = {"I":"you" , "me":"you", "my":"your",
                "we":"you", "us":"you", "mine":"yours"}


def reply(sentence):
    probability = random.randint(1, 4)
    if probability == 1:
        return random.choice(hedges)
    else:
        return random.choice(qualifiers) + changePerson(sentence)


def changePerson(sentence):
    words     = sentence.split()
    replyPlay = []
    for word in words:
        replyPlay.append(replacements.get(word, word))
    return " ".join(replyPlay)

if __name__ == '__main__':
    print("Good morning, I hope you are well today.")
    print("What can I do for you?")
    while True:    
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print("Thank you very much!")
            break
        print(reply(sentence))

