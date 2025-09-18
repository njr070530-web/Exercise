


def find(l):
    if len(l)==0:
        return (none)
    else:
        min=l[0]
        max=l[0]
        for number in l[1:]:
            if number < min:
                min=number
            elif number > max:
                max=number
            else:
                continue
    return(min,max)