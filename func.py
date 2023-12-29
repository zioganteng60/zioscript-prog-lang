def arrVal(arr, i):
    try:
        return arr[i]
    except IndexError:
        return 'null'
