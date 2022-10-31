alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# combine encrypt and decrypt functions into single function called caesar
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for letter in start_text:
    new_position = position + shift_amount
    position = alphabet.index(letter)
    end_text += alphabet[new_position]
  print(f"The {cipher_direction}d text is {end_text}")

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)


# # encrypt function 
# def encrypt(plain_text, shift_amount):
#   cipher_text = ''
#   for char in plain_text:
#     # shift forward
#     for i, letter in enumerate(alphabet):
#       if char == letter:
#         if i + shift_amount > 26:
#           cipher_text += alphabet[i + shift_amount - 26]
#         else:
#           cipher_text += alphabet[i + shift_amount]
#   print(f"the encoded text is {cipher_text}")

# test encrypt function
# encrypt(plain_text="zulu", shift_amount=5) 

# decrypt function
# def decrypt(cipher_text, shift_amount):
#   plain_text = ''
#   for char in cipher_text:
#     # shift back
#     for i, letter in enumerate(alphabet):
#       if char == letter:
#         if i - shift_amount < 0:
#           plain_text += alphabet[26 + i - shift_amount]
#         else:
#           plain_text += alphabet[i - shift_amount]

#   print(f"the decoded text is {plain_text}")

# test decrypt
# decrypt(cipher_text="mjqqt", shift_amount=5)









# alt method for index (encrypt)
# for letter in plain_text:
  # position = alphabet.index(letter)
  # new_position = position + shift_amount
  # new_letter = alphabet[new_position]
  # cipher_text += new_letter

