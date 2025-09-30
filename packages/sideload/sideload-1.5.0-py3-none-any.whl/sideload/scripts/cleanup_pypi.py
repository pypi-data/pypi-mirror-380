#!/usr/bin/env python3
"""
Admin script to delete all sideload-* packages from PyPI using browser automation
"""

import os
import sys
import asyncio
import random
from playwright.async_api import async_playwright
import pyotp

PYPI_USER = os.environ.get("PYPI_USER")
PYPI_PASSWORD = os.environ.get("PYPI_PASSWORD")
PYPI_TOTP = os.environ.get("PYPI_TOTP")  # Optional: TOTP secret key

if not PYPI_USER or not PYPI_PASSWORD:
    print("❌ PYPI_USER and PYPI_PASSWORD environment variables must be set")
    sys.exit(1)


async def human_like_mouse_movement(page):
    """Simulate human-like mouse movements across the page"""
    viewport_size = page.viewport_size
    width = viewport_size.get('width', 1280) if viewport_size else 1280
    height = viewport_size.get('height', 720) if viewport_size else 720

    for _ in range(random.randint(3, 6)):
        x = random.randint(50, width - 50)
        y = random.randint(50, height - 50)
        await page.mouse.move(x, y)
        await asyncio.sleep(random.uniform(0.15, 0.4))


async def delete_project(page, package_name: str) -> bool:
    """Delete a project from PyPI using browser automation"""
    try:
        print(f"🗑️  Deleting {package_name}...")

        # Go to project settings
        settings_url = f'https://pypi.org/manage/project/{package_name}/settings/'
        await page.goto(settings_url)

        # Check if project exists (if we get 404, project doesn't exist)
        title = await page.title()
        if "404" in title or "Not Found" in title:
            print(f"  ⚠️  Project {package_name} not found")
            return False

        # Scroll to the bottom of the page to find delete section
        await page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
        await asyncio.sleep(0.5)

        # Extract the exact project name from the page to ensure correct case
        # Look for the project name in the delete section
        exact_project_name = await page.evaluate('''() => {
            // Find the label that mentions the project name
            const labels = Array.from(document.querySelectorAll('label'));
            for (const label of labels) {
                const text = label.textContent;
                if (text && text.includes('confirm by typing the project name')) {
                    // Extract the project name from something like "confirm by typing the project name (project-name) below"
                    const match = text.match(/\\(([^)]+)\\)/);
                    if (match) return match[1];
                }
            }
            // Fallback: get from URL
            const path = window.location.pathname;
            const urlMatch = path.match(/\\/manage\\/project\\/([^\\/]+)/);
            return urlMatch ? decodeURIComponent(urlMatch[1]) : null;
        }''')

        if not exact_project_name:
            print(f"  ⚠️  Could not extract exact project name from page, using: {package_name}")
            exact_project_name = package_name
        else:
            print(f"  📝 Extracted exact project name: {exact_project_name}")

        # Find and check all "I understand..." checkboxes
        checkboxes = await page.query_selector_all('input[type="checkbox"]')
        print(f"  ✓ Found {len(checkboxes)} checkboxes")
        for checkbox in checkboxes:
            await checkbox.check()

        # Find and type project name in confirmation field
        confirm_input = await page.query_selector('input[name="confirm_project_name"]')
        if not confirm_input:
            print(f"  ⚠️  Could not find confirmation input for {package_name}")
            return False

        # Clear and type the exact project name with human-like behavior
        await confirm_input.clear()
        await asyncio.sleep(random.uniform(0.2, 0.5))

        # Move mouse before typing
        await human_like_mouse_movement(page)

        # Type each character with varying delays
        for char in exact_project_name:
            await confirm_input.type(char, delay=random.randint(80, 200))
            await asyncio.sleep(random.uniform(0.05, 0.15))

        print(f"  ✓ Typed project name: {exact_project_name}")

        # Wait a moment for the button to become enabled (human-like pause)
        await asyncio.sleep(random.uniform(1.0, 2.0))

        # Move mouse naturally
        await human_like_mouse_movement(page)

        # Find and click the delete link
        delete_link = await page.query_selector('[data-delete-confirm-target="button"]')
        if not delete_link:
            print(f"  ⚠️  Could not find delete button")
            return False

        # Check if the button is enabled
        is_disabled = await delete_link.evaluate('(el) => el.classList.contains("button--disabled") || el.hasAttribute("disabled")')
        if is_disabled:
            print(f"  ⚠️  Delete button is still disabled")
            # Take a screenshot for debugging
            await page.screenshot(path=f"debug_{package_name}.png")
            print(f"  📸 Screenshot saved as debug_{package_name}.png")
            return False

        print(f"  🖱️  Clicking delete button...")

        # Move mouse to the button area naturally
        box = await delete_link.bounding_box()
        if box:
            # Move to a random point within the button
            target_x = box['x'] + random.uniform(10, box['width'] - 10)
            target_y = box['y'] + random.uniform(10, box['height'] - 10)
            await page.mouse.move(target_x, target_y)
            await asyncio.sleep(random.uniform(0.2, 0.5))

        # Click and wait for navigation
        await delete_link.click()
        await asyncio.sleep(random.uniform(0.5, 1.0))
        await page.wait_for_load_state("networkidle")

        print(f"  ✅ Deleted {package_name}")
        return True

    except Exception as e:
        print(f"  ❌ Error deleting {package_name}: {e}")
        import traceback
        traceback.print_exc()
        # Take screenshot on error
        try:
            await page.screenshot(path=f"error_{package_name}.png")
            print(f"  📸 Error screenshot saved as error_{package_name}.png")
        except:
            pass
        return False


