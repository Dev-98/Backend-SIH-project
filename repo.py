import csv
from github import Github, Auth
import argparse


def create_repository(name, mail, passw):
  CLASSIC = "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" #os.environ.get('GITHUB_PAT') 
  try :
    # Authenticationg the Token
    auth = Auth.Token(CLASSIC)
    g = Github(auth=auth)

    repo = g.get_user().get_repo("database-SIH")
    
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
  
def get_args():
  parser = argparse.ArgumentParser(description="Kreate Automation")

  parser.add_argument('-name', type=str, 
          help="provide a URL of a GDrive file with public access")
  
  parser.add_argument("-mail", type=str,
          help="this goes with the name to create various repos for single user")

  parser.add_argument("-passw", type=str,
          help="this goes with the name to create various repos for single user")
  
  args,unknown = parser.parse_known_args()

  return args

if __name__ == "__main__":
  # args = get_args()

  # print(create_repository(args.name,args.mail,args.passw))
  file_path = 'data.csv'
  mails = []
  passwords = []
  with open("data.csv", mode='r', newline='') as file:
      reader = csv.reader(file)
      for row in reader:
          mails.append(row[1])
          passwords.append(row[2])

  print(mails,passwords)
  
 
