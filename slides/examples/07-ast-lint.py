import ast


def find_assert_tuples(tree):
    warnings = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assert):
            test = node.test
            if isinstance(test, ast.Tuple) and len(test.elts) > 0:
                warnings.append(node.lineno)
    return warnings


def main():
    bad_source = '''total = 9
assert (total == 10, "Wrong total")
'''
    fixed_source = '''total = 9
assert total == 10, "Wrong total"
'''

    for label, source in [("Before fix", bad_source), ("After fix", fixed_source)]:
        print(label)
        tree = ast.parse(source)
        warnings = find_assert_tuples(tree)
        for line in warnings:
            print(f"Line {line}: F631 assert test is a non-empty tuple")
        if not warnings:
            print("No F631 warnings.")


if __name__ == "__main__":
    main()
