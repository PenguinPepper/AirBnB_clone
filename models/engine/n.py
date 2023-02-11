with ... as f:
	models = json.loads(f)

for value in models.values():
	model = BaseModel(**my_model)
	self.new(model)


