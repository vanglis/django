#!/usr/bin/env python
#-*-coding:utf-8-*-
#author:PF.W

import rsa,base64 

def create_rsakey():
	(pubkey,privkey) = rsa.newkeys(1024)
	with open('PubKey.pem','w+') as pub:
		pub.write(pubkey.save_pkcs1().decode())
	with open('PriKey.pem','w+') as pri:
		pri.write(privkey.save_pkcs1().decode())

def encryption(strs): #RSA加密 
	PubKey = open('PubKey.pem','rb').read()
	pub_key = rsa.PublicKey.load_pkcs1(PubKey) 
	rsa_encrypt = rsa.encrypt(strs.encode(encoding="utf-8"),pub_key)
	A = lambda self,x,n:x if n<=0 else self(self,base64.standard_b64encode(x),n=n-1)
	base_encrypted =  A(A,rsa_encrypt,3)
	return base_encrypted

def decryption(strs): #RSA加密 
	PriKey = open('PriKey.pem','rb').read()
	pri_key = rsa.PrivateKey.load_pkcs1(PriKey) 
	A = lambda self,x,n:x if n<=0 else self(self,base64.standard_b64decode(x),n=n-1)
	base_decrypted = A(A,strs,3) 
	strs = rsa.decrypt(base_decrypted,pri_key).decode()
	return strs



if __name__ == '__main__':
	strs = 'abc1234566'
	print (encryption(strs))
	print (decryption(encryption(strs)))
	
