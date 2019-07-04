# Polybius-square

* An implementation of a polybius square in Python 3

* Uses a 6x6 Polybius Square that includes letters and numbers:

|x|1|2|3|4|5|6|
|---|---|---|---|---|---|---|
|**1**|P|O|L|Y|B|I|
|**2**|U|S|Q|A|R|E|
|**3**|2|0|1|9|C|D|
|**4**|F|G|H|J|K|M|
|**5**|N|T|V|W|X|Z|
|**6**|3|4|5|6|7|8|

* You can choose to include a keyword with the letters
    * For example, if you encipher the letter A on it's own, you will get the result **2.4**
    * Likewise if you encipher the letter K on it's own you will get **4.6**
    * if you encipher the letter A with the key K you will get **6.10**
    
* 


* PLAINTEXT:  
```
  This cipher uses a 6x6 square that includes letters and numbers
```
  
* CIPHERTEXT (NO KEY):
```
  5.2 4.3 1.6 2.2 3.5 1.6 1.1 4.3 2.6 2.5 2.1 2.2 2.6 2.2 2.4 6.4 5.5 6.4 2.2 2.3 2.1 2.4 2.5 2.6 5.2 4.3 2.4 5.2 1.6 5.1 3.5 1.3 2.1 3.6 2.6 2.2 1.3 2.6 5.2 5.2 2.6 2.5 2.2 2.4 5.1 3.6 5.1 2.1 4.6 1.5 2.6 2.5 2.2
```
    
* CIPHERTEXT (KEY: **LEMON**):
```
  6.5 6.9 5.12 3.4 8.6 2.9 3.7 8.9 3.8 7.6 3.4 4.8 6.12 3.4 7.5 7.7 7.11 10.10 3.4 7.4 3.4 4.10 6.11 3.8 10.3 5.6 4.10 9.8 2.8 10.2 4.8 3.9 6.7 4.8 7.7 3.5 3.9 6.12 6.4 10.3 3.9 4.11 6.8 3.6 10.2 4.9 7.7 6.7 5.8 6.6 3.9 4.11 6.8
```
