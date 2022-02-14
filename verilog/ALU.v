module ALU(mc, op, word1, word2, word3, word4, word31, word32, word33, word34, res1, res2, res3, res4);
input [2:0] mc; //111 = 64 bit, 110 = 32 bit, 100 = 16 bit
input [1:0] op; //01 = add, 11 = xor, 00 = subtraction
input [15:0] word1;
input [15:0] word2;
input [15:0] word3;
input [15:0] word4;
input [15:0] word31;//second word placeholders
input [15:0] word32;
input [15:0] word33;
input [15:0] word34;

output reg [63:0] res1 = 0;//can be used for 64, 32, or 16 bit result
output reg [31:0] res2 = 0;//used for 32 or 16 bit result
output reg [15:0] res3 = 0;//used for 16 bit result
output reg [15:0] res4 = 0;//used for 16 bit result

wire [15:0] zeros = 0;

/*
assign zeros[15] = 0;
assign zeros[14] = 0;
assign zeros[13] = 0;
assign zeros[12] = 0;
assign zeros[11] = 0;
assign zeros[10] = 0;
assign zeros[9] = 0;
assign zeros[8] = 0;
assign zeros[7] = 0;
assign zeros[6] = 0;
assign zeros[5] = 0;
assign zeros[4] = 0;
assign zeros[3] = 0;
assign zeros[2] = 0;
assign zeros[1] = 0;

*/

wire [15:0] word21;
wire [15:0] word22;
wire [15:0] word23;//final second word that will be assigned to result
wire [15:0] word24;

wire [15:0] word41;
wire [15:0] word42;
wire [15:0] word43;//another second word place holder
wire [15:0] word44;


wire [63:0] sum;//sum for addition/subtraction
wire [63:0] xorres;//result of xor
reg [63:0] fullres;//full result that will be used to assign each word
wire cout[12:0]; //carry variables

assign cout[0] = ~op[1];


XOR16v2 init1(.a(word31[15:0]), .b(cout[0]), .out(word41[15:0]));//inverting b if operation is subtraction
XOR16v2 init2(.a(word32[15:0]), .b(cout[0]), .out(word42[15:0]));
XOR16v2 init3(.a(word33[15:0]), .b(cout[0]), .out(word43[15:0]));
XOR16v2 init4(.a(word34[15:0]), .b(cout[0]), .out(word44[15:0]));

CLA16 cla1(.a(zeros[15:0]), .b(word41[15:0]), .cin(~op[1]), .sum1(word21[15:0]), .cout(cout[11]));//adding 1 for 2s comp if subtraction
CLA16 cla2(.a(zeros[15:0]), .b(word42[15:0]), .cin(~op[1]), .sum1(word22[15:0]), .cout(cout[10]));
CLA16 cla3(.a(zeros[15:0]), .b(word43[15:0]), .cin(~op[1]), .sum1(word23[15:0]), .cout(cout[9]));
CLA16 cla4(.a(zeros[15:0]), .b(word44[15:0]), .cin(~op[1]), .sum1(word24[15:0]), .cout(cout[12]));

CLA16 cla5(.a(word1[15:0]), .b(word21[15:0]), .cin(0), .sum1(sum[15:0]), .cout(cout[5]));//addition/subtraction
and(cout[1], cout[5], mc[1]);//ANDs assign carry based on mode control, 64 bit carries through operation
CLA16 cla6(.a(word2[15:0]), .b(word22[15:0]), .cin(cout[1]), .sum1(sum[31:16]), .cout(cout[6]));
and(cout[2], cout[6], mc[0]);
CLA16 cla7(.a(word3[15:0]), .b(word23[15:0]), .cin(cout[2]), .sum1(sum[47:32]), .cout(cout[7]));
and(cout[3], cout[7], mc[1]);
CLA16 cla8(.a(word4[15:0]), .b(word24[15:0]), .cin(cout[3]), .sum1(sum[63:48]), .cout(cout[8]));


XOR16 xor1(.a(word1[15:0]), .b(word21[15:0]), .out(xorres[63:48]));//XOR operation
XOR16 xor2(.a(word1[15:0]), .b(word22[15:0]), .out(xorres[47:32]));
XOR16 xor3(.a(word1[15:0]), .b(word23[15:0]), .out(xorres[31:16]));
XOR16 xor4(.a(word1[15:0]), .b(word24[15:0]), .out(xorres[15:0]));





always @* begin

if(op[0] & op[1]) begin //addition or subtraction operation
	fullres[63:0] <= xorres[63:0];//assign addition/subtraction result
end

else begin  //xor operation
	fullres[63:0] <= sum[63:0];//assign xor result
end






//assign each output res based off mc

if(mc[0]==1 & mc[1]==1 & mc[2]==1) begin//if statements to assign result to word or words depending on mc variable
	res1[63:0] <= fullres[63:0];
end

else if(~mc[0] & mc[1] & mc[2]) begin
   res2[31:0] <= fullres[63:32];
	res1[31:0] <= fullres[31:0];
end

else if(~mc[0] & ~mc[1] & mc[2]) begin
   res4[15:0] <= fullres[63:48];
	res3[15:0] <= fullres[47:32];
	res2[15:0] <= fullres[31:16];
	res1[15:0] <= fullres[15:0];
end

//else if()

end

endmodule


module ALU_tb;//testbench to run module
reg [2:0] mc;
reg [1:0] op;
reg [15:0] word1;
reg [15:0] word2;
reg [15:0] word3;
reg [15:0] word4;
reg [15:0] word31;
reg [15:0] word32;
reg [15:0] word33;
reg [15:0] word34;
wire [63:0] res1;//can be used for 64, 32, or 16 bit result
wire [31:0] res2;//used for 32 or 16 bit result
wire [15:0] res3;//used for 16 bit result
wire [15:0] res4;//used for 16 bit result
  
ALU test(mc, op, word1, word2, word3, word4, word31, word32, word33, word34, res1, res2, res3, res4);
  
initial begin
mc=3'b111; //111 = 64bit, 110 = 32 bit, 100 = 16 bit
op=2'b11; //10 = add, 11 = xor, 00 = sub
word1=16'h0001;
word2=16'h0001;
word3=16'h0000;
word4=16'h0001;
word31=16'h0000;
word32=16'h0000;
word33=16'h0000;
word34=16'h0001;


#10;
end

//initial begin
//$monitor("a=%h b=%h, sum=%h\n",a,b,sum);
//end

endmodule

