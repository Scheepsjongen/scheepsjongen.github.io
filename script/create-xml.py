#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import xml.etree.ElementTree as ET
from xml.dom import minidom

import re

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/documents.readonly']

# The ID of a sample document.
DOCUMENT_ID = '1-CV_PGPRQ9QWrslMaCJbxLHn9GhvErrBrSgiA6M_ieE'
# DOCUMENT_ID = '1gDsQwSv-APA2_xm4aRiXAObV4j01vHb_-WQniYQ3jLk'

def main():
    """Shows basic usage of the Docs API.
    Prints the title of a sample document.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('docs', 'v1', credentials=creds)

    # Retrieve the documents contents from the Docs service.
    document = service.documents().get(documentId=DOCUMENT_ID).execute()

    
    content = document.get('body').get('content')
    ps = (p.get('paragraph') for p in content if p.get('paragraph') != None)

    rg = re.compile(r'^((\d+)\.\s?)?(.*)')
    i = 0
    s = ''
    lastQuestion = -1
    mode = ''
    question = None

    root = ET.Element('section', 
                        {
                            "class":"quiz", 
                            "data-title":"Scheepsjongen", 
                            "data-subtitle":"Тест для перевірки теоретичних знань кандидатів на отримання посвідчення судноводія малого/маломірного судна (unofficial)"
                        })

    rgx = re.compile(r'\(\s*Правильна Відповідь\s*\)', re.IGNORECASE)

    def writeElement(s, question):
        if s != '' and int(lastQuestion ) > 170: 
            if mode == 'question':
                question = ET.SubElement(root, 'section', {'class': 'question', 'number': '1.' + str(lastQuestion)})
                txt = ET.SubElement(question, 'section', {'class': 'text'}) 
            else:
                answer = ET.SubElement(question, 'section', {'class': 'answer'})
                txt = ET.SubElement(answer, 'section', {'class': 'text'}) 

                if rgx.search(s):
                    answer.attrib['data-correct'] = 'data-correct'
                    s = rgx.sub('', s)

            txt.text = s

        return question

    for p in ps:
        for e in p.get('elements'):
            t = e.get('textRun')
            if t != None:
                c = t.get('content').strip()
                i = i + 1
                if c == '': continue
                qn = rg.match(c)

                if qn is not None:
                    currentQuestion = qn.group(2)
                    if currentQuestion == None or int(currentQuestion) < int(lastQuestion): 
                        s = s + ' ' + c
                        continue

                    question = writeElement(s, question)

                    s = qn.group(3)

                    if currentQuestion != lastQuestion:
                        lastQuestion = currentQuestion
                        mode = 'question'
                    else:
                        mode = 'answer'
    writeElement(s, question)

    xml = ET.tostring(root, 'utf-8')
    new_xml = minidom.parseString(xml).toprettyxml(indent='   ')

    with open('../quiz/pre-2021-test.xml', 'w') as f:
        f.write(new_xml)

if __name__ == '__main__':
    main()
