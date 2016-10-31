17_sites_monitoring
===================

Скрипт проверяет состояние каждого сайта из файла, переданного в качестве обязательного параметра.

Пример использование
-----

```
~$ python3 check_sites_health.py site_list.txt
             URL                     200 OK                 Expiration date
 http://www.obrnadzor.gov.ru           Yes     Less than a month left or can't get it.      
      http://stat.edu.ru               Yes     Less than a month left or can't get it.      
      http://www.nica.ru               Yes                    01.11.2017                    
     http://www.lexed.ru               Yes                    17.04.2017                    
        http://www.ru                  Yes                    01.07.2017           
```
