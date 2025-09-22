# Project3
I used dictionaryapi.dev and DeepSeek to enhace a chat dataset downloaded from Hinge. 

Notes on the process:

Step 1. Dataset aquisition. I downloaded data from Hinge. All chat data is included in prompts.json. 

Step 2. Data cleaning. I used pandas to covert the JSON file to a CSV file, then  ordered the rows by time (so the chats could be read in chronological order). 

Step 3. Connect w the API (dictionary) and DeepSeek. This part took a lot of tries. First, I had issues with runtime because I was calling DeepSeek and the dictionary API for every single coversation. It was taking forever to load, so decreased the frequency to weekly. Second, the dictionary API does not contain definitions for words like and/for/to/etc. In order to identify slang or abbreviations, my program retrieved the definition of each word in a given message. If a definition was found, the word was assumed to be 'standard english'. Words without definitions were identified as outside standard english. (Note: this strategy is not perfect and probably overcounts nonstandard words, ex: typos). Since transitional words were not included in the dictionary API, they were being included in 'top_unknown_words', where I was trying to isolate slang. Hardcoding it did not solve the issue, but since the block had taken so long to run, I decided to fix the issue in processing instead of during the API calls. 

Together, the dictionary API and DeepSeek add another level of analysis of writing style in informal settings. The new dataset could be used to gain insights on the role of abbreviations, the level of sophistication, and common themes / topics of conversation in informal chat conversations. 
