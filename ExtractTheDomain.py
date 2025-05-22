def domain_name(url):
    url = url.replace("www.", "")
    i = 0
    while url[i] not in ('/','.'):
        i += 1
    j = i + 1
    while url[j] != '.' and j < len(url) - 1:
        j += 1

    return url[i + 2: j] if url[i] == '/' else url[:i]
    


#this is the url of the kata: https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python

#this is a example of the input
print(domain_name("www.xakep.ru"))
        