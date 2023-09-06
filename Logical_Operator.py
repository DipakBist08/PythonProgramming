#is_Magician=False

#is_Expert=True

#check if Magician and expert:"You are Master Magician"

#Check if magician but not expert:"at least you are getting there"

#if you are not a magicain:"You need magic power"
is_Magician=False
is_Expert=True
if is_Magician or is_Expert:
    print("You are Master Magician.")
elif is_Magician or not is_Expert:
    print('At Least You are getting there.')
elif not is_Magician:
    print('You need a magic power.')
else:
    print('Learn some Magic Tricks.')
