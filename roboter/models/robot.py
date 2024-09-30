import os
import sys
import csv
import string
sys.path.append("roboter")

from views import console

sys.path.append(os.path.join(os.path.dirname(__file__), 'package/package_requests'))

import requests

class Robot(object):

    def __init__(self, speak_color="green"):
        self.speak_color = speak_color

    def apiRequests(self, book_name):
        payload = {'q': book_name}
        response = requests.get('https://www.googleapis.com/books/v1/volumes', params=payload)

        if response.status_code == 404:
            template = console.get_template('noneResult.txt', self.speak_color)
            print(template)
        
        if response.status_code == 200:
            template = console.get_template('save.txt', self.speak_color)
            template = string.Template(template)
            result = response.json()
            result_total = result['totalItems']
            answer = input(template.substitute({
                'result_count': result_total
            }))

            while not answer:
                template = console.get_template('noneAnswer.txt', self.speak_color)
                answer = input(template)
                
            if answer == 'Yes':
                with open('roboter/result.csv', 'w', newline='') as csv_w_file:
                    fieldnames = ['ID', 'ETAG', 'SELFLINK', 'TITLE', 'AUTHORS', 'DESCRIPTION', 'PUBLISHDATE']
                    writer = csv.DictWriter(csv_w_file, fieldnames=fieldnames)
                    writer.writeheader()

                    data_box = console.resultReturn(result)
                
                    writer.writerows(data_box)
                    print('CSVを生成しました。')

            elif answer == 'No':
                print('終了します。')
    
    def question(self):
        template = console.get_template('question.txt', self.speak_color)
        book_name = input(template)
        
        while not book_name:
            book_name = input(template)

        self.apiRequests(book_name)
