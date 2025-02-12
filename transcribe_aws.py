# @! create function to transcribe audio mp3 file using aws transcribe service and save output to file

import boto3

def transcribe_audio(file_uri, output_file):
    transcribe = boto3.client('transcribe')
    job_name = 'transcription_job'
    transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': file_uri},
        MediaFormat='mp3',
        LanguageCode='en-US'
    )
    while True:
        status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
        if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
            break
    if status['TranscriptionJob']['TranscriptionJobStatus'] == 'COMPLETED':
        response = transcribe.get_transcription_job(TranscriptionJobName=job_name)
        transcript_file_uri = response['TranscriptionJob']['Transcript']['TranscriptFileUri']
        with open(output_file, 'w') as f:
            f.write(transcript_file_uri)
        print(f"Transcription saved to {output_file}")

# Example usage
transcribe_audio('s3://bucket-name/audio.mp3', 'transcription_aws.json')
