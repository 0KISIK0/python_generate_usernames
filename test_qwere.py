import json
from qwere import open_l,split1,gen,allfunc

def read_data(test_name):
    with open("data.json") as data:
        data = json.load(data)
        input=data[test_name]["input"]
        output=data[test_name]["output"]
        return input,output
    
#print(read_data("open_l"))

def test_open_l():
    input,output = read_data("open_l")
    if len(input) == len(output):
       for i in range(len(input)):
           assert open_l(input[i]) == output[i]

def test_split1():
    input,output = read_data("split1")
    if len(input) == len(output):
       for i in range(len(input)):
           assert split1(input[i]) == output[i]


def test_gen():
    input,output = read_data("gen")
    if len(input) == len(output):
       for i in range(len(input)):
           assert gen(input[i]) == output[i]

def test_allfunc():
    input,output = read_data("allfunc")
    allfunc(input,"output_test.txt")
