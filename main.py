from transformers import pipeline

classifier = pipeline("sentiment-analysis")
ans = classifier(input("Enter your string: "))
print("Mood is " + ans[0]['label'] + ' with probability = ' + str(round(ans[0]['score'] * 100, 2)) + "%")
