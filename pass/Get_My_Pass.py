#!/usr/bin/env python
# -*- coding:utf-8 -*-
#desc: This script is used to Get The Pass Of Site Or App for tib
#date: 2014-4-6

import sys,os,hashlib,time,json
import platform
import shutil
import time
import re

#some global vars
#1.pass_store_file
#2.dir_name
dir_name = "tib"
pass_file_name = "password.tib"

args = sys.argv

The_needed_dir = os.path.expanduser('~') + os.sep + dir_name
if os.path.exists(The_needed_dir) is not True:
	os.makedirs(The_needed_dir)
pass_store_file = The_needed_dir + os.sep + pass_file_name

#json.loads this pass_store_file
if os.path.exists(pass_store_file) and os.path.isfile(pass_store_file):
	if os.path.getsize(pass_store_file) > 0:
		original_info = json.loads(open(pass_store_file).read())
		New_ID = len(original_info) + 1
	else:
		original_info = {}
		New_ID = len(original_info) + 1
else:
	original_info = {}
	New_ID = len(original_info) + 1

def check_arg(args):
	#if len(args) != 4 and len(args) != 5 and len(args) != 3 and len(args) != 6 and len(args) != 2:
	if len(args) != 5 and len(args) != 6 and len(args) != 2:
		help_me()
	if len(args) == 5 and args[4] != "del":
		if args[2] != "site" and args[2] != "app" and args[2] != "other":
			print "*" * 50
			print "Wrong Type .... Here should be [site|app|other]"
			print "*" * 50
			help_me()
	if len(args) == 6:
		if args[3] != "site" and args[3] != "app" and args[3] != "other":
			print "*" * 50
			print 'Wrong Type .... Please check the "type" ---> [site|app|other]'
			print "*" * 50
			help_me()

def backup_the_file(file_path):
	if os.path.exists(file_path) is True:
		bak_file_name = os.path.split(file_path)[1] + '.' + time.strftime("%Y-%m-%d") + '.bak'
		new_file_path = os.path.split(file_path)[0] + os.sep + bak_file_name
		shutil.copy(file_path,new_file_path)

def check_the_platform():
	if platform.system().lower() == 'linux':
		return "linux"
	elif platform.system().lower() == 'darwin':
		return "mac"
	elif platform.system().lower() == 'windows':
		return "win"
	else:
		return "Unknown"

def get_the_num(New_ID,tmp_list):
   New_ID = int(New_ID) + 1
   if str(New_ID) not in tmp_list:
	  #get_the_num(New_ID,tmp_list)
	  return New_ID
   else:
	  #return get_the_num(New_ID,tmp_list)
	  #print New_ID
	  #return New_ID
	  return get_the_num(New_ID,tmp_list)

def deal_with_delete(original_dic,User,Pass,Keyword):
	for k,v in original_dic.items():
		if v['username'] == str(User) and v['password'] == str(Pass) and v['keyword'] == str(Keyword):
			original_dic.pop(k)
	#Store info to file
	last_info = json.dumps(original_info,ensure_ascii=False,sort_keys=False,indent=4)
	tmp_f = open(pass_store_file,'w')
	tmp_f.write(last_info)
	tmp_f.close()
	if check_the_platform() == 'linux':
		os.system("Format_script.sh %s" % pass_store_file)
	backup_the_file(pass_store_file)

def help_me():
	print '''\n\tUsage:\n\t\t%s [username] [site|app|other] [baidu.com|Path] "Some Descriptions Here If You Need To Add.."\n''' % args[0]
	print '''\t\t\tCommon usage of the script\n'''
	print '''\t\t%s [username] [password] [site|app|other] [baidu.com|Path] "Some Descriptions Here If You Need To Add.."\n''' % args[0]
	print '''\t\t\tWill add the info to pass_store_file direct\n'''
	print '''\t\t%s "Keyword"\n''' % args[0]
	print '''\t\t\tWill find the result related to keyword\n'''
	print '''\t\t%s "Username" "Password" "Keyword" "del"\n''' % args[0]
	print '''\t\t\tWill delete the record according to the combination of three: username + password + keyword\n'''
	sys.exit()

