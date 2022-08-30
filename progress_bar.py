#A progress bar function I made for CLI while working on some web scraping.

#pre: Iterable function calls this per-iteration
#post: progress bar is returned with percentage  
def progress_bar (current, total, length, message):
    percentage = current / total
    current_length = math.floor(length * percentage)
    #clear
    print(chr(27) + "[2J")
    status = message + '\n'
    progress_bar = togo_bar = ''
    start = "Progress: [" + '{:.0%}'.format(percentage) + "] <"
    for i in range(current_length):
        progress_bar += '='
    for i in range(length - current_length):
        togo_bar += '-'
    end = '>'

    return (status + start + progress_bar + togo_bar + end)
