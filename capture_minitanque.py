from pathlib import Path
from time import sleep
from playwright.sync_api import sync_playwright

base = Path(r"C:\Users\User\Downloads\minitanque_documentacion")
images_dir = base / "images"
images_dir.mkdir(parents=True, exist_ok=True)

url = "http://localhost:8001/minitanque%20(1).html"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=1)
    page.goto(url, wait_until="networkidle")
    page.screenshot(path=str(images_dir / "00_inicial.png"), full_page=False)
    print("saved 00_inicial.png")

    page.locator("#selSpeed").select_option("4")
    page.locator("#btnSort").click()
    page.wait_for_function("document.querySelector('#prepSt').innerText.includes('Listo')", timeout=30000)
    page.screenshot(path=str(images_dir / "01_clasificacion.png"), full_page=False)
    print("saved 01_clasificacion.png")

    page.locator("#btnAuto").click()
    print("auto started")

    # Capture several phases while the mission runs.
    capture_plan = [
        ("02_aproximacion", 4),
        ("03_recogida", 10),
        ("04_transporte", 18),
        ("05_entrega", 30),
        ("06_final", 45),
    ]

    for name, delay in capture_plan:
        page.wait_for_timeout(delay * 1000)
        page.screenshot(path=str(images_dir / f"{name}.png"), full_page=False)
        print(f"saved {name}.png")

    browser.close()

print("All screenshots captured")
