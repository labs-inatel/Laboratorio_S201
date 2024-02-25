10 LET A = 0
20 LET B = 0
30 LET C = 0
40 LET DELTA = 0

50 INPUT "NUM1"; A
60 INPUT "NUM2"; B
70 INPUT "NUM3"; C

80 DELTA = (B*B) - (4*A*C)

90 IF DELTA < 0 THEN GOTO 100 ELSE GOTO 120
100 PRINT "Nao possuem raizes reais"
110 END

120 IF DELTA > 0 THEN GOTO 130 ELSE GOTO 170
130 PRINT "Possuem raizes reais distintas:"
140 PRINT "X1: " + (-B + SQR(DELTA))/(2*A)
150 PRINT "X2: " + (-B - SQR(DELTA))/(2*A)
160 END

170 PRINT "Possuem raizes reais iguais: " + (-B+SQR(DELTA))/(2*A)
180 END
