from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "screenshots"
OUT.mkdir(exist_ok=True)

WIDTH = 1440
HEIGHT = 900
BG = "#091321"
PANEL = "#131f31"
CARD = "#1a2940"
BORDER = "#294764"
TEXT = "#f3efe1"
SUB = "#b8c7dc"
ACCENT = "#8bc5ff"
WARN = "#ffd76d"


def font(size: int, bold: bool = False):
    candidates = [
        "C:/Windows/Fonts/seguisb.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
    ]
    for candidate in candidates:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


TITLE = font(54, True)
SECTION = font(18, False)
BODY = font(26, False)
CARD_TITLE = font(18, False)
CARD_BODY = font(22, False)


def wrapped(draw, text, xy, wrap_width, font_obj, fill, line_gap=10):
    words = text.split()
    lines = []
    current = ""
    for word in words:
        trial = word if not current else f"{current} {word}"
        if draw.textlength(trial, font=font_obj) <= wrap_width:
            current = trial
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    x, y = xy
    line_height = font_obj.size + line_gap
    for line in lines:
        draw.text((x, y), line, font=font_obj, fill=fill)
        y += line_height


def shell():
    image = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((30, 30, WIDTH - 30, HEIGHT - 30), 28, fill=PANEL, outline=BORDER, width=2)
    return image, draw


def hero():
    image, draw = shell()
    draw.text((90, 82), "PLATFORM FOUNDATION BLUEPRINT", font=SECTION, fill=ACCENT)
    wrapped(draw, "Give the control-plane portfolio a real infrastructure floor.", (90, 130), 1150, TITLE, TEXT, 8)
    wrapped(draw, "VPC lanes, load-balanced compute, and observability alarms across dev and prod.", (90, 270), 1040, BODY, SUB, 8)
    stats = [
        ("NETWORK", "Public + private subnet lanes"),
        ("COMPUTE", "ALB and ECS-style cluster"),
        ("OBSERVABILITY", "Logs and 5xx alarm"),
        ("ENVIRONMENTS", "Dev and prod overlays"),
    ]
    x = 90
    for title, body in stats:
        draw.rounded_rectangle((x, 380, x + 285, 555), 22, fill=CARD, outline=BORDER, width=2)
        draw.text((x + 24, 406), title, font=CARD_TITLE, fill=ACCENT)
        wrapped(draw, body, (x + 24, 456), 230, CARD_BODY, TEXT, 6)
        x += 305
    draw.rounded_rectangle((90, 620, WIDTH - 90, 790), 24, fill=CARD, outline=BORDER, width=2)
    draw.text((120, 652), "DECISION FRAME", font=CARD_TITLE, fill="#ffbfdc")
    wrapped(draw, "This repo is the substrate that makes reliability, policy, and governance services feel deployable instead of hypothetical.", (120, 694), 1120, font(34, True), TEXT, 8)
    image.save(OUT / "01-hero.png")


def module_lanes():
    image, draw = shell()
    draw.text((90, 82), "MODULE LANES", font=SECTION, fill=ACCENT)
    wrapped(draw, "Three modules, one foundation shape.", (90, 130), 960, TITLE, TEXT, 8)
    modules = [
        ("NETWORK", "VPC, public subnets, private subnets, internet gateway"),
        ("COMPUTE", "ECS cluster, ALB, target group, ingress boundary"),
        ("OBSERVABILITY", "Log group, 5xx alarm, service visibility"),
    ]
    x = 110
    for title, body in modules:
        draw.rounded_rectangle((x, 290, x + 360, 640), 24, fill=CARD, outline=BORDER, width=2)
        draw.text((x + 28, 322), title, font=CARD_TITLE, fill=ACCENT)
        wrapped(draw, body, (x + 28, 390), 300, font(30, True), TEXT, 8)
        x += 390
    image.save(OUT / "02-module-lanes.png")


def envs():
    image, draw = shell()
    draw.text((90, 82), "ENVIRONMENT OVERLAYS", font=SECTION, fill=ACCENT)
    wrapped(draw, "Keep the composition stable and move environment differences into tfvars.", (90, 130), 1150, TITLE, TEXT, 8)
    env_cards = [
        ("DEV", "10.40.0.0/16", "us-east-1a · us-east-1b", "Fast iteration, platform validation"),
        ("PROD", "10.60.0.0/16", "us-east-1a · us-east-1b", "Critical traffic, stronger tagging"),
    ]
    x = 180
    for title, cidr, zones, body in env_cards:
        draw.rounded_rectangle((x, 310, x + 420, 690), 24, fill=CARD, outline=BORDER, width=2)
        draw.text((x + 28, 344), title, font=font(26, True), fill=ACCENT)
        draw.text((x + 28, 412), cidr, font=font(40, True), fill=TEXT)
        draw.text((x + 28, 478), zones, font=font(24, False), fill=WARN)
        wrapped(draw, body, (x + 28, 548), 340, CARD_BODY, SUB, 6)
        x += 470
    image.save(OUT / "03-environments.png")


def proof():
    image, draw = shell()
    draw.text((90, 82), "VALIDATION PROOF", font=SECTION, fill=ACCENT)
    wrapped(draw, "Blueprint, module structure, and plan flow in one proof layer.", (90, 130), 1080, TITLE, TEXT, 8)
    draw.rounded_rectangle((90, 300, 780, 790), 24, fill="#07101c", outline=BORDER, width=2)
    proof_lines = [
        "terraform init",
        "terraform plan -var-file=\"environments/dev.tfvars\"",
        "",
        "modules/",
        "  network/",
        "  compute/",
        "  observability/",
        "",
        "environments/",
        "  dev.tfvars",
        "  prod.tfvars",
    ]
    mono = font(24, False)
    y = 336
    for line in proof_lines:
        draw.text((120, y), line, font=mono, fill="#c8f7a5" if line.startswith("terraform") else SUB)
        y += 34
    draw.rounded_rectangle((820, 300, WIDTH - 90, 790), 24, fill=CARD, outline=BORDER, width=2)
    draw.text((850, 332), "WHY THIS COUNTS", font=CARD_TITLE, fill=ACCENT)
    wrapped(draw, "It shows platform thinking at the infrastructure layer, which gives the rest of the backend portfolio a credible deployment context.", (850, 400), 450, font(28, True), TEXT, 8)
    image.save(OUT / "04-proof.png")


if __name__ == "__main__":
    hero()
    module_lanes()
    envs()
    proof()
