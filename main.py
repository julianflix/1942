#!/usr/bin/env python3
"""
1942-lite — Top-Down Warplane Shooter (Pygame, single-file)
- Player moves in 4 directions, shoots with Space.
- Enemies spawn based on a level text file with letters denoting types.
- Clusters of same letters produce bigger enemies (connected components).
- Drops: health packs, ammo, enhanced weapon (triple-shot for 10s).
- Player has 5 lives, respawns at death location with brief invulnerability.
- Safe Zone appears after level spawns are exhausted. Reach it to win.

Level file: levels/level1.txt
Letters:
  S: Shooter
  K: Kamikaze
  B: Big enemy (or cluster of any letter becomes big automatically)
  . or space: empty

Controls:
  Move: Arrow keys / WASD
  Shoot: Space
  Pause: P
  Quit: Esc or Q
  Debug overlay: F1
"""
from __future__ import annotations
import os, sys, time, math, random
import pygame

# ---------------------------- Configuration ----------------------------
WIDTH, HEIGHT = 800, 600
FPS = 60

PLAYER_SPEED = 300.0
PLAYER_BULLET_SPEED = 600.0
PLAYER_BULLET_COOLDOWN = 0.15
PLAYER_START_LIVES = 5
INVULN_AFTER_DEATH = 2.0  # seconds
ENHANCED_WEAPON_DURATION = 10.0  # seconds (triple shot)

ENEMY_BASE_SPEED = 120.0
KAMIKAZE_SPEED = 160.0
ENEMY_BULLET_SPEED = 300.0
ENEMY_FIRE_COOLDOWN = (1.2, 2.4)  # random range

SPAWN_ROW_MS = 800  # how fast we consume level rows (ms)

DROP_CHANCE = 0.35
DROP_TYPES = ["health", "ammo", "enhanced"]

SAFE_ZONE_TAIL_MS = 5000  # after last spawn row considered, wait before safe zone shows

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 220, 0)
RED = (220, 40, 40)
YELLOW = (250, 220, 80)
BLUE = (60, 160, 255)
GRAY = (100, 100, 100)

# ---------------------------- Helpers ----------------------------
def load_level_grid(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f]
    # normalize widths
    maxw = max((len(l) for l in lines), default=0)
    norm = [(l + " " * max(0, maxw - len(l)))[:maxw] for l in lines]
    return norm

def connected_components(grid: list[str]) -> list[dict]:
    """
    Find connected components (4-neighbour) of non-empty letters.
    Each component yields:
      - letter
      - cells: list[(r,c)]
      - min_r, max_r, min_c, max_c
    """
    if not grid:
        return []
    R, C = len(grid), len(grid[0])
    visited = [[False]*C for _ in range(R)]
    comps = []
    for r in range(R):
        for c in range(C):
            ch = grid[r][c]
            if ch not in (" ", ".", "\t") and not visited[r][c]:
                # BFS/DFS
                stack = [(r,c)]
                visited[r][c] = True
                cells = []
                while stack:
                    rr, cc = stack.pop()
                    cells.append((rr, cc))
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = rr+dr, cc+dc
                        if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and grid[nr][nc] == ch:
                            visited[nr][nc] = True
                            stack.append((nr, nc))
                rows = [rr for rr, _ in cells]
                cols = [cc for _, cc in cells]
                comps.append({
                    "letter": ch,
                    "cells": cells,
                    "min_r": min(rows),
                    "max_r": max(rows),
                    "min_c": min(cols),
                    "max_c": max(cols),
                    "area": len(cells),
                })
    # sort by min_r so earlier rows spawn first
    comps.sort(key=lambda d: d["min_r"])
    return comps

# ---------------------------- Entities ----------------------------
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, vy, color=YELLOW, friendly=True):
        super().__init__()
        self.image = pygame.Surface((4, 10), pygame.SRCALPHA)
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x,y))
        self.vy = vy
        self.friendly = friendly

    def update(self, dt):
        self.rect.y += int(self.vy * dt)
        if self.rect.bottom < 0 or self.rect.top > HEIGHT:
            self.kill()

