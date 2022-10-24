print("Choose one monthly blog topics")
print("national economy - foreign affairs - weather")
topic_option=input("type your topic: ")
topic=topic_option.lower() #change topic_option to lowercase for avoid errors
if topic in("national economy", "foreign affairs", "weather"): #'in' operator compare the different options separated by commas
    print("Chosen Topic: "+topic)
else:
    print("this topic is not contemplated")