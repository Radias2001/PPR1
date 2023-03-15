from transformers import pipeline


classifier = pipeline("fill-mask")
ans = classifier(input("Enter your string with <mask>: "))

for i in ans:
    print(i['sequence'] + ' with probability = ' + str(round(i['score'] * 100, 2)) + "%")
