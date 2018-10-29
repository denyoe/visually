from django.db import models

class media(models.Model):
	title=models.CharField()
	original_url=models.CharField()
	internal_url=models.CharField()
	m_format=models.CharField()
	created_at=models.CharField()
	uploader=models.CharField()

	def __str__(self):
		return self.title + ' ( ' + self.url + ' ) ' + '[ ' + self.uploader + ' ]'

