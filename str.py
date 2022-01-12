def fun():
	i=0
	while i<1:
		n=int(input("enter the number :"))
		a=str(n)
		string=" "
		j=0
		while j<len(a):
			
			if a[j]=="1":
				string+="one"
			elif a[j]=="2":
				string+="two"
			elif a[j]=="3":
				string+="three"
			elif a[j]=="4":
				string+="four"
			elif a[j]=="5":
				string+="five"
			elif a[j]=="6":
				string+="six"
			elif a[j]=="7":
				string+="seven"
			elif a[j]=="8":
				string+="eight"
			elif a[j]=="9":
				string+="nine"
			elif a[j]=="0":
				string+="zero"
			else:
				pass
			j+=1
		i+=1
		return string

print(fun())