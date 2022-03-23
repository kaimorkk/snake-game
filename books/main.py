class Bucket:
    def some_kwargs(kwarg_1,kwarg_2,kwarg_3,kwarg_4):
        print("kwarg_1:",kwarg_1)
        print("kwarg_2:",kwarg_2)
        print("kwarg_3:",kwarg_3)
        print("kwarg_4:",kwarg_4)
    kwargs = {"kwarg_1": "apple=3.5", "kwarg_2": "milk=2.5", "kwarg_3": "juice=4.9", "kwarg_4": "water=2.5"}
    some_kwargs(**kwargs)