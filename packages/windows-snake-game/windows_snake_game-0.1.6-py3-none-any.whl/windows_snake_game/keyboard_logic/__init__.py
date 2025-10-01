import sys
if sys.platform.startswith('win'):
    import msvcrt
elif sys.platform.startswith('linux'):
    import tty
    import termios
class KeyboardHandling :
    def __init__(self) :
        pass
    def windows():
        key=-1
        first_char= msvcrt.getche()
        if first_char == b'\xe0':
            second_char = msvcrt.getch()
            if second_char == b'H':
                key =0
            elif second_char == b'M' :
                key=3
            elif second_char == b'P' :
                key=2
            elif second_char == b'K' :
                key=1

        elif  first_char == b'w' or \
            first_char== b'8' :
            key =0
        elif  first_char == b'd' or \
            first_char== b'6' :
            key=3
        elif  first_char == b's' or \
            first_char== b'2' :
            key=2
        elif  first_char == b'a' or \
            first_char== b'4' :
            key=1
        elif first_char ==b' '  :
            key=4
        return key
    def linux():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)

        try:
            tty.setraw(fd)
            ch1 = sys.stdin.read(1)
            if ch1 == '\x1b':
                ch2 = sys.stdin.read(1)
                if ch2 == '[':
                    ch3 = sys.stdin.read(1)
                    if ch3 == 'A':
                        return 0
                    elif ch3 == 'B':
                        return 2
                    elif ch3 == 'C':
                        return 3
                    elif ch3 == 'D':
                        return 1
                return -1
            elif  str(ch1) == "w" :
                return 0
            elif  str(ch1) == "d" :
                return 3
            elif  str(ch1) == "s" :
                return 2
            elif  str(ch1) == "a" :
                return 1
            elif str(ch1) == " ":
                return 4

            else :
                return -1

        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


def handle_keyboard() :
    __KeyboardHandling=KeyboardHandling()
    if sys.platform.startswith('win'):
        return KeyboardHandling.windows()
    elif sys.platform.startswith('linux'):
        return KeyboardHandling.linux()


    else:
        raise "This game made for windows and linux "
        exit()

if __name__ == "__main__":
    for  i in range(20) :
        print(handle_keyboard())
        