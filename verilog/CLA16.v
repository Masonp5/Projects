
module CLA16(a,b, cin, sum1, cout);
input [15:0] a;
input [15:0] b;
input cin;

output [15:0] sum1;
output cout;


wire c1,c2,c3; 

 
CLA4 cla1b (.a(a[3:0]), .b(b[3:0]), .cin(cin), .res(sum1[3:0]), .cout(c1));//making 16 bit cla adder from 4 4bit adders
CLA4 cla2b (.a(a[7:4]), .b(b[7:4]), .cin(c1), .res(sum1[7:4]), .cout(c2));//carry from last adder is used in next adder
CLA4 cla3b(.a(a[11:8]), .b(b[11:8]), .cin(c2), .res(sum1[11:8]), .cout(c3));
CLA4 cla4b(.a(a[15:12]), .b(b[15:12]), .cin(c3), .res(sum1[15:12]), .cout(cout));

 
endmodule
 

 
module CLA4(a,b, cin, res,cout);//basic 4 bit carry lookahead adder
input [3:0] a;
input [3:0] b;
input cin;
output [3:0] res;
output cout;
 
wire [3:0] p,g,c;


 
assign p[0]=a[0]^b[0];//assigning ps and gs
assign g[0]=a[0]&b[0]; 
assign p[1]=a[1]^b[1];
assign g[1]=a[1]&b[1];
assign p[2]=a[2]^b[2];
assign g[2]=a[2]&b[2];
assign p[3]=a[3]^b[3];
assign g[3]=a[3]&b[3];
 

 
assign c[0]=cin;//assigning cs based on formula for cla adder
assign c[1]= g[0]|(p[0]&c[0]);
assign c[2]= g[1] | (p[1]&g[0]) | p[1]&p[0]&c[0];
assign c[3]= g[2] | (p[2]&g[1]) | p[2]&p[1]&g[0] | p[2]&p[1]&p[0]&c[0];
assign cout= g[3] | (p[3]&g[2]) | p[3]&p[2]&g[1] | p[3]&p[2]&p[1]&g[0] | p[3]&p[2]&p[1]&p[0]&c[0];


assign res[0]=p[0]^c[0];//assigning result
assign res[1]=p[1]^c[1];
assign res[2]=p[2]^c[2];
assign res[3]=p[3]^c[3];

endmodule