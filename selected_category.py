class SelectedCategory:
    selected_category = None

    def set(self, value):
        self.selected_category = value

    def get(self):
        return self.selected_category

selected_category_instance = SelectedCategory()