class Drop(pygame.sprite.Sprite):
    def __init__(self, x, y, kind: str):
        super().__init__()
        self.kind = kind
        self.image = pygame.Surface((16, 16), pygame.SRCALPHA)
        if kind == "health":
            pygame.draw.rect(self.image, GREEN, (0,0,16,16), border_radius=3)
            pygame.draw.line(self.image, WHITE, (8,2),(8,14), 2)
            pygame.draw.line(self.image, WHITE, (2,8),(14,8), 2)
        elif kind == "ammo":
            pygame.draw.rect(self.image, BLUE, (0,0,16,16), border_radius=3)
            pygame.draw.rect(self.image, WHITE, (6,3,4,10))
        else:  # enhanced
            pygame.draw.rect(self.image, YELLOW, (0,0,16,16), border_radius=3)
            pygame.draw.circle(self.image, WHITE, (8,8), 5, 2)
        self.rect = self.image.get_rect(center=(x,y))
        self.vy = 60

    def update(self, dt):
        self.rect.y += int(self.vy * dt)
        if self.rect.top > HEIGHT:
            self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, w=28, h=22, hp=2, color=RED):
        super().__init__()
        self.image = pygame.Surface((w,h), pygame.SRCALPHA)
        pygame.draw.rect(self.image, color, (0,0,w,h), border_radius=4)
        pygame.draw.rect(self.image, WHITE, (4, h-6, w-8, 3))
        self.rect = self.image.get_rect(center=(x,y))
        self.hp = hp
        self.vy = ENEMY_BASE_SPEED
        self.fire_t = random.uniform(*ENEMY_FIRE_COOLDOWN)
        self.time = 0.0
        self.color = color

    def update(self, dt):
        self.time += dt
        self.rect.y += int(self.vy * dt)
        if self.rect.top > HEIGHT:
            self.kill()

    def damage(self, dmg=1):
        self.hp -= dmg
        if self.hp <= 0:
            self.kill()
            return True
        return False

    def maybe_drop(self, drops_group):
        if random.random() < DROP_CHANCE:
            kind = random.choice(DROP_TYPES)
            drops_group.add(Drop(self.rect.centerx, self.rect.centery, kind))

class ShooterEnemy(Enemy):
    def __init__(self, x, y, w=28, h=22, hp=3, color=(220,80,80)):
        super().__init__(x,y,w,h,hp,color)

    def update(self, dt, bullets_group=None):
        super().update(dt)
        self.fire_t -= dt
        if bullets_group is not None and self.fire_t <= 0:
            self.fire_t = random.uniform(*ENEMY_FIRE_COOLDOWN)
            # fire straight down
            bullets_group.add(Bullet(self.rect.centerx, self.rect.bottom, ENEMY_BULLET_SPEED, color=WHITE, friendly=False))

class KamikazeEnemy(Enemy):
    def __init__(self, x, y, w=24, h=20, hp=2, color=(255,120,40)):
        super().__init__(x,y,w,h,hp,color)
        self.vy = KAMIKAZE_SPEED
        self.target_ref = None  # set to player sprite externally

    def update(self, dt):
        # steer towards player if available
        if self.target_ref is not None:
            px, py = self.target_ref.rect.center
            dx = px - self.rect.centerx
            dy = py - self.rect.centery
            d = max(1.0, math.hypot(dx, dy))
            vx = (dx / d) * 100.0
            vy = (dy / d) * self.vy / (KAMIKAZE_SPEED/100.0)
            self.rect.x += int(vx * dt)
            self.rect.y += int(vy * dt)
        else:
            self.rect.y += int(self.vy * dt)
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()

class BigEnemy(Enemy):
    def __init__(self, x, y, w_cells, h_cells, cell_w, cell_h, letter="B"):
        w = max(32, int(w_cells * cell_w * 0.9))
        h = max(28, int(h_cells * cell_h * 0.9))
        hp = 4 + (w_cells * h_cells) // 2
        super().__init__(x, y, w, h, hp, color=(200, 60, 200))
        self.letter = letter
        self.vy = ENEMY_BASE_SPEED * 0.75

