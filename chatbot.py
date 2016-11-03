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

regex_responses = { "I would like you to (?P<verb>.+) my friend (?P<name>.+)": "Sure, I'll verb name right now!",
 "Who is (?P<first_name>.+) von (?P<second_name>.+)\?": "I don't know who first_name is, but I'm sure he is from second_name.",
 "I want (?P<number>.+) scoops of (?P<flavor>.+) ice cream": "flavor ice cream, number scoops, that'll be 37 dollars",
 "I want directions to (?P<city>.+), (?P<state>.+)": "Oh, I wouldn't go to state. But if you must, beware of the girls in city."}


def extract_words(exp,sentence):
    result = re.match(exp, sentence)
    if result:
        return result.groupdict()


def responder(user_sentence):
    #match user_sentence against expression
    #if it matches return response with extracted words
    for expression in regex_responses:
        extracted_dict = extract_words (expression, user_sentence)
        if extracted_dict:
            extracted_keys = extracted_dict.keys()
            response = regex_responses[expression]
            for key in extracted_dict:
                response = response.replace(key, extracted_dict[key])
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
