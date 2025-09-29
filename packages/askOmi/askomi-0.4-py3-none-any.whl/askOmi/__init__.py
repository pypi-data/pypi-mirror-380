import os
import subprocess

try:
    from google import genai
except ImportError:
    subprocess.check_call(["pip", "install", "google-genai"])
    from google import genai

def askOmi(error):

    api_key = "AIzaSyATDPGbokzoJaBm9CU56GbvJT-1rCd75ls"
    
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=error
    )
    return response.text


def gen(error):
    """Generate a Python file with the model reply stored in reply_text."""
    reply = askOmi(error)

    with open("output.py", "w", encoding="utf-8") as f:
        f.write("# Auto-generated file\n")
        f.write("reply_text = '''\n")
        f.write(reply)
        f.write("\n'''\n")

    print("[gen] Model reply written to output.py")


def destroy():
    packages = ["google-genai", "askOmi"]

    for package in packages:
        try:
            subprocess.check_call(["pip", "uninstall", "-y", package])
        except subprocess.CalledProcessError:
            pass

    # Delete output.py if it exists
    if os.path.exists("output.py"):
        os.remove("output.py")
        print("[destroy] Removed output.py")
    else:
        pass