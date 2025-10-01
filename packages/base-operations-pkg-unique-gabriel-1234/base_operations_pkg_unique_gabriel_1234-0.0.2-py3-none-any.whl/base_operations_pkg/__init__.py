class Base:
    """
    კლასი, რომელიც ინახავს მნიშვნელობას და გთავაზობთ ძირითად ოპერაციებს.
    """
    def __init__(self, value):
        # ეს ინიციალიზებს ობიექტის მნიშვნელობას
        self.value = value

    def get_value(self):
        # აბრუნებს მიმდინარე მნიშვნელობას
        return self.value

    def set_value(self, new_value):
        # ცვლის მნიშვნელობას ახლით
        self.value = new_value

    def add_to_value(self, increment):
        # მიმდინარე მნიშვნელობას უმატებს increment-ს
        self.value += increment