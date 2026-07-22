student={
    "name":"Nimish",
    "subjects":{
        "phy":90,
        "chem":82,
        "maths":95
    }
}

# print(list(student.keys()))
# print((student.values()))
# print(((student.items())))
print((student["subjects"].get("maths")))