import git
import os

def main():
   repo = "repo"
   git_repository = input("Enter github repository url: ")
   image_name = input("Enter docker image name (username/image_name), which will be pushed to docker hub: ")
   git.Repo.clone_from(git_repository, repo)
   os.chdir(os.getcwd() + "/" + repo)
   find_files("Dockerfile",os.getcwd(), image_name)

def find_files(filename, path, image):
   for root, dir, files in os.walk(path):
      if filename in files:
         return os.system(f"docker build . -t {image} && docker push {image}")
   return False

if __name__ == '__main__':
    main()