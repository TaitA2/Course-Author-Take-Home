from incomplete_main import spell_numbers

run_cases = [
    (["Mage light"], [(1, "Mage light")]),
    (["Fireball", "Blind", "Confuse"], [(1, "Fireball"), (2, "Blind"), (3, "Confuse")]),
]

submit_cases = run_cases + [
    (
        ["Lightning Bolt", "Freeze", "Daze", "Haste"],
        [(1, "Lightning Bolt"), (2, "Freeze"), (3, "Daze"), (4, "Haste")],
    ),
    (
        ["Fireball", "Blind", "Confuse", "Lightning Bolt", "Freeze", "Daze"],
        [
            (1, "Fireball"),
            (2, "Blind"),
            (3, "Confuse"),
            (4, "Lightning Bolt"),
            (5, "Freeze"),
            (6, "Daze"),
        ],
    ),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    result = spell_numbers(input1)
    actual = spell_numbers(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {list(actual)}")
    if type(result) is enumerate and list(result) == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
