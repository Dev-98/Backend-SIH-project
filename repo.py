import csv, os
from github import Github, Auth
import argparse


CLASSIC = "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" #os.environ.get('GITHUB_PAT') 

auth = Auth.Token(CLASSIC)
g = Github(auth=auth)

repo = g.get_user().get_repo("database-SIH")

def create_repository(name, mail, passw):
  try :
    
    # Define your data
    data = [
      [name, mail, passw]
    ]

    # Define the file path
    file_path = 'data.csv'

    existing_data = []
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            existing_data.append(row[1])

    # Check if the email already exists
    for row in existing_data:
      if row == mail:
        return "User already exists"
          

    # Write data to CSV file
    with open(file_path, mode='a', newline='') as file:
      writer = csv.writer(file)
      writer.writerows(data)

    file_content = repo.get_contents(file_path)
    # Commit the updated file to the repository

    repo.update_file('data.csv', 'Updated data', open(file_path, 'rb').read(),file_content.sha, branch='main')
    
    return "Data uploaded successfully"
  
  except Exception as e:
    return str(e)
  
def check_mail(email):
  
  file_path = 'data.csv'
  mails = []
  
  file_content = repo.get_contents(file_path)
  csv_data = file_content.decoded_content.decode('utf-8').splitlines()

  reader = csv.reader(csv_data)
  for row in reader:
    mails.append(row[1])
  
  if email.lower() in mails :
      return True
  else:
      return False


if __name__ == "__main__":
  # args = get_args()

  # print(create_repository(args.name,args.mail,args.passw))
  # file_path = 'data.csv'
  # mails = []
  # passwords = []
  # with open("data.csv", mode='r', newline='') as file:
  #     reader = csv.reader(file)
  #     for row in reader:
  #         mails.append(row[1])
  #         passwords.append(row[2])

  # print(mails,passwords)
  
  if check_mail("dev28@gmail.com"):
    print("Worked")
  
  else:
    print("Didn't Worked")
     
