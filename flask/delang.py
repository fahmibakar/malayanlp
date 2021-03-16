import malaya
# import docx
import json

from flask import Flask, jsonify, request, Response
app = Flask(__name__)

total = {}
italic = []

@app.route('/', methods=['GET'])
def show_pydocs():
   # checking_language_italic()
   error = []
   eng = False
   italic = ""
   page = ""

   i = 0
   count = len(total)

   while i < count:

      obj = total[i]
      for key in obj:
         if key ==  "Page":
            page = obj[key]
         if key == "italic":
            italic = obj[key]
         if key == "text":
            deep = malaya.language_detection.deep_model()
            naive = malaya.stem.naive()
            for word in obj[key].split():
               stem = naive.stem_word(word)
               detect = deep.predict([stem])
               if 'manglish' in detect or 'eng' in detect:
                  if italic == "no":
                     item = {"text": obj[key]}
                     item["language"] = "ENG"
                     item["page"] = page
                     error.append(item)

               # if 'malay' in detect or 'ind' in detect or 'other' in detect or 'rojak' in detect:
               #    if italic == "yes":
               #       item = {"text": obj[key]}
               #       item["language"] = "MALAY"
               #       item["page"] = page
               #       error.append(item)


      i = i + 1

   return jsonify(error)

@app.route('/', methods=['POST'])
def add_line():
   global total
   try:
      total = request.get_json()
      response = Response("OK", 201, mimetype='application/json')
      # if checking_language_italic(request_data):
      print(total)
      return response
   except:
      print ('error')

if __name__ == '__main__':
   app.run(port=4000, debug = True, use_reloader=True)