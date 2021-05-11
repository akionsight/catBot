from dotenv import load_dotenv
import os 


load_dotenv()

allowed_channels = os.getenv('ALLOWED_CHANNELS').split()
token = os.getenv('TOKEN')


