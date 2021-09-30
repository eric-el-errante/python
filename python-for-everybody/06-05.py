text = "X-DSPAM-Confidence:    0.8475"
start = text.find(" ")
number_string = text[start :]
number = number_string.strip()
fnumber = float(number)
print(fnumber)
print(type(fnumber))