import string
import random
from modules import stats

lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
digits = list(string.digits)
punc = list(string.punctuation)
mix = lower+upper+digits+punc
#characters_num = input("how many characters for the password :")
def gen(min_len=8,
	max_len=12,
	lower_percent=10,
	upper_percent=20,
	digits_percent=50,
	punc_percent=30,
	randomize=False):
 password=str()
 length=random.choice(range(min_len,max_len))
 if(randomize==True):
  password=str().join(random.sample(mix,length)) # Generating completly random password
 else:
  lp=round((lower_percent/100)*length) # Lower actual percent
  up=round((upper_percent/100)*length) # Upper actual percent
  dp=round((digits_percent/100)*length) # Digits actual percent
  pp=round((punc_percent/100)*length) # Punctuation actual percent
  password += str().join(random.sample(lower,lp))
  password += str().join(random.sample(upper,up))
  password += str().join(random.sample(digits,dp))
  password += str().join(random.sample(punc,pp))
  stat=stats.PasswordStats(password)
  strength=stat.strength()*100
 return password,round(strength)
if __name__=='__main__':
 print(gen(6))
