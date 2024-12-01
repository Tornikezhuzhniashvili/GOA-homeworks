#დავალება 1
#შექმენით სია list_of_names, რომელშიც ინახება სახელები. დაწერეთ კოდი, რომელიც ითვლის, რამდენჯერ მეორდება კონკრეტული სახელი (მაგალითად, "დავით") სიაში.


list_of_names=["tornike", "luka", "tornike", "nika", "beqa", "tornike", "givi"]
name_count = 0
name = "tornike"
for char in list_of_names:
    if char in name:
        name_count += 1

print(name_count)