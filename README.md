# Project3
'''
notes on the process:

step 1. I downloaded my info from Hinge

step 2. clean hinge info. I changed JSON to CSV and ordered the rows by time (so the chats made more sense). For reference, the chats only include my side of each conversation.

step 3. connect w API (dictionary) and deepseek. This part took a lot of tries. First, I had issues with runtime because I was calling deepseek and the dictionary for every single coversation. It was taking forever to load, so I changed it so that they were called less frequently (every week). Second, the dictionary API does not contain definitions for words like and/for/to/etc. My program retrieved definitions of words in order to determine if a word was standard english or not. The idea was to identify slang or abbreviations. However, since transitional words were not included in the dictionary, they were being included in 'top_unknown_words', where I was trying to isolate slang. Hardcoding it did not solve the issue, but since the block had taken so long to run, I decided to fix the issue in processing instead of during the API calls.
'''
