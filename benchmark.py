import sys
import subprocess
import time
import gramfuzz
from matplotlib import pyplot as plt
from matplotlib import style

sys.path.append('domato')

from grammar import Grammar

def test_domato(grammar, start_symbol, tries):
    grammar = "grammars/" + grammar + ".txt"
    start = time.time()
    my_grammar = Grammar()
    my_grammar.parse_from_file(grammar)
    for i in range(tries):
        result = my_grammar.generate_symbol(start_symbol)
    end = time.time()
    runtime = end - start
    return runtime

def test_dharma(grammar, tries):
    command = "dharma -grammars grammars/" + grammar + ".dg -count " + str(tries)
    start = time.time()
    result = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
    end = time.time()
    if(result.returncode!=0):
        print("Crash de dharma, returncode="+result.returncode)
        return -1
    else:
        runtime = end - start
        return runtime

def test_grammarinator(grammar, start_symbol, tries):
    command1 = "grammarinator-process grammars/" + grammar + ".g4 -o grammarinator --no-actions"
    command2 = "grammarinator-generate -l grammarinator/" + grammar + "Unlexer.py -p grammarinator/" + grammar + "Unparser.py -r " + \
    start_symbol + " -o grammarinator/tests/test_%d.html -n " + str(tries) + " -d 10"
    result = subprocess.run(command1, stdout=subprocess.PIPE, shell=True)
    start = time.time()
    result = subprocess.run(command2, stdout=subprocess.PIPE, shell=True)
    end = time.time()

    runtime = end - start
    return runtime

def test_gramfuzz(grammar, start_symbol, tries):
    grammar = "grammars/" + grammar + ".py"
    start = time.time()
    fuzzer = gramfuzz.GramFuzzer()
    fuzzer.load_grammar(grammar)
    result = fuzzer.gen(cat=start_symbol, num=tries, max_recursion=10)
    end = time.time()
    runtime = end - start
    return runtime


def print_benchmark(x,y1,y2,y3,y4,grammar):
    fig=plt.figure()
    style.use('ggplot')
    plt.plot(x,y1,'g',label='domato',linewidth=2)
    plt.plot(x,y2,'c',label='dharma',linewidth=2)
    plt.plot(x,y3,'b',label='grammarinator',linewidth=2)
    plt.plot(x,y4,'m',label='gramfuzz',linewidth=2)
    plt.suptitle('Grammar-based fuzzers benchmark', fontsize=18)
    plt.title(grammar, fontsize=10)
    plt.ylabel('Time in seconds')
    plt.xlabel('Number of test cases')
    plt.legend()
    plt.grid(True,color='k')
    fig.savefig("benchmark.png")
    plt.show()


def main():
    if (len(sys.argv) != 4):
        print("Usage : python3 benchmark.py [grammar_name] [start_symbol] [max_number_of_test_cases_generated]")
    else:

        grammar = sys.argv[1]
        start_symbol = sys.argv[2]
        max_tries = int(sys.argv[3])

        x = [] # X-axis values
        y1 = [] # Y-axis values for domato
        y2 = [] # Y-axis values for dharma
        y3 = [] # Y-axis values for grammarinator
        y4 = [] # Y-axis values for gramfuzz

        tries = 10
        first_tries = [50, 100, 200, 500]
        first_tries_index = 0
        while tries <= max_tries :
            print("")
            print("--- Currently generating " + str(tries) + " test cases ---")
            print("")

            x.append(tries)

            time_domato = test_domato(grammar, start_symbol, tries)
            time_dharma = test_dharma(grammar, tries)
            time_grammarinator = test_grammarinator(grammar, start_symbol, tries)
            time_gramfuzz = test_gramfuzz(grammar,start_symbol,tries)

            y1.append(time_domato)
            y2.append(time_dharma)
            y3.append(time_grammarinator)
            y4.append(time_gramfuzz)

            if(tries < 500):
                tries = first_tries[first_tries_index]
                first_tries_index += 1
            else:
                tries += 500

        print_benchmark(x,y1,y2,y3,y4,grammar)

        # Cleaning step
        result = subprocess.run("rm -rf __pycache__ grammarinator/tests grammarinator/__pycache__", shell=True)
        result = subprocess.run("rm grammarinator/*.py", shell=True)
        result = subprocess.run("rm -rf domato/__pycache__", shell=True)


if __name__=="__main__":
    main()
