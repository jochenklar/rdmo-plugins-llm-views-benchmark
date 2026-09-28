import json
import os

from config import (
    BASE_URL,
    JSON_PATH,
    MODELS,
    PASSWORD,
    PDF_PATH,
    PROVIDER,
    TIMEOUT,
    TIMEOUT_ASYNC,
    USERNAME,
    VIEWPORT,
)
from playwright.sync_api import sync_playwright

os.environ['DEBUG'] = 'pw:api'  # show Playwright's own log of every action


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page(viewport=VIEWPORT)
        page.set_default_timeout(TIMEOUT)

        # login
        page.goto(f'{BASE_URL}/account/login/')
        page.fill('input[name="username"]', USERNAME)
        page.fill('input[name="password"]', PASSWORD)
        page.click('input[type="submit"]')
        page.wait_for_load_state('networkidle')

        for model in MODELS[PROVIDER]:
            json_path = JSON_PATH / PROVIDER / f'{model}.json'
            json_path.parent.mkdir(exist_ok=True, parents=True)

            pdf_path = PDF_PATH / PROVIDER / f'{model}.pdf'
            pdf_path.parent.mkdir(exist_ok=True, parents=True)

            # go to project
            page.goto(f'{BASE_URL}/projects/1/')
            page.wait_for_load_state('networkidle')

            # find the view for the description
            row = page.locator('tr').filter(has=page.get_by_role('cell', name=f'{PROVIDER}, {model}', exact=True))
            row.get_by_role('link').first.click()

            # wait for the error or the panel
            panel = page.locator('.panel-body', has_text='Model provider')
            error = page.locator('.text-danger')
            panel.or_(error).first.wait_for(timeout=TIMEOUT_ASYNC)

            # handle error
            if error.count() > 0:
                error_message = error.first.inner_text().strip()
                with open(json_path, 'w') as fp:
                    json.dump({'error': error_message}, fp, indent=2)
                continue

            # parse and write info
            dts = panel.locator('dt').all_inner_texts()
            dds = panel.locator('dd').all_inner_texts()
            info = {dt.strip().rstrip(':'): dd.strip() for dt, dd in zip(dts, dds, strict=True)}

            with open(json_path, 'w') as fp:
                json.dump(info, fp, indent=2)

            # export PDF, circumvent browser pdf display
            href = page.get_by_role('link', name='PDF', exact=True).get_attribute('href')
            response = page.request.get(f'{BASE_URL}{href}')
            pdf_path.write_bytes(response.body())

        input('Press Enter to close the browser...')
        browser.close()


if __name__ == '__main__':
    main()
