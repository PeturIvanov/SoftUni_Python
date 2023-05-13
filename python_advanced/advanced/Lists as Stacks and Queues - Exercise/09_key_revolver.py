from collections import deque

bullet_price = int(input())

gun_barrel_max = int(input())

gun_barrel = gun_barrel_max

bullets = deque([int(b) for b in input().split()])

locks = deque([int(l) for l in input().split()])

intelligence_value = int(input())

bullets_shot = 0
while locks and bullets:
    current_lock = locks.popleft()
    current_bullet = bullets.pop()

    gun_barrel -= 1
    bullets_shot += 1

    if current_bullet > current_lock:
        print("Ping!")
        locks.appendleft(current_lock)
    else:
        print("Bang!")

    if gun_barrel == 0 and bullets:
        gun_barrel = gun_barrel_max if len(bullets) >= gun_barrel_max else len(bullets)
        print("Reloading!")

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    profit = abs(intelligence_value - bullet_price * bullets_shot)
    print(f"{len(bullets)} bullets left. Earned ${profit}")
