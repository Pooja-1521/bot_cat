from polly_speak import speak
import boto3

def handle_command(command):
    if 'time' in command:
        from datetime import datetime
        now = datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {now}")

    elif 'start instance' in command:
        ec2 = boto3.client('ec2', region_name='us-east-1')
        ec2.start_instances(InstanceIds=['i-1234567890abcdef0'])  # replace with your instance ID
        speak("Starting the EC2 instance.")

    elif 'stop instance' in command:
        ec2 = boto3.client('ec2', region_name='us-east-1')
        ec2.stop_instances(InstanceIds=['i-1234567890abcdef0'])
        speak("Stopping the EC2 instance.")

    else:
        speak("Sorry, I don't understand that command yet.")
