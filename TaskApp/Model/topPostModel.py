class TopPostModel():

	def __init__(self, post_id, post_title, post_body, total_number_of_comments):
		self.post_id = post_id
		self.post_title = post_title
		self.post_body = post_body
		self.total_number_of_comments = total_number_of_comments
	def toJson(self):
		return {
			"post_id": self.post_id,
			"post_title": self.post_title,
			"post_body": self.post_body,
			"total_number_of_comments": self.total_number_of_comments
		}