# ---------------------------- Player ----------------------------
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.base_image = pygame.Surface((28,28), pygame.SRCALPHA)
        # Simple stylized plane
        pygame.draw.polygon(self.base_image, BLUE, [(14,0),(24,16),(14,12),(4,16)])
        pygame.draw.polygon(self.base_image, WHITE, [(14,4),(18,12),(14,10),(10,12)])
        pygame.draw.rect(self.base_image, WHITE, (12,12,4,12))
        self.image = self.base_image.copy()
        self.rect = self.image.get_rect(center=(x,y))
        self.speed = PLAYER_SPEED
        self.lives = PLAYER_START_LIVES
        self.invuln_t = 0.0
        self.shoot_t = 0.0
        self.ammo = 9999  # soft cap; not strictly enforced here
        self.enhanced_until = 0.0

    def has_enhanced(self, now: float) -> bool:
        return now < self.enhanced_until

    def grant_enhanced(self, now: float):
        self.enhanced_until = max(self.enhanced_until, now + ENHANCED_WEAPON_DURATION)

    def update(self, dt, keys):
        vx = vy = 0.0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            vx -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            vx += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            vy -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            vy += self.speed
        self.rect.x += int(vx * dt)
        self.rect.y += int(vy * dt)
        self.rect.clamp_ip(pygame.Rect(0,0,WIDTH,HEIGHT))
        if self.invuln_t > 0:
            self.invuln_t -= dt

    def shoot(self, now: float, bullets_group):
        if self.shoot_t > now:
            return
        self.shoot_t = now + PLAYER_BULLET_COOLDOWN
        # consume ammo if you later add limited ammo mechanics
        cx, cy = self.rect.centerx, self.rect.top
        if self.has_enhanced(now):
            # triple shot
            bullets_group.add(Bullet(cx, cy, -PLAYER_BULLET_SPEED, color=YELLOW, friendly=True))
            b1 = Bullet(cx-10, cy, -PLAYER_BULLET_SPEED, color=YELLOW, friendly=True)
            b2 = Bullet(cx+10, cy, -PLAYER_BULLET_SPEED, color=YELLOW, friendly=True)
            bullets_group.add(b1, b2)
        else:
            bullets_group.add(Bullet(cx, cy, -PLAYER_BULLET_SPEED, color=YELLOW, friendly=True))

    def damage(self):
        if self.invuln_t > 0:
            return False
        self.lives -= 1
        self.invuln_t = INVULN_AFTER_DEATH
        return self.lives >= 0

# ---------------------------- Level + Spawning ----------------------------
class SpawnEvent:
    def __init__(self, min_row, cx, cy, w_cells, h_cells, letter):
        self.min_row = min_row  # when to spawn (row index time)
        self.cx = cx
        self.cy = cy
        self.w_cells = w_cells
        self.h_cells = h_cells
        self.letter = letter
        self.spawned = False

class LevelTimeline:
    def __init__(self, grid):
        self.grid = grid
        self.R = len(grid)
        self.C = len(grid[0]) if self.R else 0
        self.cell_w = WIDTH / max(1, self.C)
        self.cell_h = 28  # vertical spacing for spawn positioning reference
        # Precompute connected components
        comps = connected_components(grid)
        self.events: list[SpawnEvent] = []
        for comp in comps:
            # center in component's bounding box
            cminr, cmaxr = comp["min_r"], comp["max_r"]
            cminc, cmaxc = comp["min_c"], comp["max_c"]
            center_c = (cminc + cmaxc + 1) / 2.0
            w_cells = cmaxc - cminc + 1
            h_cells = cmaxr - cminr + 1
            cx = int(center_c * self.cell_w)
            cy = -int(h_cells * self.cell_h) - 20  # start above screen
            self.events.append(SpawnEvent(cminr, cx, cy, w_cells, h_cells, comp["letter"]))
        self.events.sort(key=lambda e: e.min_row)
        self.row_timer = 0.0
        self.row_index = 0
        self.last_spawn_ms = 0
        self.done_spawning = False
        self.all_spawned_time = None

    def update(self, dt_ms, enemies_group, player_ref, enemy_bullets):
        # advance "row time"
        self.row_timer += dt_ms
        while not self.done_spawning and self.row_timer >= SPAWN_ROW_MS * (self.row_index + 1):
            self.row_index += 1
            # spawn all events whose min_row == row_index - 1
            target_row = self.row_index - 1
            for ev in self.events:
                if not ev.spawned and ev.min_row == target_row:
                    ev.spawned = True
                    self._spawn_event(ev, enemies_group, player_ref, enemy_bullets)
        if not self.done_spawning and self.row_index >= self.R:
            self.done_spawning = True
            self.all_spawned_time = pygame.time.get_ticks()

    def _spawn_event(self, ev: SpawnEvent, enemies_group, player_ref, enemy_bullets):
        # map letters to enemy behavior
        letter = ev.letter.upper()
        if ev.w_cells * ev.h_cells > 1 or letter == "B":
            # Big enemy
            e = BigEnemy(ev.cx, ev.cy, ev.w_cells, ev.h_cells, self.cell_w, self.cell_h, letter=letter)
        elif letter == "S":
            e = ShooterEnemy(ev.cx, ev.cy)
        elif letter == "K":
            e = KamikazeEnemy(ev.cx, ev.cy)
            e.target_ref = player_ref
        else:
            # default small enemy (drifts down)
            e = Enemy(ev.cx, ev.cy)
        enemies_group.add(e)

