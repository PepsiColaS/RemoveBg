from flask import Flask, render_template, request, send_from_directory
from PIL import Image
from script_rm import remove_bg

app = Flask(__name__)

@app.route('/sendImg', methods=['POST'])
def upload_image():
  if request.method == 'POST':
    image = request.files['image']
    img = Image.open(image)
    img.save("static/downlds/"+image.filename)

    new_img = remove_bg(image.filename)
    print(new_img)
    #image.filename #Название файла
    #Наверное полученные фотки можно не сохранять, а сразу загонять в скрипт для обработки
    #return send_from_directory('ready_img', new_img.split('/')[1])
    return {"response":"ответ", "path2img":new_img}, 200

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

# fgfg
# fgfg