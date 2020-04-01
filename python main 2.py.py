def fun(nestedDict,Dic,currentkey):
    for key in nestedDict.keys():
        if type(nestedDict[key])==int:
            Dic[(currentkey+"."+key).strip(".")]==nestedDict[key]
        else:
            Dic=fun(nestedDict[key],Dic,(currentkey+"."+key).strip("."))
    return Dic


def func_dic(nestedDic):
    return fun(nestedDic,dict(),"")

def main():
    nestedDictionary={"key":3,"foo":{"a":5,"bar":{"baz":8}}}
    dicten=fun_dic(nestedDictionary)
    print(dicten)

if _name_ == "_main_":
    main()
