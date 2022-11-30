# Given a Binary Tree filled with Person objects, where each Person has an age attribute,
# determine the age range.

def get_age_range(people_tree):
    if not people_tree.root:
        return 0

    def walk(root, youngest=0, oldest=0):
        # determine base case
        if not root:
            return youngest, oldest
        # return something out here
        if root.value < youngest:
            youngest = root.value
        elif root.value > oldest:
            oldest = root.value

        youngest, oldest = walk(root.left, youngest, oldest)
        youngest, oldest = walk(root.right, youngest, oldest)

        return youngest, oldest

    first_peron = people_tree.root
    youngest, oldest = walk(first_peron, first_peron.value, first_peron.value)
    return f'The range is {oldest} to {youngest}'

    # people_tree = 25
    #     25
    #   /     \
    # 40       18
