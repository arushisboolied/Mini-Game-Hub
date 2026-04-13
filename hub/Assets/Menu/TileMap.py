import sys
import os
import pygame
import pytmx
import pytmx.util_pygame

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TMX_PATH = os.path.join(BASE_DIR, "Map.tmx")

FPS = 60


# ── Animation helpers ─────────────────────────────────────────────────────────

def build_anim_table(tmx_data: pytmx.TiledMap):
    table = {}
    for gid, props in tmx_data.tile_properties.items():
        frames = props.get("frames")
        if frames:
            table[gid] = [(f.gid, f.duration) for f in frames]
    return table


def current_frame_gid(frames, total_ms):
    period = sum(d for _, d in frames)
    t = total_ms % period
    for gid, dur in frames:
        if t < dur:
            return gid
        t -= dur
    return frames[-1][0]


# ── Rendering ─────────────────────────────────────────────────────────────────

def draw_map(surface, tmx_data, anim_table, total_ms):
    tw = tmx_data.tilewidth
    th = tmx_data.tileheight

    for layer in tmx_data.visible_layers:
        if not isinstance(layer, pytmx.TiledTileLayer):
            continue

        for x, y, gid in layer:
            if gid == 0:
                continue

            if gid in anim_table:
                gid = current_frame_gid(anim_table[gid], total_ms)

            img = tmx_data.get_tile_image_by_gid(gid)
            if img is None:
                continue

            iw, ih = img.get_size()

            tileset = tmx_data.get_tileset_from_gid(gid)
            if hasattr(tileset, "tileoffset") and tileset.tileoffset:
                offset_x, offset_y = tileset.tileoffset
            else:
                offset_x, offset_y = 0, 0

            px = x * tw + offset_x
            py = y * th + (th - ih) + offset_y

            surface.blit(img, (px, py))


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    if not os.path.exists(TMX_PATH):
        print(f"ERROR: {TMX_PATH} not found.")
        sys.exit(1)

    pygame.init()

    screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
    pygame.display.set_caption("Tiny Swords Map (Resizable)")
    clock = pygame.time.Clock()

    print("Loading map…")
    tmx_data = pytmx.util_pygame.load_pygame(TMX_PATH, pixelalpha=True)

    map_px_w = tmx_data.width * tmx_data.tilewidth
    map_px_h = tmx_data.height * tmx_data.tileheight

    anim_table = build_anim_table(tmx_data)

    canvas = pygame.Surface((map_px_w, map_px_h), pygame.SRCALPHA)

    total_ms = 0

    # initial scale setup
    def compute_scale(win_w, win_h):
        scale = min(win_w / map_px_w, win_h / map_px_h)
        disp_w = int(map_px_w * scale)
        disp_h = int(map_px_h * scale)
        off_x = (win_w - disp_w) // 2
        off_y = (win_h - disp_h) // 2
        return disp_w, disp_h, off_x, off_y

    win_w, win_h = screen.get_size()
    disp_w, disp_h, off_x, off_y = compute_scale(win_w, win_h)
    scaled = pygame.Surface((disp_w, disp_h))

    print("Ready — resize window freely")

    while True:
        dt = clock.tick(FPS)
        total_ms += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_ESCAPE, pygame.K_q):
                    pygame.quit()
                    sys.exit()

            elif event.type == pygame.VIDEORESIZE:
                win_w, win_h = event.w, event.h
                screen = pygame.display.set_mode((win_w, win_h), pygame.RESIZABLE)

                disp_w, disp_h, off_x, off_y = compute_scale(win_w, win_h)
                scaled = pygame.Surface((disp_w, disp_h))

        canvas.fill((0, 0, 0, 0))
        draw_map(canvas, tmx_data, anim_table, total_ms)

        scaled = pygame.transform.scale(canvas, (win_w, win_h))
        screen.blit(scaled, (0, 0))

        pygame.display.flip()


if __name__ == "__main__":
    main()