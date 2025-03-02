module make_1_or_2_active_out_of_10(
    input bit A,
    input bit B,
    input bit C,
    input bit D,
    input bit E,
    input bit F,
    input bit G,
    input bit H,
    input bit I,
    input bit J,
    output bit Y
);
    // Count the number of inputs that are '1'
    bit [4:0] sum;
    assign sum = A + B + C + D + E + F + G + H + I + J;

    // Output is true when sum equals any of the specified counts
    assign Y = (sum == 5'd1) || (sum == 5'd2);

endmodule
