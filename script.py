

names = ["keba", "tokyo", "jozi"]

emailDomain = ["gamail", "outlook", "yahoo"]

emails = []

arr = tuple(zip(names, emailDomain))

print(arr)

for name, domain in zip(names, emailDomain):
    emails.append(f'{name}@{domain}.com')


print('\n', emails)
