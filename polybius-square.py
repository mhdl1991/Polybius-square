#Polybius cipher
class PolybiusCipher:
    def __init__(self, symbols = list("POLYBIUSQARE2019CDFGHJKMNTVWXZ345678") ):
        """Make a 6 x 6 polybius square with letters and numbers"""
        self.symbols = symbols
        self.polybius_square = [symbols[i:i+6] for i in (0, 6, 12, 18, 24, 30)]
    
    def draw_polybius_square(self):
        """Print the polybius square"""
        print("x|1|2|3|4|5|6|")
        for i in range(6):
            print("--------------")
            print("" + str(i+1) + "|" + "|".join(self.polybius_square[i]) + "|")
        print("--------------")
        
    def encipher_letter(self,letter,key = ''):
        """
            return (row,column) of letter in Polybius square, encoded with a key letter k if available
            if you have the letter A
            without a key letter this will return (1,1) (if you didn't use a jumbled alphabet)
            likewise the letter Z will return (5,2)
            if you use the letter A as a key to encipher the letter Z, this will return (6,3)
        """
        if not letter in self.symbols:
            return (0,0)
        else:
            m, n = self.encipher_letter(key)
            return [ (i+1+m, j+1+n) for i in range(6) for j in range(6) if letter in self.polybius_square[i][j] ][0]
    
    def encipher_message(self,plaintext, key=""):
        ciphertext = ""
        _plaintext = "".join(plaintext.upper().split())
        if key: 
            ciphertext = " ".join([ "%d.%d"%(self.encipher_letter(_plaintext[i],key=key[i%len(key)])) for i in range(len(_plaintext))])
        else:
            ciphertext = " ".join([ "%d.%d"%(self.encipher_letter(_plaintext[i],key='')) for i in range(len(_plaintext))])
            
        return ciphertext


pb = PolybiusCipher()
print("A program that uses a Polybius Square to encipher messages")
pb.draw_polybius_square()
print()
plaintext = "This cipher uses a 6x6 square that includes letters and numbers"
key = "LEMON"
print("PLAINTEXT:\n\t %s"%(plaintext))
print("CIPHERTEXT (NO KEY):\n\t %s"%(pb.encipher_message(plaintext) ))
print("CIPHERTEXT (KEY: LEMON):\n\t %s"%(pb.encipher_message(plaintext, key = key) ))

