import requests


# a=requests.get("https://www.google.com/search?q=ind+vs+aus&rlz=1C1GCEA_enIN1017IN1017&oq=&gs_lcrp=EgZjaHJvbWUqCQgDECMYJxjqAjIJCAAQIxgnGOoCMgkIARAjGCcY6gIyCQgCECMYJxjqAjIJCAMQIxgnGOoCMgkIBBAjGCcY6gIyCQgFECMYJxjqAjIJCAYQIxgnGOoCMgkIBxAjGCcY6gLSAQk0MDIwajBqMTWoAgiwAgE&sourceid=chrome&ie=UTF-8#sie=m;/g/11v13jnlwd;5;/m/021vk;dt;fp;1;;;")
# print(a.text)


#postMethod
data={
    'title': "tanaya",
    'age':'20'
}
url="https://www.google.com/search?q=ind+vs+aus&rlz=1C1GCEA_enIN1017IN1017&oq=&gs_lcrp=EgZjaHJvbWUqCQgDECMYJxjqAjIJCAAQIxgnGOoCMgkIARAjGCcY6gIyCQgCECMYJxjqAjIJCAMQIxgnGOoCMgkIBBAjGCcY6gIyCQgFECMYJxjqAjIJCAYQIxgnGOoCMgkIBxAjGCcY6gLSAQk0MDIwajBqMTWoAgiwAgE&sourceid=chrome&ie=UTF-8#sie=m;/g/11v13jnlwd;5;/m/021vk;dt;fp;1;;;"
a=requests.post(url,json=data)

print(a.text)