# ---------------------------- Game ----------------------------
class Game:
    def __init__(self, level_path="levels/level1.txt"):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("1942-lite")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("consolas", 18)
        self.bigfont = pygame.font.SysFont("consolas", 28)
        self.running = True
        self.paused = False
        self.debug = False

        # Background starfield
        self.stars = [(random.randint(0,WIDTH-1), random.randint(0,HEIGHT-1), random.randint(1,3))
                      for _ in range(120)]

        # Sprites
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.player_bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.drops = pygame.sprite.Group()

        # Player
        self.player = Player(WIDTH//2, HEIGHT-70)
        self.all_sprites.add(self.player)

        # Level
        grid = load_level_grid(level_path)
        self.timeline = LevelTimeline(grid)

        # Safe zone
        self.safe_zone_active = False
        self.safe_zone_y = HEIGHT - 80

        # misc
        self.last_time = time.perf_counter()

    def spawn_safe_zone_if_ready(self):
        if not self.timeline.done_spawning:
            return
        # after a tail, show safe zone
        if self.timeline.all_spawned_time is not None:
            if pygame.time.get_ticks() - self.timeline.all_spawned_time >= SAFE_ZONE_TAIL_MS:
                self.safe_zone_active = True

    def update_starfield(self, dt):
        for i, (x,y,s) in enumerate(self.stars):
            y += int(50*s*dt)
            if y >= HEIGHT:
                y = 0
                x = random.randint(0, WIDTH-1)
            self.stars[i] = (x,y,s)

    def draw_starfield(self, surf):
        for x,y,s in self.stars:
            c = (180,180,180) if s==1 else (220,220,220) if s==2 else (255,255,255)
            surf.fill(c, (x,y,1,1))

    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000.0
            dt_ms = dt * 1000.0
            self.handle_events()
            if not self.paused:
                self.update(dt, dt_ms)
            self.render()

        pygame.quit()

    def handle_events(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.running = False
            elif e.type == pygame.KEYDOWN:
                if e.key in (pygame.K_ESCAPE, pygame.K_q):
                    self.running = False
                elif e.key == pygame.K_p:
                    self.paused = not self.paused
                elif e.key == pygame.K_F1:
                    self.debug = not self.debug

        keys = pygame.key.get_pressed()
        if not self.paused:
            self.player.update(0, keys)  # position update is in update(); here only to read keys for shooting
            if keys[pygame.K_SPACE]:
                self.player.shoot(time.perf_counter(), self.player_bullets)

    def update(self, dt, dt_ms):
        keys = pygame.key.get_pressed()
        self.player.update(dt, keys)

        # Spawn timeline
        self.timeline.update(dt_ms, self.enemies, self.player, self.enemy_bullets)
        self.spawn_safe_zone_if_ready()

        # Update sprites
        for e in list(self.enemies):
            if isinstance(e, ShooterEnemy):
                e.update(dt, bullets_group=self.enemy_bullets)
            else:
                e.update(dt)
        self.player_bullets.update(dt)
        self.enemy_bullets.update(dt)
        self.drops.update(dt)

        # Collisions: player bullets vs enemies
        for bullet in list(self.player_bullets):
            hits = [sp for sp in self.enemies if sp.rect.colliderect(bullet.rect)]
            if hits:
                bullet.kill()
                for enemy in hits:
                    dead = enemy.damage(1)
                    if dead:
                        enemy.maybe_drop(self.drops)

        # Collisions: enemy bullets vs player
        if self.player.invuln_t <= 0:
            if pygame.sprite.spritecollideany(self.player, self.enemy_bullets) or pygame.sprite.spritecollideany(self.player, self.enemies):
                # record spot and "explode" (visual feedback could be expanded)
                px, py = self.player.rect.center
                alive = self.player.damage()
                # Clear immediate bullets overlapping
                for b in list(self.enemy_bullets):
                    if self.player.rect.colliderect(b.rect):
                        b.kill()
                if not alive:
                    # lives just went to -1 => game over
                    self.running = False
                else:
                    # respawn at same place (already done), grant brief invulnerability
                    self.player.rect.center = (px, py)

        # Collisions: player vs drops
        got = pygame.sprite.spritecollide(self.player, self.drops, dokill=True)
        now = time.perf_counter()
        for d in got:
            if d.kind == "health":
                self.player.lives = min(9, self.player.lives + 1)
            elif d.kind == "ammo":
                self.player.ammo = min(9999, self.player.ammo + 50)
            else:
                self.player.grant_enhanced(now)

        # Safe zone check
        if self.safe_zone_active and self.player.rect.top <= self.safe_zone_y:
            # Reach top of safe zone line to win
            self.win_and_exit()

    def win_and_exit(self):
        # Simple win screen
        surf = self.screen
        surf.fill(BLACK)
        txt = self.bigfont.render("SAFE ZONE REACHED! YOU WIN!", True, GREEN)
        surf.blit(txt, txt.get_rect(center=(WIDTH//2, HEIGHT//2)))
        pygame.display.flip()
        pygame.time.delay(2200)
        self.running = False

    def render(self):
        self.screen.fill(BLACK)
        self.draw_starfield(self.screen)

        # Safe zone line
        if self.safe_zone_active:
            pygame.draw.rect(self.screen, (40,120,40), (0, self.safe_zone_y, WIDTH, HEIGHT - self.safe_zone_y))

        # Sprites
        self.enemies.draw(self.screen)
        self.player_bullets.draw(self.screen)
        self.enemy_bullets.draw(self.screen)
        # player blink if invuln
        if int(self.player.invuln_t * 10) % 2 == 0 or self.player.invuln_t <= 0:
            self.screen.blit(self.player.image, self.player.rect)
        # drops
        self.drops.draw(self.screen)

        # HUD
        self.draw_hud(self.screen)

        pygame.display.flip()

    def draw_hud(self, surf):
        # Lives
        lives_s = self.font.render(f"Lives: {max(0,self.player.lives)}", True, WHITE)
        surf.blit(lives_s, (8, 8))
        # Enhanced timer
        now = time.perf_counter()
        if self.player.has_enhanced(now):
            rem = max(0.0, self.player.enhanced_until - now)
            enh_s = self.font.render(f"Enhanced: {rem:0.1f}s", True, YELLOW)
            surf.blit(enh_s, (8, 30))
        # Pause
        if self.paused:
            p = self.bigfont.render("PAUSED - P to resume, Q/Esc to quit", True, WHITE)
            surf.blit(p, p.get_rect(center=(WIDTH//2, HEIGHT//2)))
        # Debug
        if self.debug:
            dbg = self.font.render(f"Enemies: {len(self.enemies)}  PBullets: {len(self.player_bullets)}  EBullets: {len(self.enemy_bullets)}", True, GRAY)
            surf.blit(dbg, (8, HEIGHT-22))

def main():
    level = os.path.join("levels", "level1.txt")
    Game(level).run()

if __name__ == "__main__":
    main()
