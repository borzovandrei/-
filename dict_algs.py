ivan = {
    "name":  "ivan",
    "age":  3,
    "children": [{
        "name": "vasja",
        "age":  12,
    }, {
         "name": "petja",
         "age":  10,
    }],
}

darja = {
    "name":  "dasha",
    "age":  17,
    "children": [{
        "name":  "Andrei",
        "age":  21,
    }, {
        "name": "Vova",
        "age":  15,
    }],
}

emps = [ivan, darja]


def findnames(emps):
    goodnames = []
    for i in emps:
        for x in i["children"]:
            if x["age"]>=18:
                goodnames.append(i["name"])
                break
    return goodnames

print(findnames(emps))