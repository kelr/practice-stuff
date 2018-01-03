import sys

class Substitute:
	def getValue(self, key, code):
		result = ""
		critical = ""
		critical = critical.join(i for i in code if i in code and i in key)
		for char in critical:
			if char in key:
				index = str(key.index(char) + 1)
				if index == "10":
					index = "0"
				result += index
		return int(result)

def main(argv):
	sub = Substitute()
	print(sub.getValue(sys.argv[1], sys.argv[2]))

if __name__ == '__main__':
	try:
		main(sys.argv[1:])
	except:
		print("Run with: python Substitute.py key code")
		print("key must be 10 chars long, Uppercase A-Z, unique")
		print("code must be 1-9 chars long, Uppercase A-Z")
		print("code must have one character that is also in key")
