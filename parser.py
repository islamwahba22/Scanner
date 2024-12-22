class RecursiveDescentParser:
    def __init__(self):
        self.grammar = {}
        self.start_symbol = ''
        self.input_seq = []  
        self.index = 0

    def input_grammar(self):
        self.grammar.clear()
        self.start_symbol = input("Enter the start non-terminal: ").strip()

        num_rules = int(input("Enter the number of rules: "))
        for _ in range(num_rules):
            lhs, rhs = input("Enter rule (Format: NonTerminal -> production): ").split("->")
            lhs, rhs = lhs.strip(), rhs.strip()
            if lhs not in self.grammar:
                self.grammar[lhs] = []
            self.grammar[lhs].append(rhs)

        print("\nGrammar Entered:")
        for lhs, rhs_list in self.grammar.items():
            print(f"{lhs} -> {' | '.join(rhs_list)}")

    def is_simple_grammar(self):
        for lhs, productions in self.grammar.items():
            for prod in productions:
                if prod and prod[0].isupper():
                    print(f"The Grammar isn't simple")
                    return False
        print("The Grammar is Simple.")
        return True

    def parse(self, sequence):
        self.input_seq = list(sequence)
        self.index = 0

        def match(symbol):
            if self.index < len(self.input_seq) and self.input_seq[self.index] == symbol:
                self.index += 1
                return True
            return False

        def parse_non_terminal(non_terminal):
            if non_terminal not in self.grammar:
                return False
            for production in self.grammar[non_terminal]:
                saved_index = self.index
                success = True
                for symbol in production:
                    if symbol.isupper():
                        if not parse_non_terminal(symbol):
                            success = False
                            break
                    else:
                        if not match(symbol):
                            success = False
                            break
                if success:
                    return True
                self.index = saved_index  
            return False

        result = parse_non_terminal(self.start_symbol) and self.index == len(self.input_seq)
        return result

    def run(self):
        while True:
            print("\n1- Enter Grammar")
            print("2- Check if Grammar is Simple")
            print("3- Parse a String")
            print("4- Exit")

            choice = input("Enter your choice: ").strip()
            if choice == '1':
                self.input_grammar()
            elif choice == '2':
                self.is_simple_grammar()
            elif choice == '3':
                sequence = input("Enter the string to parse: ").strip()
                if self.parse(sequence):
                    print("The input string is ACCEPTED.")
                else:
                    print("The input string is REJECTED.")
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    parser = RecursiveDescentParser()
    parser.run()