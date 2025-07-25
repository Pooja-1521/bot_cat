import boto3

def speak(text):
    polly = boto3.client('polly', region_name='us-east-1')  # Choose your region
    response = polly.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId='Joanna'
    )

    with open('speech.mp3', 'wb') as file:
        file.write(response['AudioStream'].read())

    # Play the speech (Windows only, or use `playsound`)
    import playsound
    playsound.playsound('speech.mp3')
