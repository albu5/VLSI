// Benchmark "Adder02" written by ABC on Thu Nov 26 22:51:26 2015

module Adder02 ( 
    a00, a01, b00, b01,
    y00, y01, y02  );
  input  a00, a01, b00, b01;
  output y00, y01, y02;
  wire n7, n8, n9, n10, n11, n12, n13, n14, n15, n16, n17, n18, n19, n20;
  assign n7 = a00 & ~b00;
  assign n8 = ~a00 & b00;
  assign n9 = ~n7 & ~n8;
  assign n10 = a01 & ~b01;
  assign n11 = ~a01 & b01;
  assign n12 = ~n10 & ~n11;
  assign n13 = a00 & b00;
  assign n14 = ~n12 & ~n13;
  assign n15 = n12 & n13;
  assign n16 = ~n14 & ~n15;
  assign n17 = ~b01 & ~n13;
  assign n18 = a01 & ~n17;
  assign n19 = b01 & n13;
  assign n20 = ~n18 & ~n19;
  assign y00 = ~n9;
  assign y01 = ~n16;
  assign y02 = ~n20;
endmodule


