"""
Profile management commands for Jobtty.io
"""

import click
import os
from pathlib import Path
from rich.prompt import Prompt, Confirm
from rich.console import Console

from ..core.display import console, show_error, show_success, show_info
from ..core.config import JobttyConfig
from ..core.api_client import JobttyAPI

config = JobttyConfig()
api = JobttyAPI()

@click.group()
def profile():
    """
    👤 Manage your JobTTY profile
    """
    pass

@profile.command()
@click.argument('cv_path', required=False)
@click.option('--text', help='CV content as text instead of file')
def upload_cv(cv_path, text):
    """
    📄 Upload your CV to your profile
    
    Examples:
    jobtty profile upload-cv /path/to/cv.pdf
    jobtty profile upload-cv --text "My CV content here"
    """
    
    if not config.is_authenticated():
        show_error("🔐 You need to login first")
        if Confirm.ask("Login now?"):
            # Redirect to auth - user needs to login first
            console.print("💡 Please run: jobtty login")
        return
    
    console.print("\n[bold bright_cyan]📄 CV Upload[/bold bright_cyan]\n")
    
    if text:
        # Upload CV as text
        console.print("📝 Uploading CV as text...")
        try:
            result = api.upload_cv_text(text)
            show_success("✅ CV uploaded successfully!")
            console.print("💼 Your CV is now attached to your profile")
            console.print("🚀 You can now apply to jobs and your CV will be included automatically")
        except Exception as e:
            show_error(f"Failed to upload CV: {str(e)}")
            
    elif cv_path:
        # Upload CV file
        cv_file = Path(cv_path)
        
        if not cv_file.exists():
            show_error(f"❌ File not found: {cv_path}")
            return
            
        if not cv_file.suffix.lower() in ['.pdf', '.doc', '.docx', '.txt']:
            show_error("❌ Supported formats: PDF, DOC, DOCX, TXT")
            return
            
        console.print(f"📁 Uploading: {cv_file.name}")
        
        try:
            result = api.upload_cv_file(cv_path)
            show_success("✅ CV uploaded successfully!")
            console.print("💼 Your CV is now attached to your profile")
            console.print("🚀 You can now apply to jobs and your CV will be included automatically")
        except Exception as e:
            show_error(f"Failed to upload CV: {str(e)}")
    else:
        # Interactive mode
        choice = Prompt.ask(
            "How would you like to upload your CV?",
            choices=["file", "text"],
            default="file"
        )
        
        if choice == "file":
            cv_path = Prompt.ask("📁 Path to your CV file")
            # Recursive call with the path
            upload_cv.callback(cv_path, None)
        else:
            console.print("📝 Enter your CV content (press Ctrl+D when done):")
            cv_lines = []
            try:
                while True:
                    line = input()
                    cv_lines.append(line)
            except EOFError:
                pass
            
            cv_text = "\n".join(cv_lines)
            if cv_text.strip():
                # Recursive call with text
                upload_cv.callback(None, cv_text)
            else:
                show_error("❌ No CV content provided")

@profile.command()
def show():
    """
    👁️ Show your profile information
    """
    
    if not config.is_authenticated():
        show_error("🔐 You need to login first")
        return
    
    try:
        profile_data = api.get_profile()
        user = profile_data.get('user', {})
        
        console.print("\n[bold bright_cyan]👤 Your Profile[/bold bright_cyan]\n")
        console.print(f"📧 Email: {user.get('email', 'N/A')}")
        console.print(f"👤 Name: {user.get('name', 'N/A')}")
        console.print(f"📱 Phone: {user.get('phone', 'Not set')}")
        console.print(f"💼 CV Attached: {'✅ Yes' if user.get('cv_attached') else '❌ No'}")
        
        if not user.get('cv_attached'):
            console.print("\n💡 Upload your CV: jobtty profile upload-cv")
            
    except Exception as e:
        show_error(f"Failed to get profile: {str(e)}")

@profile.command()
def status():
    """
    📊 Show profile completion status
    """
    
    if not config.is_authenticated():
        show_error("🔐 You need to login first")
        return
    
    try:
        profile_data = api.get_profile()
        user = profile_data.get('user', {})
        
        console.print("\n[bold bright_cyan]📊 Profile Status[/bold bright_cyan]\n")
        
        # Calculate completion
        completed_items = []
        total_items = [
            ("Email", user.get('email')),
            ("Name", user.get('name')),
            ("CV", user.get('cv_attached')),
        ]
        
        for item_name, item_value in total_items:
            status = "✅" if item_value else "❌"
            console.print(f"{status} {item_name}")
            if item_value:
                completed_items.append(item_name)
        
        completion_rate = len(completed_items) / len(total_items) * 100
        console.print(f"\n📈 Profile completion: {completion_rate:.0f}%")
        
        if completion_rate < 100:
            console.print("\n💡 Complete your profile to increase your job application success rate!")
            
    except Exception as e:
        show_error(f"Failed to get profile status: {str(e)}")