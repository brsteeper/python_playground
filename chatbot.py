import random
import re

# s1 = "I want to go to Albany, NY"
# s2 = "I want three scoops of vanilla ice cream"
# s3 = "I want world peace, what do you want?"

#exp = "I want (?P<number>.+) scoops of (?P<flavor>.+) ice cream"

# def extract_words(sentence):
#     result = re.match(exp, sentence)
#     if result:
#         return result.group(1, 2)


# print extract_thing(s1)
# print extract_thing(s2)
# print extract_thing(s3)


sassy_responses = ["Are you kidding me?", "Would you like me to call your friend?", "Stupendous"]

sensible_responses = {"directions": "you're doing fine, go straight", "weather": "Looks pretty bad out there!", "food": "I can order you some pizza"}

regex_responses = {"I want (?P<number>.+) scoops of (?P<flavor>.+) ice cream": "flavor ice cream, number scoops, that'll be 37 dollars", "I want directions to (?P<city>.+), (?P<state>.+)": "Oh, I wouldn't go to state. But if you must, beware of the girls in city."}

def extract_words(exp,sentence):
    result = re.match(exp, sentence)
    if result:
        return result.group(1, 2)


def responder(user_sentence):
    #match user_sentence against expression
    #if it matches return response with extracted words
    for expression in regex_responses:
        pattern_words = extract_words (expression, user_sentence)
        if pattern_words:
            response = regex_responses[expression]
            if "flavor" in response:
                response = response.replace("flavor", pattern_words[1])
                response = response.replace("number", pattern_words[0])
            else:
                response = response.replace("city", pattern_words[0])
                response = response.replace("state", pattern_words[1])
            return response

    
    # if keyword in user_sentence:
    #return sensible_responses[keyword]
    for keyword in sensible_responses:
        if keyword in user_sentence:
            return sensible_responses[keyword]
    #if there is no keyword match, then return a random sassy response
    return random.choice(sassy_responses)

if __name__ == "__main__":
    system_sentence = "what can I do for you? "
    while True:
        user_response = raw_input(system_sentence) 
        system_sentence = responder(user_response)
