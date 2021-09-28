def isPalindrome(s):

	def toChars(s):
		s = s.lower()
		ans = ''
		for c in s: 
			if c in 'abcdefghijklmnopqrstuvwxyz':
				ans = ans + c
		return ans

	def isPal(s):
		if len(s) <= 1:
			return True
		else:
			# GET THE END OF THE ARRAY
			print(s[0], s[-1])
			# SLICE THE ENDS OFF
			print(s[1:-1])
			return s[0] == s[-1] and isPal(s[1:-1])

	return isPal(toChars(s))

print(isPalindrome('saippuakivikauppias'))

