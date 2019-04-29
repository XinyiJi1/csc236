from typing import List


def shade_sort(colour_list: List[str]) -> None:
    """ Put colour_list in order "b" < "g" < "r".

    precondition: colour_list is a List[str] from {"b", "g", "r"}

    >>> list_ = ["r", "b", "g"]
    >>> shade_sort(list_)
    >>> list_ == ["b", "g", "r"]
    True
    >>> list_ = ["g", "b", "r", "r", "r", "r"]
    >>> shade_sort(list_)
    >>> list_ == ["b", "g", "r", "r", "r", "r"]
    True
    >>> list_ = ["b", "g", "r", "b", "b", "b"]
    >>> shade_sort(list_)
    >>> list_ == ["b", "b", "b", "b","g", "r"]
    True
    >>> list_ = ["r", "b", "g", "g", "g", "g"]
    >>> shade_sort(list_)
    >>> list_ == ["b", "g", "g", "g", "g", "r"]
    True
    >>> list_ = []
    >>> shade_sort(list_)
    >>> list_ == []
    True
    >>> list_ = ["r"]
    >>> shade_sort(list_)
    >>> list_ == ["r"]
    True

    postcondition: colour_list has same strings as before,
                   ordered "b" < "g" < "r"
    """
    # Hint: blue, green may increase while red decreases.
    #
    # loop invariants:
    #
    # 0 <= blue <= green <= red <= len(colour_list)
    # colour_list[0 : green] + colour_list[red :] same colours as before
    # and all([c == "b" for c in colour_list[0 : blue]])
    # and all([c == "g" for c in colour_list[blue : green]])
    # and all([c == "r" for c in colour_list[red :]])
    #
    blue = 0
    green = 0
    red = len(colour_list)

    while green < red:
        if colour_list[red - 1] == "r":
            red -= 1
            if colour_list[green] == "g":
                green += 1
            elif colour_list[green] == "b":
                colour_list[blue], colour_list[green] = colour_list[green], \
                                                        colour_list[blue]
                green += 1
                blue += 1
        elif colour_list[red - 1] == "g"or colour_list[red - 1] == "b":
            if colour_list[green] == "g":
                green += 1
            elif colour_list[green] == "b":
                colour_list[blue], colour_list[green] = colour_list[green], \
                                                        colour_list[blue]
                green += 1
                blue += 1
            elif colour_list[green] == "r":
                colour_list[red - 1], colour_list[green] = colour_list[green], \
                                                        colour_list[red - 1]
                red -= 1
                if colour_list[green] == "g":
                    green += 1
                elif colour_list[green] == "b":
                    colour_list[blue], colour_list[green] = \
                        colour_list[green], colour_list[blue]
                    green += 1
                    blue += 1


def four_shade_sort(colour_list: List[str]) -> None:
    """ Put colour_list in order "b" < "g" < "r" < "y".

    precondition: colour_list is a List[str] from {"b", "g", "r", "y"}

    >>> list_ = []
    >>> four_shade_sort(list_)
    >>> list_ == []
    True
    >>> list_ = ["r"]
    >>> four_shade_sort(list_)
    >>> list_ == ["r"]
    True
    >>> list_ = ["r", "b", "y", "g"]
    >>> four_shade_sort(list_)
    >>> list_ == ["b", "g", "r", "y"]
    True
    >>> list_ = ["y", "r", "g", "b", "y", "y", "y", "y"]
    >>> four_shade_sort(list_)
    >>> list_ == ["b", "g", "r", "y", "y", "y", "y", "y"]
    True
    >>> list_ = ["r", "y", "g", "b", "r", "r", "r", "r"]
    >>> four_shade_sort(list_)
    >>> list_ == ["b", "g", "r", "r", "r", "r", "r", "y"]
    True
    >>> list_ = ["g", "y", "r", "b", "g", "g", "g", "g"]
    >>> four_shade_sort(list_)
    >>> list_ == ["b", "g", "g", "g", "g", "g", "r", "y"]
    True
    >>> list_ = ["b", "r", "y", "g", "b", "b", "b", "b"]
    >>> four_shade_sort(list_)
    >>> list_ == ["b", "b", "b", "b", "b", "g", "r", "y"]
    True

    postcondition: colour_list has same strings as before,
                   ordered "b" < "g" < "r" < "y"
    """
    # loop invariants:
    #
    # 0 <= blue <= green <= red <= yellow <= len(colour_list)
    # colour_list[0 : green] + colour_list[red :] same colours as before
    # and all([c == "b" for c in colour_list[0 : blue]])
    # and all([c == "g" for c in colour_list[blue : green]])
    # and all([c == "r" for c in colour_list[red : yellow]])
    # and all([c == "y" for c in colour_list[yellow :]])
    #
    blue, green = 0, 0
    red, yellow = len(colour_list), len(colour_list)

    while green < red:
        if colour_list[red - 1] == "r" or colour_list[red - 1] == "y":
            if colour_list[red - 1] == "y":
                colour_list[red - 1], colour_list[yellow - 1] = \
                    colour_list[yellow - 1], colour_list[red - 1]
                yellow -= 1
            red -= 1
            if colour_list[green] == "g":
                green += 1
            elif colour_list[green] == "b":
                colour_list[blue], colour_list[green] = colour_list[green], \
                                                        colour_list[blue]
                green += 1
                blue += 1
        elif colour_list[red - 1] == "g" or colour_list[red - 1] == "b":
            if colour_list[green] == "g":
                green += 1
            elif colour_list[green] == "b":
                colour_list[blue], colour_list[green] = colour_list[green], \
                                                        colour_list[blue]
                green += 1
                blue += 1
            elif colour_list[green] == "r" or colour_list[green] == "y":
                colour_list[red - 1], colour_list[green] = colour_list[green], \
                                                        colour_list[red - 1]
