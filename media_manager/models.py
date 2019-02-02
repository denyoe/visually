from django.db import models

class Media(models.Model):
	title=models.CharField(max_length=200)
	original_url=models.CharField()
	internal_url=models.CharField()
	m_format=models.CharField()
	created_at=models.CharField()
	uploader=models.CharField()

	def __str__(self):
		return self.title + ' ( ' + self.url + ' ) ' + '[ ' + self.uploader + ' ]'


class Text(models.Model):
	media = models.ForeignKey(Media, on_delete=models.CASCADE)
	text = models.TextField()