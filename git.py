import requests
from bs4 import BeautifulSoup

def get_antutu_score(processor_name):
    search_url = f"https://unite4buy.com/cpu/{processor_name.replace(' ', '-')}/"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        score_element = soup.find("div", class_="cpu-an-tutu-score")
        
        if score_element:
            score = score_element.text.strip()
            return f"{processor_name} AnTuTu Score: {score}"
        else:
            return f"AnTuTu score for {processor_name} not found."

    except requests.exceptions.RequestException as e:
        return f"Error fetching data: {e}"

# Example Usage
processors = ["MediaTek Dimensity 7200", "Qualcomm Snapdragon 870"]
for processor in processors:
    print(get_antutu_score(processor))
