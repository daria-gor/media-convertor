![Docker Compose Actions Workflow](https://github.com/daria-gor/transcoder/workflows/Docker%20Compose%20Actions%20Workflow/badge.svg?branch=master)
## Transcoder 
### Минимальный каркас простого микросервисного приложения Python + Minio + FFMPEG + Docker

Источником аудиофайлов является **inbucket** каталог в MINIO, выходные файлы перемещаются в **outbucket**
> После преобразования исходные файлы удаляются

Процесс работает в бесконечном цикле, в **inbucket** можно добавлять файлы

### Схема взяимодействия контейнеров :

CORE <--> MINIO 

- **.env** - содержит все переменные окружения доступные всем контейнерам (Core / MINIO), а также задается значение битрейта выходных аудиофайлов
- **build.sh** - запускает **docker-compose.yml** 
- **purge.sh** - останавливает **docker-compose.yml** и удаляет все образы и тома связанные со сборкой. 
Это полезно при изменении кода и значений в **.env** файле.
- обратите внимание что внутри докера хосты доступны по именам указанным в **docker-compose.yml** например **minio**


