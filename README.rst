=========
Įdiegimas
=========

Įsidiegiam reikiamus paketus::

    sudo apt-get install \
        mercurial \
        git-all \
        build-essential \
        python3

Nusiklonuojam saugyklą::

    git clone git@github.com:vakaras/nma-mailer.git

„Kompiliavimas“ (esant šakniniame saugyklos kataloge)::

    make

Testinio serverio paleidimas::

    make run

Interpretatoriaus paleidimas::

    make shell
    

========
Užduotys
========

1 žingsnis
==========

Parašyti procedūrą, kuri duotais elektroninio pašto adresais
išsiųstų gautą tekstą::

    def send(emails, text):
        ...

Taip pat realizuoti funkcionalumą iliuostruojančią svetainę.
