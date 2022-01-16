import subprocess

'''
    params:
        1. time_limit: The maximum time for which the code can run.
        2. memory_limit: The maximum memory that can be allocated to the program.
'''

'''
    Exit codes used:
        -1 : Improper I/O
        1 : AC
        0 : WA
        2 : TLE
        3 : MLE
'''
submission_result = {
    -1: "Improper I/O",
    1: "AC",
    0: "WA",
    2: "TLE",
    3: "MLE"
}

def execute_code(time_limit, memory_limit):
    execution = subprocess.Popen([
        f'bash CodeExecutionEngine/code_execution_script.sh {int(time_limit)} {int(memory_limit)}'], shell=True, stdout=subprocess.PIPE)
    execution_return = execution.stdout.read()
    execution_return = str(execution_return, 'UTF-8')

    result = execution_return.split(' ')

    if(len(result) == 0):
        return "Problem encountered while executing code"

    curr_verdict = int(result[0])

    if curr_verdict not in submission_result.keys() or len(result) != 3:
        return "Invalid Output"

    return [submission_result[curr_verdict], result[1] , result[2]]

