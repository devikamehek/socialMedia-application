from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    profile_pic=models.ImageField(upload_to="profilepics",blank=True,default="/profilepics/default.webp")
    bio=models.CharField(max_length=200,null=True)
    address=models.CharField(max_length=200,null=True)
    dob=models.DateTimeField(null=True)
    following=models.ManyToManyField("self",related_name="followed_by",symmetrical=False)
    created_date=models.DateTimeField(auto_now_add=True)
    cover_pic=models.ImageField(upload_to="coverpic",blank=True,default="/profilepics/coverpic2.jpg")


    def __str__(self):
        return self.user.username
    

    # # request.user.profile.friend_request
    # @property
    # def friend_request(self):
    #     all_profiles=UserProfile.objects.all().exclude(user=self.user)
    #     following_profiles=self.following.all()
    #     suggestions=set(all_profiles)-set(following_profiles)
    #     return suggestions
    # 
    # ithu cheythitilla becoz recoreded clasil ith saved allarnu athu kond annathe session kittila.(friend suggestions kaanikunna place)
    
    
class Posts(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="postimages",null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="userposts")
    created_date=models.DateTimeField(auto_now_add=True)
    liked_by=models.ManyToManyField(User,related_name="post_like")
    

    def __str__(self):
        return self.title
    
    

class Comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="comment")
    comment_text=models.CharField(max_length=200)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE,related_name="post_comment")
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text


# ḍjango signals post_save,pre_save
# post_delete,pre_delete

def create_profile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_profile,sender=User)