if __name__ == '__main__':
	#check args
	check_arg(args)
	#Get The Info
	if len(args) == 5 and args[4] != "del":
		Username = args[1]
		Type = args[2]
		Keyword = args[3]
		Description = args[4]
	elif len(args) == 5 and args[4] == "del":
		Username = args[1]
		Password = args[2]
		Keyword = args[3]
		deal_with_delete(original_info,Username,Password,Keyword)
		sys.exit()
	elif len(args) == 6:
		Username = args[1]
		Password = args[2]
		Type = args[3]
		Keyword = args[4]
		Description = args[5]
	elif len(args) == 2:
		Keyword = args[1]
	else:
		print "Some Error.."
		sys.exit()
	#Get and print The Info
	sign = 1
	site_dic = {}
	app_dic = {}
	other_dic = {}
	print "=" * 100
	p_pass = re.compile(r"\*...\*")
	if len(original_info) >= 1:
		for k,v in original_info.items():
			v_tmp_password = v['password']
			if len(args) == 5:
				if v['username'] == Username and v['type'] == Type and Keyword.lower() in v['keyword'].lower():
					if "***" in v['password']:
						if "kamtjin5" in v['password']:
							tmp_pass = p_pass.split(v["password"],1)
							v['password'] = "H%s  or  h%s" % (tmp_pass[0][3:] + tmp_pass[1],tmp_pass[0][3:] + tmp_pass[1])
						else:
							if "2350" in v['password']:
								v['password'] = "7%s" % v["password"][3:]
							elif len(v['password'][3:]) == 3:
								v['password'] = "hkamtjin5_5%s  or  Hkamtjin5_5%s" % (v['password'][3:],v['password'][3:])
							else:
								v['password'] = v['password'][3:]
					else:
						v['password'] = "hkamtjin5_5" + v['password']
					print json.dumps(original_info["%s" % k],indent=4)
					sign = 0
			elif len(args) == 6:
				if v['username'] == Username and v['type'] == Type and Keyword.lower() in v['keyword'].lower() and v['password'] == Password:
					if "***" in v['password']:
						if "kamtjin5" in v['password']:
							tmp_pass = p_pass.split(v["password"],1)
							v['password'] = "H%s  or  h%s" % (tmp_pass[0][3:] + tmp_pass[1],tmp_pass[0][3:] + tmp_pass[1])
						else:
							if "2350" in v['password']:
								v['password'] = "7%s" % v["password"][3:]
							elif len(v['password'][3:]) == 3:
								v['password'] = "hkamtjin5_5%s  or  Hkamtjin5_5%s" % (v['password'][3:],v['password'][3:])
							else:
								v['password'] = v['password'][3:]
					else:
						v['password'] = "hkamtjin5_5" + v['password']
					print json.dumps(original_info["%s" % k],indent=4)
					sign = 0
			elif len(args) == 2:
				if Keyword.lower() == v['type']:
					if "***" in v['password']:
						if "kamtjin5" in v['password']:
							tmp_pass = p_pass.split(v["password"],1)
							v['password'] = "H%s  or  h%s" % (tmp_pass[0][3:] + tmp_pass[1],tmp_pass[0][3:] + tmp_pass[1])
						else:
							if "2350" in v['password']:
								v['password'] = "7%s" % v["password"][3:]
							elif len(v['password'][3:]) == 3:
								v['password'] = "hkamtjin5_5%s  or  Hkamtjin5_5%s" % (v['password'][3:],v['password'][3:])
							else:
								v['password'] = v['password'][3:]
					else:
						v['password'] = "hkamtjin5_5" + v['password']
					print json.dumps(original_info["%s" % k],indent=4)
					sign = 0
				elif Keyword.lower() in v['keyword'].lower() or Keyword.lower() in v['description'].lower() or Keyword.lower() in v['username'].lower():
					if "***" in v['password']:
						if "kamtjin5" in v['password']:
							tmp_pass = p_pass.split(v["password"],1)
							v['password'] = "H%s  or  h%s" % (tmp_pass[0][3:] + tmp_pass[1],tmp_pass[0][3:] + tmp_pass[1])
						else:
							if "2350" in v['password']:
								v['password'] = "7%s" % v["password"][3:]
							elif len(v['password'][3:]) == 3:
								v['password'] = "hkamtjin5_5%s  or  Hkamtjin5_5%s" % (v['password'][3:],v['password'][3:])
							else:
								v['password'] = v['password'][3:]
					else:
						v['password'] = "hkamtjin5_5" + v['password']
					print json.dumps(original_info["%s" % k],indent=4)
					sign = 0
			v['password'] = v_tmp_password
	print "=" * 100
	if sign == 1:
		if len(args) == 6:
			tt = 0
			for k,v in original_info.items():
				if v['username'] == Username and v['type'] == Type and Keyword.lower() in v['keyword'].lower() and v['password'] != Password:
					#print "Got one..\n"
					#print original_info["%s" % k]
					#print "+" * 20
					original_info["%s" % k] = {'password':"%s" % Password,'username':"%s" % Username,'type':"%s" % Type,'keyword':"%s" % Keyword,'description':"%s" % Description}
					#print original_info["%s" % k]
					tt = 1
					#sys.exit()
					#print original_info["%s" % k]
			if tt == 0:
				New_ID = get_the_num(New_ID,original_info.keys())
				original_info["%s" % New_ID] = {'password':"%s" % Password,'username':"%s" % Username,'type':"%s" % Type,'keyword':"%s" % Keyword,'description':"%s" % Description}
		elif len(args) == 5:
			New_ID = get_the_num(New_ID,original_info.keys())
			original_info["%s" % New_ID] = {'password':"%s" % hashlib.new("md5","%s" % Keyword).hexdigest()[:3],'username':"%s" % Username,'type':"%s" % Type,'keyword':"%s" % Keyword,'description':"%s" % Description}
	#Store info to file
	last_info = json.dumps(original_info,ensure_ascii=False,sort_keys=False,indent=4)
	tmp_f = open(pass_store_file,'w')
	tmp_f.write(last_info)
	tmp_f.close()
	if check_the_platform() == 'linux':
		os.system("Format_script.sh %s" % pass_store_file)
	backup_the_file(pass_store_file)
