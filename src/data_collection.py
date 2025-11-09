import requests
import os

def fetch_recordings(species_name, country_code="united states", 
                     state="washington", call_type="call", max_results=200):
    """
    get metadata from xenocanto api
    """
    base_url = "https://xeno-canto.org/api/3/recordings"
    
    query_parts = [
        f'gen:"{species_name.split()[0]}"',
        f'sp:"{species_name.split()[1]}"',   
        f'cnt:"{country_code}"',
        f'type:{call_type}',
        'q:A',
    ]
    
    query = " ".join(query_parts)
    
    params = {
        'query': query,
        'key': 'api key', #PUT API KEY HERE
        'page': 1
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    return data
#get steller's jay recordings
data_SJ = fetch_recordings('Cyanocitta stelleri', "United States","call")
num_recordings = 0
with open('../data/raw/sj/stellersjay_metadata.txt', 'w') as file:
    num_recordings += int(data_SJ['numRecordings'])
    for i, recording in enumerate(data_SJ['recordings']):
        file.write(f"{i}: {recording}\n")
        with open(f'../data/raw/sj/sj_{i}.wav', 'wb') as f:
            audio = requests.get(recording['file'])
            f.write(audio.content)
print(f'Number of steller\'s jay recordings: {num_recordings}')

#get northern flicker recordings
data_NF = fetch_recordings('Colaptes auratus', "United States","call")
num_recordings = 0
with open('../data/raw/nf/northernflicke_metadata.txt', 'w') as file:
    num_recordings += int(data_NF['numRecordings'])
    for i, recording in enumerate(data_NF['recordings']):
        file.write(f"{i}: {recording}\n")
        with open(f'../data/raw/nf/nf_{i}.wav', 'wb') as f:
            audio = requests.get(recording['file'])
            f.write(audio.content)
print(f'Number of northern flicker recordings: {num_recordings}')

#get spotted towhee recordings
data_ST = fetch_recordings('Pipilo maculatus', "United States","call")
num_recordings = 0
with open('../data/raw/st/spottedtowhee_metadata.txt', 'w') as file:
    num_recordings += int(data_ST['numRecordings'])
    for i, recording in enumerate(data_ST['recordings']):
        file.write(f"{i}: {recording}\n")
        with open(f'../data/raw/st/st_{i}.wav', 'wb') as f:
            audio = requests.get(recording['file'])
            f.write(audio.content)
print(f'Number of spotted towhee recordings: {num_recordings}')

#get black capped chickadee
data_BCC = fetch_recordings('Poecile atricapillus', "United States","call")
num_recordings = 0
with open('../data/raw/bcc/blackcappedchickadee_metadata.txt', 'w') as file:
    num_recordings += int(data_BCC['numRecordings'])
    for i, recording in enumerate(data_BCC['recordings']):
        file.write(f"{i}: {recording}\n")
        with open(f'../data/raw/bcc/bcc_{i}.wav', 'wb') as f:
            audio = requests.get(recording['file'])
            f.write(audio.content)
print(f'Number of black-capped chickadee recordings: {num_recordings}')