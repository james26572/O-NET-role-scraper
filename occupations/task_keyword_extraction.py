import openai
import time
openai.api_key = "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"

def extract_keywords(task):
    # Define the system message



    
    system_msg = 'You are a helpful assistant who understands job tasks.'

# Define the user message
    user_msg = f'''Extract the most important keywords from the following task: {task}.
    The output should be only be a list of tasks separated by commas, and just a single word
    if there is only one task.
'''
    retries = 3
    while retries > 0:
        try:
# Create a dataset using GPT
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                    request_timeout = 15,
                                                    temperature = 0,
                                                messages=[{"role": "system", "content": system_msg},
                                                {"role": "user", "content": user_msg}],
                                                )
            
            match = response["choices"][0]["message"]["content"]


            match
        except Exception as e:    
         if e: 
             print(e)   
             print('Timeout error, retrying...')    
             retries -= 1    
             time.sleep(5)    
         else:    
             raise e    
    print('API is not responding, moving on...')   
    
    return "didnt work"



task = "Generate standard or custom reports summarizing business, financial, or economic data for review by executives, managers, clients, and other stakeholders."
print(extract_keywords(task))