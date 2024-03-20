# Niezawodnośc i diagnostyka układów cyfrowych 2 - projekt
Projekt studencki temat: Transmisja w systemie FEC

# Instrukcja Github dla PyCharm

- ## Pobranie repozytorium
Repozytorium jest publiczne dlatego można skorzystać z uproszczonej wersji pobierania (polecam)

        1. Włączyć PyCharm
        2. Nowy projekt -> Get From VCS
        3. Repository URL
        4. https://github.com/cholewakrzysztof/niduc-projekt
        5. Trust Projekt
        6. GOTOWE! 

- ## Tworzenie nowej wersji kodu (Branch)
Najlepiej będzie, jeżeli każdy będzie lokalnie tworzył oddzielnego brancha (zawsze na podstawie main), tak żeby trzymac u siebie rozkopaną wersje kodu, a na Gicie działającą. To wymaga kroków:

### Rozpoczęcie pracy

Przed stworzeniem nowej wersji trzeba upewnić się, że mamy najnowszą wersje z Gita
        1. W głównym menu wybieramy Git
        2. Klikamy Pull

Potem można tworzyć nową wersję lokalną

        1. W PyCharm na górnym pasku klikamy main
        2. W liście RECENT
        3. main
        4. New Branch from 'main'
        5. Wybieramy nazwe (najlepiej to co chcemy dodać)
        6. Zaznaczamy Checkout branch!
        7. Dodajemy kod i bawimy się na lokalnej wersji kodu
        (UWAGA bez zrobienia pierwszego commitu jak bedziemy się przełączać to będzie wyglądało jakbyśmy chcieli dodać pliki do brancha main)

### Praca
Z każdą zmianą warto zapisywać wersje kodu;
        1. Najpierw upewnić się, że wszystkie zmiany są potwierdzone 
            a. Po lewej stronie menu kreska z kropką (Commit)
            b. Zaznaczamy jakie pliki chcemy zaktualizować
            c. Dodajemy opis co zmieniamy
            d. Klikamy COMMIT AND PUSH
            e. Albo COMMIT a na koniec pracy PUSH

### Koniec pracy

Kiedy uznamy, że to co chcieliśmy dodać jest gotowe trzeba dokonać scalenia wersji (tej, która działa i jest na Gicie z tą, którą naklepaliśmy lokalnie na komputerze). Jednak, żeby nie było chaosu proponuje działać na PULL REQUESTACH, czyli wystawiamy prośbę, że chcemy dodać nasz kod do wersji która mamy na Gicie. Wtedy inni mogą podejrzeć co dodaliśmy (przelecieć oczami nazwy funkcji), ewentualnie powiedzieć co jest źle, czego nie rozumieją. Sprawi to, że każdy będzie mógł osobno działac na kodzie i nie będzie trzeba tłumaczyć sobie nawzajem co się dzieje

    1. Po lewej stronie klikamy ikonke z trzema kropkami i strzałką (Pull Requests)
    2. Po prawej u góry plus 
    3. Dodajemy nazwe PR, najlepiej co się zmieni
    4. Klikamy Create Pull Request
    5. Na GitHubie w zakładce Pull Request pojawi się nasz PR, możemy go podejrzeć. Najważniejsze to Files Changed
    6. Po tym jak ktoś zatwierdzi (Merge), w prawym górnym rogu na Github pojawi się fioletowy napis Merged -> wtedy mozna bezpiecznie usunąć branch (mogę się tym zajmować)
    7. Gdy branch zostanie usunięty można usunąc go lokalnie
        a. Checkout main
        b. Stary branch -> delete
        c. Można zrobić Pull będąc na branchu main


## Przydatne linki
- [[Dokumentacja projektowa]](https://politechnikawroclawska-my.sharepoint.com/:w:/g/personal/255388_student_pwr_edu_pl/EZ0jKhnu6CZEjW8B8oB3LSgBG8Bsag9R6G1qytx9Ozjwag?e=rbccZR&fbclid=IwAR279Xb0qSu60lP9wBdzZDmErzNBe9KSR_hIWR8m9qfqn9e3y_x5Dk2364w)

- [[Organizacja zajęć (E-portal)]](https://eportal.pwr.edu.pl/pluginfile.php/341197/mod_resource/content/2/Niezawdno%C5%9B%C4%87%20i%20diagnostyka%20-%20projekt.pdf)

- [[Biblioteka komm Python]](https://pypi.org/project/komm/)


