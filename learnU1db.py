import u1db

class Task(u1db.Document):
	""" A todo item"""
	def _get_title(self):
		"""Get the task title"""
		return self.content.get('title')
	def _set_title(self,title):
		"""Set a title to the task"""
		self.content['title']= title
	title = property(_get_title, _set_title,doc="Title of the Task")
	
	def _get_done(self):
		"""Get the Task status"""
		return self.content.get('done',False)
	def _set_done(self,value):
		"""Set the done status"""
		self.content['done']=value
		
	done = property(_set_done,_get_done,doc="Done flag")
	
	def _get_tags(self):
		"""Get tag asociated with the task"""
		return self.content.setdefault('tags',[])
	def _set_tags(self,tags):
		"""set tags associated to the task"""
		self.content['tags']=list(set(tags))
	
	tags = property(_get_tags,_set_tags,doc="Task tags")

example_task = Task()
example_task.title = "Create a task class"
print(example_task.title)
print(example_task.tags)
example_task.tags=['developemente']
example_task.tags = [{'name':'Inocent','age':17}]
print(example_task.tags)
