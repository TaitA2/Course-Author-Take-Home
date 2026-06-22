# List Comprehension
List comprehension is basically just a shortcut for creating and populating a list all in one line.
It doesn't really add any *new* capabilities to your arsenal as a programmer (Probably why it's not already a lesson on Boot.Dev!), but it can be a really useful.

Besides, python programmers *love* to use it, so you'll definitely need to know how it works to understand other people's code and be a better team asset overall.

So let's get into it!


## Syntax
The syntax for list comprehension is as follows:

`new_list = [expression for element in other_iterable if condition == True]`

This seems pretty unlike a lot of the syntax we've used up until now, but there's only really one major difference: where the expression is.
If we move the expression to the end (and add a few ':'s) like this:

`for item in iterable: if condition == True: expression`

Then all of a sudden it's exactly the same syntax we know and love!
Just all pressed together on one line.

Unlike what we've done before however, the expression won't be something like `new_list.append(an_item)`.
That's because whatever the expression returns is automatically stored in the new_list.


## Example
It's sort of like a blueprint, instead of creating an empty list upfront like this:
`new_list = []`
You instead fill the brackets with a description of all the elements it should contain.
`new_list = [i for i in range(10) if i % 2 == 0] # [0, 2, 4, 6, 8]`

Up until now, to make a list of words with fewer than 5 characters, we needed to do something like this:
```
words = ["please", "hire", "Adam", "immediately"]
short_words = []
for word in words:
    if len(word) < 5:
        short_words.append(word)

# short_words = ["hire", "Adam"]
```

The same can be done in one line using list comprehension:
```
words = ["please", "hire", "Adam", "immediately"]
short_words = [word for word in words if len(word) < 5] # ["hire", "Adam"]
```

The condition part is also optional if you want to run an operation on every item in the list e.g.
```
words = ["you", "should", "hire", "Adam"]
uppers = [word.upper() for word in words]  # ["YOU", "SHOULD", "HIRE", "ADAM"]
```

Using list comprehension this way can be good for readability and organization, especially if it's a straight-forward enough operation.


<details open>
<summary><h2>Assignment</h2></summary>
Let's work on Fantasy Quest's Bestiary! Our players need to be able to view the Bestiary one alphabetical page at a time.
<br>

Use list comprehension to return only the creatures who's names start with a given letter.
<br>
Example:
<br>

```
  # bestiary_page(["cat", "dog"], c) -> ["cat"]
  # bestiary_page(["cat", "dragon", "dog"], d) -> ["dragon", "dog"]
```
<br>

</details>
<details>

<summary><h2>Tip</h2></summary>

Use the [str.startswith() method](https://python-reference.readthedocs.io/en/latest/docs/str/startswith.html) to check if a creature has the correct first_letter.

Use the [str.lower() method](https://python-reference.readthedocs.io/en/latest/docs/str/lower.html) to make sure your solution is case-insensitive.

If you need to, you can try to solve it without list comprehension first, then rearrange your code after.
</details>



<details>

<summary><h1>Multiple Choice Questions</h1></summary>

### Return Values
What will be stored in `print_odds` after this list comprehension runs?

`print_odds = [print(x) for x in range(10) if x % 2 != 0]`

1. `[None, None, None, None, None]` # Correct! Since print() runs during the list comprehension and returns None.
2. `[1, 3, 5, 7, 9]`
3. `[print(1), print(3), print(5), print(7), print(9)]`

### Syntax
Which is the correct syntax to create a list of multiples of 7 from a list called nums?
1. `sevens = [for x in nums: if x % 7 == 0: x]`
2. `sevens = [sevens.append(x) for x in nums if x % 7 == 0]`
3. `sevens = [for x in nums: if x % 7 == 0: sevens.append(x)]`
4. `sevens = [x for x in nums if x % 7 == 0]` # Correct!

</details>
