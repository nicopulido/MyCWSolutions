def domain_name(url):
    i = 1
    while url[-i] != '.':
        i += 1
    j = i + 1
    while url[-j] not in ('/','.'):
        j += 1
    
    return url[-j + 1:-i]


#this is the url of the kata: https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python

#this is a example of the input
print(domain_name("https://hyphen-site.org"))
        