# Ruská Ruleta

Jedná se o jednoduchou hru Ruská ruleta vyvinutou pomocí Pygame. Hra simuluje revolver s jedním nábojem v cylindru, který se před každým kolem otočí. Hráč si může vybrat, zda chce otočit cylindrem nebo zmáčknout spoušť. Pokud je spoušť zmáčknuta a v komoře je náboj, hra končí. Cílem je nasbírat co nejvíce bodů před tím, než padne náboj.

## Herní Mechaniky

- **Fire** zmáčkne spoušť: 
1) Náboj není v komoře - hra pokračuje, přičítá se skóre
2) Náboj je v komoře - hra končí, hráč umírá
- **Spin** roztočí válec:
1) vybere náhodnou komoru

## Instalace

1. Ujistěte se, že máte nainstalovaný Python na svém systému.
2. Nainstalujte Pygame pomocí pip:
    ```bash
    pip install pygame
    ```
3. Naklonujte repozitář nebo stáhněte soubory hry.

## Soubory

všechny sprity a pozadí jsou moje vlastní:
- Obrázek pozadí: `bar.png`
- Obrázek revolveru: `revolver.png`
- Frames animace roztočení: `spin_1.png` až `spin_7.png`
- Obrázek záblesku: `flash.png`

- Zvukové efekty (stáhnuté z pixabay.com):
  - `gunshot.mp3`
  - `empty-gun-click.mp3`
  - `revolver-spin.mp3`
  - `ear-ringing-sound.mp3`