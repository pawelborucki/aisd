def foo(i: int, stop: int) -> None:
    if i < stop:
        return
    print(i)

    foo(i - 1, stop)


foo(10, -1)