from CORE.Speak import speak
import wolframalpha
wolframalpha_app_id = 'EJ3QJT-2YHHU3AYK7'

def calculate(query):
    client = wolframalpha.Client(wolframalpha_app_id)
    indx = query.lower().split().index('calculate')
    query = query.split()[indx + 1:]
    res = client.query(''.join(query))
    answer = next(res.results).text
    print("The answer is : " + answer)
    speak("The answer is " + answer)