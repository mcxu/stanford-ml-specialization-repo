opinion_count = 0
max_opinion = 5

# while max_opinion >= opinion_count:
#     if max_opinion > opinion_count:
#         your_opinion = input("\nwhats your opinion? : ")
#         # with open ('your_opinion.txt', 'a') as your_opinion_txt:
#         #     your_opinon_txt.write(f"{your_opinion}\n")
#         print("written the message to file: ", your_opinion)
#         opinion_count += 1
#     else:
#         break 


while max_opinion > opinion_count:
    your_opinion = input("\nwhats your opinion? : ")
    # with open ('your_opinion.txt', 'a') as your_opinion_txt:
    #     your_opinon_txt.write(f"{your_opinion}\n")
    print("written the message to file: ", your_opinion)
    opinion_count += 1


