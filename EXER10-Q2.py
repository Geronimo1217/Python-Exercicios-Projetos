num=int(input("Digite um numero :"))
par=0
impar=0
somap=0
somaimp=0
a=range(num)
for i in a:
    if num % 2 == 0:
        par += 1
        somap+=par
        print("A quantidade de par é {} O somatorio dos números PARES é {}".format(par, somap))
    else:
        impar += 1
        somaimp+=impar
        print("A quantidade de impar é {} O somatorio dos números IMPAR  é {}".format(impar, somaimp))




##for i==1; i<=num; i++;