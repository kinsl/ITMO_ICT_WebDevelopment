# Задание №1

???+ question "Задание"

    Реализовать клиентскую и серверную часть приложения. Клиент отсылает серверу
    сообщение «Hello, server». Сообщение должно отразиться на стороне сервера.
    Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение должно
    отобразиться у клиента.

    Обязательно использовать библиотеку `socket`  
    Реализовать с помощью протокола UDP

=== "Сервер"

    ```Python title="server.py"
    --8<-- "laboratory_work_1/task1/server.py"
    ```
    
    - Создаём объект сокета с помощью `#!py3 socket.socket(socket.AF_INET, socket.SOCK_DGRAM)`, 
    где `socket.AF_INET` отвечает за IPv4, а `socket.SOCK_DGRAM` за протокол UDP.
    - Задаём `.timeout`, чтобы дать возможность программе поймать ++ctrl+c++.
    - С помощью `.recvfrom` получаем данные и адрес клиента, а с помощью `.sendto` возвращаем ответ.
    - Оборачиваем полученный код в `#!py3 try-except socket.timeout`, чтобы таймаут не завершил работу сервера.
    - Оборачиваем этот `#!py3 try-except` в цикл `#!py3 while True`, 
    чтобы сервер не прекратил работу после обработки первого запроса.
    - Оборачиваем цикл в `#!py3 try-except KeyboardInterrupt`, чтобы можно было завершить работу сервера по нажатию на ++ctrl+c++.

    <p align="center">
      <img src="https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/lw1/task1/server_console.png" alt="server_console.img"></a>  
      Консоль сервера
    </p>

=== "Клиент"

    ```Python title="client.py"
    --8<-- "laboratory_work_1/task1/client.py"
    ```

    - Создаём объект сокета с помощью `#!py3 socket.socket(socket.AF_INET, socket.SOCK_DGRAM)`, 
    где `socket.AF_INET` отвечает за IPv4, а `socket.SOCK_DGRAM` за протокол UDP.
    - С помощью `.sendto` отправляем запрос серверу, а с помощью `.recvfrom` получаем ответ.
    
    <p align="center">
      <img src="https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/lw1/task1/client_console.png" alt="client_console.img"></a>  
      Консоль клиента
    </p>