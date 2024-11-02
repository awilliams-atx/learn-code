"""
exercism download --track=python --exercise=flatten-array

The lists in these tests were generated like this:

    def build_lists(max_depth: int):
        tmp_list = []
        lists_by_depth = {}
        for depth in range(max_depth + 1):
            lists_by_depth[depth] = tmp_list
            tmp_list = [tmp_list, 1, None, []]
        return lists_by_depth

This approach uses indexes and a stack (two stacks actually). This doesn't
risk exceeding the maximum call stack size.

    def stack_flatten(list_of_lists):
        flattened = []
        lists = []
        indexes = []
        inner_list = list_of_lists
        index = 0
        while True:
            length = len(inner_list)
            if index == length:
                if not lists:
                    return flattened
                inner_list = lists.pop()
                index = indexes.pop()
                continue
            val = inner_list[index]
            if not isinstance(val, list):
                if val is not None:
                    flattened.append(val)
                index += 1
                continue
            if index + 1 < length:
                lists.append(inner_list)
                indexes.append(index + 1)
            inner_list = val
            index = 0

Here's an approach with generators. Generators avoid memory and runtime
costs associated with passing around temporary slices of the final list
between recursive calls. It does still run into the maximum call stack
size.

    def gen_nested_vals(vals):
        for val in vals:
            if isinstance(val, list):
                yield from gen_nested_vals(val)
            elif val is not None:
                yield val

    def generator_recursion(list_of_lists):
        return list(gen_nested_vals(list_of_lists))

Here's a recursive approach. This is the most concise, but it does run into
the maximum call stack size, and it does generate temporary lists between
each recursive call.

    def basic_recursion(vals):
        flattened = []
        for item in vals:
            if isinstance(item, list):
                flattened.extend(basic_recursion(item))
            elif item is not None:
                flattened.append(item)
        return flattened

At very shallow depths, the basic recursive approach outpaced the other
two, with the stack approach in second at 47% slower and the generator
recursive approach in a close third.

    Depth[1]
      basic_recursion      0.05338812599075027
      stack_flatten        0.07873668699176051
      generator_recursion  0.08295583998551592
    Depth[10]
      basic_recursion      0.04406500200275332
      stack_flatten        0.05756600998574868
      generator_recursion  0.07183227001223713

With a depth of 30, the stack approach has almost caught up to the basic
recursive approach, and the generator approach is about 2-3 times as slow as
the others, and it lags behind at a greater and greater pace very quickly.
By the depth of 100, it is about 4.5 times slower than the others.

    Depth[30]
      basic_recursion      0.04884088897961192
      stack_flatten        0.052460994978901
      generator_recursion  0.11695599899394438
    Depth[50]
      basic_recursion      0.05367062397999689
      stack_flatten        0.05246637499658391
      generator_recursion  0.15692753999610431
    Depth[75]
      basic_recursion      0.06009555800119415
      stack_flatten        0.05219686098280363
      generator_recursion  0.21435854598530568
    Depth[100]
      basic_recursion      0.06763857702026144
      stack_flatten        0.05209367099450901
      generator_recursion  0.2740751009841915

At a depth of 500, the basic recursive approach has fallen far behind the
stack approach. Between depths 500 and 900, basic recursion and generator
recursion go from 4x and 26x slower to 6x and 48x slower than the stack
approach.

    Depth[500]
      basic_recursion      0.19807651100563817
      stack_flatten        0.05000995399313979
      generator_recursion  1.3101625830167904
    Depth[600]
      basic_recursion      0.2261650789878331
      stack_flatten        0.04963396000675857
      generator_recursion  1.5623025490203872
    Depth[700]
      basic_recursion      0.2520555910014082
      stack_flatten        0.0496982240001671
      generator_recursion  1.8188440899830312
    Depth[800]
      basic_recursion      0.2841870170086622
      stack_flatten        0.05015806001028977
      generator_recursion  2.092441210988909
    Depth[900]
      basic_recursion      0.3086704880115576
      stack_flatten        0.04936064800131135
      generator_recursion  2.356393648980884

Now, is it possible to improve the stack approach by using iterators?

    def iterator_stack(list_of_lists):
        flattened = []
        iterators = []
        iterator = iter(list_of_lists)
        while True:
            try:
                val = next(iterator)
            except StopIteration:
                if not iterators:
                    return flattened
                iterator = iterators.pop()
                continue
            if isinstance(val, list):
                iterators.append(iterator)
                iterator = iter(val)
                continue
            if val is not None:
                flattened.append(val)

Surprisingly, it's a lot slower than the stack aproach that uses index-based
approach! At any depth, it seems to stay around 2-3x slower.

    Depth[1]
      stack_flatten        0.07937148801283911
      iterator_stack       0.15735195300658233
    Depth[10]
      stack_flatten        0.05905207199975848
      iterator_stack       0.10605324601056054
    Depth[30]
      stack_flatten        0.054125335009302944
      iterator_stack       0.09880094998516142
    Depth[50]
      stack_flatten        0.05221559200435877
      iterator_stack       0.09678180000628345
    Depth[75]
      stack_flatten        0.05105544999241829
      iterator_stack       0.09769225199124776
    Depth[100]
      stack_flatten        0.05119708101847209
      iterator_stack       0.09732960499241017
    Depth[500]
      stack_flatten        0.05035000201314688
      iterator_stack       0.0949238589964807
    Depth[900]
      stack_flatten        0.05074900601175614
      iterator_stack       0.09470854300889187
"""


def flatten(list_of_lists):
    flattened = []
    lists = []
    indexes = []
    inner_list = list_of_lists
    index = 0
    while True:
        length = len(inner_list)
        if index == length:
            if not lists:
                return flattened
            inner_list = lists.pop()
            index = indexes.pop()
            continue
        val = inner_list[index]
        if not isinstance(val, list):
            if val is not None:
                flattened.append(val)
            index += 1
            continue
        if index + 1 < length:
            lists.append(inner_list)
            indexes.append(index + 1)
        inner_list = val
        index = 0
