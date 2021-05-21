# 1.1: Getting started

```
$ docker ps -a
CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS                      PORTS     NAMES
8d2c21afd783   nginx     "/docker-entrypoint.…"   About a minute ago   Exited (0) 37 seconds ago             objective_haslett
0e0ebb7fe4fc   nginx     "/docker-entrypoint.…"   2 minutes ago        Exited (0) 23 seconds ago             sharp_hopper
75e6c5060929   nginx     "/docker-entrypoint.…"   2 minutes ago        Up 2 minutes                80/tcp    xenodochial_hofstadter

```


# 1.2: Cleanup

```
$ docker ps -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

$ docker images
REPOSITORY   TAG       IMAGE ID   CREATED   SIZE

```

# 1.3: Secret message

```
$ docker exec -it b02d bash

root@b02d609f738d:/usr/src/app# tail -f ./text.log
Secret message is: 'You can find the source code here: https://github.com/docker-hy' 
2021-05-18 15:29:38 +0000 UTC
2021-05-18 15:29:40 +0000 UTC
2021-05-18 15:29:42 +0000 UTC
2021-05-18 15:29:44 +0000 UTC
2021-05-18 15:29:46 +0000 UTC
Secret message is: 'You can find the source code here: https://github.com/docker-hy' 
2021-05-18 15:29:48 +0000 UTC
2021-05-18 15:29:50 +0000 UTC
```

# 1.4: Missing dependencies

```
$ docker run -d -it --name test ubuntu
$ docker exec -it test bash

root@eb6af7b3a7fa:/# apt update
root@eb6af7b3a7fa:/# apt install curl

$ docker exec -it test sh -c 'echo "Input website:"; read website; echo "Searching.."; sleep 1; curl http://$website;'

Input website:
helsinki.fi
Searching..
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>301 Moved Permanently</title>
</head><body>
<h1>Moved Permanently</h1>
<p>The document has moved <a href="http://www.helsinki.fi/">here</a>.</p>
</body></html>

```

# 1.5: Sizes of images

```
$ docker images
devopsdockeruh/simple-web-service   ubuntu    4e3362e907d5   2 months ago   83MB     
devopsdockeruh/simple-web-service   alpine    fd312adc88e0   2 months ago   15.7MB  

$ docker run -d -it fd3
116189bccedeccbb456887d3b0bd2527484891db3232892f324f127ba8383396

$ docker exec -it 116 sh 

/usr/src/app # tail -f ./text.log
2021-05-18 18:38:39 +0000 UTC
2021-05-18 18:38:41 +0000 UTC
Secret message is: 'You can find the source code here: https://github.com/docker-hy' 
2021-05-18 18:38:43 +0000 UTC
```

# 1.6: Hello Docker Hub

```
$ docker run -it devopsdockeruh/pull_exercise

Status: Downloaded newer image for devopsdockeruh/pull_exercise:latest
Give me the password: basics
You found the correct password. Secret message is:
"This is the secret message"
```

# 1.9: Volumes

```
$ docker run -v "$(pwd)/text.log:/usr/src/app/text.log" devopsdockeruh/simple-web-service
```