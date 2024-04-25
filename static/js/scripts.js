document.getElementById('fileButton').addEventListener('click', function()
{
    document.getElementById('image').click();
});


url_photo = ''

//Функция для отправки фото на сервер;
function send_img(){ //Срабатывает по клику на кнопку "Отправить"
    let img = document.getElementById('image');
    
    let file = img.files[0];
    let fileName = file.name; //Имя файла
    console.log(fileName);

    //Такой формат, чтобы отправить фотку на сервер;
    let formData = new FormData();
    formData.append('image', file);

    //Запрос на сервер
    let xhr = new XMLHttpRequest();
    xhr.open('POST', '/sendImg');
    //Обработка ответа
    xhr.onload = function() {
        if (xhr.status === 200) {
            console.log('Чета ответил');
            
            let json = JSON.parse(xhr.responseText);

            let for_send = document.getElementById('MyId');
            for_send.style.backgroundImage = "url('" + json['path2img'] + "')";
            url_photo = "url('" + json['path2img'] + "')";
            for_send.style.backgroundSize = "cover"; // Устанавливаем размер фона, чтобы он покрывал весь элемент
            for_send.style.backgroundPosition = "center"; // Центрируем фон

   

            let link = document.getElementById('url')
            url.style.display = "block" 

            url_photo = url_photo.replace(/url\(['"]?(.*?)['"]?\)/, '$1');
            link.setAttribute('href', url_photo)
            link.setAttribute('download', 'ready_photo.png')
            

        } else {
            console.log('Не удачно');
        }
      };
    xhr.send(formData);
}