import logging
import optparse
import time

from pytries import Trie

def main():
    p = optparse.OptionParser()
    p.add_option('--data', '-d', default="data.txt")
    options, arguments = p.parse_args()
    trie_dict = Trie()
    
    start = time.clock()
    logging.info('Processing data fill. This can take a few minutes')
    trie_dict.fill(options.data)
    end = time.clock()
    logging.info('Data processed in %g seconds', (end-start))
   
    print("")
    print("Quit with CTRL+C")
    print("")

    while(True):
        prefix = raw_input("Please type the prefix of a word: ")
        start = time.clock()
        suggestions = trie_dict.get_autocomplete(prefix)
        end = time.clock()

        print("  %d suggestions found in %g seconds :" % (
            len(suggestions),
            end-start
            )
        )

        suggestions = trie_dict.get_autocomplete(prefix)
        for suggestion in suggestions:
            print('    ' + suggestion)

if __name__ == '__main__':
   main()