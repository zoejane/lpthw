ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

# slipt(ten_things, ' ')
# call split with argument ten_things and ' '
# call split on ten_things with argument ' '
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    # pop(more_stuff)
    # call pop with argument more_stuff
    # call pop on more_stuff
    next_one = more_stuff.pop()
    print("Adding:", next_one)
    # append(stuff, next_one)
    # call append with arguments stuff and next_one
    # call append on stuff with argument next_one
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # whoa! fancy
# pop(stuff)
print(stuff.pop())
# join(' ', stuff)
print(' '.join(stuff)) # what? cool!
# join('#, stuff[3:5]')
print('#'.join(stuff[3:5])) # super stellar!