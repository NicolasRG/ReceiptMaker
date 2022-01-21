class lineTracker:

    def __init__(self, starting_height, line_spacing):
        self.starting_height = starting_height
        self.current_height = starting_height
        self.line_spacing = line_spacing

    def next_line(self, decrement=None):
        if decrement is None:
            self.current_height = self.current_height - self.line_spacing
        else:
            self.current_height = self.current_height - decrement
        return self.current_height