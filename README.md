# python-not-none
Simple decorator for preventing null arguments from being passed as a parameter.

# Usage
``````
from not_none import not_none

@not_none()
def no_none(a,b):
    return (a,b)
    
@not_none(nullable_parameters=["b"])
def allow_b_as_none(a,b):
    return (a,b)

#passes
no_none(1,1)

#fails
no_none(None,1)

#passes
allow_b_as_none(1,None)

#fails
allow_b_as_none(None,1)

  
``````

## Notes:
Using this decorator requires "()"

e.g.

```@not_none()```

not

```@not_none```