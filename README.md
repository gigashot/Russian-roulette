# Ruská Ruleta

Jedná se o jednoduchou hru Ruská ruleta vyvinutou pomocí Pygame. Hra simuluje revolver s jedním nábojem v cylindru, který se před každým kolem otočí. Hráč si může vybrat, zda chce otočit cylindrem nebo zmáčknout spoušť. Pokud je spoušť zmáčknuta a v komoře je náboj, hra končí. Cílem je nasbírat co nejvíce bodů před tím, než padne náboj.

## Funkce

- **Hlavní Menu:** Úvodní obrazovka s názvem hry, zprávou a výzvou ke spuštění hry.
- **Herní Mechanika:** Možnost otočení cylindru nebo zmáčknutí spouště.
- **Animace:** Vizuální animace pro otočení cylindru a zmáčknutí spouště.
- **Zvukové Efekty:** Realistické zvukové efekty pro otočení cylindru, zmáčknutí prázdné spouště a výstřel.
- **Sledování Skóre:** Hra sleduje a zobrazuje skóre na základě počtu úspěšných zmáčknutí spouště bez nárazu na náboj.

## Instalace

1. Ujistěte se, že máte nainstalovaný Python na svém systému.
2. Nainstalujte Pygame pomocí pip:
    ```bash
    pip install pygame
    ```
3. Naklonujte repozitář nebo stáhněte soubory hry.

## Soubory

Ujistěte se, že následující soubory jsou k dispozici ve složce `assets`:
- Obrázek pozadí: `bar.png`
- Obrázek revolveru: `revolver.png`
- Rámy animace otočení: `spin_1.png` až `spin_7.png`
- Obrázek záblesku: `flash.png`
- Zvukové efekty:
  - `gunshot.mp3`
  - `empty-gun-click.mp3`
  - `revolver-spin.mp3`
  - `ear-ringing-sound.mp3`

## Spuštění Hry

Pro spuštění hry spusťte skript `main.py`:
```bash
python main.py
```