import sys
import subprocess
import time
import gramfuzz

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
        # Here I handle the fact that a test case means several ones for DHARMA
        f = open("dharma/result.txt","w")
        f.write(result.stdout.decode('utf-8'))
        f.close()

        r = open("dharma/result.txt","r")
        lines = r.readlines()
        number_of_test_cases = 0;
        for line in lines:
            if(line.strip()!=""):
                number_of_test_cases+=1;
        runtime = (runtime / number_of_test_cases) * tries
        r.close()

        return runtime

def test_grammarinator(grammar, start_symbol, tries):
    command1 = "grammarinator-process grammars/" + grammar + ".g4 -o grammarinator --no-actions"
    command2 = "grammarinator-generate -l grammarinator/" + grammar + "Unlexer.py -p grammarinator/" + grammar + "Unparser.py -r " + \
    start_symbol + " -o grammarinator/tests/test_%d.html -n " + str(tries)
    start = time.time()
    result = subprocess.run(command1, stdout=subprocess.PIPE, shell=True)
    result = subprocess.run(command2, stdout=subprocess.PIPE, shell=True)
    end = time.time()
    runtime = end - start
    return runtime

def test_gramfuzz(grammar, start_symbol, tries):
    grammar = "grammars/" + grammar + ".py"
    start = time.time()
    fuzzer = gramfuzz.GramFuzzer()
    fuzzer.load_grammar(grammar)
    result = fuzzer.gen(cat=start_symbol, num=tries)
    end = time.time()
    runtime = end - start
    return runtime


def print_benchmark(times):
    print("")
    print("Dharma: " + str(times[0]))
    print("Domato: " + str(times[1]))
    print("Gramfuzz: " + str(times[2]))
    print("Grammarinator: " + str(times[3]))

def main():
    if (len(sys.argv) != 4):
        print("Usage : python3 benchmark.py [grammar_name] [start_symbol] [number_of_test_cases_generated]")
    else:
        grammar = sys.argv[1]
        start_symbol = sys.argv[2]
        tries = int(sys.argv[3])

        time_domato = test_domato(grammar, start_symbol, tries)
        time_dharma = test_dharma(grammar,tries)
        time_grammarinator = test_grammarinator(grammar, start_symbol, tries)
        time_gramfuzz = test_gramfuzz(grammar,start_symbol,tries)
        times = [time_dharma, time_domato, time_gramfuzz, time_grammarinator]

        print_benchmark(times)

        # Cleaning step
        result = subprocess.run("rm dharma/result.txt", shell=True)
        result = subprocess.run("rm -rf __pycache__ grammarinator/tests grammarinator/__pycache__", shell=True)
        result = subprocess.run("rm grammarinator/*.py", shell=True)
        result = subprocess.run("rm -rf domato/__pycache__", shell=True)


if __name__=="__main__":
    main()
