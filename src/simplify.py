

from collections import deque

def simplify_path(path):
    stack = deque()
    components = path.split('/')
    
    for component in components:
        if component == '..':
            if stack:
                stack.pop()
        elif component and component != '.':
            stack.append(component)
            
    return '/' + '/'.join(stack)
