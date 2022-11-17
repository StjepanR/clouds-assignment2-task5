# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging


def main(inputList: list[dict[any, any]]) -> dict[any, list[any]]:
    
    output = {}

    for dict in inputList:
        for key, value in dict.items():
            if key in output.keys():
                output.get(key).append(value)
            else:
                output[key] = [value]
    
    return output

# test = main([{"1": "a"}, {"1": "b"}, {"2": "a"}, {"3": "b"}, {"2": "c"}, {"2": "a"}])

# print(test)