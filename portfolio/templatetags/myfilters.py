""" Additional filters for my website """
import random

from django import template
register = template.Library()


@register.filter
def getrandomquote(value):
    quotes = [
        ("Measuring programming progress by lines of code is like measuring aircraft building progress by weight.",
         "Bill Gates"),
        ("Commenting your code is like cleaning your bathroom - you never want to do it, but it really does "
         "create a more pleasant experience for you and your guests.", "Ryan Campbell"),
        ("Debugging is twice as hard as writing the code in the first place. Therefore, if you write the code as "
         "cleverly as possible, you are, by definition, not smart enough to debug it.", "Brian W. Kernighan"),
        ("It always takes longer than you expect, even when you take into account Hofstadter's Law.", "Hofstadter's Law"),
        ("Programming today is a race between software engineers striving to build bigger and better idiot-proof "
         "programs, and the Universe trying to produce bigger and better idiots. So far, the Universe is winning.",
         "Rick Cook"),
        ("There are only two kinds of languages: the ones people complain about and the ones nobody uses.",
         "Bjarne Stroustrup"),
        ("It's all talk until the code runs.", "Ward Cunningham")
    ]

    return random.choice(quotes)
