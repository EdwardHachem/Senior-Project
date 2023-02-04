import utils
import pandas as pd
import xlsxwriter

# authenticating youtube api
yt = utils.youtube_authenticate()

excel_file = xlsxwriter.Workbook('yt_data.xlsx')
worksheet = excel_file.add_worksheet()
worksheet.write('A1', 'Query')
worksheet.write('B1', 'Position')
worksheet.write('C1', 'Video URL')
worksheet.write('D1', 'Video title')
worksheet.write('E1', 'Video duration')
worksheet.write('F1', 'Thumbnail URL')
worksheet.write('G1', 'Thumbnail resolution')
worksheet.write('H1', 'Highres thumbnail')
worksheet.write('I1', 'Channel title')
worksheet.write('J1', 'Upload date')
worksheet.write('K1', 'Closed captions')
worksheet.write('L1', 'Licensed content')
worksheet.write('M1', 'Projection')

row = 1
col = 0
position = 1
query = "aggressive"

request = utils.search(yt, q=query, fields='nextPageToken,items(id,snippet)', maxResults=50)

for i in range(1, 2):
    response = utils.search(yt, q=query, fields='nextPageToken,items(id,snippet)', maxResults=50).execute()
    items = response.get("items")
    for item in items:
        vid_id = item['id']['videoId']
        video_details = utils.get_video_details(yt, id=vid_id)
        duration = video_details['items'][0]['contentDetails']['duration']
        thumbnail = video_details['items'][0]['snippet']['thumbnails']['default']['url']
        thumbnail_w = video_details['items'][0]['snippet']['thumbnails']['default']["width"]
        thumbnail_h = video_details['items'][0]['snippet']['thumbnails']['default']['height']
        title = video_details['items'][0]['snippet']['title']
        thumbnail_res = "thumbnail_w" + "thumbnail_h"
        highres = "No"
        date_time = video_details['items'][0]['snippet']['publishedAt']
        upload_date_num = pd.to_datetime(date_time).date()
        format_upload_date = upload_date_num.strftime("%d %b %Y")
        channel_title = video_details['items'][0]['snippet']['channelTitle']
        closed_caption = video_details['items'][0]['contentDetails']['caption']
        licensed_content = video_details['items'][0]['contentDetails']['licensedContent']
        projection = video_details['items'][0]['contentDetails']['projection']
        if thumbnail_w >= 480 and thumbnail_h >= 360:
            highres = "Yes"
        worksheet.write(row, col, query)
        worksheet.write(row, col + 1, position)
        worksheet.write(row, col + 2, "https://www.youtube.com/watch?v=" + vid_id)
        worksheet.write(row, col + 3, title)
        worksheet.write(row, col + 4, duration)
        worksheet.write(row, col + 5, thumbnail)
        worksheet.write(row, col + 6, thumbnail_res)
        worksheet.write(row, col + 7, highres)
        worksheet.write(row, col + 8, channel_title)
        worksheet.write(row, col + 9, format_upload_date)
        worksheet.write(row, col + 10, closed_caption)
        worksheet.write(row, col + 11, licensed_content)
        worksheet.write(row, col + 12, projection)
        row += 1
        position += 1
excel_file.close()
