import random
import string

pass_len=8
char_values=string.ascii_letters+string.digits+string.punctuation



res="".join([random.choice(char_values) for i in range(pass_len)])
print("the raandom password is",res)
