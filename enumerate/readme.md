# Enumerate()
The [enumerate()](https://python-reference.readthedocs.io/en/latest/docs/functions/enumerate.html) function takes an iterable and returns pairs of (index, element).
It returns an enumerate object, which can be iterated over immediately like this:
```
for pair in enumerate(["Adam", "teaches", "gud"]):
    print(pair)
# (0, "Adam")  
# (1, "teaches")
# (2, "gud")
```
Or stored in a variable to be used later:
```
  e = enumerate(["Adam", "is", "kwl"])
```

There is also an optional parameter for the starting index.
```
  e = enmuerate(["let's", "hire", "Adam"], 1) # start counting from 1 (not 0)
  for pair in e:
      print(pair)
  # (1, "let's")
  # (2, "hire")
  # (3, "Adam")
```

## Next()

To access pairs from an enumerate object without iterating, we use `next(e)`.
```
e = enumerate(["another", "Adam", "example"], 1)
next(e) # (1, "another")
next(e) # (2, "Adam")
next(e) # (3, "example")
next(e) # ERROR
```

You *could* use a try-catch block to handle the end of the enumerate:
```
e = enumerate(words_list)

while True:
    try:
        print(next(e))
    except StopIteration:
        break

```
But this is really messy, so you can use a default value instead.
```
e = enumerate(["Lane", "likes", "Adam"], 1)

item = next(e, "end")
while item != "end":
    print(item)
    item = next(e, "end")

# (1, "Lane")
# (2, "likes")
# (3, "Adam")
```

<details open>
<summary><h2>Assignment</h2></summary>
Let's work on the Fantasy Quest spellbook. Our players should be able to see the spells they have unlocked in a numbered list.

Example:

```
1. Fireball
2. Healing spray
3. Disarm
```

Using the enumerate() function, return the player's spell list numbered starting from 1.

</details>
<details open>
<summary><h2>Note</h2></summary>
The enumerate object gets consumed when you access the elements either by iterating or using next().
Sometimes it helps to think of it less like a list of pairs, and more like a pez dispenser of pairs.
</details>

<details>
<summary><h2>Tip</h2></summary>
Use the 'start' parameter in your enumerate function.
</details>
