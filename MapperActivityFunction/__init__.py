# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import re

def main(inputPair: dict[int, str]) -> list[dict[str, str]]:
    
    output = []

    for key, value in inputPair.items():
        pom = re.sub("[({#$,:.?!-;})]", " ", value)
        pom = re.sub(" +", " ", pom)

        for word in pom.split(" "):
            output.append({word: 1})

    return output


# test = main({1: "oh-oj-oh. oh"})

# print(test)