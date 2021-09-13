from Crypto.Util.number import bytes_to_long

n = 73542616560647877565544036788738025202939381425158737721544398356851787401183516163221837013929559568993844046804187977705376289108065126883603562904941748653607836358267359664041064708762154474786168204628181667371305788303624396903323216279110685399145476916585122917284319282272004045859138239853037072761
e = 0x10001
flag = bytes_to_long(open("flag.txt", "rb").read())

print(f"n = {n}")
print(f"e = {e}")
print(f"ct = {pow(flag, e, n)}")
print("""
Transcription of image:
735426165606478775655440367887380252029393814251587377215443983568517874011835161632
289108065126883603562904941748653607836358267359664041064708762154474786168204628181
9145476916585122917284319282272004045859138239853037072761
108294440701045353595867242719660522374526250640690193563048263854806748525172379331
341078269246532299656864881223
679098724593514422867704492870375465007225641192338424726642090768164214390632598250
39563231146143146482074105407

(n, p, q)
""")

