#!/usr/bin/env python3
"""
Admin script to delete all sideload-* packages from PyPI using browser automation
"""

import os
import sys
import asyncio
from playwright.async_api import async_playwright

PYPI_USER = os.environ.get("PYPI_USER")
PYPI_PASSWORD = os.environ.get("PYPI_PASSWORD")

if not PYPI_USER or not PYPI_PASSWORD:
    print("❌ PYPI_USER and PYPI_PASSWORD environment variables must be set")
    sys.exit(1)


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

        # Find and check all "I understand..." checkboxes
        checkboxes = await page.query_selector_all('input[type="checkbox"]')
        for checkbox in checkboxes:
            await checkbox.check()

        # Find and type project name in confirmation field
        confirm_input = await page.query_selector('input[name="confirm_project_name"]')
        if not confirm_input:
            print(f"  ⚠️  Could not find confirmation input for {package_name}")
            return False

        await confirm_input.fill(package_name)

        # Find and click the delete link that opens the modal
        # This is the button with href="#project_name-modal"
        delete_link = await page.query_selector('a.button--danger[data-delete-confirm-target="button"]')
        if not delete_link:
            print(f"  ⚠️  Could not find delete link for {package_name}")
            return False

        # Wait a moment to ensure button is enabled
        await asyncio.sleep(0.5)

        # Click the link to open the modal
        await delete_link.click()
        await asyncio.sleep(0.5)

        # Now find and click the actual delete button in the modal
        modal_delete_button = await page.query_selector('button[type="submit"]')
        if not modal_delete_button:
            print(f"  ⚠️  Could not find modal delete button for {package_name}")
            return False

        await modal_delete_button.click()
        await page.wait_for_load_state("networkidle")

        print(f"  ✅ Deleted {package_name}")
        return True

    except Exception as e:
        print(f"  ❌ Error deleting {package_name}: {e}")
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

            # Fill in login credentials
            print("   Filling credentials...")
            await page.fill('#username', PYPI_USER)
            await page.fill('#password', PYPI_PASSWORD)

            # Submit login form
            await page.click('input[type="submit"]')
            await asyncio.sleep(1)

            # Wait for user to complete TOTP if required
            current_url = page.url
            if '/account/two-factor/' in current_url:
                print("   ⚠️  TOTP required - please enter your 2FA code in the browser...")
                while True:
                    current_url = page.url
                    # Wait until we're not on TOTP page anymore
                    if '/account/two-factor/' not in current_url:
                        break
                    await asyncio.sleep(1)

            print("✅ Login completed!")

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