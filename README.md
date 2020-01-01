# Fuzzer benchmarking tool

## Getting started:

### Prerequisites:

To run this benchmark tool, you need :
- Python3 installed
- Grammarinator installed : pip3 install grammarinator
- Gramfuzz installed : pip3 install gramfuzz
- Dharma installed : pip3 install dharma
- Creating the grammar files needed for each fuzzer in the grammars/ directory (WARNING: their name must be the same, the only difference must be the file format)

### Running

Usage : python3 benchmark.py [grammar_name] [start_symbol] [max_number_of_test_cases_generated]

[grammar_name] : file name of the files in grammars/ without the file extension !
[start_symbol] : symbol from which the test cases must be created
[max_number_of_test_cases_generated] : explicit enough, must be > 50, > 1000 is more significative though

### Additional warnings

At the moment, the program doesn't handle grammars with recursive rules. This will be implemented in the near future