async def get_user_projects(page) -> list[str]:
    """Get all projects owned by the user that start with sideload-"""
    try:
        print("🔍 Fetching your PyPI projects...")

        # Go to projects page
        await page.goto('https://pypi.org/manage/projects/')
        await page.wait_for_load_state("networkidle")

        # Extract project names
        projects = await page.evaluate('''() => {
            const links = Array.from(document.querySelectorAll('a[href*="/manage/project/"]'));
            return links.map(link => {
                const match = link.href.match(/\\/manage\\/project\\/([^\\/]+)\\//);
                return match ? match[1] : null;
            }).filter(name => name && name.startsWith('sideload-'));
        }''')

        return projects

    except Exception as e:
        print(f"❌ Error fetching projects: {e}")
        return []


async def main():
    print("🧹 PyPI Sideload Package Cleanup Tool")
    print("=" * 50)
    if PYPI_TOTP:
        print("🔐 TOTP auto-generation enabled")
    else:
        print("⚠️  TOTP auto-generation disabled (set PYPI_TOTP to enable)")
    print()

    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        try:
            # Navigate to PyPI login page
            print("🔐 Logging in to PyPI...")
            print("   Opening login page...")
            await page.goto('https://pypi.org/account/login/')

            # Fill in login credentials (fast, no need to be slow here)
            print("   Filling credentials...")
            await page.fill('#username', PYPI_USER)
            await asyncio.sleep(random.uniform(0.2, 0.4))
            await page.fill('#password', PYPI_PASSWORD)
            await asyncio.sleep(random.uniform(0.3, 0.6))

            # Submit login form
            await page.click('input[type="submit"]')
            await asyncio.sleep(2)

            # Wait for user to complete TOTP if required
            current_url = page.url
            if '/account/two-factor/' in current_url:
                if PYPI_TOTP:
                    print("   🔐 Generating TOTP code...")

                    # Simulate human-like delay before interacting
                    await asyncio.sleep(random.uniform(1.5, 2.5))

                    # Move mouse around naturally across the page
                    print("   🖱️  Moving mouse naturally...")
                    await human_like_mouse_movement(page)

                    totp = pyotp.TOTP(PYPI_TOTP)
                    code = totp.now()
                    print(f"   ✓ Generated TOTP code: {code}")

                    # Find TOTP input field and enter the code
                    totp_input = await page.query_selector('input[name="totp_value"]')
                    if not totp_input:
                        totp_input = await page.query_selector('input[type="text"]')

                    if totp_input:
                        # Click on the input field naturally
                        await totp_input.click()
                        await asyncio.sleep(random.uniform(0.4, 0.8))

                        # Type each character slowly with human-like delays
                        print("   ⌨️  Typing TOTP code slowly...")
                        for i, char in enumerate(code):
                            await totp_input.type(char, delay=random.randint(100, 250))
                            await asyncio.sleep(random.uniform(0.1, 0.25))
                            # Occasionally move mouse during typing
                            if i % 2 == 0:
                                x = random.randint(200, 600)
                                y = random.randint(200, 500)
                                await page.mouse.move(x, y)

                        print("   ✓ Entered TOTP code")

                        # Wait a bit before submitting (like a human would)
                        await asyncio.sleep(random.uniform(0.8, 1.5))

                        # More mouse movements
                        print("   🖱️  Moving mouse before submit...")
                        await human_like_mouse_movement(page)

                        # Submit the form
                        submit_button = await page.query_selector('button[type="submit"]')
                        if not submit_button:
                            submit_button = await page.query_selector('input[type="submit"]')

                        if submit_button:
                            await submit_button.click()
                            print("   ✓ Submitted TOTP, waiting for response...")

                            # Wait for navigation
                            await asyncio.sleep(4)

                            # Check if we've successfully logged in
                            current_url = page.url
                            if '/account/' in current_url or '/manage/' in current_url:
                                print("   ✓ Successfully logged in!")
                            elif '/account/two-factor/' in current_url:
                                # Still on 2FA page - likely a captcha
                                print("\n" + "=" * 60)
                                print("   🤖 CAPTCHA DETECTED!")
                                print("   👤 Please solve the captcha in the browser window")
                                print("   ⏳ Waiting for you to complete it...")
                                print("=" * 60 + "\n")

                                # Wait for user to solve captcha - keep checking
                                # We need to wait until we're actually logged in (on account page or similar)
                                while True:
                                    await asyncio.sleep(2)
                                    current_url = page.url
                                    # Check if we've successfully logged in (not just left the 2FA page)
                                    if ('/account/' in current_url or '/manage/' in current_url) and '/account/two-factor/' not in current_url:
                                        break
                                    # Print status every 2 seconds to show we're still waiting
                                    print("   ⏳ Still waiting for captcha completion...", end='\r')

                                print("\n   ✓ Captcha solved and logged in! Continuing...")
                            else:
                                print(f"   ⚠️  Unexpected page: {current_url}")
                                print("   ⏳ Waiting for login to complete...")
                                # Wait until we're on a known good page
                                while True:
                                    await asyncio.sleep(2)
                                    current_url = page.url
                                    if '/account/' in current_url or '/manage/' in current_url:
                                        break
                                    print("   ⏳ Still waiting...", end='\r')
                                print("\n   ✓ Login completed!")
                        else:
                            print("   ⚠️  Could not find submit button")
                    else:
                        print("   ⚠️  Could not find TOTP input field")
                else:
                    print("   ⚠️  TOTP required - please enter your 2FA code in the browser...")
                    print("   👤 Waiting for you to complete 2FA (and captcha if present)...")
                    while True:
                        await asyncio.sleep(2)
                        current_url = page.url
                        # Wait until we're actually logged in
                        if '/account/two-factor/' not in current_url and ('/account/' in current_url or '/manage/' in current_url):
                            break
                        print("   ⏳ Still waiting for 2FA completion...", end='\r')
                    print("\n   ✓ 2FA completed!")

            print("\n✅ Login completed!")

            # Get all sideload projects
            projects = await get_user_projects(page)

            if not projects:
                print("❌ No sideload-* projects found")
                return

            print(f"\n📋 Found {len(projects)} sideload projects:")
            for pkg in projects:
                print(f"  - {pkg}")

            # Delete each project
            print("\n🗑️  Deleting projects...\n")
            deleted = 0
            for pkg in projects:
                if await delete_project(page, pkg):
                    deleted += 1

            print(f"\n✅ Deleted {deleted}/{len(projects)} projects")

        finally:
            await browser.close()


if __name__ == "__main__":
    asyncio.run(main())