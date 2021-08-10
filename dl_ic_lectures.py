import os
import json

jsr = input('[?]Enter the raw json: ')
# jsd = jsr.replace('}]','}').replace('[{','{')
jd = json.loads(jsr)

num_jd = len(jd)


for idx in range(num_jd):
	par_dir = jd[idx]['SubjectName']
	ts_dir = f'{jd[idx]["TeachId"]}___{jd[idx]["TopicName"]}___{jd[idx]["TeachDesc"]}'
	# ts_dir = f'{jd[idx]["TeachId"]}___{jd[idx]["TeachDesc"]}___{jd[idx]["TopicName"]}'
	dirp = f'{par_dir}/{ts_dir}'

	urlp = f'https://bbvideo.blackboardlive.com:550/hls/{jd[idx]["SessionCode"]}'
	wget_cmd = f'''wget -N --read-timeout=4 -r -nH --cut-dirs=2 --no-parent --reject="index.html*"  {urlp} -P "{dirp}"'''
	
	try:
		os.makedirs(dirp, exist_ok=True)
		print(f'\n\n\n\n-------------------[+] Created {dirp} ------------------------')
		print(f'Executing: {wget_cmd}\n')
		os.system(wget_cmd)

	except Exception as e:
		print(e)


print('[+]Hare Krishna! All went well............')		

