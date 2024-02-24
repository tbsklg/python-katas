start = lambda fn: fn([])
end = lambda stack: stack[0]
push = lambda stack: lambda x: lambda fn: fn(stack + [x])
add = lambda stack: lambda fn: fn(stack[:-2] + [stack[-1] + stack[-2]])
sub = lambda stack: lambda fn: fn(stack[:-2] + [stack[-1] - stack[-2]])
mul = lambda stack: lambda fn: fn(stack[:-2] + [stack[-1] * stack[-2]])
div = lambda stack: lambda fn: fn(stack[:-2] + [stack[-1] // stack[-2]])
