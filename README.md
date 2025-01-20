# AOVV - Autonomous Avoiding Obstacles Robot

## Opis Projektu
AOVV to projekt autonomicznego robota zdolnego do unikania przeszkód (poruszającego się z punktu A do B), oparty na Raspberry Pi 4B jako głównym module sterującym. Robot wykorzystuje różnorodne sensory i algorytmy do realizacji zadań związanych z SLAM (Simultaneous Localization and Mapping) oraz autonomiczną jazdą.

## Aktualna zawartość repozytorium

Repozytorium (obecnie) zawiera kody źródłowe w Pythonie obsługujące następujące komponenty:

### Obsługa sensorów
- **LoRa**: Moduł komunikacji długodystansowej.
- **TB6612FNG**: Sterownik silników DC.
- **TCRT5000**: Czujnik linii do detekcji podłoża.
- **BNO085**: IMU (Inertial Measurement Unit) do pomiarów orientacji.

### Testowanie protokołów
- **SPI**: Kod testujący poprawność komunikacji w protokole SPI.
- **I2C**: Kod testujący poprawność komunikacji w protokole I2C.

### Główne zadania projektu
- Stworzenie AOVV

## Zadania poboczne projektu
- Tworzenie nodów dla czujników.
- integracja node'ów z czujników z głównym wątkiem.
- Implementacja głównego wątku obsługującego algorytmy SLAM i autonomiczną nawigację.

## Struktura katalogów
```
sensors_codes_python/
└── sensor-tests
    ├── bno085_rev0.py
    ├── env
    │   ├── bin
    │   ├── lib
    │   ├── lib64 -> lib
    │   └── pyvenv.cfg
    ├── lora_client_rev0
    ├── pySX127x
    │   ├── build
    │   ├── dist
    │   ├── LORA_CLIENT_encrypted.py
    │   ├── LORA_CLIENT.py
    │   ├── lora_sender.py
    │   ├── LORA_SERVER_encrypted.py
    │   ├── LORA_SERVER.py
    │   ├── lora_util.py
    │   ├── pyLoRa.egg-info
    │   ├── rx_cont.py
    │   ├── setup.py
    │   ├── socket_client.py
    │   ├── socket_transceiver.py
    │   ├── SX127x
    │   ├── test_lora.py
    │   └── tx_beacon.py
    ├── stan_dzialania_czujnikow_rev0.md
    ├── tb6612fng_rev0.py
    ├── tcrt5000_rev0.py
    └── test_dzialania_i2c_spi_rev0.py
```
W katalogu sensor_tests są obecnie zgromadzone kody pythonowe do testowania czujników, a także niezbędna pod SX127X oraz środowisko wirtualne pythona env do własnegio testowania kodów.

## Wymagania
UWAGA: Przed zainstalowaniem adafruit-blinka upewnij się że poprawnie skonfigurowałeś wszystkie interfejsy do pracy, ustawiłeś częstotliwość I2C na 400000Hz oraz poprawnie podłączyłeś wszystkie piny!
Automatyczny config interfejsów:
```
sudo raspi-config nonint do_i2c 0
sudo raspi-config nonint do_spi 0
sudo raspi-config nonint do_serial_hw 0
sudo raspi-config nonint do_ssh 0
sudo raspi-config nonint do_camera 0
sudo raspi-config nonint disable_raspi_config_at_boot 0
```

- **Python 3.8+**
- **Raspberry Pi 4B**
- Zainstalowane biblioteki:
  - `spidev`
  - `RPi.GPIO`
  - `pyLoRa` (i repo: https://github.com/rpsreal/pySX127x)
  - `i2c-tools libgpiod-dev python3-libgpiod`
  - `adafruit-blinka`
  - `adafruit-circuitpython-bno08x` 

## Instrukcja uruchomienia

1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/twoje-repozytorium/AOVV.git
   ```
2. Przejdź do katalogu projektu:
   ```bash
   cd AOVV
   ```
3. Uruchom wybrany skrypt, np. test komunikacji I2C i SPI:
   ```bash
   python sensors_codes_python/sensor-tests/test_dzialania_i2c_spi_rev0.py
   ```

## Plan rozwoju

- [ ] Napisanie node'ów do czujników na bazie python codes. 
- [ ] Dodanie algorytmu unikania przeszkód.
- [ ] Integracja SLAM z danymi z sensorów z node'ów.
- [ ] Optymalizacja sterowania silnikami.
- [ ] Instalacja zawieszenia oraz upgrade płytki PCB.
- [ ] Testy w środowisku rzeczywistym.

## Wsparcie
W razie problemów lub pytań, prosimy o kontakt poprzez zgłoszenie w sekcji [Issues](https://github.com/twoje-repozytorium/AOVV/issues).

## Licencja
Projekt jest udostępniany na licencji GNU GPL. Szczegóły znajdują się w pliku `LICENSE`.
