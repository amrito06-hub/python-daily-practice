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
  print("This is palindrome")

else:
  print("This is not palindrome")  



