#!/usr/bin/env python

import markov
import random
from twitter import *

def main():
    settings = [line.rstrip('\n') for line in file('settings.txt')]
    source = file('corpus/all.txt')
    generator = markov.Markov(source)
    length = random.randint(20,140)
    output = generator.generate_markov_text(length)
    output = output.lower()
    print output

    # and now to sing:
    # wasn't sure which key was which - 
    # https://gist.github.com/smartboyathome/2599146
    token = settings[0]    
    token_key = settings[1] 
    con_secret = settings[2]
    con_secret_key = settings[3]
    twitter = Twitter(auth=OAuth(token, token_key, con_secret_key, con_secret))
    twitter.statuses.update(status=output)

if __name__ == "__main__":
    main()
