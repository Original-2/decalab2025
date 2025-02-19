def generate_verilog_combinations(num_inputs, active_counts, module_name=None):
    if module_name is None:
        counts_str = '_or_'.join(str(c) for c in active_counts)
        module_name = f"make_{counts_str}_active_out_of_{num_inputs}"

    input_names = [chr(65 + i) for i in range(num_inputs)]

    sum_bits = (num_inputs).bit_length()

    verilog_code = [
        f"module {module_name}(",
        "    " + ",\n    ".join([f"input bit {name}" for name in input_names]) + ",",
        "    output bit Y",
        ");",
        ""
    ]

    verilog_code.extend([
        f"    // Count the number of inputs that are '1'",
        f"    bit [{sum_bits}:0] sum;",
        f"    assign sum = {' + '.join(input_names)};",
        f""
    ])

    comparisons = []
    for count in active_counts:
        comparisons.append(f"sum=={sum_bits+1}'d{count}")

    verilog_code.extend([
        f"    // Output is true when sum equals any of the specified counts",
        f"    assign Y = {'|'.join(comparisons)};",
        f"",
        f"endmodule"
    ])

    return "\n".join(verilog_code)

def generate_combinational_terms(num_inputs, active_count):
    from itertools import combinations

    input_names = [chr(65 + i) for i in range(num_inputs)]
    terms = []

    for high_indices in combinations(range(num_inputs), active_count):
        term_parts = []
        for i in range(num_inputs):
            if i in high_indices:
                term_parts.append(input_names[i])
            else:
                term_parts.append(f"~{input_names[i]}")
        terms.append(" & ".join(term_parts))

    return terms

def generate_verilog_combinational(num_inputs, active_counts, module_name=None):
    if module_name is None:
        counts_str = ''.join(str(c) for c in active_counts)
        module_name = f"make_{counts_str}_active_out_of_{num_inputs}_comb"

    input_names = [chr(65 + i) for i in range(num_inputs)]

    verilog_code = [
        f"module {module_name}(",
        "    " + ",\n    ".join([f"input bit {name}" for name in input_names]) + ",",
        "    output bit Y",
        ");"
    ]

    for count in active_counts:
        terms = generate_combinational_terms(num_inputs, count)
        if not terms:
            continue

        if len(terms) > 3:
            verilog_code.append(f"    // {count} active combinations ({len(terms)} cases)")
            verilog_code.append(f"    bit num_{count}_active;")
            verilog_code.append(f"    assign num_{count}_active = ")

            chunk_size = 3
            for i in range(0, len(terms), chunk_size):
                chunk = terms[i:i+chunk_size]
                line = "        " + " | ".join(f"({term})" for term in chunk)
                if i + chunk_size < len(terms):
                    line += " |"
                else:
                    line += ";"
                verilog_code.append(line)

        else:
            verilog_code.append(f"    // {count} active combinations ({len(terms)} cases)")
            verilog_code.append(f"    bit num_{count}_active;")
            verilog_code.append(f"    assign num_{count}_active = {' | '.join(f'({term})' for term in terms)};")

        verilog_code.append("")

    active_wires = [f"num_{count}_active" for count in active_counts if generate_combinational_terms(num_inputs, count)]
    verilog_code.append("    // Output is true for any of the specified cases")
    verilog_code.append(f"    assign Y = {' | '.join(active_wires)};")
    verilog_code.append("")
    verilog_code.append("endmodule")

    return "\n".join(verilog_code)

if __name__ == "__main__":
    # verilog_comb =     generate_verilog_combinations(12, [12])
    verilog_comb = generate_verilog_combinational(10, [4,5])
    print(verilog_comb)
