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
<<<<<<< HEAD
  print("This is palindrome")

else:
  print("This is not palindrome")  



=======
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
>>>>>>> 68397f6a0de1d237243434799073ee6563ace5ba
