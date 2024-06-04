import shelve, pyperclip, sys

with shelve.open('mcb') as mcb_shelf:
    if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
        mcb_shelf[sys.argv[2]] = pyperclip.paste()
    elif len(sys.argv) == 2:
        if sys.argv[1].lower() == 'list':
            pyperclip.copy(str(list(mcb_shelf.keys())))
        elif sys.argv[1] in mcb_shelf:
            pyperclip.copy(mcb_shelf[sys.argv[1]])
    elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
            if sys.argv[2] in mcb_shelf:
                del mcb_shelf[sys.argv[2]]


