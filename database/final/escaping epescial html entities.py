# import  re
# def replacehtmlspecials(string):
#     chars = {
#     '&#160;':' ',
#     '&#167;':'Section ',
#     '&#146;':'\'',
#     '&#147;':'\"',
#     '&#148;':'\"',
#     '&#174;':'',
#     '&#168;':'',
#     '&#153;':'',
#     '&#128;':'(euro)',
#     '&#163;':'(british pound)',
#     '&#150;':'-',
#     '&#165;':'(yen)',
#     '&#169;':'copyright ',
#     }

# 	charlist = ['&#160;','abhi']
#     for key in charlist:
#         if chars[key]:
#             string = re.sub(key, chars[key], string)
#             return string

# k="Psychology: Martin E. P. Seligman&#8217;s Visionary Science and Positive Psychology: Applications and Interventions."

import re, htmlentitydefs


def unescape(text):
    def fixup(m):
        text = m.group(0)
        if text[:2] == "&#":
            # character reference
            try:
                if text[:3] == "&#x":
                    return unichr(int(text[3:-1], 16))
                else:
                    return unichr(int(text[2:-1]))
            except ValueError:
                pass
        else:
            # named entity
            try:
                text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
            except KeyError:
                pass
        return text # leave as is
    return re.sub("&#?\w+;", fixup, text)