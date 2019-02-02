from django.db import models

class Media(models.Model):
	title 			= models.CharField(max_length=255)
	original_url	= models.CharField(max_length=255)
	internal_url	= models.CharField(max_length=255)
	m_format		= models.CharField(max_length=20)
	created_at		= models.DateTimeField(auto_now_add=True)
	uploader		= models.EmailField(max_length=255) # email

	def __str__(self):
		return self.title + ' [' + self.m_format + ']' + ' ( ' + self.internal_url + ' ) ' + '[ ' + self.uploader + ' ]'
		# return "{} posted at {}".format(
  #           self.question_text,
  #           self.pub_date)



class Text(models.Model):
	media 	= models.ForeignKey(Media, on_delete=models.CASCADE)
	text 	= models.TextField()
