#------01--------
#cities = ["new york city", "mountain view", "chicago", "los angeles"]
# # for city in cities:
# #   print(city.title())
# for index in range(len(cities)):
#   cities[index] = cities[index].title()
#   print(cities)

# range(start, stop, step)


# ----------02------------
# sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

# for word in sentence:
#     print(word)

# for i in range(5, 35, 5):
#   print(i)

#----------03--------- 
# names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
# usernames = []

# for name in names:
#     usernames.append(name.lower().replace(" ", "_"))

# print(usernames)

# ---------04-----------
# names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
# for name in names:
#   name = name.lower().replace(" ", "_")
#   print(name)

# -----------05--------
# names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
# usernames = []

# for name in names:
#     usernames.append(name.lower().replace(" ", "_"))

# print(usernames)



# -----------06------------
# tokens = ['<greeting>', 'Hello World!', '</greeting>']

# count = 0
# for token in tokens:
#     if token[0] == '<' and token[-1] == '>':
#         count += 1

# print(count)


# ------------07-----------
# items = ['first string', 'second string']
# html_str = "<ul>\n"          # The "\n" here is the end-of-line char, causing
#                              # chars after this in html_str to be on next line

# for item in items:
#     html_str = html_str + "<li>{}</li>\n".format(item)
# html_str2 = html_str + "</ul>"

# print(html_str2)


# ------------08-----------
# usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# for i in range(len(usernames)):
#     usernames[i] = usernames[i].lower().replace(" ", "_")

# print(usernames)

# for i in range(len(usernames)):
#   usernames[i] = usernames[i].lower().replace(" ", "_")
#   print(usernames)


# ------------09------------
colors = ['Red', 'Blue', 'Green', 'Purple']
lower_colors = [ ]

for color in colors:
    lower_colors.append(color.lower())
print(lower_colors)

