module XOR16v2(a,b, out);// simple xor for an array to be xor with 0

input [15:0] a;
input b;
output [15:0] out;

xor(out[15], a[15], b);
xor(out[14], a[14], b);
xor(out[13], a[13], b);
xor(out[12], a[12], b);
xor(out[11], a[11], b);
xor(out[10], a[10], b);
xor(out[9], a[9], b);
xor(out[8], a[8], b);
xor(out[7], a[7], b);
xor(out[6], a[6], b);
xor(out[5], a[5], b);
xor(out[4], a[4], b);
xor(out[3], a[3], b);
xor(out[2], a[2], b);
xor(out[1], a[1], b);
xor(out[0], a[0], b);


endmodule