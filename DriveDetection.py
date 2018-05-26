import os

ALPHABET = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
DRIVES = []

def main():
	for l in range(6):
		for i in ALPHABET:
			try:
				if os.chdir(i+':'):
					print('aYY')
			except:
				ALPHABET.remove(i)
	DRIVES.append(ALPHABET)
	return(DRIVES)

if __name__ == '__main__':
	main()
