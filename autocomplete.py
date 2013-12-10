import logging
import optparse
import time

from pytries import Trie

def fill(trie, data_file):
    '''
    Initialize the Trie with the content of a file.
    The file should have a word per line

    '''
    data = open(data_file,'r')
    for line in data:
        trie[line.strip()]=True
    data.close()

def main():
    p = optparse.OptionParser()
    p.add_option('--data', '-d', default="data.txt")
    options, arguments = p.parse_args()
    trie_dict = Trie()
    
    start = time.clock()
    logging.info('Processing data fill. This can take a few minutes')
    fill(trie_dict, options.data)
    end = time.clock()
    logging.info('Data processed in %g seconds', (end-start))
   
    print("")
    print("Quit with CTRL+C")
    print("")

    while(True):
        prefix = raw_input("Please type the prefix of a word: ")
        start = time.clock()
        suggestions = trie_dict.prefix(prefix)
        end = time.clock()

        idx = 0
        for suggestion in suggestions:
            idx += 1
            print('    ' + str(suggestion[0]))

        print("  %d suggestions found in %g seconds :" % (
            idx,
            end-start
            )
        )

if __name__ == '__main__':
   main()