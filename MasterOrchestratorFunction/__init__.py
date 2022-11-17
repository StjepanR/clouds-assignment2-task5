# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json

import azure.functions as func
import azure.durable_functions as df

# test1 = {1: "a a a a a a a b a a a b a c a d d d a b c"}
# test2 = {2: "a b c d"}
# test3 = {3: "aaa bbb bb aa cc c a bb cc c aa a a"}

def orchestrator_function(context: df.DurableOrchestrationContext):
    
    tests = yield context.call_activity("GetInputDataFn", "test")

    tasks1 = []

    for test in tests:
        tasks1.append(context.call_activity("MapperActivityFunction", test))
    
    results = yield context.task_all(tasks1)

    tasks2 = []
    for result in results:
        tasks2.append(context.call_activity("ShufflerActivityFunction", result))
    results = yield context.task_all(tasks2)

    tasks3 = []
    for result in results:
        tasks3.append(context.call_activity("ReducerActivityFunction", result))
    results = yield context.task_all(tasks3)

    print(results)
    
    return results

main = df.Orchestrator.create(orchestrator_function)