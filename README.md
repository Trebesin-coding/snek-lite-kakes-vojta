# Hodnocení:

Povedená hra a všechny dobrá práce!
Vtipný snake, za něj +.

V téhle části kódu se hodně věcí opakuje, nešlo by vytvořit funkci a vyhnout se tak opakovanému psaní stejného kódu? 🤔

```python


    if not green_coin_existence:
        green_coin_time += clock.get_time()
        if green_coin_time > 3000:
            green_coin_x = random.randint(0, screen_width - 40)
            green_coin_y = random.randint(0, screen_height - 40)
            green_coin_rect = green_coin_surf.get_rect(midbottom=(green_coin_x, green_coin_y))
            green_coin_existence = True
            green_coin_time = 0

    if green_coin_existence:
        green_coin_time_despawn += clock.get_time()
        if green_coin_time_despawn >= 2000:
            green_coin_x = (screen_width * 40)
            green_coin_y = (screen_height * 40)
            green_coin_rect = green_coin_surf.get_rect(midbottom=(green_coin_x, green_coin_y))
            green_coin_existence = False
            green_coin_time_despawn = 0



    if not gold_coin_existence:
        gold_coin_time += clock.get_time()
        if gold_coin_time >= gold_coin_time_spawn:
            gold_coin_x = random.randint(0, screen_width - 40)
            gold_coin_y = random.randint(0, screen_height - 40)
            gold_coin_rect = gold_coin_surf.get_rect(midbottom=(gold_coin_x, gold_coin_y))
            gold_coin_existence = True
            gold_coin_time = 0
            gold_coin_time_spawn = random.randint(10, 30) * 1000

    if gold_coin_existence:
        gold_coin_time_despawn += clock.get_time()
        if gold_coin_time_despawn >= 2000:
            gold_coin_x = (screen_width * 40)
            gold_coin_y = (screen_height * 40)
            gold_coin_rect = gold_coin_surf.get_rect(midbottom=(gold_coin_x, gold_coin_y))
            gold_coin_existence = False
            gold_coin_time_despawn = 0

```
