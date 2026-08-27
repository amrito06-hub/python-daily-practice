word = input("Enter a word: ")
start = 0
end = len(word) - 1
reverse = True

while start < end:
    if word[start] != word[end]:
        reverse = False
        break

    start += 1
    end -= 1

if(reverse):
  print("This is palin")

else:
  print("This is not palin")  


"""word = input("Enter a Name: ")

start = 0
end = len(word) - 1

reverse = True

while start < end :
    if word[start] != word[end]:
        reverse = False
        break

    start += 1
    end -= 1

if(reverse):
    print("This is Palindrom")

else:
    print("This is not Palindrom") """
