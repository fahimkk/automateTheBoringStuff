""" start = time.time()
num_iteration = 1

for password in password_list:
    if pdf_read.decrypt(password):
        print(password)
        break
    elif pdf_read.decrypt(password.lower()):
        print(password.lower())
        break
    num_iteration += 1
end= time.time()
print(num_iteration)
print(end - start) """