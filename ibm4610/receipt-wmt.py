from escpos.printer import Serial

p = Serial(devfile='COM5', baudrate=9600, parity='N', stopbits=1, timeout=1.00, dsrdtr=True)

p.text("\033@") # Reset
p.text("\033C\100") # Set sheet eject length
p.text("\0331") # Select 1/8-inch line spacing
p.text("\033$\000\030") # Set left margin

p.text("\033a\000") # Left align
p.text("See back of receipt for your chance\n")
p.text("to win $1000 ID #:7N77MVS1VUY\n")

p.text("\033a\001") # Center align
p.image("C:\\Users\\Alexander\\Desktop\\download.jpg")
p.text("978-851-6265 Mgr:BETH WATERHOUSE\n")
p.text("333 MAIN ST\n")
p.text("TEWKSBURY MA 01876\n")

p.text("\033a\000") # Left align
p.text("ST# 02222 OP# 009056 TE# 56 TR# 00079\n")

p.text("PRNCS DIA RING 00128182447 F  52000.00 T\n")
p.text("PRNCS DIA RING 00128182447 F  52000.00 T\n")
p.text("PRNCS DIA RING 00128182447 F  52000.00 T\n")
p.text("PRNCS DIA RING 00128182447 F  52000.00 T\n")
p.text("PRNCS DIA RING 00128182447 F  52000.00 T\n")
p.text("PRNCS DIA RING 00128182447 F  52000.00 T\n")
p.text("PRNCS DIA RING 00128182447 F  52000.00 T\n")
p.text("PRNCS DIA RING 00128182447 F  52000.00 T\n")
p.text("PRNCS DIA RING 00128182447 F  52000.00 T\n")
p.text("PRNCS DIA RING 00128182447 F  52000.00 T\n")
p.text("PRNCS DIA RING 00128182447 F  52000.00 T\n")
p.text("PRNCS DIA RING 00128182447 F  52000.00 T\n")
p.text("PRNCS DIA RING 00128182447 F  52000.00 T\n")
p.text("PRNCS DIA RING 00128182447 F  52000.00 T\n")
p.text("PRNCS DIA RING 00128182447 F  52000.00 T\n")
p.text("PRNCS DIA RING 00128182447 F  52000.00 T\n")
p.text("PRNCS DIA RING 00128182447 F  52000.00 T\n")
p.text("PRNCS DIA RING 00128182447 F  52000.00 T\n")
p.text("PRNCS DIA RING 00128182447 F  52000.00 T\n")
p.text("PRNCS DIA RING 00128182447 F  52000.00 T\n")
p.text("                   SUBTOTAL 1040000.00  \n")
p.text("         TAX 1    6.250 %     65000.00  \n")
p.text("                      TOTAL 1105000.00  \n")
p.text("                  CASH TEND 1105000.00  \n")
p.text("                 CHANGE DUE       0.00  \n")

p.text("\033a\001") # Center align
p.text("# ITEMS SOLD 20\n")
p.text("TC# 6802 0004 2947 2838 4956\n")
p.barcode("68020004294728384956", "CODE128", height=58, width=2, pos='OFF', font='A', align_ct=True, function_type='B')

p.text("Low Prices You Can Trust. Every Day.\n")
p.text("05/26/20      14:24:56\n")
p.text("Scan with Walmart app to save receipts\n")

p.qr("US retail giant Walmart has begun rolling out its Walmart Pay QR code-based...", size=5)

p.text("\n")

p.cut()
