print('''
 ___  _   _  ____  _  _  __    _  _  ___  _   _ 
/ __)( )_( )(_  _)( \/ )/__\  ( \( )/ __)( )_( )
\__ \ ) _ (  _)(_  \  //(__)\  )  ( \__ \ ) _ ( 
(___/(_) (_)(____)  \/(__)(__)(_)\_)(___/(_) (_)
                                                 ''')

print("IP \t          Date time \t          Request \t")

with open("website.log", "r") as f:
    lines= f.readlines()
with open("output.txt", 'w+') as nf:
    for line in lines:  
         line= line.split(" ")
         nf.write("{} \t {} \t {}\t\n" .format(line[0], line[3].replace('[',' '), line[5].replace('"', ' ')))

