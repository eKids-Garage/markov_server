text = "A>B\nB|>C"

def interpret(in_str, program, debug_mode = False):
    log = [(in_str)]
    while True:
        stop = False
        for instruction in program:
            if log[-1].find(instruction[0]) == -1:
                continue
            else:
                log.append(log[-1].replace(instruction[0], instruction[1], 1))
                stop = instruction[2]
                break
        if stop == True:
            break
    
    if debug_mode == True:
        return log
    else:
        return log[-1]

def parse_line(line):
    if line.find("|>") != -1:
            return (str(line).split("|>", 1)[0], str(line).split("|>", 1)[1], True)
    else:
        if line.find(">") != -1:
            return (str(line).split(">", 1)[0], str(line).split(">", 1)[1], False)
        else:
            return () 

