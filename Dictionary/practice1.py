food = {
    "food1":"apple",
    "food2":"banana"
}
print(food)
food["food1"] = "graps"
print(food)


food.update({"food2":"orange"})
print(food)
food.pop("food2")

print(food)


uobs = {
    "department":{
        "dep1":"bscs",
        "dep2":"bsse"
    },
    "assignemnt":{
        "ass1":"web",
        "ass2":"python"
    }
}
print(uobs)
for x, obj in uobs.items():
  print(x)
  print(obj)
  for y in obj:
    print(y + ':', obj[y])




