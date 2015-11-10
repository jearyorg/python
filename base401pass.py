import base64
if __name__ == "__main__":
	files = open('result.txt', 'w')
	for u in open("user.txt"):			 
		for s in open("pass.txt"):			 
			files.write(base64.encodestring(u.strip()+":"+s.strip()))  			
			
