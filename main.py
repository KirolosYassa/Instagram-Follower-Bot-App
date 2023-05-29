from Instagram import Instagram


user = Instagram(url="https://www.instagram.com/coding_dev_/")
user.sign_in()
user.follow_the_followers_users()