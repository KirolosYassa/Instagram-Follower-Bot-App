from Instagram import Instagram


user = Instagram(profile_name="daily.it.is.time.to.get.up")
user.sign_in()
user.find_followers()   
user.follow()

