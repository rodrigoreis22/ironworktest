from apiclient.discovery import build

DEVELOPER_KEY = "AIzaSyAnEy2O9Iwf1qn7-U8AxoajQ2nw0OlDxyg"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def get_videos_by_channel(channel_id, sync_date):
	youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)
	search_response = youtube.search().list(
            order='date',
            channelId=channel_id,
            publishedAfter=sync_date,
            part="id,snippet",
            maxResults=50,
          ).execute()
	for search_result in search_response.get("items", []):
		if search_result["id"]["kind"] == "youtube#video":
			title = search_result["snippet"]["title"]
			published_at = search_result["snippet"]["publishedAt"]
			video_id = search_result["id"]["videoId"]
			watch_link = "https://www.youtube.com/watch?v=%s" % (video_id)
			print "%s \t %s \t %s \t %s" % (title, published_at, video_id, watch_link)

	#print search_response

def main():
	get_videos_by_channel('UCccOBk6ck17-l_x2THCshdw','2014-01-01T00:00:00.000Z')

if __name__ == "__main__":
	main()